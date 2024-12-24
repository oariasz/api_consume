import requests
import os
import json


API_KEY = 'd4414ed6f553a656245521410c941e47'
TOKEN_ACCESS = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNDQxNGVkNmY1NTNhNjU2MjQ1NTIxNDEwYzk0MWU0NyIsIm5iZiI6MTczNDg0MzkxMS45OTYsInN1YiI6IjY3Njc5ZTA3YjY3ZTQ1NDcyNTVlNGE5NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vmzkjHFWBKcvOAAjjTIm7HiHzaDvsZLsNgbY0Ig6VB4'
BASE_URL = "https://api.themoviedb.org/3"

def get_runtime(movie_id):
    # Endpoint to fetch movie details
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "en-US"}

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        movie_data = response.json()  # Parse JSON response
        runtime = movie_data.get("runtime")  # Get the runtime field
        if runtime:
            return runtime
        else:
            return 'N/A'
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return None
    
def get_providers(movie_id, country_code='US'):
    # Endpoint to fetch movie details
    url = f"{BASE_URL}/movie/{movie_id}/watch/providers"
    params = {"api_key": API_KEY}

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        watch_data = response.json()  # Parse JSON response

        # Get watch providers for a specific country (e.g., "US")
        providers = watch_data.get("results", {}).get(country_code, {})

        if providers:
            print(f"Watch providers in {country_code}:")
            if "flatrate" in providers:
                print("Streaming:")
                for provider in providers["flatrate"]:
                    print(f"- {provider['provider_name']}")
            if "rent" in providers:
                print("\nRent:")
                for provider in providers["rent"]:
                    print(f"- {provider['provider_name']}")
            if "buy" in providers:
                print("\nBuy:")
                for provider in providers["buy"]:
                    print(f"- {provider['provider_name']}")
        else:
            print(f"No watch provider information available for country: {country_code}")
    else:
        print(f"Error: {response.status_code} - {response.reason}")
    
def get_credits(movie_id):
    # Get the credits for the movie
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    params = {
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        credits_data = response.json()  # Parse JSON response
        cast = credits_data.get("cast", [])  # Get the cast information

        # Print main characters (first 10 actors)
        print("Main Characters:")
        for actor in cast[:20]:  # Limit to the top 20 actors
            print(f"Name: {actor['name']} as {actor['character']}")

import requests

def get_similar_movies(movie_id, language="en-US", max_results=10):
    """
    Fetches a list of similar movies for a given movie ID.
    
    Args:
        movie_id (int): The TMDB ID of the movie.
        language (str): Language for the response (default is "en-US").
        max_results (int): Maximum number of similar movies to return.
    
    Returns:
        list: A list of dictionaries containing similar movies with their details.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar"
    params = {
        "api_key": API_KEY,
        "language": language,
        "page": 1  # Start with the first page
    }

    similar_movies = []
    
    while len(similar_movies) < max_results:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            
            # Add movies to the list, respecting the max_results limit
            similar_movies.extend(results[:max_results - len(similar_movies)])
            
            # Check if there are more pages to fetch
            if params["page"] >= data.get("total_pages", 1):
                break
            
            # Increment the page number
            params["page"] += 1
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            break
    
    return similar_movies

def get_rating(movie_id):
    """
    Fetches the rating (vote_average) of a movie from TMDB.

    Args:
        movie_id (int): The TMDB ID of the movie.
    Returns:
        float: The movie's rating (vote_average) or None if not found.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        movie_data = response.json()
        return movie_data.get("vote_average")  # Extract the rating
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return None

def get_videos(movie_id, language="en-US"):
    """Fetches the videos (trailers, teasers, clips) of a movie from TMDB."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
    params = {"api_key": API_KEY, "language": language}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error fetching videos: {response.status_code} - {response.reason}")
        return None


def get_images(movie_id):
    """Fetches the images (posters, backdrops, logos) of a movie from TMDB."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    params = {"api_key": API_KEY}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching images: {response.status_code} - {response.reason}")
        return None


