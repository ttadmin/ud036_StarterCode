""" This module contains the movie content to be displayed. """
import media
import fresh_tomatoes

# Begin Constants
TOY_STORY = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


AVATAR = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")


RED_DAWN = media.Movie("Red Dawn",
                       "A group of American kids fights a Russian invasion.",
                       "https://upload.wikimedia.org/wikipedia/en/f/f0/Red_dawn.jpg",
                       "https://www.youtube.com/watch?v=1_I4WgBfETc")


MOVIES = [AVATAR, RED_DAWN, TOY_STORY]


TARGET_SITE = fresh_tomatoes.NewTomato()
# End Constants


TARGET_SITE.open_movies_page(MOVIES)
