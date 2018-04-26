# Python web servers

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088)

Lesson 2. Python web servers

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Python web server basics](#python-web-server-basics)
  - [01. Lesson 2 Introduction](#01-lesson-2-introduction)
  - [02. Review of Clients, Servers and Protocols](#02-review-of-clients-servers-and-protocols)
  - [03. HTTP and Response Codes](#03-http-and-response-codes)
  - [04. Building a Server with HTTPBaseServer](#04-building-a-server-with-httpbaseserver)
  - [05. Quiz: Running a Web Server](#05-quiz-running-a-web-server)
  - [06. Port Forwarding](#06-port-forwarding)
  - [07. Responding to Multiple GET Requests](#07-responding-to-multiple-get-requests)
  - [08. Quiz: Hola Server](#08-quiz-hola-server)
  - [09. Adding POST to web server](#09-adding-post-to-web-server)
  - [10. Quiz: Running the POST Web Server](#10-quiz-running-the-post-web-server)
- [Adding CRUD](#adding-crud)
  - [11. Adding CRUD to our Website](#11-adding-crud-to-our-website)
  - [12. Quiz: CRUD Objectives](#12-quiz-crud-objectives)
  - [13. Adding CRUD Hints](#13-adding-crud-hints)
  - [14. Quiz: CRUD Hints](#14-quiz-crud-hints)
  - [15. Quiz: Objective 1](#15-quiz-objective-1)
  - [16. Quiz: Objective 2](#16-quiz-objective-2)
  - [17. Quiz: Objective 3](#17-quiz-objective-3)
  - [18. Quiz: Objective 4](#18-quiz-objective-4)
  - [19. Quiz: Objective 5](#19-quiz-objective-5)
  - [20. Lesson 2 Wrap-Up](#20-lesson-2-wrap-up)
- [Feedback on Lesson 2](#feedback-on-lesson-2)

## Python web server basics

### 01. Lesson 2 Introduction

Reviewing HTTP

### 02. Review of Clients, Servers and Protocols

- TCP
- IP
- UDP

### 03. HTTP and Response Codes

`GET`, `POST`, etc.

### 04. Building a Server with HTTPBaseServer

### 05. Quiz: Running a Web Server

I cloned the [files](https://github.com/udacity/Full-Stack-Foundations) into my vagrant directory for the last lesson. The files for this lesson are in *Full-Stack-Foundations/Lesson-2*.

I started the web server

```bash
$ vagrant ssh
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$ cd Full-Stack-Foundations/Lesson-2/first-web-server
vagrant@vagrant:/vagrant/Full-Stack-Foundations/Lesson-2/first-web-server$ python webserver.py
```

I navigated to [http://localhost:8080/hello](http://localhost:8080/hello) and got the correct response.

### 06. Port Forwarding

> Port forwarding allows us to open pages in our browser from the web server from our virtual machine as if they were being run locally. See which ports are being used for this class. If you want to use another port you can add another line to the vagrant file and run "vagrant reload" from a terminal in the directory of your vagrant file on your host machine. More information about port forwarding is available [here](https://docs.vagrantup.com/v2/networking/forwarded_ports.html).

### 07. Responding to Multiple GET Requests

Hola server:

```bash
vagrant@vagrant:/vagrant/Full-Stack-Foundations/Lesson-2/first-web-server$ cd ../hola-server
vagrant@vagrant:/vagrant/Full-Stack-Foundations/Lesson-2/hola-server$ python webserver.py
```

[http://localhost:8080/hola](http://localhost:8080/hola)

> ¡Hola!

### 08. Quiz: Hola Server

### 09. Adding POST to web server

Lesson-2/post-web-server

### 10. Quiz: Running the POST Web Server

Did it

## Adding CRUD

### 11. Adding CRUD to our Website

Adding CRUD capabilities for restaurant database

### 12. Quiz: CRUD Objectives

1. Read: List restaurants for user on website [http://localhost:8080/restaurants](http://localhost:8080/restaurants)
2. Add edit and delete links to website after restaurant names
3. Create: Add page at [http://http://localhost:8080/new](http://http://localhost:8080/new) with add restaurant feature that performs a `POST` request
4. Update: Rename restaurant feature at [http://localhost:8080/restaurant/id/edit](http://localhost:8080/restaurant/id/edit)
5. Delete: Delete restaurant feature takes user to confirmation page, and removes the restaurant from the database with a `POST` request

It was helpful to see Lorenzo break down the objective into steps. I do this for my projects!

**I just followed along in the solution code, rather than writing the solutions myself, in the interest of time. It is also more effective and efficient to produce the webserver using Flask, which we'll thankfully be doing in the next lesson!**

**The code hasn't been updated for Python 3, but will run with Python 2 in vagrant. Each webserver.py directory must also have the database_setup.py file.**

### 13. Adding CRUD Hints

> - You have already seen all the necessary code
> - Import necessary modules
> - Reconstruct do_GET and do_POST
> - use `print` statements to debug
> - View page source in browser

### 14. Quiz: CRUD Hints

### 15. Quiz: Objective 1

Instructor notes:

> Error in video - Replace lines 12 and 13 with:
>
> ```python
> DBSession = sessionmaker(bind=engine)
>
> session = DBSession()
> ```
>
> Objective 1 solution can be found [here](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-1-Solution/webserver.py)
>
> Note:
>
> A few times I say backslash "\" in this course, all slashes in this course should be forward slashes "/"

### 16. Quiz: Objective 2

>Objective 2 Solution Code can be found [here](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-2-Solution/webserver.py)

### 17. Quiz: Objective 3

> Note
>
> messagecontent = fields.get('newRestaurantName') should be indented such that it is inside the 'if' block
> Objective 3 Solution Code can be found [here](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-3-Solution/webserver.py)

### 18. Quiz: Objective 4

> Objective 4 Solutions can be found [here](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-4-Solution/webserver.py)

### 19. Quiz: Objective 5

> Note
>
> line 128 (ctype, pdict....) is not a necessary line of code to implement this solution.
> Code for Objective 5 can be found [here](https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-2/Objective-5-Solution/webserver.py)

### 20. Lesson 2 Wrap-Up

## Feedback on Lesson 2

Lorenzo did a nice job teaching here as well, but the lesson could benefit from some cleanup. The code could be updated from Python 2 to Python 3. It's confusing to break up the material into so many different versions of the same files. Each of the Lesson-2/ solution directories in the GitHub repo also needs the database_setup.py file to run properly.

[(Back to TOC)](#table-of-contents)