def get_reviews(movie_id, language="en-US"):
    """Fetches the reviews of a movie from TMDB."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    params = {"api_key": API_KEY, "language": language}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error fetching reviews: {response.status_code} - {response.reason}")
        return None


def get_genres(movie_id, language="en-US"):
    """Fetches the genres of a movie from TMDB."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": language}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("genres", [])
    else:
        print(f"Error fetching genres: {response.status_code} - {response.reason}")
        return None


def get_recommendations(movie_id, language="en-US"):
    """Fetches the recommended movies for a given movie ID."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
    params = {"api_key": API_KEY, "language": language}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error fetching recommendations: {response.status_code} - {response.reason}")
        return None


def get_director(movie_id):
    """
    Fetches the director of a movie from TMDB by checking the crew in credits.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = {"api_key": API_KEY}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        credits = response.json()
        crew = credits.get("crew", [])
        for person in crew:
            if person.get("job") == "Director":
                return person.get("name")
        return None  # Director not found
    else:
        print(f"Error fetching director: {response.status_code} - {response.reason}")
        return None

def _print_helpline():
    print('Q - Quit  |  C - Credits  |  S - Similar Movies  |  P - Watch Providers  |  I - Images  |  V - Videos  ')

# --- MAIN ---
if __name__ == '__main__':
    os.system('clear')    # Clears the screen
    print('-'*20)
    


    MOVIE = 'The Godfather'
    url = f"https://api.themoviedb.org/3/search/movie?query={MOVIE}&include_adult=false&language=en-US&page=1"


    # Parameters for the request
    params = {
        "api_key": API_KEY,  # Your API key
        "language": "en-US",  # Optional: Language for the response
        'page': 1
    }
    headers = {"accept": "application/json"}

    all_movies = []
    while True:
        # print(f'Fetching page {params['page']}/{data['total_pages']}...')    
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            total_pages = data['total_pages']
            results = data['results']
            all_movies.extend(results)
            
            if params['page'] >= total_pages:
                break
            
            # Increments the page to fetch the next one
            params['page'] += 1
        else:
            print(f'Error: {response.status_code} - {response.reason}')
            break

    if all_movies:
        sorted_movies = sorted(all_movies, key=lambda x: x["popularity"], reverse=True)
    print('Total movies: ', len(all_movies))
    print(list(all_movies[0].keys()))
    
    for movie in sorted_movies:

        print('====================')
        print('ID:                 ', movie['id'])
        print('Title:              ', movie['title'])
        print('Original Title:     ', movie['original_title'])
        print('Release Date:       ', movie['release_date'])
        print('Director:           ', movie['release_date'])
        print('Popularity:         ', movie['popularity'])
        print('Rating:             ', get_rating(movie['id']))
        print('Duration (minutes): ', get_runtime(movie['id']))
        _print_helpline()
        
        c = input()
        if c.lower() == 'q':
            break
        if c.lower() == 'c':     # Get the credits
            get_credits(movie['id'])
        if c.lower() == 'd':     # Get the watch providers
            director = get_director(movie['id'])
            if director:
                print(f"\nDirector: {director}")
            else:
                print("\nDirector not found.")            
        if c.lower() == 'p':     # Get the watch providers
            get_providers(movie['id'])
        if c.lower() == 'i':     # Get the images associated with the movie
            images = get_images(movie['id'])
            if images:
                print("\nPosters:")
                for poster in images.get('posters', []):
                    print(f"- {poster['file_path']}")
                print("\nBackgrops:")
                for poster in images.get('backdrops', []):
                    print(f"- {poster['file_path']}")
        if c.lower() == 'v':     # Get the images associated with the movie
            videos = get_videos(movie['id'])
            if videos:
                print("Videos:")
                for video in videos:
                    print(f"- {video['name']} ({video['type']}) on {video['site']}")
            
        if c.lower() == 's':     # Get the similar movies
            # Fetch similar movies
            similar_movies = get_similar_movies(movie_id=movie['id'], max_results=5)

            # Print the similar movies
            print("\nSimilar Movies:")
            for movie in similar_movies:
                print(f"Title: {movie['title']}, Release Date: {movie['release_date']}, Rating: {movie['vote_average']}")

    quit()
    pretty_json = json.dumps(response.json(), indent=4)
    # print(response.text)
    print(type(response.text))
    print(pretty_json)