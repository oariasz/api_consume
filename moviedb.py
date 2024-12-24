import requests
import os
import json
from dotenv import load_dotenv


class MovieDB:
    """Class to interact with The Movie Database (TMDB) API."""

    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, language="en-US"):
        """
        Initialize the MovieDB class with an API key and language.

        Args:
            api_key (str): TMDB API key.
            language (str): Language for responses (default: "en-US").
        """
        load_dotenv()
        self.api_key = os.getenv("TMDB_API_KEY")

        if not self.api_key:
            raise ValueError("TMDB_API_KEY not found in the .env file.")
        print(f"TMDB_API_KEY Loaded!")
        self.language = language

    def _make_request(self, endpoint, params=None):
        """
        Helper method to make a GET request to the TMDB API.

        Args:
            endpoint (str): The API endpoint to query.
            params (dict): Query parameters for the request.

        Returns:
            dict: JSON response from the API.
        """
        if params is None:
            params = {}
        params["api_key"] = self.api_key
        params["language"] = self.language
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        # print('make_request: -------------------------')
        # print(f"{self.BASE_URL}{endpoint}")
        # print(params)
        # print('make_request: -------------------------')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            return None

    def get_movie_details(self, movie_id):
        """Fetches all details of a movie."""
        return self._make_request(f"/movie/{movie_id}")

    def get_runtime(self, movie_id):
        """Get the runtime of a movie."""
        details = self.get_movie_details(movie_id)
        return details.get("runtime", "N/A") if details else "N/A"

    def get_providers(self, movie_id, country_code="US"):
        """Get watch providers for a movie."""
        data = self._make_request(f"/movie/{movie_id}/watch/providers")
        if data:
            return data.get("results", {}).get(country_code, {})
        return {}

    def get_credits(self, movie_id):
        """Get the cast of a movie."""
        data = self._make_request(f"/movie/{movie_id}/credits")
        return data.get("cast", []) if data else []

    def get_similar_movies(self, movie_id, max_results=10):
        """Get similar movies."""
        similar_movies = []
        page = 1
        while len(similar_movies) < max_results:
            data = self._make_request(f"/movie/{movie_id}/similar", params={"page": page})
            if data and "results" in data:
                similar_movies.extend(data["results"][: max_results - len(similar_movies)])
                if page >= data.get("total_pages", 1):
                    break
                page += 1
            else:
                break
        return similar_movies

    def get_rating(self, movie_id):
        """Get the rating of a movie."""
        details = self.get_movie_details(movie_id)
        return details.get("vote_average") if details else None

    def get_videos(self, movie_id):
        """Get videos (trailers, teasers) for a movie."""
        data = self._make_request(f"/movie/{movie_id}/videos")
        return data.get("results", []) if data else []

    def get_trailers(self, movie_id):
        """Get trailers for a movie."""
        videos = self.get_videos(movie_id)
        return [video for video in videos if video.get("type") == "Trailer"]

    def get_all_images(self, movie_id, image_type=None):
        """
        Get images (posters, backdrops, logos) for a movie.

        Args:
            movie_id (int): The TMDB ID of the movie.
            image_type (str): Type of images to fetch ('posters', 'backdrops', 'logos').

        Returns:
            list or dict: List of URLs for the specified image type, 
                        or a dictionary of all image types if no type is specified.
        """
        
        data = self._make_request(f"/movie/{movie_id}/images")
        # TODO: print(f'URL con json de imágenes: {self.BASE_URL}/movie/{movie_id}/images')
        if not data:
            print('ERROR: NO HAY DATA')
            return {}

        # TODO: print(json.dumps(data, indent=4))  # Check the structure of the JSON

        if image_type:
            # Return specific image type as a list of URLs
            images = data.get(image_type, [])
            return [f"https://image.tmdb.org/t/p/original{img['file_path']}" for img in images]

        # Return all image types as a dictionary
        print('Todos los tipos de imágenes!!!!')
        all_images = {
            "posters": [f"https://image.tmdb.org/t/p/original{img['file_path']}" for img in data.get("posters", [])],
            "backdrops": [f"https://image.tmdb.org/t/p/original{img['file_path']}" for img in data.get("backdrops", [])],
            "logos": [f"https://image.tmdb.org/t/p/original{img['file_path']}" for img in data.get("logos", [])]
        }
        
        # print(json.dumps(data, indent=4))  # Check the structure of the JSON
        return all_images
    
    def get_reviews(self, movie_id):
        """Get reviews for a movie."""
        data = self._make_request(f"/movie/{movie_id}/reviews")
        return data.get("results", []) if data else []

    def get_genres(self, movie_id):
        """Get genres for a movie."""
        details = self.get_movie_details(movie_id)
        return details.get("genres", []) if details else []

    def get_recommendations(self, movie_id):
        """Get movie recommendations."""
        data = self._make_request(f"/movie/{movie_id}/recommendations")
        return data.get("results", []) if data else []

    def get_director(self, movie_id):
        """Get the director of a movie."""
        data = self._make_request(f"/movie/{movie_id}/credits")
        if data:
            for crew in data.get("crew", []):
                if crew.get("job") == "Director":
                    return crew.get("name")
        return None

    def get_overview(self):
        overview = movie['overview']
        return overview

    def get_poster_path(self):
        path = f"https://image.tmdb.org/t/p/original{movie['poster_path']}"
        return path
    
    def get_backdrop_path(self):
        path = f"https://image.tmdb.org/t/p/original{movie['backdrop_path']}"
        return path
    
    
