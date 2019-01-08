import media
from flask import Flask, render_template, url_for
from tmdbapi import TMDBMovie, TMDBList

app = Flask(__name__)

nav = [
    ("/", "home", "Home"),
    ("/populars/", "populars", "Populars"),
    ("/top-rated/", "top-rated", "Top Rated"),
    ("/upcoming/", "upcoming", "Upcoming")
]


def get_trailer_id(videos):
    # Fetch videos returned from the API call
    for video in videos['results']:
        # Looking for Youtube trailer
        if (video['type'] == 'Trailer' and video['site'] == "YouTube"):
            return video['key'].replace('http:', 'https:')
    return ''


def get_media_movie_list(tmdbmovies, limit=18):
    '''
        This function fetches results from the api call,
        for each of them get the trailer id and build
        the image path. This function return a list of
        media.Movie instances
    '''
    movie_list = list()
    i = 0
    # API slightly different json formats on different methods
    # Sometimes movies are stored in 'results' field other in 'items' field
    # Either cases we instanciate a TMDBMovie object, retrieve its videos and
    # pass those to get_trailer_id to get the trailer, build the image path
    # and in the end we create a corresponding media.Movie object and store it
    # in a list that will be returned from the function
    if ("results" in tmdbmovies):
        for item in tmdbmovies["results"]:
            movie = TMDBMovie(item['id'])
            videos = movie.videos()
            trailer = get_trailer_id(videos)
            image = 'https://image.tmdb.org/t/p/w342' + item['poster_path']
            movie_list.append(media.Movie(
                item['title'], item['overview'], image, trailer))
            i = i + 1
            if (i >= limit):
                break
    elif ("items" in tmdbmovies):
        for item in tmdbmovies["items"]:
            movie = TMDBMovie(item['id'])
            videos = movie.videos()
            trailer = get_trailer_id(videos)
            image = 'https://image.tmdb.org/t/p/w342' + item['poster_path']
            movie_list.append(media.Movie(
                item['title'], item['overview'], image, trailer))
            i = i + 1
            if (i >= limit):
                break
    return movie_list


@app.route("/")
def home():
    '''
        Return the list of my favourite movies.
        The list id is hardcoded for simplicity.
    '''
    # Instanciate a TMDBList with the id of my list
    my_list = TMDBList(47599)
    # Get the list as media.Movie objects passing the json
    # retrieved from the API to get_media_movie_list()
    movie_list = get_media_movie_list(my_list.info())
    # Render the template with Flask and serve it
    return render_template("media.html", navbar=nav, title='Home',
                           active_page="home", medias=movie_list)


@app.route("/populars/")
def populars():
    # Use the 'popular' static method of TMDBMovie class
    # to retrieve the popular movies
    movies = TMDBMovie.popular()
    # Get the list as media.Movie objects passing the json
    # retrieved from the API to get_media_movie_list()
    movie_list = get_media_movie_list(movies)
    # Render the template with Flask and serve it
    return render_template("media.html", navbar=nav, title='Populars',
                           active_page="populars", medias=movie_list)


@app.route("/top-rated/")
def top_rated():
    # Use the 'top_rated' static method of TMDBMovie class
    # to retrieve the top rated movies
    movies = TMDBMovie.top_rated()
    # Get the list as media.Movie objects passing the json
    # retrieved from the API to get_media_movie_list()
    movie_list = get_media_movie_list(movies)
    # Render the template with Flask and serve it
    return render_template("media.html", navbar=nav, title='Top Rated',
                           active_page="top-rated", medias=movie_list)


@app.route("/upcoming/")
def upcoming():
    # Use the 'upcoming' static method of TMDBMovie class
    # to retrieve the upcoming movies
    movies = TMDBMovie.upcoming()
    # Get the list as media.Movie objects passing the json
    # retrieved from the API to get_media_movie_list()
    movie_list = get_media_movie_list(movies)
    # Render the template with Flask and serve it
    return render_template("media.html", navbar=nav, title='Upcoming',
                           active_page="upcoming", medias=movie_list)
