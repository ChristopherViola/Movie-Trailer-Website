from .tmdbbase import TMDBBase


class TMDBMovie(TMDBBase):
    '''
    This class implements the movie feature of TMDB API.

    More info: https://developers.themoviedb.org/3/movies

    Currently under develpment.

    API method  :   Status

    Get Details :   Working thru info()

    Get Videos  :   Working thru videos()

    Get Popular :   Working thru popular() (static method)

    Get Top Rated :   Working thru top_rated() (static method)

    Get Upcoming :   Working thru upcoming() (static method)

    Others      :   To be implemented
    '''

    def __init__(self, id):
        self.id = id

    def info(self):
        '''
            Implements "Get Details"
            https://developers.themoviedb.org/3/lists/get-movie-details
        '''
        return TMDBMovie.api_call(str(self.id))

    def videos(self):
        '''
            Implements "Get Videos"
            https://developers.themoviedb.org/3/movies/get-movie-videos
        '''
        return TMDBMovie.api_call(str(self.id)+'/videos')

    @staticmethod
    def popular():
        '''
            Implements "Get Popular"
            https://developers.themoviedb.org/3/movies/get-popular-movies
        '''
        return TMDBMovie.api_call('popular')

    @staticmethod
    def top_rated():
        '''
            Implements "Get Top Rated"
            https://developers.themoviedb.org/3/movies/get-top-rated-movies
        '''
        return TMDBMovie.api_call('top_rated')

    @staticmethod
    def upcoming():
        '''
            Implements "Get Upcoming"
            https://developers.themoviedb.org/3/movies/get-upcoming
        '''
        return TMDBMovie.api_call('upcoming')
