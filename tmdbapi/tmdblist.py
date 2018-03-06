from .tmdbbase import TMDBBase


class TMDBList(TMDBBase):
    '''
        This class implements the list feature
        of TMDB API.

        More info: https://developers.themoviedb.org/3/lists

        Currently under develpment.
        API method  :   Status
        Get Details :   Working thru info()
        Others      :   To be implemented
    '''

    def __init__(self, id):
        self.id = id

    def info(self):
        '''
            Implements "Get Details"
            https://developers.themoviedb.org/3/lists/get-list-details
        '''
        return TMDBList.api_call(str(self.id))
