# Udacity full-stack web developer nanodegree
# 01. Programming fundamentals and the web
# Lesson 09: Make classes: movie website


# import the media file, which contains the class definition
import media
import webbrowser

# create an object, or specific instance, of the class Movie
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")
print(toy_story.storyline)
print(media.Movie.valid_ratings)

# add another instance
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=a0CDJZu4M5I")
print(avatar.storyline)
webbrowser.open_new_tab(avatar.trailer_youtube_url)

# instance for 12. Quiz: Play Your Favorite Trailer
# blade_runner
blade_runner = media.Movie(
    "Blade Runner",
    "A detective hunts renegade replicants in dystopian Los Angeles 2019",
    "https://en.wikipedia.org/wiki/File:Blade_Runner_poster.jpg",
    "https://www.youtube.com/watch?v=qoEyZoOTtss")
print(blade_runner.storyline)
webbrowser.open_new_tab(blade_runner.trailer_youtube_url)

# additions for Lesson 10_03: using predefined class variables
print(media.Movie.__doc__)  # documentation function
print(media.Movie.__name__)  # prints the class function name
print(media.Movie.__module__)  # prints module name
