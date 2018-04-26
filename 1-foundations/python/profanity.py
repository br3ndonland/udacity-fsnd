# Profanity checker mini-project
# Code rewritten for Requests

import requests


def read_text():
    """Read the contents of a text file."""
    quotes = open('movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    """Check the text file for profanity."""
    # web query
    r = requests.get('http://www.wdylike.appspot.com/?q=' + text_to_check)
    # output
    if 'true' in r.text:
        print('Profanity Alert!')
    elif 'false' in r.text:
        print('This document has no curse words!')
    else:
        print('Could not scan the document properly.')


read_text()
