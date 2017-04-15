import webbrowser

# Importing the webbrowser from Python standard library

class Movie():
    """ The Movie class creates a object for each movie and allocates memory
        to store movie information"""

    VALID_RATINGS = ['G','PG','PG-13','R']
    
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """init method initialises movie content to the attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """this method will pop up the browser tap with the Movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
