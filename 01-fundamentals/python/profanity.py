from urllib.request import urlopen


def read_text():
    """Read the contents of a text file."""
    quotes = open('movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    """Check the text file for profanity."""
    connection = urlopen('http://www.wdylike.appspot.com/?q=' + text_to_check)
    output = connection.read()
    print(output)
    connection.close()


read_text()
