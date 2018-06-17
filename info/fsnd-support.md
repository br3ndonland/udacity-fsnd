# Udacity support

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Description](#description)
- [2018](#2018)
  - [201806](#201806)
  - [201805](#201805)
  - [201804](#201804)
  - [201803](#201803)
  - [201802](#201802)
  - [201801](#201801)
- [2017](#2017)
  - [201712](#201712)
  - [201711](#201711)
  - [201710](#201710)
  - [201709](#201709)
  - [201708](#201708)

## Description

This file contains correspondence from my Udacity mentors, in reverse chronological order. We messaged through the Udacity in-classroom chat app. There are also a few emails from Udacity support.

## 2018

### 201806

#### 20180616 Linux server config

June 13, 2018

I'm stuck on the Linux server configuration and need help

I got everything done, except I can't get Apache to serve the app

My repo is here https://github.com/br3ndonland/udacity-fsnd-p6-server

How can I get more help with the server configuration?
4:50 pm
June 14, 2018

> Hey, Brendon!
>
> Hold on, let me see your repo
>
> Geez, what a weird error
>
> Have u trying checking the logs?
>
> Try:
>
> `ls /var/log/apache2`
>
> and see if there's an error.log file
>
> If so, open it with nano like nano /var/log/apache2/error.log and u may find more informations
>
> And paste it here so I can see ass well 😁
5:20 am

Yep, I've been checking the error logs

That's good advice

So far, it looks like a problem with the WSGI file catalog.wsgi, or the Apache configuration file catalog.conf

Here's the error log. I also like to view it with `tail`.

```shell
grader@udacity6:~$ sudo tail /var/log/apache2/error.log
[Thu Jun 14 23:02:41.631345 2018] [wsgi:warn] [pid 8194:tid 139834844821376] mod_wsgi: Compiled for Python/3.5.1+.
[Thu Jun 14 23:02:41.631401 2018] [wsgi:warn] [pid 8194:tid 139834844821376] mod_wsgi: Runtime using Python/3.5.2.
[Thu Jun 14 23:02:41.632303 2018] [mpm_event:notice] [pid 8194:tid 139834844821376] AH00489: Apache/2.4.18 (Ubuntu) mod_wsgi/4.3.0 Python/3.5.2 configured -- resuming normal operations
[Thu Jun 14 23:02:41.632335 2018] [core:notice] [pid 8194:tid 139834844821376] AH00094: Command line: '/usr/sbin/apache2'
[Thu Jun 14 23:03:11.876286 2018] [wsgi:error] [pid 8197:tid 139834738947840] [remote 24.13.227.94:8662] mod_wsgi (pid=8197): Target WSGI script '/var/www/catalog/catalog.wsgi' cannot be loaded as Python module.
[Thu Jun 14 23:03:11.876397 2018] [wsgi:error] [pid 8197:tid 139834738947840] [remote 24.13.227.94:8662] mod_wsgi (pid=8197): Exception occurred processing WSGI script '/var/www/catalog/catalog.wsgi'.
[Thu Jun 14 23:03:11.883608 2018] [wsgi:error] [pid 8197:tid 139834738947840] [remote 24.13.227.94:8662] Traceback (most recent call last):
[Thu Jun 14 23:03:11.883666 2018] [wsgi:error] [pid 8197:tid 139834738947840] [remote 24.13.227.94:8662]   File "/var/www/catalog/catalog.wsgi", line 10, in <module>
[Thu Jun 14 23:03:11.883674 2018] [wsgi:error] [pid 8197:tid 139834738947840] [remote 24.13.227.94:8662]     from application import app as application
[Thu Jun 14 23:03:11.883696 2018] [wsgi:error] [pid 8197:tid 139834738947840] [remote 24.13.227.94:8662] ImportError: No module named 'application'
```

6:05 pm
June 15, 2018

> That's awesome!
>
> Now looks like it can't find the application module...
>
> Do u have an application.py file in the same directory?
5:54 am

Yep, application.py is the main app file. That's what I'm confused about.

I'll keep trying!
12:19 pm
June 16, 2018

> That's weird!
>
> If u feel comfortable with that, I can try to access it via SSH and check if I can find the problemm
>
> but for that, I would need your key file :/
6:28 pm

I got it working today! I did some work on the WSGI file, but I realized that WSGI wasn't serving up the app from my virtual environment. I just installed the Python modules outside of the virtual environment, and it worked!

[http://catalog.br3ndonland.com/](http://catalog.br3ndonland.com/)
10:48 pm

#### 20180608

June 06, 2018

> Hey, Brendon! I've been a bit away in the past days (I'm so soorrrryyy! Had some health problems...), but here i am again! :) How about a check-in? Can u tell me what u've done in the last days? Did u accomplish anything? Did u have any problems?
5:10 pm

June 08, 2018

Nice to hear from you Luiz. I hope you're feeling better.

I just completed and submitted the neighborhood map project! Almost done with the program!
10:00 pm

June 09, 2018

> Awesooooome! Glad to hear you're almost there! :D
>
> Keep up with the hardwork!
10:39 am

### 201805

#### 20180506

May 05, 2018

Hey, Brendon! How is the nanodegree going? :) Did you accomplish anything in the last days? Did u get stuck on anything? Remember to tell me if you need some help so I can try to help yooou! :D
3:22 pm

Hey Luiz. Things are going well. I'm learning JavaScript and the Google Maps API.
6:40 pm
May 06, 2018

Awesome :)

Lemme know if u get stuck on anything

### 201804

#### 20180427-29

April 28, 2018

Finally got my Flask catalog project submitted! Time to move on to lots of JavaScript!
1:31 am

Awesooome, Brendooon! :D Congratz!

I hope u enjoy JS :)

I got the Udacity reviews back already on my Flask app. I passed with no corrections needed! The reviewer said, "I really commend you for this project."

YES!

9:27 pm
April 29, 2018

Awesoooome! Congraaaatz, Brendon! :D

Noooooow.. frontend, right? :D

#### 20180407

Hey Luiz. I got the pages and JSON of the Flask item catalog app debugged, but I'm still struggling to implement authentication.

The code we used in the OAuth lessons was outdated and poorly formatted (as you saw from all the open pull requests). The `oauth2client` library used in the lessons [has been deprecated](https://google-auth.readthedocs.io/en/latest/oauth2client-deprecation.html), so even if it runs in the virtual machine, I would like to use something better. Google has created [google-auth](https://google-auth.readthedocs.io/en/latest/index.html#) as a replacement. I'm working on implementing google-auth, it's just taking some time.

Do you have any other suggestions?

2:42 am

>Geez, those deprecated features are a pain :(
>
>I'd suggest you google-auth or oauthlib
>
>But I THINK google-auth would be easier to manage

11:48 am

I agree. I'll keep working on it!

#### 20180401

April 01, 2018

CHECKIN TIME! :D Hey hey hey, Brendon! I hope you had a good weekend! Can you tell me how was the week? Did you accomplish anything? Did you have any problems in the nanodegree?

7:07 pm

Hey Luiz. Things went pretty well this week. I have the item catalog app built now. I need to debug it, and I'm hoping to submit the project in the next few days.

7:31 pm
April 02, 2018

That's awesooome, Brendon! :) Let me know if you have any problems, ok?

[(Back to TOC)](#table-of-contents)

### 201803

#### 20180321-23

> Hey theeere. I wasn't able to checkin with u this Sunday as I wanted, so would you mind to do it now? It won't take much time, I promiseeeeee!!! I do this so I can try to help you through the lessons :) I just wanted to know what you accomplished this week and if you had problems with anything...

Hey Luiz

I finished the Part 3 lessons, and I'm working on the item catalog project now.

I have set up the database and item catalog. I'm now coding the app routes in the main application.

10:03 am

> Aweeesome, Brendon! Are you stuck on something?
>
> Count with me if you need some help, ok?
>
> 11:55 pm

March 23, 2018

I'm working on adding OAuth right now

Not stuck yet, but I'll let you know if I need help

2:39 pm

> AWESOME! Good luck with the lesson :)
> 4:22 pm

#### 20180311-12

> Hey, Brendon! I hope everything is fine! :) So, since Udacity stopped with the weekly checkins, I'd like to do it myself so I can keep track of your progress and know exactly how I can help you... How was this week? What did you accomplish? Did you have any problem with any lesson?
>
> Have a nice week! :D

Hi Luiz, thanks for checking in. I worked through the first two lessons on APIs in part 3 (lessons 14-15). The [Udacity code](https://github.com/udacity/APIs) has a lot of issues. I'm thinking about submitting a pull request to fix the repo.

> :( The repo has a lot of open pull requests, so yeah, it has some problems hahah I think it's a great idea opening a pull request if you've found any problems! It's a great way to practice reading code made by other programmers
>
> About the lessons: let me know if you have any problem, ok? Don't hesitate to send me a message! :D

#### 20180309 mentor chat intro

> Hi, welcome to Udacity's Classroom Mentorship Program! I will be your mentor throughout the course and I'm looking forward to working with you! Why did you choose to enroll in this Nanodegree?

&iexcl;Hola Luiz! I'm Brendon. I'm a nutrition scientist learning web development to build technology tools for science.

I have been working through the Full Stack Web Developer Nanodegree program for a few months now. I am in part 3, about to start the item catalog app project.

I also won a [Udacity Grow with Google](https://www.udacity.com/grow-with-google) Scholarship, and just finished the materials in the challenge course.

I'm looking forward to finishing the rest of the program with your help!

> HAHAHAHAH Don't worry about Luis-Luiz.. They do it everytime so I'm used to it
>
> And nice to meet you, Brendon! :D i hope u're enjoying the nanodegree and I hope I can help you through the lessons :D
>
> Let me know if you get stuck on something or if you have any doubt, ok?

9:38 am

That sounds great. Thank you, Luiz!

9:42 am

> Np!

#### Mentor change email

New mentor, Luiz Felipe F.

date: Thu, Mar 8, 2018 at 12:46 PM

subject: Hi Brendon, meet your mentor!

Full Stack Web Developer Nanodegree Program

Ready to meet your new mentor?

Hi Brendon,

A great mentor can be the difference between struggle and success, and that’s why we provide dedicated mentors for our students. Our mentors are experienced Udacity alumni who are trained to help you succeed and make the most of your experience.

Your mentor, Luiz, will be your guide through the Full Stack Web Developer Nanodegree. Luiz will:

- Check in with you weekly to make sure that you are on track
- Help you to set learning goals
- Guide you to supplementary resources when you get stuck
- Respond to any questions you have about the program

So what are you waiting for? Luiz is waiting in the classroom!

Best,
The Mentorship Team

#### FSND changes

##### Email

date: Fri, Feb 23, 2018 at 7:11 PM

subject: Changes to your Full Stack Web Developer Nanodegree Program

Full Stack Web Developer Nanodegree Program

Hi Brendon,

We have some exciting news about the Full Stack Web Developer Nanodegree Program to share with you: starting on March 7, 2018, Full Stack students will have access to Classroom Mentorship and our newly launched Chat feature for the entirety of their program.

Here's what you can expect:
You will be able to benefit from the familiarity, experience and knowledge enabled by being matched with a single classroom mentor throughout the duration of your program. In addition to answering questions about content and projects, these classroom mentors will also be available to help keep you motivated and engaged in the curriculum.

You can also reach out to your student community through our new chat feature. Without ever leaving the Udacity classroom, you now can: get to know your fellow students, discuss tough concepts, and share your ideas about projects.

What does this mean for you?
In order to provide this improved experience, the FSND Discussion forums will no longer be moderated by forum mentors after March 7, 2018. Similar to the forums, you will be able to chat with your in-classroom mentor and ask them any questions you have about the course or your project and expect a response time within 24 hours or less.

Here's how to get started with Chat:
Once you log in, click the Chat icon at the bottom left of the classroom. You'll be asked to share a few details about yourself to help your student peers get to know you!

Then, in the "My Classmates" group, you can talk with every student enrolled in your program. We also have special study groups where you can find other students at the same stage of learning. This feature is designed for you. The more you participate, the better it will be!

In the spirit of lifelong learning, help us by sharing your experience about the new Chat feature. If you have any feedback or requests, please reach out through [this form](https://docs.google.com/forms/d/e/1FAIpQLSc2E1ayFIkOMQAm0NrZoX_77Yqaf579tLL8rlptLbt2Gasx3A/viewform).

Happy learning,

The Full Stack Web Developer Team

##### Forum

See [forum post](https://discussions.udacity.com/t/changes-to-services-offerings/625299)

david.harris

Hello everyone!

You should have received an email regarding this, but I wanted to take a moment here to highlight some changes to the program that are effective as of yesterday: **March 7th, 2018**.

Expansion to Classroom Mentorship

Beginning today, your classroom mentor will be with you through the entire program! Previously mentors were assigned until you successfully passed any two projects in the Full Stack program. In response to student feedback about some of the specific challenges of the later projects, we are expanding mentorship to allow you personal access to your mentor until you graduate!

New In-Classroom Chat feature

Udacity’s research has shown that students who learn from and share knowledge with others are more likely to complete the Nanodegree program. With that in mind, we are rolling out a new in-classroom chat feature.

You can find the chat feature by clicking the blue button in the lower left corner of the screen when you are logged into your Full Stack Nanodegree curriculum.

[(Back to TOC)](#table-of-contents)

### 201802

None

### 201801

Logs database analysis correspondence: 20180129 Monday - 20180203 Saturday

Just letting you know my progress today: I am almost done with the logs analysis project.

I'm stuck at the end of the third SQL query

You can see exactly where I'm at in my methods log [here](https://github.com/br3ndonland/udacity-fsnd03-p01-logs/blob/master/logs-methods.md#display-the-error-percentage).

> hey Brendon, good to see you progressing with the project
>
> Could you tell me where exactly are you facing the problem with the query?

Yes, as I show in my [methods log](https://github.com/br3ndonland/udacity-fsnd03-p01-logs/blob/master/logs-methods.md#display-the-error-percentage), I was working on the third query, identifying days on which >1% of requests were errors. I have columns in the table for total requests and error requests, but I couldn't create another column in the output to calculate the percentage of errors. I just got around it by formatting the output with Python code.

I got the project submitted.

I also found it strange that `psycopg2` doesn't format the Python output like the plain-text tables from PostgreSQL. The whole point of `psycopg2` is to work with `psql`, so why doesn't it return the same output?

February 01, 2018

> Hi Brendon
>
> Good Luck with the submission and do let me know how does it go for you

February 02, 2018

Thanks

I completed the project! I passed code review and implemented the reviewer's suggestions.

I'm now working through the rest of the lessons in part 3.

February 03, 2018

> Whoa
>
> Bang on
>
> Keep it up mate

20180126 Friday-20180128 Sunday planning FSND+GWG

Got this message:

> Automated check-ins have been upgraded to personalized ones. Update your mentor on your progress at any time!

Definitely a good idea. The check-in emails and reminders were a little annoying.

Hey Shivang! Hope you're doing well.

I won the Udacity Grow With Google scholarship! I was accepted to the intermediate web developer track. There is a three month challenge round. If I do well, I can win another scholarship to a more advanced Mobile Web Specialist program.

I would like some help in planning out my schedule for the FSND and the Grow With Google (GWG) program.

For the FSND, I'm in part 3 (databases), on the first SQL project, the logs analysis. I was thinking I should spend the next month getting to the end of the lessons in part 3, and at least get started on the next project, the neighborhood map.

I can then do the GWG program. GWG has ten lessons. I don't know much JavaScript yet, but I think I can get it done in 1-2 months.

That will set me up nicely to do the JavaScript in Part 4 of the FSND.

What do you think?

> HI Brendon
>
> 1 month seems too much just for part 3
>
> Let's try 3 weeks?
>
> 1 week : logs analysis
>
> 2 weeks : Item Catalog
>
> It'll be a bit challenging but I think it's worth a try
>
> And again we can reduce the 1 month for 10 lessons by about 1.5 weeks
>
> How many hours do you plan to put in?
>
> We can discuss and work on a detailed schedule accordingly

Thank you very much for your input, Shivang.

I think I can get the logs analysis project done, and reviewed, by the end of this week (Friday, February 2). Let's make that a goal.

I can also plan to do the item catalog in two weeks also.

I might need an extra week for the remaining lessons 6-18 in part 3 before doing the item catalog project. It looks like a lot of information and I want to learn it well.

I might need to change my approach to the lessons also. The lessons are important, but each lesson can take me 5-10 hours to complete. For example, the first four lessons in part 3 (the introduction to SQL) took me about 20 hours over several days. I push myself to get the answers to the quizzes on my own. Maybe I should set a time limit on the lessons, and just move on from each quiz if I don't get the answer in a few tries.

I can put in about 30 hours per week until I complete the Nanodegree program. I have a vacation coming up in a few weeks, but I will still put in some hours watching lessons during the vacation.

> Hey Brendon
>
> I must say, it's really great to have a mentee who is so committed to the ND
>
> I really appreciate it
>
> :)
>
> Sounds good, let's try to get it done
>
> And it's okay to spend time on lessons
>
> The more you push yourself, the more you learn
>
> I would suggest you set a time limit on the quizzes, or even a maximum number of tries
>
> And after you finish a particular lesson, you can come back and try out its quizzes again
>
> It would be sort of a revision, as well as solving quizzes
>
> I hope this helps :)
>
> 30 hours a week is really great
>
> I say, lets complete log analysis and item catalog in 2 weeks, and then see how the rest pans out
>
> we can flex your schedule a bit according to your speed
>
> let me know if that works for you
>
> :)

Thank you, Shivang! I appreciate your support.

The Nanodegree program has been amazing so far. I have really grown as a developer.

That sounds like a great strategy for the lessons.

I will plan to check in with you at least once a week, and maybe more if I get stuck on anything.

> that's great, Brendon
>
> I'm really glad you liked the idea
>
> feel free to reach out to me any and everytime you need help
>
> And hey, you can update me anytime
>
> Anytime you are working, just leave a little message to keep me updated :)

Awesome. I will. Thanks so much!

[(Back to TOC)](#table-of-contents)

## 2017

### 201712

December 17, 2017

Hi Shivang! I hope you're doing well.

This week I finished Part 2 of the Nanodegree program on Developer Tools! The early lessons on Bash and Git were easy for me, but the Python HTTP work was more challenging. Two parts down, three to go!

I will be celebrating the holidays for the next two weeks, so I will keep the computer work light, but I'm excited to dive into SQL for Part 3 of the Nanodegree program.

*Are you currently stuck on anything? If so, what are you facing?*

No, I'm progressing well.

Feedback to Udacity
four stars
improve: personalized support
notes: Shivang has been very supportive. In general, the Udacity mentor relationship could be strengthened to be more directly involved in the learning process.

Hey Brendon

Great worrk

Try giving [this](https://developer.mozilla.org/en-US/docs/Web/HTTP) a read as well if you're interested in diving in a bti deep

*bit

Happy Holidays

:D
2:30 pm

December 03, 2017

Hey Shivang! Things are well here.

Past week

I'm moving on to part 2 of the Nanodegree program, and flying through the lessons because I am already familiar with bash and git.

I also applied to the [Udacity Grow with Google scholarship](https://www.udacity.com/grow-with-google) this week. I hope I get it!

Upcoming weeks

I will get started on Part 3 (Backend).

> Are you currently stuck on anything? If so, what are you facing?

No, I'm progressing well.

2:08 pm

December 04, 2017

> Hey brendon
>
> Awesome work
>
> checkout pluralsight as well for a scholarship
>
> It will also benifit you
>
> Keep up the good work
>
> Happy to see you progressing so well
>
> :)

12:08 pm

[(Back to TOC)](#table-of-contents)

### 201711

NOVEMBER 12, 2017 2:08 pm

> Hey Brendon
> How are things on your end?

NOVEMBER 21, 2017 1:39 pm
Hi Shivang
Good to hear from you
Things are well with me. I just finished the portfolio website project.
I used the webpage design to create a full website with Jekyll, and hosted the site with GitHub Pages. The website includes a homepage, an "About" page where I introduce myself and my Udacity work, a "Methods" page explaining how I built the site in detail, a "Rubric" page providing the Udacity project documentation, and a "Review" page documenting the Udacity code review.
It was good to learn the Bootstrap framework, but Bootstrap is complicated, so it took a long time.
You can see the website [here](https://br3ndonland.github.io/udacity/).

[(Back to TOC)](#table-of-contents)

### 201710

21 Saturday: Udacity mentor check-in with Shivang Bhandari

> > What did you accomplish in the past week?
>
> I have now completed 100% of the lessons in Part One of the nanodegree! I'm working on my portfolio site. I'm using Bootstrap 4 as a base template and learning to integrate Bootstrap into my HTML and CSS.
>
> > What are your goals for the coming week?
>
> This week, I would like to complete my portfolio site.
>
> > Are you currently stuck on anything? If so, what are you facing?
>
> No, I'm progressing well.

Messaging:

> Awesome
> Keep up the good work mate
> :)

08 Sunday: Udacity mentor check-in with Shivang Bhandari

> > What did you accomplish in the past week?
>
> I completed lesson 12 HTML, lesson 13 CSS, and started working more with Chrome Developer Tools. I also resubmitted my resume and received a very helpful review. The resume looks good now, and I need to focus on building a portfolio of projects.
>
> > What are your goals for the coming week?
>
> This week, I would like to complete all the front-end lessons, and start working on my portfolio site.
>
> > Are you currently stuck on anything? If so, what are you facing?
>
> No, I'm progressing well.

Messaging:

> Hey
Congratulations on the resume project and do share a link with me if you have it hosted somewhere
I would like to give it a look
And best of luck for your goals for the coming week
:)
7:36 am
Thanks! I would be happy to share the resume with you.

11:59 am
OCTOBER 10, 2017
> Awesome
> Quite an impressive Resume
> :)

[(Back to TOC)](#table-of-contents)

### 201709

30 Saturday: Udacity mentor check-in with Shivang Bhandari

> > What did you accomplish in the past week?
>
> I'm pleased to report that I completed my first project, the movie trailer website. Only had a few minor corrections after initial submission. I also started working on front-end stuff like HTML, CSS, and JavaScript, and built a few simple websites.
>
> > What are your goals for the coming week?
>
> This week, I would like to complete all the front-end lessons, and start working on my portfolio site.
>
> > Are you currently stuck on anything? If so, what are you facing?
>
> No, I'm progressing well.

Messaging:

> Hey
> Congratulations on the First Project
> Good Luck for the Front-End Portion this week
> Let me know if you need some help from my end

22 Friday: Udacity mentor check-in with Shivang Bhandari

> > What are your goals for the upcoming week?
>
> Progress
>
> fsnd
>
> - Completed movie website mini-project
>
> jobs
>
> - Submitted resume and cover letter for Udacity review. The reviews were very helpful.
> - Put together job application materials: updated my LinkedIn, Glassdoor, Indeed, Angellist; put together resume and cover letters
> - Attended several events about startups and tech jobs, and met a number of interesting and helpful people
> - Applied for my first job
>
> Goals
>
> fsnd
>
> - Complete Lesson 10: Make Classes: advanced topics, including final project
> - Complete 50% of Movie Trailer Website project
>
> jobs
>
> - Revise resume and cover letter based on Udacity suggestions
> - Apply for my second job
>
> *Are you currently stuck on anything?- Nope, progressing well and loving it!

Messaging:

> Hi Brendon
> Thank you so much for such a detailed update on what you are doing
> I'm happy to see you do the career portion of the course along with the core curriculum
> Good luck with your project
> :)

04 Monday (Labor Day): Udacity mentor check-in with Shivang Bhandari

> > What are your goals for the coming week?
>
> Things went well last week. I'm just finishing up lesson 8 (use classes: profanity editor), which was the goal I set last week.
>
> This week, I'm hoping to complete 50% of the "Make classes: Movie Website" section.
>
> > Let us know how helpful your Mentor has been, so we can continue to improve your learning experience. This information will not be shared with your Mentor.
>
> Responsive and supportive.

Messaging:

> hey
> Good to see you are making such awesome progress
> Keep it up
> :)

[(Back to TOC)](#table-of-contents)

### 201708

25 Friday: Udacity mentor check-in with Shivang Bhandari

> > What are your goals for the coming week?
>
> Based on my progress so far, in the next week, I would like to complete lesson 7 (use classes: send text) and lesson 8 (use classes: profanity editor) in the programming fundamentals section of the course.
>
> I was checking out the course materials to plan out my timeline. It looks like the movie trailer project is overdue already, but I think it's because I signed up during discovery week, and then paused the degree for a while. It might be counting from when I signed up. I started the degree about three weeks after I signed up.
>
> It will probably take me another week or two to complete the movie trailer project.
>
> > Are you currently stuck on anything?
> No, I'm progressing well.

Messaging:

> Hey
>
> Thanks for checking in
>
> Yes the deadlines mentioned are from the day you enroll in the course
>
> And these are soft deadlines so you don't need to worry about them
>
> :)

21 Monday: Udacity mentor check-in with Shivang Bhandari

> Hi Shivang, the course went well last week. I completed lesson 1 (using functions) and I am moving on to lesson 2 (classes).
>
> The Python syntax has been coming along. Monday of last week was the day when I first felt like I was thinking like a programmer.
>
> I got to the exercise where we had to create a timer to encourage taking breaks while working at the computer.
>
> When adding a loop to the break counter, I came up with a more efficient way to do it than the instructor's example. I used a for loop instead of a while loop, reducing the required amount of code from six lines to three (not counting the two lines required to load modules). This might seem like a trivial exercise, but I realized the significance of the thought process because I had taken time to learn about computing history. I thought about how Bill Gates and Paul Allen's major accomplishment while at Harvard was writing a BASIC interpreter for the Altair in 3.2 kilobytes of text, leaving memory free to write other programs and launching the personal computing software industry.
>
> My performance during this exercise demonstrated that I had moved beyond the rote completion of exercises to think independently in the most efficient and Pythonic way. I'm becoming a programmer!
>
> My goal this week is to complete the entire lesson 2.

Messaging:

> Hey
> Thank you so much for updating me
> It's good to see you are progressing in the course and are enjoying it
> Congratulations on getting through the quizes
> And yes I highly appreciate you taking a new way to do the problem in a more efficient manner
> Let's get the goal done by the end of next week
> Good Luck
> :)

12 Saturday: Udacity mentor check-in with Shivang Bhandari

> Hi Shivang! I’m Brendon Smith. I have a PhD in nutrition and have been a postdoc researcher and lab manager at Harvard for two years. I want to build new technology tools to make science more efficient and reproducible.
>
> I have experience with R, Python, Git, and front-end web development. Some of my friends at MIT told me about Udacity. I’m looking forward to learning here!

Messaging:

> Hey Brendon
> Great to E-Meet you
> Welcome to the Udacity Family.
> It is so great to see a person with so much experience in hand and still learning
> I hope you will enjoy this course and I'll be here incase you need any help.
> Feel free to reach out anytime

1:06 pm

> Thank you for your support, Shivang! Yes, I am always challenging myself and learning new things. I will check in with you regularly as I progress through the course.

1:12 pm

AUGUST 15, 2017

> Great
> Happy to connect
> And Just Let me know if you've come up with a schedule for this course
> If not, we can discuss and set up some deadlines to help you stay on track
> :)

**11 Friday:** Began Udacity Full Stack Web Developer nanodegree

**08 Tuesday:** I was considering the Intro to Programming nanodegree but decided to jump into the Full Stack Web Developer nanodegree. Got a credit applied to my account.

> Hey there Brendon,
>
> Thanks for reaching back out! It's great to hear you're moving forward with your Full Stack Web Developer Nanodegree program enrollment. While our Terms of Service prevent me from being able to refund you after your free trial has concluded for any program, I'm happy to add a credit of $99.50 to your account.
>
> It looks like you've already received some credit previously, so I'm happy to say you have a current credit balance of $240.42. This money will be prioritized in a withdrawal before your credit card on file. With this you should have enough credit for a full free month and a discounted second month for your Full Stack Web Developer Nanodegree program!
>
> I hope you enjoy your time in your new program.
>
> Happy learning,
>
> Ryan
>
>
> > Brendon W Smith
> > Aug 8, 9:52 AM PDT
> >
> > Hi,
> >
> > I communicated with Ryan Wright in Support about my goals and computing experience. Based on his input, I decided to jump into the Full Stack Web Developer Nanodegree.
> >
> > I was charged for the Intro to Programming Nanodegree, but didn't use it. Could I have a refund or a credit applied to my account?
> >
> > Thanks for your help.
> >
> > Brendon

**06 Sunday:** Contacted Udacity for assistance in curriculum planning:

> Hi! I would like some assistance selecting a nanodegree program. I have a PhD in Nutritional Sciences, and have been a postdoc and lab manager in a molecular biology lab at Harvard for two years. Some of my friends at MIT told me about Udacity.
>
> Programming background:
> After using SAS for statistical programming during graduate school, I continued by learning R using free online resources, and completed three online courses through DataCamp. I kept detailed notes and created a reference guide to statistical programming in R using Markdown and HTML syntax, and shared it freely online on [Rpubs](https://rpubs.com/br3ndonland/Rguide) and GitHub. I also wrote R code to analyze proteomics data during my postdoc. I expanded my skills by attending a week-long Intro to Python course during Harvard’s Computefest this year, as well as a workshop on Git and front-end coding at Harvard’s Innovation Labs.
>
> Plans:
> I would now like to pursue a career in computer programming, software engineering and lab automation. My overall goal is to develop new hardware and software solutions to make scientific research more efficient and reproducible. I'm in the process of leaving my job at Harvard, and will have a few months of pay while I gain computational skills and look for jobs. Chan/Zuckerberg Initiative would be an example of a company I would like to work for.
>
> I have no work commitments in August. Starting in September, I will be taking two courses through the Harvard Extension School for the fall semester, Intensive Introduction to Computer Science, and Introduction to Programming in C++.
>
> Udacity curriculum:
> I have now done the first three lessons in the Udacity Intro to Computer Science course (as recommended for the Full Stack Web Developer degree). It has been helpful, but it is time-consuming, and I don't think it's totally necessary for me at this stage. I also enrolled in the Intro to Programming Nanodegree, but again, I'm not sure if it's necessary for me.
>
> Considering my goals and time frame (leaving my job with a few months of pay), I'm wondering if it would be best for me to jump into the Full Stack Web Developer degree. I can concentrate on it during August, and then continue to work on it during the fall semester as I am able. How does that sound?
>
> Thanks for your help!

The response wasn't particularly helpful, but at least it was good for me to articulate where I'm at.

> Hi Brendon,
>
> Thanks for writing in! The Nanodegree program you choose will depend on your existing knowledge and skills, your interests, and your career goals. Our Nanodegree programs generally fall into the categories of Web Development, Software Engineering, App Development, Data Science and other predictive modeling, and Machine Learning.
>
> I encourage you to take a look through our Course Catalog, using the menu on the left to sort your searches. You can read through the overview pages of Nanodegree programs that look interesting, and check the Prerequisites section to make sure you have the knowledge required to be successful in the program.
>
> You can also use our Pathfinder tool to help you find the Nanodegree program that's right for you.
>
> Given your experience, however, it sounds to me like you would be best fit in an intermediate program above our Intro to Programming Nanodegree Program. That being said, our Pathfinder Tool truly is your best bet for diagnosing where you will fit best.
>
>
> Happy learning,
>
> Ryan

[(Back to TOC)](#table-of-contents)