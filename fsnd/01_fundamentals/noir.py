# Udacity full-stack web developer nanodegree
# 01. Programming fundamentals and the web
# Lesson 09: Make classes: movie website
# Movie Website Mini-Project

# import the media file, which contains the class definition
import media
import fresh_tomatoes_noir

# film noir: double_indemnity
double_indemnity = media.Movie(
    "Double Indemnity, 1944",
    "An insurance agent tries to game the system and win his love interest",
    "https://upload.wikimedia.org/wikipedia/en/3/35/Double_indemnity.jpg",
    "https://www.youtube.com/watch?v=l7AjKUDyrCE")

# film noir: out_of_the_past
out_of_the_past = media.Movie(
    "Out of the Past, 1947",
    "A man begins a new life in a small town, but has to confront his past",
    "https://upload.wikimedia.org/wikipedia/en/a/a6/Outofthepast.jpg",
    "https://www.youtube.com/watch?v=fryuS6Zd_mc")

# neo noir: chinatown
chinatown = media.Movie(
    "Chinatown, 1974",
    "A detective tries to unravel a conspiracy in 1937 Los Angeles",
    "https://upload.wikimedia.org/wikipedia/en/3/38/Chinatownposter1.jpg",
    "https://www.youtube.com/watch?v=20FfiP7g4tU")

# neo noir: body_heat
body_heat = media.Movie(
    "Body Heat, 1981",
    "An attorney meets a beautiful woman and gets mixed up in a murder",
    "https://upload.wikimedia.org/wikipedia/en/2/2c/Body_heat_ver1.jpg",
    "https://www.youtube.com/watch?v=cXGlUtoYtNE")

# future noir: blade_runner
blade_runner = media.Movie(
    "Blade Runner, 1982",
    "A detective hunts renegade replicants in dystopian Los Angeles 2019",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
    "https://www.youtube.com/watch?v=qoEyZoOTtss")

# future noir: the_terminator
the_terminator = media.Movie(
    "The Terminator, 1984",
    "A combat cyborg is sent back in time to stop its human enemy",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",
    "https://www.youtube.com/watch?v=-fN82upbGPo")

movies = [double_indemnity, out_of_the_past, chinatown, body_heat,
          blade_runner, the_terminator]
fresh_tomatoes_noir.open_movies_page(movies)
