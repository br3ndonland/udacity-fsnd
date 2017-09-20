# Udacity full-stack web developer nanodegree
# 01. Programming fundamentals and the web
# Lesson 09: Make classes: movie website


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        pass
