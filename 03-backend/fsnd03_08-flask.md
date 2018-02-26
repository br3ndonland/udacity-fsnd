# Developing with the Flask framework

**Udacity Full Stack Web Developer Nanodegree program**

Part 03. Backend

Lesson 08. Frameworks

Brendon Smith

br3ndonland

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Lesson 08 overview](#lesson-08-overview)
  - [8.01. Introducing Frameworks and Flask](#801-introducing-frameworks-and-flask)
  - [8.02. Lesson 3 Overview](#802-lesson-3-overview)
  - [8.03. Running Your First Flask Application](#803-running-your-first-flask-application)
  - [8.04. Quiz: First Flask App Quiz](#804-quiz-first-flask-app-quiz)
- [Database](#database)
  - [8.05. Adding Database to Flask Application](#805-adding-database-to-flask-application)
  - [8.06. Quiz: Adding Database to Flask Application Quiz](#806-quiz-adding-database-to-flask-application-quiz)
  - [8.07. Routing](#807-routing)
  - [8.08. Quiz: Routing Create Quiz](#808-quiz-routing-create-quiz)
- [Templates](#templates)
  - [8.09. Templates](#809-templates)
  - [8.10. Quiz: Templates Quiz](#810-quiz-templates-quiz)
- [URL for](#url-for)
  - [8.11. Quiz: URL for Quiz](#811-quiz-url-for-quiz)
- [Forms](#forms)
  - [8.12. Form Requests and Redirects](#812-form-requests-and-redirects)
  - [8.13. Quiz: Edit Menu Item Form Quiz](#813-quiz-edit-menu-item-form-quiz)
  - [8.14. Quiz: Delete Menu Item](#814-quiz-delete-menu-item)
- [Message flashing](#message-flashing)
  - [8.15. Message Flashing](#815-message-flashing)
  - [8.16. Quiz: Message Flashing Quiz](#816-quiz-message-flashing-quiz)
- [Styling](#styling)
  - [8.17. Quiz: Styling](#817-quiz-styling)
- [JSON](#json)
  - [8.18. Responding With JSON](#818-responding-with-json)
  - [8.19. Quiz: JSON Quiz](#819-quiz-json-quiz)
  - [8.20. Lesson 3 Wrap-Up](#820-lesson-3-wrap-up)
- [Feedback on Lesson 08](#feedback-on-lesson-08)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Lesson 08 overview

### 8.01. Introducing Frameworks and Flask

Frameworks take care of repetitive tasks and allow us to focus on unique features of our projects. Lorenzo likened frameworks to cake mix. The manual web server code we did in the last lesson is like baking from scratch.


### 8.02. Lesson 3 Overview

* Database
* Templates
* url_for
* Forms
* Message flashing
* JSON
* Styling


### 8.03. Running Your First Flask Application

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

http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

View the code for [project.py](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-3/01_First-Flask-App/project.py)


### 8.04. Quiz: First Flask App Quiz

`@app.route('/')` is needed to specify behavior for the homepage.


## Database

### 8.05. Adding Database to Flask Application

Importing the SQLAlchemy code for the restaurant database.


### 8.06. Quiz: Adding Database to Flask Application Quiz

### 8.07. Routing

URL creation can be automated with naming rules:

```
path/<type: variable_name>/path/
```

`type` can be `int`, `string`, or `path`.

It is helpful to leave the trailing slash.


### 8.08. Quiz: Routing Create Quiz

## Templates

### 8.09. Templates

Flask allows storage of HTML templates with 

```render_template(variable, keyword_objects)
```

so you don't have to repeatedly type `output` strings. Usually, developers create a sub-directory called *templates* and put their templates there.

*HTML escaping* allows transfer of data from Python and databases into HTML.


### 8.10. Quiz: Templates Quiz

```
{% logical code for Python %}
{{ printed output code }}
```

HTML templates don't get to use Python indendation and spacing, so we have to inclde instructions to terminate loops:

```
{% endfor %}
{% endif %}
```

## URL for

### 8.11. Quiz: URL for Quiz

URLs can be mapped to specific Python functions with `url_for()`

```html
<a href='{{url_for('editMenuItem', restaurant_id = restaurant.id, menu_id = i.id) }}'>Edit</a>

</br>
<a href = '{{url_for('deleteMenuItem', restaurant_id = restaurant.id, menu_id = i.id ) }}'>Delete</a>
```


Instructor notes

> Download the menu.html file. Add url_for() links to edit and delete each menu item
> 
> https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-3/07_Menu-Template-Quiz/menu.html
> 
> Flask Documentation for url_for can be found here.
> 
> https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-3/10_url_for-Solution/menu.html


## Forms

### 8.12. Form Requests and Redirects
### 8.13. Quiz: Edit Menu Item Form Quiz
### 8.14. Quiz: Delete Menu Item

## Message flashing

### 8.15. Message Flashing

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


### 8.16. Quiz: Message Flashing Quiz

## Styling

### 8.17. Quiz: Styling

Flask can look for CSS, JS, and media files inside of a *static/* directory.


## JSON

### 8.18. Responding With JSON

Let's say there's a service called *yum!* that wants to read data from your restaurant menu database and display it to users based on their location. To see the list of restaurants and menus in the database, *yum!* doesn't need to waste bandwith parsing HTML and CSS, it just needs the data.

What do we need? I knew the answer- an **API**! I've been wanting to get into APIs for a while now. Finally!

**RESTful** - REpresentational State Transfer. Sending the data over the internet with HTTP.

**API** - Application Programming Interface

APIs frequently use **JSON** (JavaScript Object Notation), which uses `{"key": "value",}` pairs. The Flask `jsonify` package allows us to easily configure an API endpoint for the application. `jsonify` converts our database into JSON.


### 8.19. Quiz: JSON Quiz
### 8.20. Lesson 3 Wrap-Up

## Feedback on Lesson 08

Lorenzo did a great job with this lesson. All of his instructor materials were well-crafted, and it is very useful to learn the Flask framework.