# FRONT-END functions
def get_query(message='Introduzca el nombre de la película: '):
    print()
    query = input(message)
    if query:
        return query
    else:
        return 'The Godfather'
   
# --- MAIN ---
if __name__ == "__main__":
    # Clear the screen
    os.system("clear")
    print("Welcome to the TMDB CLI!")
    print("-" * 30)

    # Initialize the MovieDB class
    # API_KEY = 'd4414ed6f553a656245521410c941e47'  # Replace with your TMDB API key
    
    # Load environment variables from .env file
    load_dotenv()

    tmdb = MovieDB()

    # Example movie search
    # movie_name = "The Godfather"
    movie_name = get_query()
    search_url = f"{tmdb.BASE_URL}/search/movie"
    search_results = tmdb._make_request("/search/movie", params={"query": movie_name, "include_adult": False})

    if search_results and "results" in search_results:
        sorted_movies = sorted(search_results["results"], key=lambda x: x["popularity"], reverse=True)

        for movie in sorted_movies:
            print("\n=========================")
            print(f"ID:           {movie['id']}")
            print(f"Title:        {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            print(f"Popularity:   {movie['popularity']}")
            print(f"Rating:       {tmdb.get_rating(movie['id'])}")
            print(f"Duration:     {tmdb.get_runtime(movie['id'])} minutes")
            print(f"Director:     {tmdb.get_director(movie['id'])}")
            print("\nOptions: Enter - Next | O - Overview | C - Cast | R - Recommended | P - Watch Providers | I - Images | V - Videos | Q - Quit")

            choice = input("Enter your choice: ").lower()
            if choice == "q":
                break
            elif choice == "c":
                cast = tmdb.get_credits(movie["id"])
                print("\nCast:")
                for actor in cast[:10]:
                    print(f"- {actor['name']} as {actor['character']}")
            # elif choice == "s":
            #     similar_movies = tmdb.get_similar_movies(movie["id"])
            #     print("\nSimilar Movies:")
            #     for smovie in similar_movies:
            #         print(f"- {smovie['title']} ({smovie['release_date']})")
            elif choice == "r":
                recommended_movies = tmdb.get_recommendations(movie["id"])
                print("\nRecommended Movies:")
                for rmovie in recommended_movies:
                    print(f"- {rmovie['title']} ({rmovie['release_date']})")                    
            elif choice == "p":
                providers = tmdb.get_providers(movie["id"])
                print("\nWatch Providers:")
                for provider_type, provider_list in providers.items():
                    print(f"{provider_type.capitalize()}:")
                    for provider in provider_list:
                        print(f"- {provider['provider_name']}")
                        
            elif choice == "o":
                print('Overview: ---------------------------------------')
                print(tmdb.get_overview())
                print('-------------------------------------------------')
                # images = tmdb.get_images(movie["id"])
                                        
            elif choice == "i":
                print('\nImages: --------------------------------------')
                print('Poster Path: ', tmdb.get_poster_path())
                print('Backdrop Path: ', tmdb.get_backdrop_path())
                # images = tmdb.get_images(movie["id"])

            elif choice == "v":
                videos = tmdb.get_videos(movie["id"])
                print("\nVideos:")
                for video in videos:
                    print(f"- {video['name']} ({video['type']}) on {video['site']}")
