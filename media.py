'''
    Contains class definitions for some media types.
    Retrieved from Udacity's Full Stack Developer Nanodegree.
'''


class Movie():
    '''
        Movie class from Udacity course.
        Holds data for a movie.
    '''

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.story_line = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
