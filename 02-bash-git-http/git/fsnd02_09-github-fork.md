# GitHub: Working on another developer's repository

**Udacity Full Stack Web Developer Nanodegree program**

Part 02. Developer Tools

Lesson 09. Working on another developer's repository (from [free Git course](https://www.udacity.com/course/version-control-with-git--ud123))

Brendon Smith

br3ndonland


## Notes

* We forked and cloned repos.
* We cloned the [Google Chrome lighthouse](https://github.com/GoogleChrome/lighthouse) project.
  - `$ git shortlog -s -n` can be used to display the commit authors.
  - `$ git log --author="Paul Lewis"` can be used to display commits by specific authors.
  - `$ git log --grep "css bug"` can be used to search for the commits that mention a css bug.


## What To Work On

Let's say you're using some third-party library to help you build a project. What happens if, while you're using this third-party library, you come across a bug or a misspelling? You have the skill to be able to fix it, but you don't have direct access to make modifications to the original library. Well that's not a problem because you know that forking another developer's repository copies it to your account and gives you full access to git pull and git push to it!

But what are you supposed to do now that you've got full access to a duplicate of the other developer's project. We'll look at this in the next section but if you have forked a project and you have code in your fork that's not in the original project, you can get code into the original project by sending the original project's maintainer a request to include your code changes. This request is known as a "Pull Requests". Again, we'll look at sending and working with pull requests in the next lesson.

So you know it's possible to get your code in the original project and you know you want to help and fix this spelling/code mistake. So you got something to work on! But how do you go about actually contributing to the project in the way that the original project maintainer will be happy with and will end up actually incorporating your changes?

The first thing you should always look for in a project is a file with the name CONTRIBUTING.md.


### CONTRIBUTING.md File

The name of the `CONTRIBUTING.md file is typically written in all caps so that it's easily seen. As you could probably tell by its name, this file lists out the information you should follow to contribute to the project. You should look for this file before you start doing development work of any kind.

Let's look at the lighthouse project's contributing file:

You can see that the top line of the file says:

  > We'd love your help! This doc covers how to become a contributor and submit code to the project.

There are two main sections to this file:

* the "For Contributors" section
* the "For Maintainers" section

Each one of these sections has subsections of its own to instruct readers on how to contribute to and work with this project.

Let's take a look at the section on signing the contributors license. You can see that to be able to contribute to this project you need to sign Google's Contributor License Agreement.


### Topic Branches

The best way to organize the set of commits/changes you want to contribute back to the project is to put them all on a topic branch. Now what do I mean by a topic branch? Unlike the master branch which is the default branch that holds all of the commits for your entire project, a topic branch host commits for just a single concept or single area of change.

For example if there is a problem with the login form for logging into the website, then a branch name to address this specific issue could be called:

* login
* login-bug
* signup-bug
* login-form-bug

etc.

There are plenty of names that can be used for a topic branch's name. You just want to use a clear descriptive name for the branch so that if, for example, you list out all of the branches you can immediately see what changes are supposed to be in a branch just by its name.


## Best Practices

### Write Descriptive Commit Messages

While we're talking about naming branches clearly that describe what changes the branch contains, I need to throw in another reminder about how critical it is to write clear, descriptive, commit messages. The more descriptive your branch name and commit messages are the more likely it is that the project's maintainer will not have to ask you questions about the purpose of your code or have dig into the code themselves. The less work the maintainer has to do, the faster they'll include your changes into the project.


### Create Small, Focused Commits

This has been stressed numerous times before but make sure when you are committing changes to the project that you make smaller commits. Don't make massive commits that record 10+ file changes and changes to hundreds of lines of code. You want to make smaller, more frequent commits that record just a handful of file changes with a smaller number of line changes.

Think about it this way: if the developer does not like a portion of the changes you're adding to a massive commit, there's no way for them to say, "I like commit A, but just not the part where you change the sidebar's background color." A commit can't be broken down into smaller chunks, so make sure your commits are in small enough chunks and that each commit is focused on altering just one thing. This way the maintainer can say I like commits A, B, C, D, and F but not commit E.


### Update The README

And lastly if any of the code changes that you're adding drastically changes the project you should update the README file to instruct others about this change.


## Recap

Before you start doing any work, make sure to look for the project's CONTRIBUTING.md file.

Next, it's a good idea to look at the GitHub issues for the project

* look at the existing issues to see if one is similar to the change you want to contribute
* if necessary create a new issue
* communicate the changes you'd like to make to the project maintainer in the issue

When you start developing, commit all of your work on a topic branch:

* do not work on the master branch
* make sure to give the topic branch clear, descriptive name

As a general best practice for writing commits:

* make frequent, smaller commits
* use clear and descriptive commit messages
* update the README file, if necessary

