# Project: TMDB Streamlit UI
## Project Description
This project utilizes the TMDB API to create a user-friendly Streamlit interface for browsing and exploring movie information. It features a clean and modern design with intuitive navigation, allowing users to search for movies, view details, and discover recommendations.

## Features
Movie Search: Search for movies by title.
Movie Details: View movie details, including:
Title
Release Date
Popularity
Rating
Duration
Director
Overview
Cast
Recommendations
Watch Providers
Posters
Backdrops
Navigation: Navigate between movies using "previous" and "next" buttons.
Clear Search: Clear the search query and reset the UI.
Setup Instructions
Create a Virtual Environment:
bash

## Verify

Open In Editor
Run
Copy code
python -m venv .venv
source .venv/bin/activate
Install Dependencies:
bash

## Verify

Open In Editor
Run
Copy code
pip install -r requirements.txt
Set Environment Variable:
Create a .env file in the project root.
Add the following line, replacing YOUR_API_KEY with your actual TMDB API key:

## Verify

Open In Editor
Run
Copy code
TMDB_API_KEY=YOUR_API_KEY
Run the Application:
bash

## Verify

Open In Editor
Run
Copy code
streamlit run streamlit_app.py
Usage Instructions
MovieDB API (moviedb.py):

## Initialization:

Import the MovieDB class from moviedb.py.
Create an instance of MovieDB.
The api_key will be automatically loaded from the .env file.
Methods:

* get_movie_details(movie_id): Fetches details of a movie by its TMDB ID.
* get_runtime(movie_id): Retrieves the runtime of a movie.
* get_providers(movie_id, country_code="US"): Gets watch providers for a movie in the specified country.
* get_credits(movie_id): Retrieves the cast of a movie.
* get_similar_movies(movie_id, max_results=10): Fetches similar movies

# UI

BLACKBOXAI

This appears to be a wireframe of a movie browsing application. Here is a breakdown of the elements:

Main Sections

Title: This section contains the title of the movie.
Details: Contains further details about the movie, such as release date, popularity, rating, duration, director, and crew.
Movie Overview: This section contains a brief overview of the movie.
Movie Query: This section allows users to search for movies.
Recommended: This section lists movies that the user may be interested in.
Navigation Elements

Previous Movie: Navigates to the previous movie in a list or search results.
Next Movie: Navigates to the next movie in a list or search results.
Clear: Clears the movie query or search.
More: Provides additional information or options.
User Interface Elements

Movie Image (Poster): Displays the movie poster.
Movie Poster Thumbnails: Small images representing the recommended movies.
Trailers: Link to trailers for the movie.
Additional Features:

User Input: The "Movie Query" area allows users to search or enter movie titles.
Data Display: The application displays various details about the movie based on user interaction or selections.
Possible Functionality

Movie Search: Users can search for movies by title, genre, director, or actors.
Movie Recommendations: The app recommends movies based on user preferences or viewing history.
Movie Detail View: The app provides a detailed view of a movie, including its synopsis, cast, crew, reviews, and trailers.
Movie List/Gallery: The app displays a list or gallery of movies, potentially organized by category, release date, popularity, or rating.
Note: The wireframe provides a high-level view of the application's layout and features. The actual implementation might involve additional elements and interactions.