# README

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/)

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/br3ndonland/udacity-fsnd/master?urlpath=lab)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Projects](#projects)
- [Lessons](#lessons)
  - [Strategies](#strategies)
  - [Course progression](#course-progression)
- [Code](#code)
  - [Markdown](#markdown)
  - [Python](#python)
  - [Software](#software)

## Description

This is a repository for [Udacity Full Stack Web Developer Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) (FSND) course notes and materials.

## Projects

The Full Stack Web Developer Nanodegree program is focused on projects, in which students can independently implement what they have learned in the lessons. I stored each project in its own repository.

1. [Python web server movie trailer site](https://github.com/br3ndonland/udacity-fsnd-p1-python-movie-site)
2. [Portfolio website](https://br3ndonland.github.io/udacity/)
3. [SQL database logs analysis](https://github.com/br3ndonland/udacity-fsnd-p3-sql)
4. [Python Flask catalog app](https://github.com/br3ndonland/udacity-fsnd-p4-flask-catalog)
5. [Neighborhood map app](https://br3ndonland.github.io/udacity-map/)
6. [Linux server deployment](https://github.com/br3ndonland/udacity-fsnd-p6-server)

## Lessons

Udacity provides lessons prior to each project. The lesson curriculum could benefit from some reorganization. I have included my suggested organization below, and have organized repository materials in my suggested order.

### Strategies

- **Limit lesson time**: Speed up videos to 1.5x or 2x, and set a timer when working through the lessons. I used the [Pomodoro technique](https://lifehacker.com/productivity-101-a-primer-to-the-pomodoro-technique-1598992730), and limited myself to 25 minutes max per lesson section. I would often complete 2-3 lesson sections per 25 minute interval.
- **Limit quiz attempts**: When I was getting started, I aimed to complete 100% of the lesson material, and I took the quizzes too seriously. I pushed myself to get answer quiz questions correctly without checking solutions. This caused me to hit sticking points, and I would sometimes take 1-2 days just to complete a quiz. As I went on, I set a limit of three quiz attempts. If I didn't get it in three attempts, I would check the solution and move on.
- **Focus on the projects**: The Nanodegree is awarded for projects, not lessons and quizzes. As you advance, you may want to just skip directly to the projects, and go back through the lessons as needed.

See my [program feedback](info/fsnd-feedback.md) for more comments.

### Course progression

Here is how I would suggest progressing through the FSND program:

1. **Programming foundations**
    - [Shell Workshop](https://www.udacity.com/course/shell-workshop--ud206)
    - [Version Control with Git](https://www.udacity.com/course/version-control-with-git--ud123)
    - [GitHub & Collaboration](https://www.udacity.com/course/github-collaboration--ud456)
    - [Programming Foundations with Python](https://www.udacity.com/course/programming-foundations-with-python--ud036)
    - [HTTP & Web Servers](https://www.udacity.com/course/http-web-servers--ud303): Python web servers
    - Project 1: Python web server (movie trailer site)
2. **The front-end**
    - [Intro to HTML and CSS](https://www.udacity.com/course/intro-to-html-and-css--ud001)
    - [Responsive Web Design Fundamentals by Google](https://www.udacity.com/course/responsive-web-design-fundamentals--ud893)
    - Project 2: Portfolio website
3. **The back-end**
    - [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)
    - Project 3: SQL database logs analysis
4. **Web applications**
    - [Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088): CRUD, web servers, Flask, agile
    - [Authentication & Authorization: OAuth](https://www.udacity.com/course/authentication-authorization-oauth--ud330)
    - Project 04: Flask item catalog app
    - JavaScript
    - jQuery
    - [Intro to AJAX](https://www.udacity.com/course/intro-to-ajax--ud110)
    - APIs
    - [Designing RESTful APIs](https://www.udacity.com/course/designing-restful-apis--ud388)
    - Project 05: Neighborhood map
5. **Servers**
    - Linux server deployment
    - Project 06: Linux server

[(Back to TOC)](#table-of-contents)

## Code

### Markdown

#### Markdown intro

**Markdown is a syntax for easy generation of HTML pages from plain text files.** It has most of the functionality of HTML while being much easier to read, and is very widely used (for example, READMEs on GitHub).

I take notes on the lessons in Markdown.

When coding projects, I keep **computational narratives** describing what I do at each step, like journals or lab notebooks. I learned how to keep computational narratives from scientific computing in Jupyter Notebook/JupyterLab and RMarkdown. **Computational narratives capture the process, so I can retrace my steps, retain what I have learned, and teach others.**

Examples of my computational narratives are available for projects including the [portfolio website](https://br3ndonland.github.io/udacity/methods/) and the [SQL database logs analysis](https://github.com/br3ndonland/udacity-fsnd-p3-sql/blob/master/logs-methods.md). I also created a [Markdown guide](https://github.com/br3ndonland/udacity-google/blob/master/markdown-guide.md) during the Grow with Google program to explain how I use Markdown.

#### Syntactic suggestions

Suggestions for standardized Markdown formatting have been provided by [markdownlint](https://github.com/DavidAnson/markdownlint) and [Markdown Style Guide](http://www.cirosantilli.com/markdown-style-guide/). Here are a few personal pointers:

##### Headers

- Create headers with `#`. Each `#` increases header level (`##` is outline level two), up to six levels.
- **For organization, I reserve H1 (`#`) for the title of the file at the top. Major headers begin with H2 (`##`).**
- I use headers to create a **Table of Contents (TOC)** at the beginning of the file.
  - **I add `## Table of Contents` before the TOC for navigation.**
  - **I include [(Back to TOC)](#table-of-contents) links after each section for easy navigation back to the table of contents.** Simply write `[(Back to TOC)](#table-of-contents)`.
  - I add and auto-update TOCs in vscode with the [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) extension.
  - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one), JupyterLab and RStudio provide inline TOC displays ([see below](#jupyterlab)).
  - Prior to vscode, I was adding and updating TOCs with [DocToc](https://github.com/thlorenz/doctoc) from the command line.

##### Lists

- I use dashes exclusively for lists.
- When adding an unordered list to an ordered list, I indent with four spaces.

##### File extensions

- Several different extensions can be used, including .md, .mdown, and .markdown.
- **I prefer to use .md for brevity and consistency.**

### Python

Python code is formatted for Python 3 and [PEP 8](http://pep8.org/). Line length is relaxed to 100 characters when permitted.

### Software

For the foundational Python programming work (part 1, lessons 00-11), I took notes and ran my code in Jupyter notebook files. Jupyter notebook was a nice way to bundle Markdown-formatted notes with Python code, but it lacked the speed and autocompletion features of other text editors.

As I continued, I kept separate files for code and Markdown notes. I was originally writing in Sublime Text, but switched to [vscode](https://code.visualstudio.com/). I configure [Visual Studio Code (vscode)](https://code.visualstudio.com/) using [Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) with [this gist](https://gist.github.com/br3ndonland/d6ad1f6eae5ee149ac2530774d13899e).

For my terminal application, I switched from iTerm2 to [Hyper](https://hyper.is/).

I used Google Chrome and Firefox Quantum as web browsers.

Some of the work was done in a Vagrant Linux virtual machine with the following components:

- Oracle [VirtualBox](https://www.virtualbox.org/wiki/Downloads) Version 5.2.6 r120293 (Qt5.6.3)
  - Software that runs special containers called virtual machines, like Vagrant.
- [Vagrant](https://www.vagrantup.com/) 2.0.1 with Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-75-generic i686)
  - Software that provides the Linux operating system in a defined configuration, allowing it to run identically across many personal computers. Linux can then be run as a virtual machine with VirtualBox.
- [Udacity Virtual Machine configuration](https://github.com/udacity/fullstack-nanodegree-vm)
  - Repository from Udacity that configures Vagrant.
  - My personal fork of the configuration is also available on [GitHub](https://github.com/br3ndonland/fullstack-nanodegree-vm) if needed.

[(Back to TOC)](#table-of-contents)