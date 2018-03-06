from . import session


class TMDBBase(object):
    ''' Base class that implements an API call.
    Any inerithed class will be able to fetch its base url
    extracted from the class name '''

    # base url property
    base_url = session.params['api_url']

    @classmethod
    def api_call(cls, action):
        '''
            This is a class method.
            Any child will call its own method accordingly to its name.
            TMDBxxx will call xxx method and so on.'''
        url = TMDBBase.base_url
        # Extract method from class name
        cls_url = cls.__name__[4:].lower()
        # If this is not TMDBBase
        if (cls_url != 'base'):
            # Append class name to API url
            url = url + cls_url + '/'
        # Append requested action to the method
        path = url + action
        # Make the actual call
        response = session.get(path)
        # Return the response in Json format
        return response.json()
