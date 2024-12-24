# MovieDB Streamlit App

## Description

The **MovieDB Streamlit App** is a user-friendly interface for exploring movie data using the TMDB (The Movie Database) API. This app is designed to provide an intuitive and elegant experience for users, enabling them to search for movies, view detailed information, and explore related data directly from TMDB.

The project leverages a Python class, `MovieDB`, to handle all API interactions and integrates it seamlessly with a Streamlit-based UI to deliver a modern and polished user interface.

---

## Features

- **Movie Search**: Search for movies by title and retrieve detailed information.
- **Elegant Design**: Modern and user-friendly interface, designed for simplicity and ease of use.
- **TMDB Integration**: Fetches real-time movie data from TMDB API.
- **Modular Architecture**: Clean separation between API logic (`MovieDB`) and the UI.
- **Open Source**: Well-documented and ready for contribution.

---

## Project Structure

```plaintext
.
├── moviedb.py         # Contains the MovieDB class for API interactions
├── app.py             # Streamlit UI implementation
├── requirements.txt   # List of required Python packages
├── README.md          # Project documentation
└── design_assets/     # Assets for the UI design (optional)
```

---

## Prerequisites

Before running the app, ensure you have the following installed:

- Python (version matching your environment)
- pip (Python package installer)

---

## Installation and Setup

Follow these steps to set up and run the application:

### Step 1: Clone the Repository

```bash
git clone https://github.com/oariasz/moviedb-streamlit-app.git
cd moviedb-streamlit-app
```

### Step 2: Create a Virtual Environment

Replace `3.x.x` with your exact Python version if needed.

```bash
python3.x.x -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up TMDB API Key

1. Sign up for an API key from [TMDB's API](https://www.themoviedb.org/documentation/api).
2. Create a `.env` file in the project root and add your API key:

   ```plaintext
   TMDB_API_KEY=your_api_key_here
   ```

### Step 5: Run the Streamlit App

```bash
streamlit run app.py
```

---

## Usage

### Searching for Movies

1. Enter the movie title in the search bar.
2. View results with detailed information, including:
   - Title
   - Overview
   - Release date
   - Ratings
   - Related movies (if available).

### Exploring Details

- Click on any movie result to see additional details and recommendations.

---

## Development

### Code Overview

- **`moviedb.py`**:
  - Contains the `MovieDB` class that handles all TMDB API requests.
  - Modular and reusable for other applications.

- **`app.py`**:
  - Implements the Streamlit-based UI.
  - Fetches data via the `MovieDB` class and displays it elegantly.

### Adding Features

Feel free to extend the app by adding new features, such as:
- Actor/Director information
- Sorting and filtering options
- Genre-based searches

---

## Publishing to GitHub

1. Initialize a local repository:

   ```bash
   git init
   git remote add origin https://github.com/oariasz/moviedb-streamlit-app.git
   ```

2. Commit and push changes:

   ```bash
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

---

## Contributions

We welcome contributions! If you’d like to add features or fix bugs:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

For any questions or suggestions, please reach out to:

- **Email**: [oariasz72@gmail.com](mailto:oariasz72@gmail.com)
- **GitHub**: [oariasz](https://github.com/oariasz)

---