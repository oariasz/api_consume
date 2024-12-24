import streamlit as st
from moviedb import MovieDB

# Initialize TMDB API client
tmdb = MovieDB()

# Page Title
st.title("🎥 TMDB Explorador de Películas")
st.write("Explora los detalles de tus películas favoritas, trailers, recomendaciones, y más usando la API de The Movie Database!")

# Movie Search Section
movie_query = st.text_input("🔍 Buscar película", placeholder="Escriba el nombre de una película y presiona Enter...")

if movie_query:
    # Fetch Search Results
    search_results = tmdb._make_request("/search/movie", params={"query": movie_query, "include_adult": False})

    if search_results and "results" in search_results:
        movies = sorted(search_results["results"], key=lambda x: x["popularity"], reverse=True)

        for movie in movies:
            st.write("---")
            st.subheader(movie["title"])
            st.write(f"**Fecha de Lanzamiento:** {movie.get('release_date', 'Unknown')}")
            st.write(f"**Popularidad:** {movie.get('popularity', 'N/A')}")
            st.write(f"**Rating Promedio:** {movie.get('vote_average', 'N/A')} / 10")

            # Display Poster
            poster_path = f"https://image.tmdb.org/t/p/original{movie.get('poster_path')}" if movie.get('poster_path') else None
            if poster_path:
                st.image(poster_path, width=150)
            
            # Button to Show More Details
            if st.button(f"Ver Detalles de {movie['title']}", key=movie["id"]):
                st.session_state.selected_movie_id = movie["id"]
                break

        # Display a message if no more results are available
        if not movies:
            st.warning("No se encontró esa película")

# Movie Details Section
if "selected_movie_id" in st.session_state:
    movie_id = st.session_state.selected_movie_id
    movie_details = tmdb.get_movie_details(movie_id)

    if movie_details:
        st.write("---")
        st.header(f"🎬 {movie_details['title']}")
        st.write(f"**Reseña:** {movie_details.get('overview', 'No hay reseña disponible.')}")
        st.write(f"**Fecha de Lanzamiento:** {movie_details.get('release_date', 'Unknown')}")
        st.write(f"**Duración:** {movie_details.get('runtime', 'N/A')} minutes")
        st.write(f"**Director:** {tmdb.get_director(movie_id)}")
        st.write(f"**Géneros:** {', '.join([genre['name'] for genre in movie_details.get('genres', [])])}")
        st.write(f"**Rating:** {movie_details.get('vote_average', 'N/A')} / 10")

        # Display Poster and Backdrop
        poster_path = tmdb.get_all_images(movie_id, "posters")[0] if tmdb.get_all_images(movie_id, "posters") else None
        if poster_path:
            st.image(poster_path, caption="Movie Poster", use_column_width=True)

        # Display Trailers
        trailers = tmdb.get_trailers(movie_id)
        if trailers:
            st.subheader("📽️ Trailers")
            for trailer in trailers:
                st.video(f"https://www.youtube.com/watch?v={trailer['key']}")

        # Display Recommendations
        recommendations = tmdb.get_recommendations(movie_id)
        if recommendations:
            st.subheader("🍿 Recomendadas")
            for rec in recommendations[:5]:  # Show top 5 recommendations
                rec_poster = f"https://image.tmdb.org/t/p/original{rec.get('poster_path')}" if rec.get('poster_path') else None
                col1, col2 = st.columns([1, 5])
                with col1:
                    if rec_poster:
                        st.image(rec_poster, width=100)
                with col2:
                    st.write(f"**{rec['title']}**")
                    st.write(f"Release Date: {rec.get('release_date', 'Desconocido')}")
                    st.write(f"Rating: {rec.get('vote_average', 'N/A')} / 10")

        # Display Cast
        st.subheader("🎭 Elenco")
        cast = tmdb.get_credits(movie_id)
        for actor in cast[:10]:  # Show top 10 cast members
            st.write(f"{actor['name']} as {actor['character']}")

        # Reviews Section
        reviews = tmdb.get_reviews(movie_id)
        if reviews:
            st.subheader("📝 Opiniones")
            for review in reviews[:5]:  # Show top 5 reviews
                st.write(f"**{review['author']}**: {review['content']}")

# Footer
st.write("---")
st.markdown("**TMDB Explorador de Películas** - Desarrollado por Omar Arias - Estratek")
