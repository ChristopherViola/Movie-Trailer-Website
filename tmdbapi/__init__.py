import requests
import config

# Retrieve the api key from configuration file
TMDB_API_KEY = config.api_key
# Define constant API base url
TMDB_API_URL = 'https://api.themoviedb.org/3/'
# start a session
session = requests.Session()
# Initialize session params
session.params = {}
# Store our params
session.params['api_key'] = TMDB_API_KEY
session.params['api_url'] = TMDB_API_URL

from .tmdbmovie import TMDBMovie
from .tmdblist import TMDBList
