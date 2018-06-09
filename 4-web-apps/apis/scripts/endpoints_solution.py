from flask import Flask

app = Flask(__name__)
# Create the appropriate app.route() functions. Test and see if they work.


# Make an app.route() decorator for the URI '/puppies'
@app.route('/puppies')
def puppies_function():
    """App route function for the URI '/puppies'."""
    return "Yes, puppies!"


# Make an app.route() decorator here that takes in an integer named 'id'
# for when the client visits a URI like "/puppies/5"
@app.route('/puppies/<int:id>')
def puppies_function_id(id):
    """App route function for the URI '/puppies/' with id integer."""
    return 'This method will act on the puppy with id {}'.format(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
