# Agile iterative development

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo svg">
</a>

Udacity Full Stack Web Developer Nanodegree program

[Full Stack Foundations course](https://www.udacity.com/course/full-stack-foundations--ud088)

Lesson 4. Agile iterative development

Brendon Smith

br3ndonland

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [01. Lesson 4 Introduction](#01-lesson-4-introduction)
  - [02. Iterative Development](#02-iterative-development)
  - [03. Quiz: Tackling a Complex Project](#03-quiz-tackling-a-complex-project)
- [Mockups](#mockups)
  - [04. Quiz: Mockups Exercise](#04-quiz-mockups-exercise)
- [Routes and templates](#routes-and-templates)
  - [05. Quiz: Adding Routes](#05-quiz-adding-routes)
  - [06. Quiz: Adding Templates and Forms](#06-quiz-adding-templates-and-forms)
- [CRUD and JSON API](#crud-and-json-api)
  - [07. Quiz: CRUD Functionality](#07-quiz-crud-functionality)
  - [08. Quiz: API Endpoints](#08-quiz-api-endpoints)
- [Style](#style)
  - [09. Quiz: Styling Your App](#09-quiz-styling-your-app)
  - [10. Wrap-Up](#10-wrap-up)
- [Feedback on Lesson 4](#feedback-on-lesson-4)

## Overview

### 01. Lesson 4 Introduction

### 02. Iterative Development

> Some people write code by just binging as much code as possible before falling asleep, or writing code in pieces and having it be all over the place.
>
> A more effective strategy is to start simple and layer on complexity as you go, not adding a new feature until the current feature is finished. When each feature is finished, we stop, test, debug and share to make sure we always have a working application. This way, clients, project managers, and team members always know what the project status is and what's to follow.
>
> This is called **iterative development.**
>
> **Agile** refers to the ability to easily change an application. Because there is always a working prototype, if someone asks for changes, it is easily done.

### 03. Quiz: Tackling a Complex Project

Break the project down into steps, and outline deliverables that will be present at each step.

Lorenzo used the restaurant menu app as an example.

- Mockups
  - Deliverables: Mock-ups and URLs for each page in the menu app.
- Routing
  - Deliverables: At the end of this iteration, you should have a running Flask application, and be able to navigate to all of the URLs, even if the pages are not yet created.
- Templates and forms
  - Deliverables: Functional templates and forms
- CRUD functionality
  - Deliverables: Ability to Create, Read, Update, and Delete.
- API endpoints
  - Deliverables: Ability to send API data in JSON.
- Styling and message flashing
  - Deliverables: Nicely styled app pages and messages when database is changed.

Quiz: pros and cons of "top-down" approach focusing on front-end first vs "bottom-up."

## Mockups

### 04. Quiz: Mockups Exercise

You can use wireframing apps, or just pen and paper.

<img src="img/fsnd03_09_04-mockup01.png" alt="Mockup process screenshot 01">

<img src="img/fsnd03_09_04-mockup02.png" alt="Mockup process screenshot 02">

<img src="img/fsnd03_09_04-mockup03.png" alt="Mockup process screenshot 03">

## Routes and templates

### 05. Quiz: Adding Routes

Lorenzo got the Flask application started and set up the page URLs.

<img src="img/fsnd03_09_04-mockup04.png" alt="Mockup process screenshot 04">

### 06. Quiz: Adding Templates and Forms

Lorenzo created empty HTML files that will serve as templates. Python will throw an error if the database has not yet been created, so he created a temporary database called "fake menu items."

## CRUD and JSON API

### 07. Quiz: CRUD Functionality

- SQLAlchemy commands: show, new, edit, delete
- url_for
- redirect
- GET and POST

This is one of the more time-consuming steps.

### 08. Quiz: API Endpoints

Use `jsonify` and `serialize` to return JSON when HTTP request is made to:

- /restaurants/JSON
- restaurants/restaurant_id/menu/JSON
- restaurants/restaurant_id/menu/menu_id/JSON

## Style

### 09. Quiz: Styling Your App

- Static: CSS, JS, images
- Message flashing:
  - New restaurant created
  - Restaurant successfully edited
  - Restaurant successfully deleted
  - New menu item created
  - Menu item successfully edited
  - Menu item successfully deleted

### 10. Wrap-Up

Instructor notes

> You can view [this article](http://flask.pocoo.org/docs/0.10/deploying/) on deploying Flask applications, but I highly recommend adding some [security](https://pythonhosted.org/Flask-Security/) to your application before publishing it on the internet.
>
> A basic version of the final project can be found [here](https://github.com/lobrown/Full-Stack-Foundations/tree/master/Lesson-4/Final-Project).

## Feedback on Lesson 4

Really helpful to think through agile development. This will help me complete my Udacity projects, and my work projects when I get a web development job.

It was confusing to work through app development again here though, when we already did it in the previous lesson. It would be more helpful to discuss agile development first, then work through the whole Flask app creation process in that way, so the code base is cohesive.

[(Back to TOC)](#table-of-contents)