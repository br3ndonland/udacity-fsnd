# Flask

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088)

Lesson 3. Flask

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Lesson overview](#lesson-overview)
  - [01. Introducing Frameworks and Flask](#01-introducing-frameworks-and-flask)
  - [02. Lesson 3 Overview](#02-lesson-3-overview)
  - [03. Running Your First Flask Application](#03-running-your-first-flask-application)
  - [04. Quiz: First Flask App Quiz](#04-quiz-first-flask-app-quiz)
- [Database](#database)
  - [05. Adding Database to Flask Application](#05-adding-database-to-flask-application)
  - [06. Quiz: Adding Database to Flask Application Quiz](#06-quiz-adding-database-to-flask-application-quiz)
  - [07. Routing](#07-routing)
  - [08. Quiz: Routing Create Quiz](#08-quiz-routing-create-quiz)
- [Templates](#templates)
  - [09. Templates](#09-templates)
  - [10. Quiz: Templates Quiz](#10-quiz-templates-quiz)
- [URL for](#url-for)
  - [11. Quiz: URL for Quiz](#11-quiz-url-for-quiz)
- [Forms](#forms)
  - [12. Form Requests and Redirects](#12-form-requests-and-redirects)
  - [13. Quiz: Edit Menu Item Form Quiz](#13-quiz-edit-menu-item-form-quiz)
  - [14. Quiz: Delete Menu Item](#14-quiz-delete-menu-item)
- [Message flashing](#message-flashing)
  - [15. Message Flashing](#15-message-flashing)
  - [16. Quiz: Message Flashing Quiz](#16-quiz-message-flashing-quiz)
- [Styling](#styling)
  - [17. Quiz: Styling](#17-quiz-styling)
- [JSON](#json)
  - [18. Responding With JSON](#18-responding-with-json)
  - [19. Quiz: JSON Quiz](#19-quiz-json-quiz)
  - [20. Lesson 3 Wrap-Up](#20-lesson-3-wrap-up)
- [Feedback on Lesson 3](#feedback-on-lesson-3)

## Lesson overview

### 01. Introducing Frameworks and Flask

Frameworks take care of repetitive tasks and allow us to focus on unique features of our projects. Lorenzo likened frameworks to cake mix. The manual web server code we did in the last lesson is like baking from scratch.

### 02. Lesson 3 Overview

- Database
- Templates
- url_for
- Forms
- Message flashing
- JSON
- Styling

### 03. Running Your First Flask Application

Simple "Hello, World!" Flask app

```python
# Import Flask class from flask library
from flask import Flask
# Create an instance of class Flask
# Each time the application runs, a special variable 'name' is defined.
app = Flask(__name__)


# Decorators that wrap our function inside Flask's 'app.route' function.
@app.route('/')  # This is a decorator.
@app.route('/hello')
def HelloWorld():
    return "Hello World"


# "if __name__ == '__main__':" describes what to do if the code is being
# executed by the Python interpreter.
# The app run by the Python interpreter is assigned '__main__' to its
# name variable.
# If the file is imported instead, the 'if' statement will not run.
# Other imported Python files are assigned the name of the Python file.
if __name__ == '__main__':
    # Turn on debugging to reload when code is changed
    app.debug = True
    # Listen on all public IP addresses for compatibility with vagrant
    app.run(host='0.0.0.0', port=5000)

```

Instructor notes:

A quick tutorial on decorators:

[http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)

View the code for [project.py](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-3/01_First-Flask-App/project.py)

### 04. Quiz: First Flask App Quiz

`@app.route('/')` is needed to specify behavior for the homepage.

## Database

### 05. Adding Database to Flask Application

Importing the SQLAlchemy code for the restaurant database.

<details>
  <summary>Code from project.py</summary>

```python
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')
def HelloWorld():
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
    return output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

```

</details>

### 06. Quiz: Adding Database to Flask Application Quiz

### 07. Routing

URL creation can be automated with naming rules:

```text
path/<type: variable_name>/path/
```

`type` can be `int`, `string`, or `path`.

It is helpful to leave the trailing slash.

### 08. Quiz: Routing Create Quiz

## Templates

### 09. Templates

Flask allows storage of HTML templates with

```text
render_template(variable, keyword_objects)
```

so you don't have to repeatedly type `output` strings. Usually, developers create a sub-directory called *templates- and put their templates there.

*HTML escaping- allows transfer of data from Python and databases into HTML.

### 10. Quiz: Templates Quiz

```text
{% logical code for Python %}
{{ printed output code }}
```

HTML templates don't get to use Python indendation and spacing, so we have to inclde instructions to terminate loops:

```text
{% endfor %}
{% endif %}
```

## URL for

### 11. Quiz: URL for Quiz

URLs can be mapped to specific Python functions with `url_for()`

```html
<a href='{{url_for('editMenuItem', restaurant_id = restaurant.id, menu_id = i.id) }}'>Edit</a>

</br>
<a href = '{{url_for('deleteMenuItem', restaurant_id = restaurant.id, menu_id = i.id ) }}'>Delete</a>
```

Instructor notes

> Download the [menu.html file](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-3/07_Menu-Template-Quiz/menu.html). Add url_for() links to edit and delete each menu item
>
> Flask Documentation for url_for can be found [here](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-3/10_url_for-Solution/menu.html).

## Forms

### 12. Form Requests and Redirects

### 13. Quiz: Edit Menu Item Form Quiz

### 14. Quiz: Delete Menu Item

## Message flashing

### 15. Message Flashing

Flask includes a messaging system to notify users after actions are completed. It uses sessions to persist settings across multiple web pages. It is invoked with `flash('Message here!')`. Retrieve flashed messages with `get_flashed_messages()`

`app.secret_key = 'key_name'` is used to establish sessions.

I need sessions to persist the color scheme on my [Udacity portfolio site](https://br3ndonland.github.io/udacity/)!

> Errata:
>
> Around 1:20 in the video, the instructor mentions adding code to newmenuitem.html. However, the file he is actually editing is menu.html. To follow along with this instruction, you should edit menu.html and not newmenuitem.html.
> Instructor notes:
>
> https://github.com/udacity/Full-Stack-Foundations/tree/master/Lesson-3/16_Flash-Messaging
> Click here to learn more about the 'with' statement in python: http://effbot.org/zone/python-with-statement.htm


### 16. Quiz: Message Flashing Quiz

## Styling

### 17. Quiz: Styling

Flask can look for CSS, JS, and media files inside of a *static/- directory.

## JSON

### 18. Responding With JSON

Let's say there's a service called *yum!- that wants to read data from your restaurant menu database and display it to users based on their location. To see the list of restaurants and menus in the database, *yum!- doesn't need to waste bandwith parsing HTML and CSS, it just needs the data.

What do we need? I knew the answer- an **API**! I've been wanting to get into APIs for a while now. Finally!

**RESTful*- - REpresentational State Transfer. Sending the data over the internet with HTTP.

**API*- - Application Programming Interface

APIs frequently use **JSON*- (JavaScript Object Notation), which uses `{"key": "value",}` pairs. The Flask `jsonify` package allows us to easily configure an API endpoint for the application. `jsonify` converts our database into JSON.

### 19. Quiz: JSON Quiz

### 20. Lesson 3 Wrap-Up

## Feedback on Lesson 3

Lorenzo did a great job with this lesson. All of his instructor materials were well-crafted, and it is very useful to learn the Flask framework.

[(Back to TOC)](#table-of-contents)