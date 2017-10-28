readme
========================

<p align="left">
    <a href="https://www.udacity.com/">
        <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300">
    </a>
</p>

**Udacity Full Stack Web Developer Nanodegree program**

Brendon Smith | br3ndonland

---

## Description

I document everything obsessively, especially my computing activities. Step right up and learn about the cool things I'm doing with Udacity!


## Program

The [Full Stack Web Developer Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) was co-created by Udacity, Amazon, GitHub, AT&T, and Google. The program teaches skills including Python programming, HTML, CSS, JavaScript, and AJAX for front-end development, back-end databases, and Linux server deployment.

---

## Mentality and accomplishments

I am a molecular nutrition scientist building skills in web development to create a more efficient, reproducible, and sustainable research culture.

**My goal with Udacity is not to finish as quickly as possible, but to learn as much as possible, and to become the best programmer possible.** Throughout the Nanodegree program, I went beyond the requirements to strengthen my skills. Examples:

* **Part 1, Programming Fundamentals**
    - *fsnd01_05_functions:* 
        + **This was my first milestone as a computer programmer.** I began my transition into web development with background info about computing history, operating systems, and programming, mostly from [Harvard cs50](https://cs50.harvard.edu/), [Udacity cs101](https://www.udacity.com/course/intro-to-computer-science--cs101), and [David Evans cs4414](http://rust-class.org/index.html). When I began learning Python syntax, progress was slow, and I wasn't able to express myself. It felt very much like the mental exhaustion of learning a spoken language. For example, while I was in Spain, although I was already fluent in Spanish, it required more mental effort to do simple things like go to a store or order food at a restaurant. The Udacity introductory materials actually recommended that I start with a beginner Nanodegree program first, but I knew that with my motivation and education, I could fill in the gaps in my knowledge and competency. 
        + I launched into the Full Stack Web Developer Nanodegree program and kept at it. I got to an exercise where we had to create a break timer. The timer opens a YouTube video every two hours, to encourage people to take a break while working on the computer. I wrote the code independently, then checked the instructor's solution. **When adding a loop to the break counter, I came up with a more efficient way to program it** by using a `for` loop instead of a `while` loop, reducing the required amount of code from eight lines to five. **I realized the significance of the thought process because I had taken time to learn about computing history.** I thought about how Bill Gates and Paul Allen's major accomplishment while at Harvard was writing a BASIC interpreter for the Altair in 3.2 kilobytes of text, leaving memory free to write other programs and launching the personal computing software industry. Walter Isaacson wrote an article on this topic, "[Dawn of a revolution](http://news.harvard.edu/gazette/story/2013/09/dawn-of-a-revolution/)," *Harvard Gazette* 201309, and the corresponding book, *The Innovators*. **My performance during this exercise demonstrated that I had moved beyond the rote completion of exercises to think independently in the most efficient and Pythonic way.**
    - *fsnd01_06_classes_turtles:*
        + In the turtles mini-project, instead of just drawing a shape, I imported a gif for the background, and looped through a colorspace to create a psychedelic effect. 
    - *fsnd01_08_classes_checker:*
        + In the profanity checker mini-project, I adapted the code for Python 3.6.2 and made it as concise as possible. When I realized there was a more effective way to write the program with the `Requests` module, I learned about it and rewrote my code.
    - *[fsnd01-p01-movies](https://github.com/br3ndonland/udacity-fsnd01-p01-movies):*
        + For my first project, I created a movie trailer website. I personalized it with a film noir theme, and wrote a mini-review for each movie. I passed code review with only minor corrections.

---

## Code formatting

Python code is [PEP 8](https://www.python.org/dev/peps/pep-0008/) compliant.

For the foundational Python programming work (lessons 00-11), I took notes and ran my code in Jupyter notebook files. Jupyter notebook is a nice way to bundle Markdown-formatted notes with Python code, but it lacks the speed and autocompletion features of Sublime Text. As I continued into front-end web development, I started writing my code in Sublime Text, keeping separate files for code and Markdown notes.

Jupyter notebook setup: for more, see [br3ndonland_computing_setup.mdown](https://github.com/br3ndonland/general/blob/master/br3ndonland_computing_setup.mdown)

* [Anaconda](https://docs.anaconda.com/anaconda/install/)
    - jupyter notebook
        + [jupyter-themes](https://github.com/dunovank/jupyter-themes)
            * `pip install jupyterthemes`
            * mods: `jt -t chesterish -f ubuntu -fs 14 -altp -tfs 16 -nf sourcesans -nfs 16 -ofs 12 -cellw 88% -T`
            * shutdown jupyter notebook kernel, clear browser cache, restart browser, restart jupyter notebook
        + [jupyter version control with nbdime](http://nbdime.readthedocs.io/en/latest/)
            * terminal: `pip install nbdime` (may already be installed through anaconda. to check, enter `conda list` at the command line).
            * `nbdime config-git --enable --global` (can also enable for individual repositories)
            * Add [jupyter .gitignore](https://github.com/jupyter/notebook/blob/master/.gitignore) to directory (or to $HOME/.config/git/ignore for global configuration), to avoid recognizing notebook checkpoint files.
