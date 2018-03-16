# Agile iterative development

**Udacity Full Stack Web Developer Nanodegree program**

Part 03. Backend

Lesson 09. Agile iterative development (from free course [Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088))

Brendon Smith

br3ndonland

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [The agile iterative development process](#the-agile-iterative-development-process)
  - [9.01. Lesson 4 Introduction](#901-lesson-4-introduction)
  - [9.02. Iterative Development](#902-iterative-development)
  - [9.03. Quiz: Tackling a Complex Project](#903-quiz-tackling-a-complex-project)
  - [9.04. Quiz: Mockups Exercise](#904-quiz-mockups-exercise)
  - [9.05. Quiz: Adding Routes](#905-quiz-adding-routes)
  - [9.06. Quiz: Adding Templates and Forms](#906-quiz-adding-templates-and-forms)
  - [9.07. Quiz: CRUD Functionality](#907-quiz-crud-functionality)
  - [9.08. Quiz: API Endpoints](#908-quiz-api-endpoints)
  - [9.09. Quiz: Styling Your App](#909-quiz-styling-your-app)
  - [9.10. Wrap-Up](#910-wrap-up)
- [Feedback on Lesson 09](#feedback-on-lesson-09)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## The agile iterative development process

### 9.01. Lesson 4 Introduction

### 9.02. Iterative Development

> Some people write code by just binging as much code as possible before falling asleep, or writing code in pieces and having it be all over the place.
> 
> A more effective strategy is to start simple and layer on complexity as you go, not adding a new feature until the current feature is finished. When each feature is finished, we stop, test, debug and share to make sure we always have a working application. This way, clients, project managers, and team members always know what the project status is and what's to follow. 
> 
> This is called **iterative development.**
> 
> **Agile** refers to the ability to easily change an application. Because there is always a working prototype, if someone asks for changes, it is easily done.


### 9.03. Quiz: Tackling a Complex Project

Break the project down into steps, and outline deliverables that will be present at each step.

Lorenzo used the restaurant menu app as an example.

* Mockups
	- Deliverables: Mock-ups and URLs for each page in the menu app.
* Routing
	- Deliverables: At the end of this iteration, you should have a running Flask application, and be able to navigate to all of the URLs, even if the pages are not yet created.
* Templates and forms
	- Deliverables: Functional templates and forms
* CRUD functionality
	- Deliverables: Ability to Create, Read, Update, and Delete.
* API endpoints
	- Deliverables: Ability to send API data in JSON.
* Styling and message flashing
	- Deliverables: Nicely styled app pages and messages when database is changed.


Quiz: pros and cons of "top-down" approach focusing on front-end first vs "bottom-up."


### 9.04. Quiz: Mockups Exercise

You can use wireframing apps, or just pen and paper.

<img src="img/fsnd03_09_04-mockup01.png" alt="Mockup process screenshot 01">

<img src="img/fsnd03_09_04-mockup02.png" alt="Mockup process screenshot 02">

<img src="img/fsnd03_09_04-mockup03.png" alt="Mockup process screenshot 03">


### 9.05. Quiz: Adding Routes

Lorenzo got the Flask application started and set up the page URLs.

<img src="img/fsnd03_09_04-mockup04.png" alt="Mockup process screenshot 04">


### 9.06. Quiz: Adding Templates and Forms

Lorenzo created empty HTML files that will serve as templates. Python will throw an error if the database has not yet been created, so he created a temporary database called "fake menu items."


### 9.07. Quiz: CRUD Functionality

* SQLAlchemy commands: show, new, edit, delete
* url_for
* redirect
* GET and POST

This is one of the more time-consuming steps.


### 9.08. Quiz: API Endpoints

Use `jsonify` and `serialize` to return JSON when HTTP request is made to:

* /restaurants/JSON
* restaurants/restaurant_id/menu/JSON
* restaurants/restaurant_id/menu/menu_id/JSON


### 9.09. Quiz: Styling Your App

* Static: CSS, JS, images
* Message flashing:
	- New restaurant created
	- Restaurant successfully edited
	- Restaurant successfully deleted
	- New menu item created
	- Menu item successfully edited
	- Menu item successfully deleted


### 9.10. Wrap-Up


Instructor notes

> You can view [this article](http://flask.pocoo.org/docs/0.10/deploying/) on deploying Flask applications, but I highly recommend adding some [security](https://pythonhosted.org/Flask-Security/) to your application before publishing it on the internet.
> 
> A basic version of the final project can be found [here](https://github.com/lobrown/Full-Stack-Foundations/tree/master/Lesson-4/Final-Project).

## Feedback on Lesson 09

Really helpful to think through agile development. This will help me complete my Udacity projects, and my work projects when I get a web development job.

It was confusing to work through app development again here, when we already did it in the previous lesson. It would be more helpful to discuss agile development first, then work through the whole app creation process, so the code base is cohesive.