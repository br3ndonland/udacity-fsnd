# Data and Tables

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)

## Table of Contents

- [Lesson 1. Relational Concepts: Data and Tables](#lesson-1-relational-concepts-data-and-tables)
  - [1.01. Welcome to RDB](#101-welcome-to-rdb)
  - [1.02. What's a database](#102-whats-a-database)
  - [1.03-05. Quizzes about tables and data types](#103-05-quizzes-about-tables-and-data-types)
  - [1.06-08. Anatomy of a table with zoo animals](#106-08-anatomy-of-a-table-with-zoo-animals)
  - [Aggregations](#aggregations)
  - [1.10-11. Queries](#110-11-queries)
  - [1.12-16. `JOIN`, `id` and `PRIMARY KEY`](#112-16-join-id-and-primary-key)
  - [1.17. Quiz: Database concepts](#117-quiz-database-concepts)
  - [Feedback on Lesson 1](#feedback-on-lesson-1)
- [Lesson 2. Elements of SQL](#lesson-2-elements-of-sql)
  - [2.01. SQL is for Elephants](#201-sql-is-for-elephants)
  - [2.02. Talk to the Zoo Database](#202-talk-to-the-zoo-database)
  - [2.03. Types in the SQL World](#203-types-in-the-sql-world)
  - [2.04. Just a few SQL types](#204-just-a-few-sql-types)
  - [2.05. Select Where](#205-select-where)
  - [2.06. Comparison Operators](#206-comparison-operators)
  - [2.07. The One Thing SQL is Terrible At](#207-the-one-thing-sql-is-terrible-at)
  - [2.08. The Experiment Page](#208-the-experiment-page)
  - [2.09. Quiz: Select Clauses](#209-quiz-select-clauses)
  - [2.10. Why Do It in the Database](#210-why-do-it-in-the-database)
  - [2.11. Quiz: Count All the Species](#211-quiz-count-all-the-species)
  - [2.12. Quiz: Insert: Adding Rows](#212-quiz-insert-adding-rows)
  - [2.13. Joining tables: Find the Fish-Eaters](#213-joining-tables-find-the-fish-eaters)
  - [2.14. After Aggregating](#214-after-aggregating)
  - [2.15. More Join Practice](#215-more-join-practice)
  - [2.16. Wrap up](#216-wrap-up)
  - [2.17. Installing the Virtual Machine](#217-installing-the-virtual-machine)
  - [2.18. Reference — Elements of SQL](#218-reference-—-elements-of-sql)
  - [All the tables in the zoo database](#all-the-tables-in-the-zoo-database)
  - [Time](#time)
  - [Feedback on Lesson 2](#feedback-on-lesson-2)
- [Lesson 3. Python DB-API](#lesson-3-python-db-api)
  - [3.01. Welcome to your Database](#301-welcome-to-your-database)
  - [3.02. What's a DB-API](#302-whats-a-db-api)
  - [3.03. Writing Code with DB API](#303-writing-code-with-db-api)
  - [3.04. Quiz: Trying out DB API](#304-quiz-trying-out-db-api)
  - [3.05. Quiz: Inserts in DB API](#305-quiz-inserts-in-db-api)
  - [3.06. Running the Forum](#306-running-the-forum)
  - [3.07. Hello PostgreSQL](#307-hello-postgresql)
  - [3.08. Give That App a Backend](#308-give-that-app-a-backend)
  - [3.09. Bobby Tables, Destroyer of Posts](#309-bobby-tables-destroyer-of-posts)
  - [3.10. Curing Bobby Tables](#310-curing-bobby-tables)
  - [3.11. Spammy Tables](#311-spammy-tables)
  - [3.12. Quiz: Stopping the Spam](#312-quiz-stopping-the-spam)
  - [3.13. Quiz: Updating Away the Spam](#313-quiz-updating-away-the-spam)
  - [3.14. Quiz: Deleting the Spam](#314-quiz-deleting-the-spam)
  - [3.15. Conclusion](#315-conclusion)
  - [3.16. Reference — Python DB-API](#316-reference-—-python-db-api)
  - [Feedback on Lesson 3](#feedback-on-lesson-3)
- [Lesson 4: Deeper into SQL](#lesson-4-deeper-into-sql)
  - [4.01. Intro to Creating Tables](#401-intro-to-creating-tables)
  - [4.02. Normalized Design Part One](#402-normalized-design-part-one)
  - [4.03. Normalized Design Part Two](#403-normalized-design-part-two)
  - [4.04. Quiz: What's Normalized](#404-quiz-whats-normalized)
  - [4.05. Create Table and Types](#405-create-table-and-types)
  - [4.06. Quiz: Creating and Dropping](#406-quiz-creating-and-dropping)
  - [4.07. Quiz: Declaring Primary Keys](#407-quiz-declaring-primary-keys)
  - [4.08. Declaring Relationships](#408-declaring-relationships)
  - [4.09. Quiz: Foreign Keys](#409-quiz-foreign-keys)
  - [4.10. Self Joins Surprise Quiz](#410-self-joins-surprise-quiz)
  - [4.11. Counting What Isn't There](#411-counting-what-isnt-there)
  - [4.12. Subqueries](#412-subqueries)
  - [4.13. Quiz: One Query Not Two](#413-quiz-one-query-not-two)
  - [4.14. Quiz: Views](#414-quiz-views)
  - [4.15. Reference — Deeper into SQL](#415-reference-—-deeper-into-sql)
  - [4.16. Outro](#416-outro)
  - [Feedback on Lesson 4](#feedback-on-lesson-4)

## Lesson 1. Relational Concepts: Data and Tables

### 1.01. Welcome to RDB

1. Relational concepts
2. SQL queries
3. Python DB-API
4. Advanced SQL

Instructor: Karl Krueger

### 1.02. What's a database

We can either structure application data in memory or in "durable storage." Databases are in durable storage. Items in memory are deleted when the application is closed, but items in durable storage persist.

### 1.03-05. Quizzes about tables and data types

Got them all on the first try.

### 1.06-08. Anatomy of a table with zoo animals

- Karl was buried in a pile of stuffed animals.
- We answered some questions about a database table.

### Aggregations

```sql
AVG
COUNT
MIN
MAX
SUM
```

### 1.10-11. Queries

Our first Udacity SQL query!

```sql
SELECT food FROM diet WHERE species = 'orangutan'
```

How queries happen:

<img src="img/fsnd03_01_11.png">

Karl used the example

```sql
$ psql zoo
zoo => SELECT 2+2 as SUM
```

**Every result returned from a database query is in the form of a table.**

### 1.12-16. `JOIN`, `id` and `PRIMARY KEY`

- Separate, but related tables can reference each other. In Karl's example, one table can list pictures of cats, and another table can track which cat pictures were shown to each person, and which they voted for.
- Tables can also be combined with `JOIN`.

  <img src="img/fsnd03_01_13.png">

- Keys are used to "unambiguously relate a row of one table to a row of another." A `PRIMARY KEY` is a column in a table that uniquely identifies rows.
- Quiz: student ID number and email address could be used as primary keys. Not everyone has a driver's license. "The birthday problem": only need 23 people in a room to have a 50% chance of two people sharing a birthday.
- *How many animals eat fish?*

  ```sql
  -- This SQL query will join the two tables to find out what foods each animal can eat:
  select animals.name, animals.species, diet.food
    from animals join diet
    on animals.species = diet.species;
  ```

### 1.17. Quiz: Database concepts

- We created some database tables for zoo donors, and filled in the tables with the info given.
- I rocked it!

### Feedback on Lesson 1

Clear, helpful and fun! Thanks Karl and Udacity!

[(Back to TOC)](#table-of-contents)

## Lesson 2. Elements of SQL

### 2.01. SQL is for Elephants

### 2.02. Talk to the Zoo Database

They embedded a SQL interpreter in the browser.

```sql
select name, birthdate from animals where species = 'gorilla';
```

When using `SELECT` to isolate columns, either type the column names, with a comma between each name, or just use `*` for wildcard to retrieve all columns.

### 2.03. Types in the SQL World

**Always put 'single quotes' around text strings and datetime values.**

Also see cs50 Lecture 10 20171027 SQL and Databases 0:48:00

### 2.04. Just a few SQL types

Here's just a sampling of the many data types that SQL supports. We won't be using most of these types in this course, though.

The exact list of types differs from one database to another. For a full list of types, check the manual for your database, such as [this one for PostgreSQL](http://www.postgresql.org/docs/9.4/static/datatype.html).

#### Text and string types

text — a string of any length, like Python str or unicode types.
char(n) — a string of exactly n characters.
varchar(n) — a string of up to n characters.

#### Numeric types

- integer — an integer value, like Python int.
- real — a floating-point value, like Python float. Accurate up to six decimal places.
- double precision — a higher-precision floating-point value. Accurate up to 15 decimal places.
- decimal — an exact decimal value.

#### Date and time types

- date — a calendar date; including year, month, and day.
- time — a time of day.
- timestamp — a date and time together.

### 2.05. Select Where

```sql
-- find the names of all the animals that are not
-- gorillas and not named 'Max'.
--
-- my answer
select name from animals where species IS NOT 'gorilla' AND name IS NOT 'Max';

--Karl's solutions
-- first one
select name from animals where (not species = 'gorilla') AND (not name = 'Max');
-- DeMorgan's rule allows us to switch not x and not y into not x or y
select name from animals where not (species = 'gorilla' or name = 'Max');
-- SQL supports the "bang equals" or not equals operator !=
select name from animals where species != 'gorilla' and name != 'Max';
```

### 2.06. Comparison Operators

`=`, `<`, `>`, `<=`, `>=`, `!=`

```sql
-- Find all the llamas born between January 1, 1995 and December 31, 1998.
-- Fill in the 'where' clause in this query.

select * from animals where species = 'llama' and birthdate > '1995-01-01' and birthdate < '1998-12-31'
```

I actually found this quiz kind of difficult, because I wasn't sure if I could perform a mathematical operation like `>` on a string, and because I needed a few tries to get the syntax correct.

### 2.07. The One Thing SQL is Terrible At

**The one thing SQL is terrible at: listing your tables and columns in a standard way!**

They showed an image of an "official IBM flowcharting stencil GX20-8020-1 (late 1970s)."

#### Reference

[18. Reference — Elements of SQL](#18-reference--elements-of-sql)

### 2.08. The Experiment Page

They gave us some test syntax to query the zoo database.

```sql
-- Uncomment one of these queries and use "Test Run" to run it.
-- You'll see the results below.  Then try your own queries as well!

-- select max(name) from animals;

-- select * from animals limit 10;

-- select * from animals where species = 'orangutan' order by birthdate;

-- select name from animals where species = 'orangutan' order by birthdate desc;

-- select name, birthdate from animals order by name limit 10 offset 20;

-- select species, min(birthdate) from animals group by species;

-- select name, count(*) as num from animals
-- group by name
-- order by num desc
-- limit 5;
```

### 2.09. Quiz: Select Clauses

Here are the new select clauses introduced in the previous video (also see part 11 below for another summary):

`... limit count`

Return just the first (count) rows of the result table.

`... limit count offset skip`

Return count rows starting after the first skip rows.

`... order by columns`

`... order by columns desc`

Sort the rows using the columns (one or more, separated by commas) as the sort key. Numerical columns will be sorted in numerical order; string columns in alphabetical order. With desc, the order is reversed (desc-ending order). For example, `order by species, name` will sort the result rows first by the species column, then within each species, sort by the name column.

`... group by columns`

Change the behavior of aggregations such as max, count, and sum. With group by, the aggregation will return one row for each distinct value in columns.

For example,

```sql
select species, min(birthdate) from animals group by species;
```

for each species, find the smallest value of birthdate (the oldest animal's birthdate).

```sql
select name, count(*) as num from animals group by name;
```

count all the rows, call the count column "num," and aggregate by values of the "name" column.

I didn't complete the quiz, because there were too many options, and the solution video wasn't working.

### 2.10. Why Do It in the Database

Why query the database for `limit 100 offset 10` when you could just write `results[10:110]` in Python?

- Speed: "The database can generally do these things a lot faster than Python can. Especially when you get to tables with lots or rows, or complicated queries that join several tables. And you can easily have a table with millions of rows. Sorting a million items in Python can take around a second. If you're writing a web app, that's a second that your user is staring at their browser, wondering why your app is so freaking slow, and it's taking up memory to do that too. In contrast, a database can generally do these operations much faster. **There are a number of tricks you can use to make it faster still. The big one is called indexing.**"
- Space

### 2.11. Quiz: Count All the Species

#### Select clauses

These are all the select clauses we've seen in the lesson so far.

##### where

The where clause expresses restrictions — filtering a table for rows that follow a particular rule. where supports equalities, inequalities, and boolean operators (among other things):

- `where species = 'gorilla'` — return only rows that have 'gorilla' as the value of the species column.
- `where name >= 'George'` — return only rows where the name column is alphabetically after 'George'.
- `where species != 'gorilla' and name != 'George'` — return only rows where species isn't 'gorilla' and name isn't 'George'.

##### limit / offset

The limit clause sets a limit on how many rows to return in the result table. The optional offset clause says how far to skip ahead into the results. So `limit 10 offset 100` will return 10 results starting with the 101st.

##### order by

The `order by` clause tells the database how to sort the results — usually according to one or more columns. So `order by species, name` says to sort results first by the species column, then by name within each species.

Ordering happens before limit/offset, so you can use them together to extract pages of alphabetized results. (Think of the pages of a dictionary.)

The optional desc modifier tells the database to order results in descending order — for instance from large numbers to small ones, or from Z to A.

##### group by

The group by clause is only used with aggregations, such as max or sum. Without a group by clause, a select statement with an aggregation will aggregate over the whole selected table(s), returning only one row. With a group by clause, it will return one row for each distinct value of the column or expression in the group by clause.

#### Quiz

```sql
-- Write a query that returns all the species in the zoo, and how many
-- animals of each species there are, sorted with the most populous
-- species at the top.
--
-- The result should have two columns:  species and number.
--
-- The animals table has columns (name, species, birthdate) for each animal.
```

My first near-winner was

```sql
select species, count(*) as num from animals order by num;
```

but I was confused why it was only returning zebras. The quiz explained:
> You've encountered a nonstandard behavior in SQLite, which is giving you weird results because your query has a count aggregation but doesn't use group by.
>
> Make sure to use group by whenever you use an aggregation.
>
> ```text
> +---------+-----+
> | species | num |
> +=========+=====+
> |   zebra |  89 |
> +---------+-----+
> ```

After running a few more tries in the interpreter, I got it!

```sql
select species, count(*) as num from animals group by species order by num desc;
```

> AHA! I AM INVINCIBLE!

Boris Grishenko, Goldeneye

<img src="img/fsnd03_02_11.png">

### 2.12. Quiz: Insert: Adding Rows

The basic syntax for the `insert` statement:

`insert into table ( column1, column2, ... ) values ( val1, val2, ... );`

If the values are in the same order as the table's columns (starting with the first column), you don't have to specify the columns in the insert statement:

`insert into table values ( val1, val2, ... );`

For instance, if a table has three columns (a, b, c) and you want to insert into a and b, you can leave off the column names from the `insert` statement. But if you want to insert into b and c, or a and c, you have to specify the columns.

A single `insert` statement can only insert into a single table. (Contrast this with the select statement, which can pull data from several tables using a join.)

```python
#
# Insert a newborn baby opossum into the animals table and verify that it's
# been added. To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
#
# SELECT_QUERY should find the names and birthdates of all opossums.
#
# INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
# (Or you can choose any other date you like.)
#
# The animals table has columns (name, species, birthdate) for each individual.
#

SELECT_QUERY = '''
select name, birthdate from animals where species = 'opossum';
'''

INSERT_QUERY = '''
insert into animals values ('Griswold', 'opossum', '2018-01-16');
'''

```

### 2.13. Joining tables: Find the Fish-Eaters

#### 2.13 Quiz

IT'S JOIN TIME!

<img src="img/fsnd03_02_13.png">

```sql
-- Find the names of the individual animals that eat fish.
-- Your query should only return the name column.
-- The animals table has columns (name, species, birthdate) for each individual.
-- The diet table has columns (species, food) for each food that a species eats.

```

I struggled with this exercise. After a few unsuccessful attempts, I went back to the first `join` presented in lesson 1.16:

```sql
-- This SQL query will join the two tables to find out what foods each animal can eat:
select animals.name, animals.species, diet.food
  from animals join diet
  on animals.species = diet.species;
```

I was able to quickly narrow the query result down to the proper `name` column and join the tables, but couldn't figure out where to select just the fish diet:

```sql
select animals.name, diet.food = 'fish'
  from animals join diet
  on animals.species = diet.species;
```

Everything in lesson 2 made sense to me, until "2.13. Find the Fish-Eaters." I was able to quickly narrow the query result down to the proper `name` column and join the tables, but couldn't figure out where to select just the fish diet. The instructional video makes it look like you only need three lines of SQL code for the query, but you actually need a fourth line to specify the restriction. There should have been an extra step where he explained how to incorporate restrictions into joins.

#### Solution

After about an hour, I simply had to check the solution:

```sql
-- Find the names of the individual animals that eat fish.
-- Your query should only return the name column.
-- old syntax
select animals.name from animals join diet
  on animals.species = diet.species
  where food = fish;
```

<img src="img/fsnd03_02_13-solution-old.png">

```sql
-- Find the names of the individual animals that eat fish.
-- Your query should only return the name column.
-- simple syntax
select name from animals, diet
  where animals.species = diet.species
  and diet.food = 'fish';
```

<img src="img/fsnd03_02_13-solution-simple.png">

**I think the point was that the columns you use in a join don't have to be the columns you ask for in a query result.**

### 2.14. After Aggregating

#### `where` vs. `having`

- `where` is a restriction on the source tables.
- `having` is a restriction on the result *after* aggregation.

#### Quiz: Aggregating

<img src="img/fsnd03_02_14.png">

```sql
-- Find the one food that is eaten by only one animal.
--
-- The animals table has columns (name, species, birthdate) for each
-- individual.
-- The diet table has columns (species, food) for each food that a
-- species eats.
```

I got this one relatively quickly. I actually used the simple syntax, and the instructor used the complicated syntax:

```sql
-- Find the one food that is eaten by only one animal.
-- Brendon's solution

select food, count(*) as num
  from diet group by food
  having num = 1;
```

> Here's the solution I got:
>
> ```sql
> -- Find the one food that is eaten by only one animal.
> -- Instructor's solution
> select food, count(*) as num
>   from animals join diet
>   on animals.species = diet.species
>   group by food
>   having num = 1;
> ```
>
> Here, I'm still using a join condition that matches the two tables up using the species column, as we've seen earlier in the lesson. But now I'm adding a count with group by food, to find out how many animals eat each food. Then the having num = 1 clause extracts only those rows where the count is equal to 1.

### 2.15. More Join Practice

#### Database reference

See 2.7 above for description of database.

#### 2.15 Quiz

```sql
-- List all the taxonomic orders, using their common names, sorted by the
-- number of animals of that order that the zoo has.
--
-- The animals table has (name, species, birthdate) for each individual.
-- The taxonomy table has (name, species, genus, family, t_order) for each species.
-- The ordernames table has (t_order, name) for each order.
--
-- Be careful:  Each of these tables has a column "name", but they don't
-- have the same meaning!  animals.name is an animal's individual name.
-- taxonomy.name is a species' common name (like 'brown bear').
-- And ordernames.name is the common name of an order (like 'Carnivores').
```

**This one was another struggle that took me hours.**

##### Review

To start, I reviewed the previous sections:

- The sample queries from 2.8:

  ```sql
  select name, count(*) as num from animals
    group by name
    order by num desc
    limit 5;
  ```

- The last section in which I had sorted stuff, "2.11. Quiz: Count All the Species":

  ```sql
  select species, count(*) as num from animals group by species order by num desc;
  ```

- The difficult quiz in "2.13. Find the Fish-Eaters":

  ```sql
  -- Find the names of the individual animals that eat fish.
  -- Your query should only return the name column.
  -- simple syntax
  select name from animals, diet
    where animals.species = diet.species
    and diet.food = 'fish';
  ```

##### Planning

I saw that I needed to do a join and then a sort, and started planning my approach.

- Join the three tables based on their commonalities
  - Join animals and taxonomy on species (not name, names are different between the two tables)
  - Join taxonomy and ordernames on t_order (again, not on name, names different)
- Count and sort/order the rows
- *List all the taxonomic orders, using their common names:*
  - only display ordernames.name
- *sorted by the number of animals of that order that the zoo has*
  - This requires a join, and a sort.
- *Does it have to be all in one query, or can it be in two queries, like 2.12?*
  - I think it's one query, because 2.12 had one `SELECT` query and one `INSERT` query. This is just a `SELECT` query.

##### Approach

**I broke the problem down and repeatedly iterated my code.**

- First step: try a few queries to look at the tables.

  ```sql
  select * from ordernames limit 10;
  ```

- Next: try some joins.

  ```sql
  -- this seems to successfully join the three tables
  select * from animals, taxonomy, ordernames
    where animals.species = taxonomy.species
    and taxonomy.t_order = ordernames.t_order;
  ```

- Next: try some sorts.

  ```sql
  -- sample sort of ordernames, without join
  select name, count(*) as num from ordernames group by name order by num desc;
  ```

  ```sql
  -- sample sort of animals, without join
  -- close to what we want to see
  select species, count(*) as num from animals
    group by species
    order by num desc;
  ```

- **Next: combine the join and sort. This was the difficult part. I was only able to get it to display two order names, "primates," and "lizards and snakes." I was frustrated by this point, and had spent hours on this one quiz.**

  ```sql
  -- This was as well as I could do on my own.
  -- This only displays primates, and lizards and snakes.
  select ordernames.name, count(*) as num from animals, taxonomy, ordernames
    where animals.species = taxonomy.species
    and taxonomy.t_order = ordernames.t_order
    group by ordernames.name
    order by num desc;
  ```

- **Solutions: For my own sanity, I had to stop and check the instructor's solution after ~5 hours. I was only off from the "simple syntax" solution by one word: I had `taxonomy.species` instead of `taxonomy.name`. I want to understand why I didn't have it right, but the instructor notes don't explain it, and the solution video is complete fluff. Walk us through the solution, don't just talk about the animals!**

  ```sql
  -- Instructor's simple solution:
  select ordernames.name, count(*) as num from animals, taxonomy, ordernames
    where animals.species = taxonomy.name
    and taxonomy.t_order = ordernames.t_order
    group by ordernames.name
    order by num desc;
  ```

  ```sql
  -- And here's another, this time using the explicit join style:
  select ordernames.name, count(*) as num
    from (animals
      join taxonomy on animals.species = taxonomy.name)
      as ani_tax
      join ordernames
        on ani_tax.t_order = ordernames.t_order
    group by ordernames.name
    order by num desc
  ```

  > I think the upper version is much more readable than the lower one, because in the explicit join style you have to explicitly tell the database what order to join the tables in — ((a join b) join c) — instead of just letting the database worry about that.
  >
  > If you're using a more barebones database (like SQLite) there can be a performance benefit to the explicit join style. But in PostgreSQL, the more server-oriented database system we'll be using next lesson, the query planner should optimize away any difference.

### 2.16. Wrap up

### 2.17. Installing the Virtual Machine

[fullstack-nanodegree-vm-instructions.md](fullstack-nanodegree-vm-instructions.md)

### 2.18. Reference — Elements of SQL

This is a reference for the material covered in the "Elements of SQL" lesson.

#### SQL Data Types

Here's just a sampling of the many data types that SQL supports. We won't be using most of these types in this course, though. The exact list of types differs from one database to another. For a full list of types, check the manual for your database, such as this one for PostgreSQL.

##### Text and string

**text** — a string of any length, like Python str or unicode types.
**char(n)** — a string of exactly n characters.
**varchar(n)** — a string of up to n characters.

##### Numeric

**integer** — an integer value, like Python **int**.
**real** — a floating-point value, like Python **float**. Accurate up to six decimal places.
**double precision** — a higher-precision floating-point value. Accurate up to 15 decimal places.
**decimal** — an exact decimal value.

##### Date and time

**date** — a calendar date; including year, month, and day.
**time** — a time of day.
**timestamp** — a date and time together.
**timestamp with time zone** — a timestamp that carries time zone information.

The type **timestamp with time zone** can be abbreviated to **timestamptz** in PostgreSQL.

#### Select statement

The most basic form of the select statement is to select a single scalar value:

```sql
select 2 + 2 ;
```

More usefully, we can select one or more columns from a table. With no restrictions, this will return all rows in the table:

```sql
select name, species from animals ;
```

Columns are separated by commas. Use `*` to select all columns from the tables:

```sql
select * from animals;
```

Quite often, we don't want all the data from a table. We can restrict the rows using a variety of select clauses, listed below. There are also a wide variety of functions that can apply to columns; including aggregation functions that operate on values from several rows, such as **max** and **count**.

##### where clause

The **where** clause expresses restrictions — filtering a table for rows that follow a particular rule. where supports equalities, inequalities, and boolean operators (among other things):

`where species = 'gorilla'` — return only rows that have 'gorilla' as the value of the species column.
`where name >= 'George'` — return only rows where the name column is alphabetically after 'George'.
`where species != 'gorilla' and name != 'George'` — return only rows where species isn't 'gorilla' and name isn't 'George'.

##### limit and offset clauses

The **limit** clause sets a limit on how many rows to return in the result table. The optional **offset** clause says how far to skip ahead into the results. So `limit 10 offset 100` will return 10 results starting with the 101st.

##### order by clause

The order by clause tells the database how to sort the results — usually according to one or more columns. So `order by species, name` says to sort results first by the species column, then by name within each species.

Ordering happens before limit/offset, so you can use them together to extract pages of alphabetized results. (Think of the pages of a dictionary.)

The optional **desc** modifier tells the database to order results in descending order — for instance from large numbers to small ones, or from Z to A.

##### group by clause

The **group by** clause is only used with aggregations, such as **max** or **sum**. Without a **group by** clause, a select statement with an aggregation will aggregate over the whole selected table(s), returning only one row. With a **group by** clause, it will return one row for each distinct value of the column or expression in the **group by** clause.

##### having

The **having** clause works like the where clause, but it applies after **group by** aggregations take place. Here's an example:

```sql
select col1, sum(col2) as total
    from table
    group by col1
    having total > 500 ;
```

Usually, at least one of the columns will be an aggregate function such as count, max, or sum on one of the tables' columns. In order to apply having to an aggregated column, you'll want to give it a name using **as**.

For instance, if you had a table of items sold in a store, and you wanted to find all the items that have sold more than five units, you could use:

```sql
select name, count(*) as num from sales having num > 5;
```

You can have a select statement that uses only where, or only group by, or group by and having, or where and group by, or all three of them! But it doesn't usually make sense to use having without group by.

If you use both **where** and **having**, the **where** condition will filter the rows that are going *into* the aggregation, and the **having** condition will filter the rows that come *out of* it.

You can read more about **having** here: [http://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-HAVING](http://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-HAVING)

#### Insert statement

The basic syntax for the insert statement:

```sql
insert into tablename ( col1, col2, ... ) values ( val1, val2, ... );

```

If the values are in the same order as the table's columns (starting with the first column), you don't have to specify the columns in the insert statement:

```sql
insert into tablename values ( val1, val2, ... );

```

For instance, if a table has three columns **(a, b, c)** and you want to insert into **a** and **b**, you can leave off the column names from the insert statement. But if you want to insert into **b** and **c**, or **a** and **c**, you have to specify the columns.

Normally, a single insert statement can only insert into a single table. (Contrast this with the select statement, which can pull data from several tables using a join.)

### All the tables in the zoo database

A database of zoo animals is used as an example in many of the code exercises in this course. Here's a list of all the tables available in it, and what the columns in each table refer to —

#### animals

This table lists individual animals in the zoo. Each animal has only one row. There may be multiple animals with the same name, or even multiple animals with the same name and species.

**name** — the animal's name (example: 'George')
**species** — the animal's species (example: 'gorilla')
**birthdate** — the animal's date of birth (example: '1998-05-18')

#### diet

This table matches up species with the foods they eat. Every species in the zoo eats at least one sort of food, and many eat more than one.

**species** — the name of a species (example: 'hyena')
**food** — the name of a food that species eats (example: 'meat')

The **diet** table shows an example of the important database concept of *normalization*. If a species eats more than one food, there will be more than one row for that species. We do this instead of having multiple food columns (or storing a list in a single column), both of which would make select statements impractical.

#### taxonomy

This table gives the (partial) biological taxonomic names for each species in the zoo. It can be used to find which species are more closely related to each other evolutionarily.

**name** — the common name of the species (e.g. 'jackal')
**species** — the taxonomic species name (e.g. 'aureus')
**genus** — the taxonomic genus name (e.g. 'Canis')
**family** — the taxonomic family name (e.g. 'Canidae')
**t_order** — the taxonomic order name (e.g. 'Carnivora')

If you've never heard of this classification, don't worry about it; the details won't be necessary for this course. But if you're curious, the Wikipedia article [Taxonomy (biology)](https://en.wikipedia.org/wiki/Taxonomy%5F%28biology%29) may help.

The **t_order** column is not called **order** because "order" is a reserved keyword in SQL.

#### ordernames

This table gives the common names for each of the taxonomic orders in the taxonomy table.

**t_order** — the taxonomic order name (e.g. 'Cetacea')
**name** — the common name (e.g. 'whales and dolphins')

Karl's rainbow cat T-shirt is [The Time is Meow](https://shirt.woot.com/offers/the-time-is-meow) by Rasabi, printed by Woot.

### Time

Lesson 1: ~4 hours 20170115
Lesson 2: 15 hours (~10 hours on 20170116 for 2.1-2.14, ~5 hours on 20170117 for 2.15 More Join Practice)

### Feedback on Lesson 2

#### Full version

I found *Lesson 01. Relational Concepts: Data and Tables* to be clear and intuitive, and I finished in a few hours.

I got stuck on two quizzes in *Lesson 02. Elements of SQL*:

1. *2.13. Find the Fish Eaters:* I was able to quickly narrow the query result down to the proper `name` column and join the tables, but couldn't figure out where to select just the fish diet. The instructional video makes it look like you only need three lines of SQL code for the query, but you actually need a fourth line to specify the restriction. There should have been an extra step where he explained how to incorporate restrictions into joins.
2. *2.15. More Join Practice:* I struggled with this problem for ~5 hours, and I put in the time because I really wanted to learn the syntax. I broke the problem down, repeatedly iterated my code, got as close as I could, and finally checked the solution. I was only off from the "simple syntax" solution by one word: I had `taxonomy.species` instead of `taxonomy.name`. I want to understand why I didn't have it right, but the instructor notes don't explain it, and the solution video is complete fluff. Walk us through the solution, don't just talk about the animals!

#### Concise version to fit into the 512 character limit of the feedback box

Sticking points:

1. *2.13. Find the Fish Eaters:* The instructional video makes it look like you only need three lines of SQL code for the query, but you need a fourth line to specify the restriction. There should be an extra step explaining how to incorporate restrictions into joins.
2. *2.15. More Join Practice:* I was only off from the "simple syntax" solution by one word: I had `taxonomy.species` instead of `taxonomy.name`. The instructor notes don't explain it, and the solution video is just fluff.

[(Back to TOC)](#table-of-contents)

## Lesson 3. Python DB-API

### 3.01. Welcome to your Database

We'll be using Python to connect to our database in a secure, reliable way.

### 3.02. What's a DB-API

<img src="img/fsnd03_03_02.png">

Each database system has its own library:

| Database system | DB-API module |
|:----------------|--------------:|
| SQLite | sqlite3 |
| PostgreSQL | psycopg2 |
| ODBC | pyodbc |
| MySQL | mysql.connector |

### 3.03. Writing Code with DB API

Here's the general process, with my notes based on the instructor Karl's video. This code can be run against a web browser to identify active cookies. Both Chrome and Firefox use SQLite databases to store cookies.

```python
# Import the library for the type of database.
import sqlite3

# Specify the database, called Cookies here.
# The sqlite3.connect() function returns a connection object.
conn = sqlite3.connect("Cookies")

# Next, make a cursor, which runs queries and fetches results.
# The cursor is used to scan through results, like a text cursor in an editor.
cursor = conn.cursor

# Execute a query using the cursor.
cursor.execute("select host_key from cookies limit 10")

# Fetch all results from the query using the cursor.
# The results can be fetched one at a time by using fetchone() instead.
results = cursor.fetchall()

print(results)

# Be sure to close connections when done to avoid stale connections.
conn.close()

```

### 3.04. Quiz: Trying out DB API

Got it on my first try!

```python
# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
#

import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()

```

### 3.05. Quiz: Inserts in DB API

Must add `pg.commit()` to commit changes to database. Changes such as inserts are tracked as transactions in the database (see the `.schema` explanation in cs50 Lecture 10 20171027 SQL and Databases). Changes are made with **atomicity**, meaning they are made entirely, like a single indivisible atom, or not at all.

```python
# This code attempts to insert a new row into the database, but doesn't
# commit the insertion.  Add a commit call in the right place to make
# it work properly.
#

import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()

```

### 3.06. Running the Forum

```bash
vagrant@vagrant:~$ cd /vagrant/forum
vagrant@vagrant:/vagrant/forum$ ls
forumdb.py  forum.py  forum.sql  solution
vagrant@vagrant:/vagrant/forum$ python forum.py
 - Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
```

It just uses python code to run the forum, it doesn't have a database yet.

### 3.07. Hello PostgreSQL

#### Reference info

See *16. Reference — Python DB-API*

Here's a fun one to run in `psql` while your forum web app is running:

`select * from posts \watch`

(Note that `\watch` replaces the semicolon.) This will display the contents of the `posts` table and refresh it every two seconds, so you can see changes to the table as you use the app.

In order to do this, you'll need two terminal sessions into your VM — one running the forum app, and the other running `psql`. You can connect to the VM from any number of terminal windows at once — just open up another terminal, change to the `vagrant` directory, and type `vagrant ssh` again.

### 3.08. Give That App a Backend

```text
vagrant@vagrant:/vagrant/forum$ psql forum
psql (9.5.10)
Type "help" for help.

forum=> select 2+2 as a, 4+4 as b;
 a | b
---+---
 4 | 8
(1 row)

forum=> select * from posts;
 content | time | id
---------+------+----
(0 rows)
```

### 3.09. Bobby Tables, Destroyer of Posts

We tried entering some different types of posts. The instructor Karl said posts with one apostrophe, like
> That's cool
return an internal server error. I was not able to get the error. Karl acknowledges that not everyone will get the bug.

We tried an SQL Injection attack (SQLi) by entering `'); delete from posts; --` as a forum post.

### 3.10. Curing Bobby Tables

We had to revise the *forumdb.py* code here to prevent SQLi, loosely following the paradigm from 3.3-3.5.

As the [psycopg docs](http://initd.org/psycopg/docs/usage.html#the-problem-with-the-query-parameters) warn:
> Warning: Never, never, NEVER use Python string concatenation (+) or string parameters interpolation (%) to pass variables to a SQL query string. Not even at gunpoint.

There is also a [Bobby Tables website](http://bobby-tables.com/) with instructions on how to prevent SQLi in various programming languages.

**It was preferable to follow along in the solution files here.** Karl jumped from `sqlite3` to `psycopg2` and made several other changes to the code. I didn't feel like I had enough information to arrive at the solution independently. I found the code in a separate *solution/* directory and just followed along from there.

### 3.11. Spammy Tables

Karl showed us how to inject some JavaScript spam by submitting this as a forum post:

```html
<script>
setTimeout(function() {
    var tt = document.getElementById('content');
    tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>Spam, spam, spam, spam,<br>Wonderful spam, glorious spam!</h2>";
    tt.form.submit();
}, 2500);
</script>
```

This is called a **script injection attack**.

### 3.12. Quiz: Stopping the Spam

[`bleach`](http://bleach.readthedocs.org/en/latest/) is a python library for stopping spam. Based on the bleach docs, I added `bleach.clean(content)` to the forum code.

We considered both **input sanitization** and **output sanitization.**

*How should we approach the spam?*

> Clearing out bad data before it ever gets into the database — **input sanitization** — is one effective approach to preventing attacks like this one.
>
> But we'll still have to clean out the bad data that's already in the database.

### 3.13. Quiz: Updating Away the Spam

**Karl presented updating the forum posts as one option, but it's not effective. You just replace the spam posts with something else, but all the posts are still there. The posts really need to be deleted.**

> *Instructor notes:*
>
> The syntax of the **update** statement:
>
> **update** *table* **set** *column* **=** *value* **where** *restriction* **;**
>
> The *restriction* works the same as in **select** and supports the same set of operators on column values.
>
> The **like** operator supports a simple form of text pattern-matching. Whatever is on the left side of the operator (usually the name of a text column) will be matched against the pattern on the right. The pattern is an SQL text string (so it's in **'single quotes'**) and can use the **%** sign to match any sub-string, including the empty string.
>
> If you are familiar with regular expressions, think of the **%** in **like** patterns as being like the regex **.*** (dot star).
>
> If you are more familiar with filename patterns in the Unix shell or Windows command prompt, **%** here is a lot like ***** (star) in those systems.
>
> For instance, for a table row where the column **fish** has the value **'salmon'**, all of these restrictions would be true:
>
> - **fish like 'salmon'**
> - **fish like 'salmon%'**
> - **fish like 'sal%'**
> - **fish like '%n'**
> - **fish like 's%n'**
> - **fish like '%al%'**
> - **fish like '%'**
> - **fish like '%%%'**
>
> And all of these would be false:
>
> - **fish like 'carp'**
> - **fish like 'salmonella'**
> - **fish like '%b%'**
> - **fish like 'b%'**
> - **fish like ''**

### 3.14. Quiz: Deleting the Spam

The `DELETE` statement functions like `SELECT`, `UPDATE`, and the other SQL commands.

```sql
DELETE FROM table WHERE restriction;
```

If we want to delete the spam from the forum, we would run

```sql
DELETE * FROM posts WHERE content = 'cheese';
```

### 3.15. Conclusion

### 3.16. Reference — Python DB-API

This is a reference for the material covered in the "Python DB-API" lesson.

#### Python DB-API Quick Reference

For a full reference to the Python DB-API, see [the specification](https://www.python.org/dev/peps/pep-0249/) and the documentation for specific database modules, such as [sqlite3](https://docs.python.org/2/library/sqlite3.html) and [psycopg2](http://initd.org/psycopg/docs/).

**module.connect(...)**
Connect to a database. The arguments to **connect** differ from module to module; see the documentation for details. **connect** returns a **Connection** object or raises an exception.

For the methods below, note that you *don't* literally call (for instance) `Connection.cursor()` in your code. You make a `Connection` object, save it in a variable (maybe called `db`) and then call `db.cursor()`.

**Connection.cursor()**
Makes a **Cursor** object from a connection. Cursors are used to send SQL statements to the database and fetch results.

**Connection.commit()**
Commits changes made in the current connection. You must call **commit** before closing the connection if you want changes (such as inserts, updates, or deletes) to be saved. Uncommitted changes will be visible from your currect connection, but not from others.

**Connection.rollback()**
Rolls back (undoes) changes made in the current connection. You must roll back if you get an exception if you want to continue using the same connection.

**Connection.close()**
Closes the connection. Connections are always implicitly closed when your program exits, but it's a good idea to close them manually especially if your code might run in a loop.

**Cursor.execute(*statement*)**
**Cursor.execute(*statement, tuple*)**
Execute an SQL statement on the database. If you want to substitute variables into the SQL statement, use the second form — see [the documentation](http://initd.org/psycopg/docs/usage.html#query-parameters) for details.

If your statement doesn't make sense (like if it asks for a column that isn't there), or if it asks the database to do something it can't do (like delete a row of a table that is referenced by other tables' rows) you will get an exception.

**Cursor.fetchall()**
Fetch all the results from the current statement.

**Cursor.fetchone()**
Fetch just one result. Returns a tuple, or **None** if there are no results.

#### `psql` Quick Reference

The **psql** command-line tool is really powerful. There's a complete reference to it [in the PostgreSQL documentation](http://www.postgresql.org/docs/9.4/static/app-psql.html).

To connect **psql** to a database running on the same machine (such as your VM), all you need to give it is the database name. For instance, the command **psql forum** will connect to the **forum** database.

From within **psql**, you can run any SQL statement using the tables in the connected database. Make sure to end SQL statements with a semicolon, which is not always required from Python.

You can also use a number of special **psql** commands to get information about the database and make configuration changes. The `\d posts` command shown in the video is one example — this displays the columns of the **posts** table.

Some other things you can do:

`\dt` — list all the tables in the database.

`\dt+` — list tables plus additional information (notably, how big each table is on disk).

`\H` — switch between printing tables in plain text vs. HTML.

##### br3ndonland addition: exiting command prompt

Type `\q` and then press ENTER to quit psql.

#### Bleach documentation

Read the documentation for Bleach here: [http://bleach.readthedocs.org/en/latest/](http://bleach.readthedocs.org/en/latest/)

#### Update and delete statements

The syntax of the **update** and **delete** statements:

**update** *table* **set** *column* **=** *value* **where** *restriction* **;**
**delete from** *table* **where** *restriction* **;**

The **where** restriction in both statements works the same as in **select** and supports the same set of operators on column values. In both cases, if you leave off the **where** restriction, the update or deletion will apply to *all rows* in the table, which is usually not what you want.

#### like operator

The **like** operator supports a simple form of text pattern-matching. Whatever is on the left side of the operator (usually the name of a text column) will be matched against the pattern on the right. The pattern is an SQL text string (so it's in **'single quotes'**) and can use the **%** sign to match any sub-string, including the empty string.

If you are familiar with regular expressions, think of the **%** in **like** patterns as being like the regex **.*** (dot star).

If you are more familiar with filename patterns in the Unix shell or Windows command prompt, **%** here is a lot like ***** (star) in those systems.

For instance, for a table row where the column **fish** has the value **'salmon'**, all of these restrictions would be true:

- **fish like 'salmon'**
- **fish like 'salmon%'**
- **fish like 'sal%'**
- **fish like '%n'**
- **fish like 's%n'**
- **fish like '%al%'**
- **fish like '%'**
- **fish like '%%%'**

And all of these would be false:

- **fish like 'carp'**
- **fish like 'salmonella'**
- **fish like '%b%'**
- **fish like 'b%'**
- **fish like ''**

#### Spam

The term "spam" referring to junk posts comes from [Monty Python's "Spam" sketch](https://www.youtube.com/watch?v=anwy2MPT5RE). On the Internet, "spamming" was first used to mean [repetitious junk messages](http://www.templetons.com/brad/spamterm.html) intended to disrupt a group chat. Later, it came to refer to unsolicited ads on forums or email; and more recently to more-or-less any repetitious or uninvited junk message.

### Feedback on Lesson 3

I thought the material in this lesson was important and helpful, but I didn't really arrive at the solution code independently. I found it more practical to follow along in the solution files starting at "10. Curing Bobby Tables", where Karl switched from `sqlite3` to `psycopg2` and made several other changes to the code.

[(Back to TOC)](#table-of-contents)

## Lesson 4: Deeper into SQL

### 4.01. Intro to Creating Tables

### 4.02. Normalized Design Part One

> In a **normalized database**, the relationships among the tables match the relationships that are really among the data.
>
> Check out William Kent's paper ["A Simple Guide to Five Normal Forms in Relational Database Theory"](http://www.bkent.net/Doc/simple5.htm) for a lot more about normalization and how it can help your database design.

### 4.03. Normalized Design Part Two

1. Every row has the same number of columns.
2. There is a unique **key**, and everything in a row says something about the key.
3. Facts that don't relate to the key belong in different tables.
4. Tables shouldn't imply relationships that don't exist.

### 4.04. Quiz: What's Normalized

### 4.05. Create Table and Types

> User-facing code doesn't *usually* create new tables.

Normally when creating an application, the database is created up front.

### 4.06. Quiz: Creating and Dropping

> Since not everything fits on the screen at once, here's what to try in **psql**:
>
> - Create a new database called **fishies** (or whatever you like).
> - Connect to it with **\\c fishies**, or by exiting **psql** and running **psql fishies**.
> - In the new database, create a table that has two columns: a **text** column and a **serial** column.
> - Try running **insert** statements into this table, providing only a value for the **text** column. (For an example, scroll down to the bottom of this page.)
>
> Look up these commands in the PostgreSQL documentation:
>
> - [Create Database](http://www.postgresql.org/docs/9.4/static/sql-createdatabase.html)
> - [Drop Database](http://www.postgresql.org/docs/9.4/static/sql-dropdatabase.html)
> - [Create Table](http://www.postgresql.org/docs/9.4/static/sql-createtable.html)
> - [Drop Table](http://www.postgresql.org/docs/9.4/static/sql-droptable.html)
>
> Here's an example **insert** statement you might try. Replace *sometable- with the name of the table you created:
>
> **insert into *sometable* values ('This is text!');**
>
> For more detail on the **serial** type, take a look at the last section of this page in the PostgreSQL manual: [http://www.postgresql.org/docs/9.4/static/datatype-numeric.html](http://www.postgresql.org/docs/9.4/static/datatype-numeric.html)

```text
vagrant@vagrant:/vagrant$ psql
psql (9.5.10)
Type "help" for help.

vagrant=> CREATE DATABASE sardines;
CREATE DATABASE
vagrant=> \c sardines
You are now connected to database "sardines" as user "vagrant".
sardines=> CREATE TABLE FISH (
sardines(> text text,
sardines(> serial varchar );
CREATE TABLE
sardines=> INSERT INTO FISH values ('This is text!');
INSERT 0 1
sardines=>
```

A serial is a sequence, an internal data structure.

### 4.07. Quiz: Declaring Primary Keys

*Single column primary keys:* enter "primary key" when creating the column, before the comma:

```sql
CREATE TABLE students (
  id serial primary key,
  name text,
  birthdate date
);
```

*Multi-column primary keys:* enter *after* creating the columns in the table, and specify the columns to use as key:

```sql
CREATE TABLE postal_places (
  postal_code text,
  country text,
  name text,
  primary key (postal_code, country)
);
```

Quiz: if we create a second entry with the same primary key as a prior entry, SQL will return an error.

> If we set up a constraint (such as a primary key) we're asking for the database to help ensure that our data makes sense.
>
> By signaling an error, the database refuses to accept data that break the "rule" that we've created by adding a primary key constraint.

### 4.08. Declaring Relationships

As an example, Karl used a list of products, each with a corresponding SKU (Stock Keeping Unit).

**Reference constraints** can be used to tell the SQL database that a column should only have values that refer to the key of another table. They are created using `references`, followed by the table name (`products` in this case):

```sql
create table sales (
  sku text references products,
  sale_date date,
  count integer
);
```

If the column name is not the same in both tables, specify the name in parentheses, like `products (sku)`.

References ensure **referential integrity**.

### 4.09. Quiz: Foreign Keys

Columns with reference constraints are also called **foreign keys.** Foreign keys point to a primary key in the reference table. The values of a foreign key must match the values of the primary key.

### 4.10. Self Joins Surprise Quiz

Why are we taking a quiz on self joins when we haven't learned about self joins? I can look it up in external documentation or check the solution, but then why have a quiz?

#### Self joins quiz

Karl shows a list of dormitories from his college. Based on a search of the list, it looks like [Bard College at Simon's Rock](https://simons-rock.edu/), for students who graduate early from high school.

```sql
-- Roommate Finder v0.9
--
-- This query is intended to find pairs of roommates.  It almost works!
-- There's something not quite right about it, though.  Find and fix the bug.

select a.id, b.id, a.building, a.room
       from residences as a, residences as b
 where a.building = b.building
   and a.room = b.room
 order by a.building, a.room;

-- To see the complete residences table, comment out the query above,
-- uncomment this query and press "Test Run":

-- select id, building, room from residences;
```

#### Self joins quiz troubleshooting

- We are displaying the correct columns, so the `SELECT` statement is fine. Replacing the `SELECT` statement with `SELECT *` shows too many columns.
- We are displaying too many rows, which means there is a problem with the aggregation.
- I next tried modifying the `WHERE` statement.
  - Removing `and a.room = b.room` doesn't help.
  - Adding `AND NOT a.id = b.id`, or `AND a.id <> b.id` (syntax I found on [w3schools](https://www.w3schools.com/sql/sql_join_self.asp)) is a step in the right direction. It removes the rows with two of the same ID, but there are still two rows for each pair of roommates.
- **We need a multi-column primary key.**
  - So far, we've only set keys when creating tables (see 7. Quiz: Declaring Primary Keys).
  - It would look like `primary key (building, room)`.

#### Self joins quiz solution

<details><summary>Solution</summary>

The solution was actually just to add `and a.id < b.id`.

Final code:

```sql
-- Roommate Finder v1.0

select a.id, b.id, a.building, a.room
  from residences as a, residences as b
  where a.building = b.building
    and a.room = b.room
    and a.id < b.id
  order by a.building, a.room;
```

</details>

### 4.11. Counting What Isn't There

#### Instructor notes

They introduced left and right joins here. Left and right refer to the two tables being joined.

> Counting rows in a single table is something you’ve seen many times before in this course. A column aggregated with the **count** aggregation function will return the number of rows in the table, or the number of rows for each value of a **group by** clause.
>
> For instance, you saw queries like these back in Lesson 2:
>
> - `select count(*) from animals;` returns the number of animals in the zoo_
> - `select count(*) from animals where species = 'gorilla';` returns the number of gorillas_
> - `select species, count(*) from animals group by species;` returns each species’ name and the number of animals of that species_
>
> Things get a little more complicated if you want to count the results of a **join**. Consider the tables we saw earlier in Lesson 4, the **products** and **sales** tables for a store.
>
> Suppose that we want to know how many times we have sold each product. In other words, for each **sku** value in the **products** table, we want to know the number of times it occurs in the **sales** table. We might start out with a query like this:
> ```sql
> select products.name, products.sku, count(*) as num
>   from products join sales
>     on products.sku = sales.sku
>   group by products.sku;
> ```
>
> But this query might not do exactly what we want. If a particular **sku** has never been sold — if there are no entries for it in the **sales** table — then this query will not return a row for it at all.
>
> If we wanted to see a row with the number zero in it, we’ll be disappointed!
>
> However, there is a way to get the database to give us a count with a zero in it. To do this, we’ll need to change two things about this query —
> ```sql
> select products.name, products.sku, count(sales.sku) as num
>   from products left join sales
>     on products.sku = sales.sku
>   group by products.sku;
> ```
>
> This query will give us a row for every product in the **products** table, even the ones that have no sales in the **sales** table.
>
> What’s changed? First, we’re using **count(sales.sku)** instead of **count(*)**. This means that the database will count only rows where **sales.sku** is defined, instead of all rows.
>
> Second, we’re using a **left join** instead of a plain **join**.
>
> *Um, so what’s a left join?*
>
> SQL supports a number of variations on the theme of joins. The kind of join that you have seen earlier in this course is called an _inner_ join, and it is the most common kind of join — so common that SQL doesn’t actually make us say "inner join" to do one.
>
> But the second most common is the **left join**, and its mirror-image partner, the **right join**. The words “left” and “right” refer to the tables to the left and right of the join operator. (Above, the left table is **products** and the right table is **sales**.)
>
> A regular (inner) join returns only those rows where the two tables have entries matching the join condition. A **left join** returns all those rows, plus the rows where the _left_ table has an entry but the right table doesn’t. And a **right join** does the same but for the _right_ table.
>
> (Just as “join” is short for “inner join”, so too is “left join” actually short for “left outer join”. But SQL lets us just say “left join”, which is a lot less typing. So we’ll do that.)

#### Joins quiz

```sql
-- Here are two tables describing bugs found in some programs.
-- The "programs" table gives the name of each program and the files
-- that it's made of.  The "bugs" table gives the file in which each
-- bug was found.
--
-- create table programs (
--    name text,
--    filename text
-- );
-- create table bugs (
--    filename text,
--    description text,
--    id serial primary key
-- );
--
-- The query below is intended to count the number of bugs in each
-- program. But it doesn't return a row for any program that has zero
-- bugs. Try running it as it is.  Then change it so that the results
-- will also include rows for the programs with no bugs.  These rows
-- should have a 0 in the "bugs" column.

select programs.name, count(*) as num
   from programs join bugs
        on programs.filename = bugs.filename
   group by programs.name
   order by num;

```

Got it on my first try!

```sql
select programs.name, count(bugs.id) as num
   from programs left join bugs
        on programs.filename = bugs.filename
   group by programs.name
   order by num;

```

#### Quiz instructor notes

> Something to watch out for: What do you put in the count aggregation? If you leave it as count(*) or use a column from the programs table, your query will count entries that don't have bugs as well as ones that do.
>
> In order to correctly report a zero for programs that don't have any entries in the bugs table, you have to use a column from the bugs table as the argument to count.
>
> For instance, count(bugs.filename) will work, and so will count(bugs.description).

### 4.12. Subqueries

Queries within queries. How deep does the rabbit hole go?

```sql
select avg(bigscore) from
  (select max(score)
    as bigscore
    from mooseball
    group by team)
  as maxes;
```

<img src="img/fsnd03_04_12.png">

Nested like a [Russian doll](https://github.com/tthibo/SQL-Tutorial/blob/master/tutorial_files/part2.textile#subqueries-the-russian-dolls-of-sql).

> Here are some sections in the PostgreSQL documentation that discuss other forms of subqueries:
>
> - [Scalar Subqueries](http://www.postgresql.org/docs/9.4/static/sql-expressions.html#SQL-SYNTAX-SCALAR-SUBQUERIES)
> - [Subquery Expressions](http://www.postgresql.org/docs/9.4/static/functions-subquery.html)
> - [The FROM clause](http://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-FROM)

### 4.13. Quiz: One Query Not Two

```python
# Find the players whose weight is less than the average.
#
# The function below performs two database queries in order to find the right players.
# Refactor this code so that it performs only one query.
#

def lightweights(cursor):
    """Returns a list of the players in the db whose weight is less than the average."""
    cursor.execute("select avg(weight) as av from players;")
    av = cursor.fetchall()[0][0]  # first column of first (and only) row
    cursor.execute("select name, weight from players where weight < " + str(av))
    return cursor.fetchall()

```

I didn't have much patience for this quiz. I tried out a few things. It seemed like I had the two queries joined properly, but I wasn't sure how to get it to run with the Python code. Again, the solution video was not very helpful, because it only showed the SQL query, and not the surrounding Python code that I was having trouble with.

```sql
SELECT name, weight FROM players,
  (SELECT avg(weight) as av
    FROM players as subquery)
  WHERE weight < av;
```

I plugged it in to get the full Python solution:

```python
def lightweights(cursor):
    """Returns a list of the players in the db whose weight is less than the average."""
    cursor.execute(
        "SELECT name, weight FROM players, (SELECT avg(weight) as av FROM players as subquery) WHERE weight < av;")
    return cursor.fetchall()

```

### 4.14. Quiz: Views

#### Intro

When code gets too complex, developers look for ways to *refactor* it into smaller functions.

**Views** are `SELECT` queries stored in the database for use like tables. Rows can be updated or deleted from some views but not others.

#### Views quiz

This quiz was much easier because it only required a small amount of additional code.

```sql
-- Here's a select statement that runs on the zoo database.
-- It selects the species with the top five highest populations in the zoo.
-- Change it into a statement that creates a view named "topfive".

CREATE view topfive as
select species, count(*) as num
  from animals
  group by species
  order by num desc
  limit 5;


-- Don't change the statement below!  It's there to test the view.

select * from topfive;

```

### 4.15. Reference — Deeper into SQL

This is a reference for the material covered in the "Deeper into SQL" lesson.

#### The `create table` statement

The full syntax of the **create table** statement is quite complex. See the [PostgreSQL **create table** documentation](http://www.postgresql.org/docs/9.4/static/sql-createtable.html) for the whole thing. Here's the syntax for the form we're seeing in this lesson:

```sql
create table table ( column type [restriction] , ... ) [rowrestriction] ;
```

There are a lot of restrictions that can be put on a column or a row. **primary key** and **references** are just two of them. See the "Examples" section of the [**create table** documentation](http://www.postgresql.org/docs/9.4/static/sql-createtable.html) for many, many more.

#### Rules for normalized tables

In a normalized database, the relationships among the tables match the relationships that are really there among the data. Examples [here](https://www.udacity.com/course/viewer#!/c-ud197/l-3490418600/m-3514018646) refer to tables in Lessons 2 and 4.

1. Every row has the same number of columns.
    - In practice, the database system won't let us *literally* have different numbers of columns in different rows. But if we have columns that are sometimes empty (null) and sometimes not, or if we stuff multiple values into a single field, we're bending this rule.
    - The example to keep in mind here is the **diet** table from the zoo database. Instead of trying to stuff multiple foods for a species into a single row about that species, we separate them out. This makes it much easier to do aggregations and comparisons.
2. There is a unique *key* and everything in a row says something about the key.
    - The key may be one column or more than one. It may even be the whole row, as in the **diet** table. But we don't have duplicate rows in a table.
    - More importantly, if we are storing non-unique facts — such as people's names — we distinguish them using a unique identifier such as a serial number. This makes sure that we don't combine two people's grades or parking tickets just because they have the same name.
3. Facts that don't relate to the key belong in different tables.
    - The example here was the **items** table, which had items, their locations, and the location's street addresses in it. The address isn't a fact about the item; it's a fact about the location. Moving it to a separate table saves space and reduces ambiguity, and we can always reconstitute the original table using a **join**.
4. Tables shouldn't imply relationships that don't exist.
    - The example here was the **job_skills** table, where a single row listed one of a person's technology skills (like 'Linux') and one of their language skills (like 'French'). This made it look like their Linux knowledge was specific to French, or vice versa ... when that isn't the case in the real world. Normalizing this involved splitting the tech skills and job skills into separate tables.

#### The serial type

For more detail on the **serial** type, take a look at the last section of [this page in the PostgreSQL manual](http://www.postgresql.org/docs/9.4/static/datatype-numeric.html).

#### Other subqueries

Here are some sections in the PostgreSQL documentation that discuss other forms of subqueries besides the ones discussed in this lesson:

- [Scalar Subqueries](http://www.postgresql.org/docs/9.4/static/sql-expressions.html#SQL-SYNTAX-SCALAR-SUBQUERIES)
- [Subquery Expressions](http://www.postgresql.org/docs/9.4/static/functions-subquery.html)
- [The FROM clause](http://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-FROM)

Mooseball is not a real sport (yet), but you can get a roughly [ball-shaped moose](http://www.squishable.com/pc/squish_moose_15/Big_Animals/Squishable+Moose) from Squishables.

### 4.16. Outro

### Feedback on Lesson 4

*4.10. Self Joins:* I wasn't sure why we had a quiz on self joins before learning about that topic. I can look it up in external documentation or check the solution, but then why have a quiz? Also, introducing self joins right after foreign keys made me think the self joins quiz involved a multi-column foreign key, leading me away from the solution.

*4.14. Quiz: Views* was an example of an easier quiz. We only had to add a small amount of code, and it followed very well from Karl's introduction.

[(Back to TOC)](#table-of-contents)