'''
    Run the flask app defined in entertainment_center
    and open a web browser pointing to the home page
'''

from entertainment_center import app
import threading
import time
import webbrowser


def start_browser():
    '''
        Open your web browser after a short delay
        that should be enough to let Flask's server start.
    '''
    time.sleep(1)
    webbrowser.open('http://127.0.0.1:5000/')


browser_thread = threading.Thread(target=start_browser)
browser_thread.start()
app.run(host='127.0.0.1', port=5000)
