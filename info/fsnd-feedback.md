# Program feedback

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

[br3ndonland](https://github.com/br3ndonland)

## Table of Contents <!-- omit in toc -->

- [Highlights](#highlights)
- [Lessons](#lessons)
  - [Code and tech](#code-and-tech)
  - [Organization](#organization)
  - [Time](#time)
- [Mentor](#mentor)
- [Networking](#networking)
  - [Forums](#forums)
  - [Slack](#slack)
  - [In-classroom chat](#in-classroom-chat)
  - [Knowledge](#knowledge)
- [Exit survey](#exit-survey)
- [Program developments](#program-developments)

## Highlights

- **Code review was wonderful.** I was really impressed with how thoughtful and thorough the reviews were. I learned a great deal from the suggestions in the reviews. The turnaround time was very fast, sometimes only a few hours.
- The website and Android app were generally responsive and powerful.

[(Back to top)](#top)

## Lessons

### Code and tech

- It was good that we used Python instead of Ruby. Python is more flexible. For example, I also have training in data science, so I can use my Python skills for data analysis, which I couldn't really do with Ruby.
- Some frameworks, like Flask, were current, others, like Knockout, were outdated.
- The Vagrant virtual machine was helpful, but a little bit complicated. Udacity could **consider containerizing the code** for further control over the environment, and easier setup by students.
- **The code in the lessons is of inconsistent quality. We are learning, and we need to see well-structured, consistent, and current code.** Udacity is focused on releasing new Nanodegree programs, without maintaining the programs they already have. We need to learn based on current best practices, which requires frequent updates. Compare Udacity's lack of updates with someone like [Wes Bos](http://wesbos.com/), for example, who has already re-recorded his React course three times. And that's just one guy. Udacity has an entire company full of people, and they can't even maintain their lessons and code.
  - Let's look at an example, Lessons 14-18 on APIs (from free course [Designing RESTful APIs](https://www.udacity.com/course/designing-restful-apis--ud388))
    - Python 2 instead of 3
    - HTTP requests use `httplib2` instead of `requests`
    - Authentication is done with `oauth2client`, which [has been deprecated](https://google-auth.readthedocs.io/en/latest/oauth2client-deprecation.html).
    - Code is not PEP 8 compliant, yet we are required to submit PEP 8 compliant code for the item catalog project.
    - Code mixes spaces and tabs.
    - JavaScript camelCase used instead of underscores for function names.
    - Doesn't even have a proper Markdown-formatted README
    - No license. How can you distribute this material to students without a license?
    - Code exists, confusingly, in two repos: [OAuth2.0](https://github.com/udacity/OAuth2.0) and [ud330](https://github.com/udacity/ud330). The code in ud330 is formatted a little better than the OAuth repo.
- **Udacity's GitHub repos are not maintained. Pull requests are ignored or not merged.** The GitHub repos are an opportunity to enrich the student experience by teaching good open source practices, but Udacity is not doing this.
- Many of the repos are not licensed.
- In addition to videos, the lessons should have Markdown-formatted **written lesson outlines**.

[(Back to top)](#top)

### Organization

**The program could benefit from reorganization.**

#### Part 1

- I didn't find the first project, the Python movie trailer web server (after the Python programming foundations), to be very effective. I completed the project before learning about front-end and HTTP, so I didn't really know what I was doing. The project would make more sense after part 2 instead of after part 1.
- This also wasn't a really effective way to implement a web server. The server would be more effectively implemented as a Flask app, as we did for the item catalog in part 3.

#### Part 2

- Part 2 was designated as "optional," but really, all the lessons are optional, so this distinction was not useful.
- It would have been helpful to know more about the shell, Git, and GitHub before doing the first project.
- I would suggest moving the Python HTTP requests lessons (Part 02, Lessons 11-13) to Part 01 between the foundational Python programming (Part 01, Lessons 04-11) and the front-end web lessons (Part 01, lessons 12-19). This would improve the continuity of Python programming, and also teach foundations of how the web works, before moving in-depth into front-end.

#### Part 3

- Why did we go through APIs in part 3 (from course [Designing RESTful APIs](https://www.udacity.com/course/designing-restful-apis--ud388)), when we weren't going to use them until the neighborhood map project in part 4?
- We also have more API lessons in part 4. The lessons could be consolidated.

#### Part 4

- Why is part 4 called "The Frontend" when we have already been working on front-end (HTML, CSS, portfolio website)? It should be called "Web applications."
- Part 4 should include the [ES6 - JavaScript Improved course](https://www.udacity.com/course/es6-javascript-improved--ud356) and the [Asynchronous JavaScript Requests course](https://www.udacity.com/course/es6-javascript-improved--ud356).

#### Part 5

- Part 5 should provide more assistance for setting up a server in the cloud, not just in a Vagrant virtual machine.
- Container technologies should be presented as an alternative method.

#### Incorporating free courses into the Nanodegree program

There are sometimes differences in the organization between the free and Nanodegree program-bundled versions of the courses that can be confusing.

- For example, in the Python programming foundations work, the instructor Kunal says there are four lessons, but his "lesson 1" material starts on lesson 5 based on the Full Stack Web Developer Nanodegree program course navigation.
- As another example, in part 3 on databases, the four part course by Lorenzo is actually lessons 6-9.
- Having subdirectories within each program part would help with this. For example:
  - Part 1, programming foundations
    - Programming foundations with Python
      - Lesson 1
      - Lesson 2
      - Lesson 3
      - Lesson 4
- In this way, you could keep the course numbering and organization the same for the free courses and the courses within the Nanodegree program.

#### Current FSND program organization

Here is the program organization from when I entered the program in August 2017:

1. **Programming foundations**
    - [Programming Foundations with Python](https://www.udacity.com/course/programming-foundations-with-python--ud036)
    - Project 1: Python web server (movie trailer site)
    - [Intro to HTML and CSS](https://www.udacity.com/course/intro-to-html-and-css--ud001)
    - [Responsive Web Design Fundamentals by Google](https://www.udacity.com/course/responsive-web-design-fundamentals--ud893)
    - Project 2: Portfolio website
2. **Developer tools**
    - [Shell Workshop](https://www.udacity.com/course/shell-workshop--ud206)
    - [Version Control with Git](https://www.udacity.com/course/version-control-with-git--ud123)
    - [GitHub & Collaboration](https://www.udacity.com/course/github-collaboration--ud456)
    - [HTTP & Web Servers](https://www.udacity.com/course/http-web-servers--ud303): Python web servers
3. **The back-end**
    - [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)
    - Project 3: SQL database logs analysis
    - [Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088): CRUD, web servers, Flask, agile
    - [Authentication & Authorization: OAuth](https://www.udacity.com/course/authentication-authorization-oauth--ud330)
    - [Designing RESTful APIs](https://www.udacity.com/course/designing-restful-apis--ud388)
    - Project 04: Flask item catalog app
4. **The front-end**
    - JavaScript
    - jQuery
    - [Intro to AJAX](https://www.udacity.com/course/intro-to-ajax--ud110)
    - APIs
    - Project 05: Neighborhood map
5. **Servers**
    - Linux server deployment
    - Project 06: Linux server

#### Suggested FSND program organization

Here is how I would suggest progressing through the program:

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
    - [Designing RESTful APIs](https://www.udacity.com/course/designing-restful-apis--ud388)
    - Project 4: Flask item catalog app
    - [Intro to AJAX](https://www.udacity.com/course/intro-to-ajax--ud110)
    - [Google Maps APIs](https://www.udacity.com/course/google-maps-apis--ud864)
    - [JavaScript Design Patterns](https://www.udacity.com/course/javascript-design-patterns--ud989)
    - **I highly recommend additional introductory JavaScript coursework.**
      - [cs50](https://cs50.harvard.edu/) JavaScript lecture
      - [cs50 CSCI E-33a](https://cs50.github.io/web/lectures) JavaScript lecture
      - [Wes Bos JavaScript30](https://javascript30.com/)
      - [Syntax podcast](https://syntax.fm)
      - [Udacity ES6 - JavaScript Improved course](https://www.udacity.com/course/es6-javascript-improved--ud356)
      - [Udacity Asynchronous JavaScript Requests course](https://www.udacity.com/course/asynchronous-javascript-requests--ud109)
      - Mozilla Developer Network ([MDN](https://developer.mozilla.org))
        - [MDN JavaScript learning pathway](https://developer.mozilla.org/en-US/docs/Learn/JavaScript)
        - [Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
          - [Variable scope](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Variable_scope)
          - [Prototypal inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
    - Project 5: JavaScript neighborhood map
5. **Servers**
    - [Configuring Linux Web Servers](https://classroom.udacity.com/courses/ud299)
    - Project 6: Linux server configuration and app deployment

[(Back to top)](#top)

### Time

- The lessons took much longer than the time estimations show. For the first two parts, each lesson took me 6-12 hours over 1-2 days. I'm not sure if the number of hours is a useful metric. Maybe showing the number of lesson parts would be more useful.
- I took careful notes to effectively retain the material, which takes some extra time.
- I realized the **quizzes were frequently sticking points for me**, especially in Karl's lessons on Python HTTP and SQL. I pushed myself to get the quizzes correct without checking the solutions, because I wanted to make sure I was learning and thinking correctly. During the quizzes, I often felt like I wasn't getting it, or didn't have the information I needed to answer the questions. These sticking points sometimes took me a day or more to break through, and reduced my energy and motivation. With help from my mentor, I decided to speed up the lessons by limiting my quiz answer attempts, and pushing myself to complete the lessons in the time suggested by Udacity.

[(Back to top)](#top)

## Mentor

- My mentors were generally supportive and encouraging.
- I think the feedback could be more substantive and specific. I didn't find mentors helpful for specific coding challenges. The response wasn't fast enough, and the mentor usually didn't provide specific assistance with code.
- It would also help if the mentor relationship was more clearly defined. What are the boundaries? What can and can't they do for us?
- **Independence is important for success in this program.** The mentors are not involved enough to provide formative guidance, and the lesson materials don't provide enough instruction. Students that are less motivated or independent could benefit from an in-person code school instead.

[(Back to top)](#top)

## Networking

### Forums

- Forums are a helpful way to troubleshoot code, because they are organized and searchable like Stack Overflow.
- However, the responses will be slower, which is why chat is helpful.

### Slack

- When I started, the Slack workspace was just a jumble of information from people at all stages of the program. Slack was reorganized by @alex-udacity in October 2017 to have more channels, which was helpful.
- It's unclear how the changes to the forums and new in-classroom chat affect Slack.
- Someone from the forums also started up the [Udaciouspeople Slack workspace](https://discussions.udacity.com/t/udaciouspeople-ultimate-slack-for-all-with-auto-invites/38103) for students from all Nanodegree programs. Why do we need this when the FSND already has a channel?

### In-classroom chat

- It appears that Udacity expanded the previous mentor chat feature. In general, I liked this feature for communicating with my mentor. It was strange that Markdown entered in the web app showed up as plain text in the Android app.
- It's a little easier to connect with classmates, because the chat is right there, instead of in a separate tab or app.
- Markdown formatting is nice, but should be noted like it is on GitHub (Underneath the comments box, it reads "[Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/)").
- It needs to be more organized (@mentions, threads, notifications, and more clear date stamping in addition to time), and needs search, so that students can find previous answers like they can in the forums.
- There is also only a small field of view, so it's really difficult to read more than a few messages.
- Basically, I'm not sure what this adds beyond Slack.

### Knowledge

- There is a new Stack Overflow-like [knowledge base](https://knowledge.udacity.com) feature, as of 20180526. I posted an [answer](https://knowledge.udacity.com/questions/507). This may be a new version of the discussion forum.
- This should be useful in the future, because knowledge is retained, and useful answers will rise to the top.
- Frustratingly, the knowledge forum doesn't use Markdown. I have to re-format everything in HTML rich text.
- Can't sort by votes.

## Exit survey

> Which parts of the Nanodegree program, if any, were most valuable in helping you feel prepared to begin a job search or seek a promotion in this field?

Code review and resume review.

> What, if anything, would help you feel more prepared to begin a job search or seek a promotion in this field?

The code needs to be updated for Python 3, JavaScript ES6, React, Docker, and other current technologies.

> Do you believe that the Nanodegree program was worth your time?

4/5

> How likely is it that you would recommend a Udacity Nanodegree program to a friend or colleague?

6/10

> Why would you recommend or not recommend this program?

- Code and lessons
  - It was good that we used Python instead of Ruby. Python is more broadly useful.
  - Some frameworks, like Flask, were current, others, like Knockout, were outdated.
  - **The code in the lessons is of inconsistent quality. We are learning, and we need to see well-structured, consistent, and current code.**
  - **Udacity's GitHub repos are not maintained. Pull requests are ignored or not merged.**
  - The lesson content could be more thorough and informative. Videos could be longer and could go more in-depth into the content.
  - The lessons are poorly organized.
- Mentors
  - **Independence is important for success in this program.** The mentors are not involved enough to provide formative guidance, and the lesson materials don't provide enough instruction. Students that are less motivated or independent could benefit from an in-person code school instead.
- Networking
  - New Knowledge feature is useful.
  - In-classroom chat is not useful.
  - Slack is too cluttered.

## Program developments

- They frequently change the Nanodegree programs and platform, but don't have a clear changelog.
- Around June 2018, Udacity abbreviated the FSND. There are now three projects,  it costs $999, and you only have four months. They probably though there was too much overlap with the Front-End Nanodegree program (FEND). The FSND basically had most of the FEND. It was also a long program, so they probably wanted to shorten it to increase completion rates.
- They are also trying to maintain separation between FEND and the React Nanodegree program.
- They moved the career platform outside the Nanodegrees.

[(Back to top)](#top)