# GitHub

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[GitHub & Collaboration](https://www.udacity.com/course/github-collaboration--ud456)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Lesson 1. Intro to GitHub Remotes](#lesson-1-intro-to-github-remotes)
- [Lesson 2. Forking](#lesson-2-forking)
  - [Summary](#summary)
  - [What To Work On](#what-to-work-on)
  - [CONTRIBUTING.md File](#contributingmd-file)
  - [Topic Branches](#topic-branches)
  - [Best Practices](#best-practices)
  - [Recap](#recap)
- [Lesson 3. Staying in sync with remote repositories by pulling and rebasing](#lesson-3-staying-in-sync-with-remote-repositories-by-pulling-and-rebasing)
  - [Intro](#intro)
  - [Staying in sync with the source project](#staying-in-sync-with-the-source-project)
  - [Manage an active PR](#manage-an-active-pr)
  - [Squash commits with rebase](#squash-commits-with-rebase)
  - [Course wrap-up](#course-wrap-up)

## Lesson 1. Intro to GitHub Remotes

- Made a test repo `github-sample-repo` and created the three intro files in one step with `$ touch README.md index.html app.css`.
- Configured repo to push with ssh: `$ git remote set-url origin git@github.com:br3ndonland/udacity-travel-plans.git`
- Pushed with `$ git push origin master`.
  > One very important thing to know is that this `origin/master` tracking branch is not a live representation of where the branch exists on the remote repository. If a change is made to the remote repository not by us but by someone else, the `origin/master` tracking branch in our local repository will not move. We have to tell it to go check for any updates and then it will move. We'll look at how to do this in the next section.
- Made changes on github, then brought the changes to the local repo with `$ git pull origin master`.
- `Pull` vs. `fetch`: `fetch` just retrieves remote changes, but does not directly merge. It's like half of `pull`. The other half of `pull` is a merge with the local repo.

---

## Lesson 2. Forking

### Summary

- We forked and cloned repos.
- We cloned the [Google Chrome lighthouse](https://github.com/GoogleChrome/lighthouse) project.
  - `$ git shortlog -s -n` can be used to display the commit authors.
  - `$ git log --author="Paul Lewis"` can be used to display commits by specific authors.
  - `$ git log --grep "css bug"` can be used to search for the commits that mention a css bug.

### What To Work On

> Let's say you're using some third-party library to help you build a project. What happens if, while you're using this third-party library, you come across a bug or a misspelling? You have the skill to be able to fix it, but you don't have direct access to make modifications to the original library. Well that's not a problem because you know that forking another developer's repository copies it to your account and gives you full access to git pull and git push to it!
>
> But what are you supposed to do now that you've got full access to a duplicate of the other developer's project. We'll look at this in the next section but if you have forked a project and you have code in your fork that's not in the original project, you can get code into the original project by sending the original project's maintainer a request to include your code changes. This request is known as a "Pull Requests". Again, we'll look at sending and working with pull requests in the next lesson.
>
> So you know it's possible to get your code in the original project and you know you want to help and fix this spelling/code mistake. So you got something to work on! But how do you go about actually contributing to the project in the way that the original project maintainer will be happy with and will end up actually incorporating your changes?
>
> The first thing you should always look for in a project is a file with the name CONTRIBUTING.md.

### CONTRIBUTING.md File

> The name of the `CONTRIBUTING.md file is typically written in all caps so that it's easily seen. As you could probably tell by its name, this file lists out the information you should follow to contribute to the project. You should look for this file before you start doing development work of any kind.
>
> Let's look at the lighthouse project's contributing file:
>
> You can see that the top line of the file says:
>
> > We'd love your help! This doc covers how to become a contributor and submit code to the project.
>
> There are two main sections to this file:
>
> - the "For Contributors" section
> - the "For Maintainers" section
>
> Each one of these sections has subsections of its own to instruct readers on how to contribute to and work with this project.
>
> Let's take a look at the section on signing the contributors license. You can see that to be able to contribute to this project you need to sign Google's Contributor License Agreement.

### Topic Branches

> The best way to organize the set of commits/changes you want to contribute back to the project is to put them all on a topic branch. Now what do I mean by a topic branch? Unlike the master branch which is the default branch that holds all of the commits for your entire project, a topic branch host commits for just a single concept or single area of change.
>
> For example if there is a problem with the login form for logging into the website, then a branch name to address this specific issue could be called:
>
> - login
> - login-bug
> - signup-bug
> - login-form-bug
>
> etc.
>
> There are plenty of names that can be used for a topic branch's name. You just want to use a clear descriptive name for the branch so that if, for example, you list out all of the branches you can immediately see what changes are supposed to be in a branch just by its name.

### Best Practices

> #### Write Descriptive Commit Messages
>
> While we're talking about naming branches clearly that describe what changes the branch contains, I need to throw in another reminder about how critical it is to write clear, descriptive, commit messages. The more descriptive your branch name and commit messages are the more likely it is that the project's maintainer will not have to ask you questions about the purpose of your code or have dig into the code themselves. The less work the maintainer has to do, the faster they'll include your changes into the project.
>
>
> #### Create Small, Focused Commits
>
> This has been stressed numerous times before but make sure when you are committing changes to the project that you make smaller commits. Don't make massive commits that record 10+ file changes and changes to hundreds of lines of code. You want to make smaller, more frequent commits that record just a handful of file changes with a smaller number of line changes.
>
> Think about it this way: if the developer does not like a portion of the changes you're adding to a massive commit, there's no way for them to say, "I like commit A, but just not the part where you change the sidebar's background color." A commit can't be broken down into smaller chunks, so make sure your commits are in small enough chunks and that each commit is focused on altering just one thing. This way the maintainer can say I like commits A, B, C, D, and F but not commit E.
>
>
> #### Update The README
>
> And lastly if any of the code changes that you're adding drastically changes the project you should update the README file to instruct others about this change.

### Recap

> Before you start doing any work, make sure to look for the project's CONTRIBUTING.md file.
>
> Next, it's a good idea to look at the GitHub issues for the project
>
> - look at the existing issues to see if one is similar to the change you want to contribute
> - if necessary create a new issue
> - communicate the changes you'd like to make to the project maintainer in the issue
>
> When you start developing, commit all of your work on a topic branch:
>
> - do not work on the master branch
> - make sure to give the topic branch clear, descriptive name
>
> As a general best practice for writing commits:
>
> - make frequent, smaller commits
> - use clear and descriptive commit messages
> - update the README file, if necessary

---

## Lesson 3. Staying in sync with remote repositories by pulling and rebasing

### Intro

**Create pull requests from topic branches.**

- Forked the course-collaboration-travel-plans repo, then cloned it to desktop.
- Created a topic branch: `$ git checkout -b include-brendons-destinations`
- Made changes and committed to topic branch: `$ git commit -m "Add Brendon's destinations"`
- Configured repo for ssh: `$ git remote set-url origin git@github.com:br3ndonland/course-collaboration-travel-plans.git`
- Pushed the topic branch to GitHub: `$ git push origin include-brendons-destinations`
- At first, I was a little confused as to why you would need to branch if you have already forked. It's for practical reasons. When submitting a pull request, the pull request name is auto-populated from the branch name.
- On the "Open a pull request" screen:
  - the `base fork` is the original repo that the fork was created from.
  - The `head fork` is the branch in your fork that is currently set to `HEAD` on GitHub.
  - When I first got to the pull request screen, it showed `base fork: udacity/course-collaboration-travel-plans`. If I had submitted the pull request this way, it would have gone to Udacity. Instead, I switched to `base fork: br3ndonland/course-collaboration-travel-plans`. This basically becomes a merge. Udacity didn't clearly instruct the students to fork before submitting pull requests, which is why the [repo has thousands of pull requests](https://github.com/udacity/course-collaboration-travel-plans/pulls).

#### Instructor notes

> A pull request is a request for the source repository to pull in your commits and merge them with their project. To create a pull request, a couple of things need to happen:
>
> - you must fork the source repository
> - clone your fork down to your machine
> - make some commits (ideally on a topic branch!)
> - push the commits back to your fork
> - create a new pull request and choose the branch that has your new commits
>
> As you can see, it's actually not too difficult to create a pull request. When I was first learning Git, GitHub, and how to collaborate, I was extremely nervous about making commits, and working with remote repos, but especially submitting a pull request to another developer's project! As long as you following the steps we covered in the previous section on:
>
> - reviewing the project's CONTRIBUTING.md file
> - checking out the project's existing issues
> - talking with the project maintainer
>
> ...your pull request is sure to be included!

### Staying in sync with the source project

#### Stars and popularity

> Starring can be a useful feature to help you keep track of repositories you're interested in. But stars have also turned into a means of measuring a repo's popularity.
>
> If you'd rather not increase a repository's stars, then check out "watching" a repository.

#### Watching

Watching enables notification of changes to a repo.

#### Including Upstream Changes

*We have a clone of a fork. How do we stay in sync with the original master?*

<img src="img/fsnd02_10-github-pr-screenshot01.png" width="300px">

- We can either pull from the master into the origin fork and then to the clone, or just pull directly from the origin master and then push to our fork.
- Richard named the master `upstream`. It could be any name. The name `upstream` was already provided by Udacity:

  ```bash
  $ git remote -v
  origin  git@github.com:br3ndonland/course-collaboration-travel-plans.git (fetch)
  origin  git@github.com:br3ndonland/course-collaboration-travel-plans.git (push)
  upstream  https://github.com/udacity/course-collaboration-travel-plans.git (fetch)
  upstream  https://github.com/udacity/course-collaboration-travel-plans.git (push)
  ```

- Note that `origin` points to the fork.
- *Using git fetch upstream master pulled in the changes from the master branch on the upstream remote repository. What single command would we use if we want to fetch the upstream/master changes and merge them into the master branch?*
  - `git pull upstream master`
  - Remember that `pull` does both a `fetch` and `merge`.

### Manage an active PR

> The project maintainer may decide not to accept your changes right away. They might request you to make some additional changes to your code before accepting your request and merging in your changes. Most likely they will communicate their desired changes through the conversation on the pull requests page.
>
>
> One thing that I've grown to love about both the Git command line tool and the GitHub interface is how helpful they are with recommendations on what to do next. Near the bottom of the comments, there's a suggestion by GitHub that tells us how to add more commit; we need to add them to the same branch and push to my fork:
>
> > Add more commits by pushing to the include-richards-destinations branch on richardkalehoff/course-collaboration-travel-plan.
>
> When you submit a pull request, remember that you're asking another developer to add your code changes to their project. If they ask you to make some minor (even major!) changes to your pull request, that doesn't mean they're rejecting your work! It just means that they would like the code added to their project in a certain way.
>
> The CONTRIBUTING.md file should be used to list out all information that the project's maintainer wants, so make sure to follow the information there. But that doesn't mean there might be times where the project's maintainer will ask you to do a few additional things.
>
> So what should you do? Well, if you want your pull request to be accepted, then you make the change! Remember that the tab in GitHub is called the "Conversation" tab. So feel free to communicate back and forth with the project's maintainer to clarify exactly what they want you to do.
>
> It also wouldn't hurt to thank them for taking the time to look over your pull request. Most of the developers that are working on open source projects are doing it unpaid. So remember to:
>
> - be kind - the project's maintainer is a regular person just like you
> - be patient - they will respond as soon as they are able
>
> So Lam is asking that I combine my changes together before she'll merge in my pull request. Combining commits together is a process called squashing. Let's look at how to do that!
> Recap
>
> As simple as at may seem, working on an active pull request is mostly about communication!
>
> If the project's maintainer is requesting changes to the pull request, then:
>
> - make any necessary commits on the same branch in your local repository that your pull request is based on
> - push the branch to the your fork of the source repository
>
> The commits will then show up on the pull request page.

### Squash commits with rebase

`git rebase -i <base>`

- To reference commits, `HEAD~3`, SHA, branch name, or tag name can be used.
- Richard recommends making a backup branch before rebasing.

### Course wrap-up

> - [http://up-for-grabs.net/](http://up-for-grabs.net/#/)
> - [http://www.firsttimersonly.com/](http://www.firsttimersonly.com/)
> - [first-timers-only label on GitHub](https://github.com/search?utf8=%E2%9C%93&q=label%3Afirst-timers-only+is%3Aopen&type=Issues&ref=searchresults)
> - ["first timers only" blog post](https://medium.com/@kentcdodds/first-timers-only-78281ea47455)
> - try tackling some Git and GitHub challenges with the [Git-it app](https://github.com/jlord/git-it-electron)
>
> Wanna see what a developer's very first pull request is? Check out at [http://firstpr.me/](http://firstpr.me/)