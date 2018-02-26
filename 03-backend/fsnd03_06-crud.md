# CRUD

**Udacity Full Stack Web Developer Nanodegree program**

Part 03. Backend

Lesson 06. Working with CRUD

Brendon Smith

br3ndonland

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Intro](#intro)
  - [6.01. Course Intro](#601-course-intro)
  - [6.02. Prerequisites & Preparation](#602-prerequisites--preparation)
- [CRUD intro](#crud-intro)
  - [6.03. Project Introduction - CRUD](#603-project-introduction---crud)
  - [6.04. Quiz: CRUD Review 1](#604-quiz-crud-review-1)
  - [6.05. Quiz: CRUD Review 2](#605-quiz-crud-review-2)
  - [6.06. Quiz: CRUD Review 3](#606-quiz-crud-review-3)
  - [6.07. Quiz: CRUD Review 4](#607-quiz-crud-review-4)
- [SQL](#sql)
  - [6.08. SQL](#608-sql)
  - [6.09. Quiz: SQL Quiz Select](#609-quiz-sql-quiz-select)
  - [6.10. Quiz: SQL Insert Into](#610-quiz-sql-insert-into)
  - [6.11. Quiz: SQL Update](#611-quiz-sql-update)
  - [6.12. Quiz: SQL Delete](#612-quiz-sql-delete)
  - [6.13. Creating a Database and ORMs](#613-creating-a-database-and-orms)
- [SQLAlchemy](#sqlalchemy)
  - [6.14. Introducing SQLAlchemy](#614-introducing-sqlalchemy)
  - [6.15. Creating a Database - Configuration](#615-creating-a-database---configuration)
  - [6.16. Creating a Database - Class and Table](#616-creating-a-database---class-and-table)
  - [6.17. Creating a Database - Mapper](#617-creating-a-database---mapper)
  - [6.18. Putting It All Together](#618-putting-it-all-together)
  - [6.19. Quiz: Database Setup Quiz Part 1](#619-quiz-database-setup-quiz-part-1)
  - [6.20. Quiz: Database Setup Quiz Part 2](#620-quiz-database-setup-quiz-part-2)
- [CRUD process](#crud-process)
  - [6.21. CRUD Create](#621-crud-create)
  - [6.22. Quiz: CRUD Create Quiz](#622-quiz-crud-create-quiz)
  - [6.23. CRUD Read](#623-crud-read)
  - [6.24. Quiz: CRUD Read Quiz](#624-quiz-crud-read-quiz)
  - [6.25. CRUD Update](#625-crud-update)
  - [6.26. Quiz: CRUD Update Quiz](#626-quiz-crud-update-quiz)
  - [6.27. CRUD Delete](#627-crud-delete)
  - [6.28. Quiz: CRUD Delete Quiz](#628-quiz-crud-delete-quiz)
  - [6.29. CRUD Review](#629-crud-review)
- [Outro](#outro)
  - [6.30. Wrap Up](#630-wrap-up)
- [Feedback on Lesson 06](#feedback-on-lesson-06)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Intro

### 6.01. Course Intro

Lorenzo will be the instructor for this course.

*I think the next four lessons are the Full Stack Foundations course.*

We will be making **data-driven web applications.**

* Web applications: Interactive user experience.
* Data-driven: Uses data to deliver customized content.

### 6.02. Prerequisites & Preparation

* Git
* VirtualBox
* Vagrant

Already ready!


## CRUD intro

### 6.03. Project Introduction - CRUD

We're going to be creating a restaurant menu app. We will be able to:

* CREATE menu items
* READ the items we've created
* UPDATE with new items
* DELETE items

Basically all our actions on the web can be summarized by CRUD.


### 6.04. Quiz: CRUD Review 1

Reading news articles is a READ.


### 6.05. Quiz: CRUD Review 2

Clearing out junk mail is a DELETE.


### 6.06. Quiz: CRUD Review 3

Making a new blog profile is a CREATE.


### 6.07. Quiz: CRUD Review 4

Changing the number of items in an online shopping cart would be an UPDATE.


## SQL

### 6.08. SQL

SQL can go between databases and application code.


### 6.09. Quiz: SQL Quiz Select

SQL `SELECT` is like CRUD READ.


### 6.10. Quiz: SQL Insert Into

SQL `INSERT INTO` is like CRUD CREATE. It inserts a new row into the database.


### 6.11. Quiz: SQL Update

SQL `UPDATE` is like CRUD UPDATE!

> Correct! An UPDATE in SQL changes an existing row of information in a database table, just like the UPDATE in CRUD


### 6.12. Quiz: SQL Delete

SQL `DELETE` is like CRUD DELETE!


### 6.13. Creating a Database and ORMs

Restaurant menus are all pretty similar. The menu belongs to a specific restaurant, and contains menu items.

We walked through construction of the database layout. Makes sense to me!

*restaurantmenu.db*

* `Restaurant` table
	- `name`
	- `id`
* `Menu_Item` table
	- `name`
	- `description`
	- `price`
	- `course`
	- `restaurant_id` as a foreign key referencing the `Restaurant` table.

<img src="img/fsnd03_06_13-restaurantdb.png">

We will use Object-Relational Mappers (ORMs) to transform code from Python objects to SQL statements. 

## SQLAlchemy

### 6.14. Introducing SQLAlchemy

SQLAlchemy is an open-source ORM for Python. It was pre-installed in our Vagrant virtual machine.


### 6.15. Creating a Database - Configuration

* Configuration
	- At beginning of file:
		+ Import necessary modules
		+ Create instance of "declarative base"
	- At end of file:
		+ Connect database and add tables and columns
* Class
	- Represent database tables as Python classes
		+ `Restaurant` table
		+ `Menu_Item` table
	- We will use CamelCase for class names.
	- We will include table and mapper code.
* Table
	- Represents specific table in database
* Mapper
	- Maps columns of the database tables to Python objects
	- `columnName = Column(attributes,...)`
	- Example attributes
		+ String(250)
		+ Integer
		+ relationship(Class)
		+ nullable = False
		+ primary_key = True
		+ ForeignKey('some_table.id')

I followed along and filled out the code in *database_setup.py*.


### 6.16. Creating a Database - Class and Table
### 6.17. Creating a Database - Mapper
### 6.18. Putting It All Together
### 6.19. Quiz: Database Setup Quiz Part 1

`Base` should be an instance of class `declarative_base`


### 6.20. Quiz: Database Setup Quiz Part 2

`id = Column(Integer, `
`employee = relationship(Employee)`


## CRUD process

### 6.21. CRUD Create

* We walked through database creation in the Python shell. I followed along in vagrant.
* I copied *database_setup.py* into *vagrant/crud*.
* SQLAlchemy uses "sessions" to connect to the database. We can store the commands we plan to use, but not send them to the database until we run a commit.
* Setup:
	```python
	python
	>>> from sqlalchemy import create_engine
	>>> from sqlalchemy.orm import sessionmaker
	>>> from database_setup import Base, Restaurant, MenuItem
	>>> engine = create_engine('sqlite:///restaurantmenu.db')
	>>> Base.metadata.bind = engine
	>>> DBSession = sessionmaker(bind = engine)
	>>> session = DBSession()
	```
	Note use of `database_setup` to import classes, not `database_setup.py`.
* Making a new entry in the database is as easy as making a new object in Python:
	```python
	newEntry = ClassName(property = 'value', ...)
	session.add(newEntry)
	session.commit()
	```
	I did this with the restaurant menu database:
	```python
	>>> stokespurple = MenuItem(name = "Stokes Purple Sweet Potato", description = "The legendary and mysterious purple sweet potato, steamed to perfection", course = "Entree", price = "$11.99", restaurant = myFirstRestaurant)
	>>> session.add(stokespurple)
	>>> session.commit()
	```
	See *database_add_bash* for full bash code.

### 6.22. Quiz: CRUD Create Quiz

Rocked it. Entry 1 was `name`, entry 2 was `newEmployee` (the foreign key).


### 6.23. CRUD Read

I cloned the *Full-Stack-Foundations* repo into the *vagrant* directory.


### 6.24. Quiz: CRUD Read Quiz

Rocked it again. The code was working with an example database of employees. We selected all the employees, and stored them in a variable:
```python
employees = session.query(Employee).all()
```
then printed out the name of each employee:
```python
for employee in employees:
    print(employee.name)
```


### 6.25. CRUD Update

Simple four step process:

1. Find entry with `filter_by()`
	```python
	session.query(ClassName).filter_by()
	```
2. Reset values
3. Add to session
	```python
	session.add()
	```
4. Commit to database
	```python
	session.commit()
	```

For the restaurant example in this lesson:

1. Find entry with `filter_by()`
	```python
	>>> veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
	>>> for veggieBurger in veggieBurgers:
	...     print veggieBurger.id
	...     print veggieBurger.price
	...     print veggieBurger.restaurant.name
	...     print "\n"
	>>> UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 8).one()
	>>> print UrbanVeggieBurger.price
	```
2. Reset values
	```python
	>>> UrbanVeggieBurger.price = '$2.99'
	```
3. Add to session
	```python
	>>> session.add(UrbanVeggieBurger)
	```
4. Commit to database
	```python
	>>> session.commit()
	```

	Lorenzo also created another `for` loop to change all the veggie burger prices to $2.99, if they are not already that price:
	```python
	>>> for veggieBurger in veggieBurgers:
	...     if veggieBurger.price != '$2.99':
	...         veggieBurger.price = '$2.99'
	...         session.add(veggieBurger)
	...         session.commit()
	...
	>>> for veggieBurger in veggieBurgers:
	...     print veggieBurger.id
	...     print veggieBurger.price
	...     print veggieBurger.restaurant.name
	...     print "\n"
	```


I followed along. The code wasn't working for me in either Python 2 or 3. I may not have entered the setup steps correctly. I just moved on in the interest of time. I'm now trying to move through the lessons faster.

The instructor notes explain:

> Note: The id numbers and restaurants for the Veggie Burgers will be a bit different on your machine than the ones in this lesson. lotsofmenus.py was updated to have a few more restaurant options and menu items.


### 6.26. Quiz: CRUD Update Quiz

Rocked it. Just needed `session.add(RebeccasAddress)`


### 6.27. CRUD Delete

Three step process

1. Find entry
2. `session.delete(entry)`
3. `session.commit()`

### 6.28. Quiz: CRUD Delete Quiz

`session.delete(Mark)`


### 6.29. CRUD Review

#### Operations with SQLAlchemy

In this lesson, we performed all of our CRUD operations with SQLAlchemy on an SQLite database. Before we perform any operations, we must first import the necessary libraries, connect to our restaurantMenu.db, and create a session to interface with the database:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
```


#### CREATE

We created a new Restaurant and called it Pizza Palace:

```python
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
sesssion.commit()
```

We created a cheese pizza menu item and added it to the Pizza Palace Menu:

```python
cheesepizza = menuItem(name="Cheese Pizza", description =
"Made with all natural ingredients and fresh mozzarella",
course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
```


#### READ

We read out information in our database using the query method in SQLAlchemy:

```python
firstResult = session.query(Restaurant).first()
firstResult.name

items = session.query(MenuItem).all()
for item in items:
    print item.name
```


#### UPDATE

In order to update and existing entry in our database, we must execute the following commands:

1.  Find Entry
2.  Reset value(s)
3.  Add to session
4.  Execute `session.commit()`

We found the veggie burger that belonged to the Urban Burger restaurant by executing the following query:

```python
veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\\n"
```

Then we updated the price of the veggie burger to $2.99:

```python
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit() 
```


#### DELETE

To delete an item from our database we must follow the following steps:

1.  Find the entry
2.  `Session.delete(Entry)`
3.  `Session.commit()`

We deleted spinach Ice Cream from our Menu Items database with the following operations:

```python
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit()
```


## Outro

### 6.30. Wrap Up

## Feedback on Lesson 06

Lorenzo did a very nice job with this lesson. It was informative and fun, and the quiz questions made sense to me.