# Python web servers

**Udacity Full Stack Web Developer Nanodegree program**

Part 03. Backend

Lesson 07. Making a web server

Brendon Smith

br3ndonland

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python web server basics](#python-web-server-basics)
  - [7.01. Lesson 2 Introduction](#701-lesson-2-introduction)
  - [7.02. Review of Clients, Servers and Protocols](#702-review-of-clients-servers-and-protocols)
  - [7.03. HTTP and Response Codes](#703-http-and-response-codes)
  - [7.04. Building a Server with HTTPBaseServer](#704-building-a-server-with-httpbaseserver)
  - [7.05. Quiz: Running a Web Server](#705-quiz-running-a-web-server)
  - [7.06. Port Forwarding](#706-port-forwarding)
  - [7.07. Responding to Multiple GET Requests](#707-responding-to-multiple-get-requests)
  - [7.08. Quiz: Hola Server](#708-quiz-hola-server)
  - [7.09. Adding POST to web server](#709-adding-post-to-web-server)
  - [7.10. Quiz: Running the POST Web Server](#710-quiz-running-the-post-web-server)
- [Adding CRUD](#adding-crud)
  - [7.11. Adding CRUD to our Website](#711-adding-crud-to-our-website)
  - [7.12. Quiz: CRUD Objectives](#712-quiz-crud-objectives)
  - [7.13. Adding CRUD Hints](#713-adding-crud-hints)
  - [7.14. Quiz: CRUD Hints](#714-quiz-crud-hints)
  - [7.15. Quiz: Objective 1](#715-quiz-objective-1)
  - [7.16. Quiz: Objective 2](#716-quiz-objective-2)
  - [7.17. Quiz: Objective 3](#717-quiz-objective-3)
  - [7.18. Quiz: Objective 4](#718-quiz-objective-4)
  - [7.19. Quiz: Objective 5](#719-quiz-objective-5)
  - [7.20. Lesson 2 Wrap-Up](#720-lesson-2-wrap-up)
- [Feedback on Lesson 07](#feedback-on-lesson-07)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Python web server basics

### 7.01. Lesson 2 Introduction

Reviewing HTTP


### 7.02. Review of Clients, Servers and Protocols

* TCP
* IP
* UDP


### 7.03. HTTP and Response Codes

`GET`, `POST`, etc.


### 7.04. Building a Server with HTTPBaseServer

### 7.05. Quiz: Running a Web Server

I cloned the [files](https://github.com/udacity/Full-Stack-Foundations) into my vagrant directory for the last lesson. The files for this lesson are in *Full-Stack-Foundations/Lesson-2*.

I started the web server

```bash
$ vagrant ssh
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$ cd Full-Stack-Foundations/Lesson-2/first-web-server
vagrant@vagrant:/vagrant/Full-Stack-Foundations/Lesson-2/first-web-server$ python webserver.py
```

I navigated to http://localhost:8080/hello and got the correct response.


### 7.06. Port Forwarding

> Port forwarding allows us to open pages in our browser from the web server from our virtual machine as if they were being run locally. See which ports are being used for this class. If you want to use another port you can add another line to the vagrant file and run "vagrant reload" from a terminal in the directory of your vagrant file on your host machine. More information about port forwarding is available [here](https://docs.vagrantup.com/v2/networking/forwarded_ports.html).


### 7.07. Responding to Multiple GET Requests

Hola server:

```bash
vagrant@vagrant:/vagrant/Full-Stack-Foundations/Lesson-2/first-web-server$ cd ../hola-server
vagrant@vagrant:/vagrant/Full-Stack-Foundations/Lesson-2/hola-server$ python webserver.py
```

http://localhost:8080/hola

> ¡Hola!

### 7.08. Quiz: Hola Server
### 7.09. Adding POST to web server

*Lesson-2/post-web-server*


### 7.10. Quiz: Running the POST Web Server

Did it


## Adding CRUD

### 7.11. Adding CRUD to our Website

Adding CRUD capabilities for restaurant database


### 7.12. Quiz: CRUD Objectives

1. Read: List restaurants for user on website http://localhost:8080/restaurants
2. Add edit and delete links to website after restaurant names
3. Create: Add page at http://http://localhost:8080/new with add restaurant feature that performs a `POST` request
4. Update: Rename restaurant feature at http://localhost:8080/restaurant/id/edit
5. Delete: Delete restaurant feature takes user to confirmation page, and removes the restaurant from the database with a `POST` request

It was helpful to see Lorenzo break down the objective into steps. I do this for my projects!

I just followed along in the solution code, rather than writing the solutions myself, in the interest of time. It is also more effective and efficient to produce the webserver using Flask, which we'll thankfully be doing in the next lesson!

**The code hasn't been updated for Python 3, but will run with Python 2 in vagrant. Each webserver.py directory must also have the database_setup.py file.**


### 7.13. Adding CRUD Hints

> * You have already seen all the necessary code
> * Import necessary modules
> * Reconstruct do_GET and do_POST
> * use `print` statements to debug
> * View page source in browser


### 7.14. Quiz: CRUD Hints

### 7.15. Quiz: Objective 1

Instructor notes:

Error in video - Replace lines 12 and 13 with:

```python
DBSession = sessionmaker(bind=engine)

session = DBSession()
```

Objective 1 solution can be found here:

https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-1-Solution/webserver.py

Note:

A few times I say backslash "\" in this course, all slashes in this course should be forward slashes "/"


### 7.16. Quiz: Objective 2

Objective 2 Solution Code can be found here: https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-2-Solution/webserver.py


### 7.17. Quiz: Objective 3

> Note
> 
> messagecontent = fields.get('newRestaurantName') should be indented such that it is inside the 'if' block
> Objective 3 Solution Code can be found here:
> 
> https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-3-Solution/webserver.py


### 7.18. Quiz: Objective 4

> Objective 4 Solutions can be found here:
> 
> https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-4-Solution/webserver.py


### 7.19. Quiz: Objective 5

> Note
> 
> line 128 (ctype, pdict....) is not a necessary line of code to implement this solution.
> Code for Objective 5 can be found here:
> 
> https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-5-Solution/webserver.py


### 7.20. Lesson 2 Wrap-Up

## Feedback on Lesson 07

Lorenzo did a nice job teaching here as well, but the lesson could benefit from some cleanup. The code could be updated from Python 2 to Python 3. Each of the Lesson-2/ solution directories in the GitHub repo also needs the database_setup.py file to run properly.