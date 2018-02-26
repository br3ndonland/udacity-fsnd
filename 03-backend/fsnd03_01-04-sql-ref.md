# SQL reference material

**Udacity Full Stack Web Developer Nanodegree program**

Part 03. Backend

Lessons 01-04

Brendon Smith

br3ndonland

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Lesson 2](#lesson-2)
  - [2.18. Reference — Elements of SQL](#218-reference--elements-of-sql)
- [Lesson 3](#lesson-3)
  - [3.16. Reference — Python DB-API](#316-reference--python-db-api)
- [Lesson 4](#lesson-4)
  - [4.15. Reference — Deeper into SQL](#415-reference--deeper-into-sql)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Lesson 2
[back to top](#top)

###  2.18. Reference — Elements of SQL

This is a reference for the material covered in the "Elements of SQL" lesson.


#### SQL Data Types

Here's just a sampling of the many data types that SQL supports. We won't be using most of these types in this course, though. The exact list of types differs from one database to another. For a full list of types, check the manual for your database, such as this one for PostgreSQL.


##### Text and string types

**text** — a string of any length, like Python str or unicode types.  
**char(n)** — a string of exactly n characters.  
**varchar(n)** — a string of up to n characters.


##### Numeric types

**integer** — an integer value, like Python **int**.  
**real** — a floating-point value, like Python **float**. Accurate up to six decimal places.  
**double precision** — a higher-precision floating-point value. Accurate up to 15 decimal places.  
**decimal** — an exact decimal value.


##### Date and time types

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

Columns are separated by commas; use * to select all columns from the tables:

```sql
select * from animals;
```

Quite often, we don't want all the data from a table. We can restrict the rows using a variety of select clauses, listed below. There are also a wide variety of functions that can apply to columns; including aggregation functions that operate on values from several rows, such as **max** and **count**.


##### where

The **where** clause expresses restrictions — filtering a table for rows that follow a particular rule. where supports equalities, inequalities, and boolean operators (among other things):

* `where species = 'gorilla'` — return only rows that have 'gorilla' as the value of the species column.  
* `where name >= 'George'` — return only rows where the name column is alphabetically after 'George'.  
* `where species != 'gorilla' and name != 'George'` — return only rows where species isn't 'gorilla' and name isn't 'George'.


##### limit / offset

The **limit** clause sets a limit on how many rows to return in the result table. The optional **offset** clause says how far to skip ahead into the results. So `limit 10 offset 100` will return 10 results starting with the 101st.


##### order by

The order by clause tells the database how to sort the results — usually according to one or more columns. So `order by species, name` says to sort results first by the species column, then by name within each species.

Ordering happens before limit/offset, so you can use them together to extract pages of alphabetized results. (Think of the pages of a dictionary.)

The optional **desc** modifier tells the database to order results in descending order — for instance from large numbers to small ones, or from Z to A.


##### group by

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

```
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


## Lesson 3
[back to top](#top)

### 3.16. Reference — Python DB-API

This is a reference for the material covered in the "Python DB-API" lesson.


#### Python DB-API Quick Reference

For a full reference to the Python DB-API, see [the specification](https://www.python.org/dev/peps/pep-0249/) and the documentation for specific database modules, such as [sqlite3](https://docs.python.org/2/library/sqlite3.html) and [psycopg2](http://initd.org/psycopg/docs/).

***module*.connect(...)**  
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

*   **fish like 'salmon'**
*   **fish like 'salmon%'**
*   **fish like 'sal%'**
*   **fish like '%n'**
*   **fish like 's%n'**
*   **fish like '%al%'**
*   **fish like '%'**
*   **fish like '%%%'**

And all of these would be false:

*   **fish like 'carp'**
*   **fish like 'salmonella'**
*   **fish like '%b%'**
*   **fish like 'b%'**
*   **fish like ''**


#### Spam

The term "spam" referring to junk posts comes from [Monty Python's "Spam" sketch](https://www.youtube.com/watch?v=anwy2MPT5RE). On the Internet, "spamming" was first used to mean [repetitious junk messages](http://www.templetons.com/brad/spamterm.html) intended to disrupt a group chat. Later, it came to refer to unsolicited ads on forums or email; and more recently to more-or-less any repetitious or uninvited junk message.


## Lesson 4
[back to top](#top)

### 4.15. Reference — Deeper into SQL

This is a reference for the material covered in the "Deeper into SQL" lesson.


#### The `create table` statement


The full syntax of the **create table** statement is quite complex. See the [PostgreSQL **create table** documentation](http://www.postgresql.org/docs/9.4/static/sql-createtable.html) for the whole thing. Here's the syntax for the form we're seeing in this lesson:
```
**create table** _table_ **(** _column type \[restriction\]_ **,** ... **)** _\[rowrestriction\]_ **;**
```
There are a lot of restrictions that can be put on a column or a row. **primary key** and **references** are just two of them. See the "Examples" section of the [**create table** documentation](http://www.postgresql.org/docs/9.4/static/sql-createtable.html) for many, many more.


#### Rules for normalized tables

In a normalized database, the relationships among the tables match the relationships that are really there among the data. Examples [here](https://www.udacity.com/course/viewer#!/c-ud197/l-3490418600/m-3514018646) refer to tables in Lessons 2 and 4.

1. Every row has the same number of columns.

    In practice, the database system won't let us _literally_ have different numbers of columns in different rows. But if we have columns that are sometimes empty (null) and sometimes not, or if we stuff multiple values into a single field, we're bending this rule.

    The example to keep in mind here is the **diet** table from the zoo database. Instead of trying to stuff multiple foods for a species into a single row about that species, we separate them out. This makes it much easier to do aggregations and comparisons.

2. There is a unique _key_ and everything in a row says something about the key.

    The key may be one column or more than one. It may even be the whole row, as in the **diet** table. But we don't have duplicate rows in a table.

    More importantly, if we are storing non-unique facts — such as people's names — we distinguish them using a unique identifier such as a serial number. This makes sure that we don't combine two people's grades or parking tickets just because they have the same name.

3. Facts that don't relate to the key belong in different tables.

    The example here was the **items** table, which had items, their locations, and the location's street addresses in it. The address isn't a fact about the item; it's a fact about the location. Moving it to a separate table saves space and reduces ambiguity, and we can always reconstitute the original table using a **join**.

4. Tables shouldn't imply relationships that don't exist.

    The example here was the **job_skills** table, where a single row listed one of a person's technology skills (like 'Linux') and one of their language skills (like 'French'). This made it look like their Linux knowledge was specific to French, or vice versa ... when that isn't the case in the real world. Normalizing this involved splitting the tech skills and job skills into separate tables.


#### The **serial** type

For more detail on the **serial** type, take a look at the last section of [this page in the PostgreSQL manual](http://www.postgresql.org/docs/9.4/static/datatype-numeric.html).


#### Other subqueries

Here are some sections in the PostgreSQL documentation that discuss other forms of subqueries besides the ones discussed in this lesson:

* [Scalar Subqueries](http://www.postgresql.org/docs/9.4/static/sql-expressions.html#SQL-SYNTAX-SCALAR-SUBQUERIES)  
* [Subquery Expressions](http://www.postgresql.org/docs/9.4/static/functions-subquery.html)  
* [The FROM clause](http://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-FROM)

[back to top](#top)
