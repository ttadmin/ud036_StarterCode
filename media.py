""" This module contains only the Movie class. """
import webbrowser

class Movie():
    """ This class provides a way to store movie related information. """

    # Begin Constants
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # End Constants

    # Begin Constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # End Constructor

    # Begin Public Methods
    def show_trailer(self):
        """ This method provides the functionality to actually
            open the move link in a browser window. """
        webbrowser.open(self.trailer_youtube_url)

    def submit_review(self):
        """ This is a stubbed method that will allow users to
            submit their own reviews in the future."""
    # End Public Methods
