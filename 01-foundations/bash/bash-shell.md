# Shell workshop

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[Shell Workshop](https://www.udacity.com/course/shell-workshop--ud206)

## Lesson

- We used the Bash shell, the most popular UNIX-style shell.
- `$ echo $COLUMNS x $LINES` prints the terminal window size. 80x24 is common.
- `ls` commands
  - *All of these are correct!*
    - `$ ls Pictures` is the most direct way to do it.
    - `$ cd Pictures`; `ls` changes directory to the Pictures subdirectory, then runs ls in that directory.
    - `$ ls Pictures/../Pictures` is unnecessarily verbose, but it does work.
- `pwd` print working directory
  - `.` this directory
  - `..` parent directory
  - `~` tilde for home directory
  - *Why are shell commands so short?*
    - It makes for less typing. The Unix system was originally designed in an era when the connections between computers and terminals were very slow, so making commands really short made it much faster to use. This is true not only for the shell, but also for other parts of the Unix system, such as the C programming language.
- `ls -l` parameters and options
  - *If you wanted to list all the files whose names start with the word bear, how would you do it?*
    - The pattern `bear*` matches any file whose name starts with the word bear.
- `cd` and `mv` moving files
  - `mv` takes two arguments, separated by a space: origin destination
  - *I want to move the epub files back from Documents/Books to Documents. How can I do this? My current working directory is my home directory, and Documents is inside that directory.*
    - `$ mv 'Documents/Books'/- Documents`
    - `$ cd Documents; mv 'Books'/*.epub .`
    - `$ cd 'Documents/Books'; mv - ..`
  - By the way, when you quote something in the shell, you always use straight quotes. This is what you'll get if you type into a terminal window. However, if you copy and paste from a web page or document, you should be really careful to make sure that it hasn't accidentally been written with “curly quotes”. Curly quotes will not work in the shell. Single quotes and double quotes do slightly different things in the shell. If you're unsure which to use, go for single quotes.
- Downloading with `curl`
  - command (`curl`)
  - options, such as how to save the file. Use `-L` to follow redirects
  - object to operate on
  - *Enter a shell command to download [https://tinyurl.com/zeyq9vc](https://tinyurl.com/zeyq9vc) and save it as the file dictionary.txt. Remember to use the option to follow web redirects.*
    - `$ cd downloads`
    - `$ curl -o dictionary.txt -L 'https://tinyurl.com/zeyq9vc'`
  - By the way, a lot of URLs have special characters in them, such as the & sign, which have unusual meanings to the shell. That's why I'm always putting these URLs in quotes … even though these particular examples would work without them, it's a good practice to get into.
  - Also see cs50 Lecture 06 HTTP
- Removing files with `rm`
  - You have four files named Good File, Bad Name Good File, Bad File, Good Name Bad Face. You want to remove files 3 and 4, while leaving 1 and 2 intact. There are two commands below that will accomplish this goal. Choose them:
    - `$ rm 'Bad File' 'Good Name Bad Face'`
    - `$ rm *Bad F*`
- Searching and pipes with `grep` and `wc`
  - *How many words are there in dictionary.txt that match the pattern ibo?*
    - `$ grep ibo dictionary.txt | wc -l` runs the `grep` command, searches for the string `ibo` in dictionary.txt, and invokes the `wc` word count function to count the number of lines with the `-l` argument.
  - *What are grep patterns called?- Research question! You can use grep for more than just matching words. There's a specific term for the patterns that grep lets you use. Use your favorite search engine and do a little research to find out what those patterns are called.
    - *regular expressions*
    - Regular expressions are also known as regexps or regexes. There is actually a whole complex language of patterns that you can use with `grep` … which is entirely beyond the scope of this course. And regular expressions are used in lots of other programs too, including text editors … and this quiz. The regular expression used to match correct answers to this quiz is `^[Rr]eg.*[Ee]x.*` which means "any string that starts with `reg` and has `ex` in it, but upper- and lowercase R and E are both OK.
- Shell and environment variables
  - `echo $PWD` refers to an environment variable. The value of $PWD is the current working directory, same as what you'd see if you ran the pwd command. Every program you run on a Unix-like system has some working directory. It usually starts out as the directory you were in when you started that program. So the PWD variable is an environment variable. It's not just internal to the shell.
- Startup files
  - Usually located in */bin*, which stands for binary.
- Controlling the shell prompt ($PS1)
  - The instructor customized his shell prompt. I tried it out on [http://ezprompt.net/](http://ezprompt.net/), but didn't really find it necessary to change it. Changes are made to the .bash_profile.
- Aliases
  - You can set command aliases with the `alias` command.
- Shell resources
  - [The Bash Academy](http://www.bash.academy/)
  - [Bash Beginners Guide](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
  - [Bash Programming HOWTO](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)
  - [Regexr — Learn Regular Expressions](http://regexr.com/)
- Feedback from me
  - Quick, informative and fun. It's easy to ignore the command line, so I'm glad we spent some time strengthening our skills. Thanks!