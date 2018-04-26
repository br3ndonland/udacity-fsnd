# Git

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[Version control with Git](https://www.udacity.com/course/version-control-with-git--ud123)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Lesson 1. Version control intro](#lesson-1-version-control-intro)
  - [Lesson 1 parts 1-3](#lesson-1-parts-1-3)
  - [Lesson 1 part 4. Mac/Linux setup](#lesson-1-part-4-maclinux-setup)
- [Lesson 2. Create a Git repo](#lesson-2-create-a-git-repo)
- [Lesson 3. Review a repo's history](#lesson-3-review-a-repos-history)
- [Lesson 4. Add commits to a repo](#lesson-4-add-commits-to-a-repo)
  - [Bypass The Editor With The -m Flag](#bypass-the-editor-with-the--m-flag)
  - [What To Include In A Commit](#what-to-include-in-a-commit)
  - [Good Commit Messages](#good-commit-messages)
  - [Globbing Crash Course](#globbing-crash-course)
- [Lesson 5. Tagging, branching and merging](#lesson-5-tagging-branching-and-merging)
  - [Tagging](#tagging)
  - [Branching and merging](#branching-and-merging)
  - [Feedback on lesson 5](#feedback-on-lesson-5)
- [Lesson 6. Undoing changes](#lesson-6-undoing-changes)
  - [Reset vs Revert](#reset-vs-revert)
  - [Relative Commit References](#relative-commit-references)
  - [The git reset Command](#the-git-reset-command)
  - [Reset Recap](#reset-recap)

## Lesson 1. Version control intro

### Lesson 1 parts 1-3

- The instructor Richard Kalehoff introduced version control with an analogy. If playing a board game, snapping a picture during play is like making a save point.
- Most popular VCS: Git, Subversion, Mercurial
- Centralized vs. Distributed: Git is distributed (DVCS)
  - [Centralized vs. DVCS from the Atlassian Blog](http://blogs.atlassian.com/2012/02/version-control-centralized-dvcs/)
- Version Control in Daily Use
  > Google Docs' Revision history page is incredibly powerful! I've used it on several occasions to salvage text that I'd written at one point, erased, and then realized I actually did want to keep.
  >
  > But for all its ability, it's not as powerful as we'd like. What's it missing? A few that I can think of are:
  >
  > - the ability to label a change
  > - the ability to give a detailed explanation of why a change was made
  > - the ability to move between different versions of the same document
  > - the ability to undo change A, make edit B, then get back change A without affecting edit B
  >
  > The version control tool, Git, can do all of those things - and more!!! (bet you didn't see that coming!) So have I sold you yet on the awesomeness that is Git? I hope so, cause we're about to dive into it in the next section.
- Terms: see ud123-git-keyterms.pdf

### Lesson 1 part 4. Mac/Linux setup

- I installed the bash prompt configuration.
- It took me a few tries to set Sublime Text 3 as the Git editor. Got it to work with `$ git config --global core.editor "'/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl' -n -w"`

#### Instructor notes

> ##### Configuring Mac's Terminal
>
> We're about to configure the Terminal to display helpful information when in a directory that's under version control. *This is an optional step!- You do not need to re-configure your terminal for Git to work. You can complete the entire course without reconfiguring it. However, reconfiguring the Terminal makes it significantly easier to use.
>
> If you choose to configure your Terminal, here's what it should look like when you're finished.
>
> ![Finished Udacity terminal configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58a76894_ud123-l1-terminal-config-mac/ud123-l1-terminal-config-mac.png)
>
> *The terminal application on MacOS. The terminal has been configured to display version control information.*
>
>
> Configuration Steps
>
> To configure the terminal, we'll perform the following steps:
>
> 1. download the zipped file
> 2. move the directory `udacity-terminal-config` to your home directory and name it `.udacity-terminal-config` (there's a dot at the front, now!)
> 3. move the `bash_profile` file to your home directory and name it `.bash_profile` (there's a dot at the front, now!)
>     - if you *already- have a `.bash_profile` file in your home directory, transfer the content from the downloaded `bash_profile` to your existing `.bash_profile`
>
> Download the zipped file in the Resources pane to get started.
>
>
> ##### Installing Git
>
> Git is actually installed on MacOS, but we'll be reinstalling it so that we'll have the newest version:
>
> 1. go to [https://git-scm.com/downloads](https://git-scm.com/downloads)
> 2. download the software for Mac
> 3. install Git choosing all of the default options
>
> Once everything is installed, you should be able to run `git` on the command line. If it displays the usage information, then you're good to go!
>
> If you run into any issues, let us know in the forum.
>
>
> First Time Git Configuration
>
> Before you can start using Git, you need to configure it. Run each of the following lines on the command line to make sure everything is set up.
>
> ```text
> # sets up Git with your name
> git config --global user.name "<Your-Full-Name>"
>
> # sets up Git with your email
> git config --global user.email "<your-email-address>"
>
> # makes sure that Git output is colored
> git config --global color.ui auto
>
> # displays the original state in a conflict
> git config --global merge.conflictstyle diff3
>
> git config --list
> ```
>
>
> Git & Code Editor
>
> The last step of configuration is to get Git working with your code editor. Below are three of the most popular code editors. If you use a different editor, then do a quick search on Google for "associate X text editor with Git" (replace the X with the name of your code editor).
>
> Atom Editor Setup
>
> ```text
> git config --global core.editor "atom --wait"
> ```
>
>
> Sublime Text Setup
>
> ```text
> git config --global core.editor "'/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl' -n -w"
> ```
>
>
> VSCode Setup
>
> ```text
> git config --global core.editor "code --wait"
> ```
>
> If you have any questions, post them on the forum.
>
>
> ##### Everything Is All Set Up
>
> Task List
>
> - I've installed Git
> - I've configured Git with my username
> - I've configured Git with my email
> - I've configured Git to use my chosen editor
>
>
> ##### Supporting Materials
>
> [udacity-terminal-config.zip](http://video.udacity-data.com.s3.amazonaws.com/topher/2017/March/58d31ce3_ud123-udacity-terminal-config/ud123-udacity-terminal-config.zip)

[(Back to TOC)](#table-of-contents)

---

## Lesson 2. Create a Git repo

- Flew through this lesson.
- `git init`
  - Further Research
    - [Git Internals - Plumbing and Porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain) (advanced - bookmark this and check it out later)
    - [Customizing Git - Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- `git clone`
  - Successfully cloned the blog repo with `git clone https://github.com/udacity/course-git-blog-project blog-project`
- `git status`

[(Back to TOC)](#table-of-contents)

---

## Lesson 3. Review a repo's history

- This lesson was helpful. I hadn't worked with `git log` or `git show` much before this.
- `git log`
  - You can search the log by entering a string after `git log`. To search for an entry with SHA containing 8aa6668, type `git log 8aa6668`.
  - Searching by commit message:
    > Use git log to find the commit that has the message Set article timestamp color. Which commit belongs to that SHA? Provide the first 7 characters of the SHA.
    - I got stuck in a secondary prompt when searching `git log æSet article timestamp color"`. After a while, I realized bash was looking for a closing double quotation character. I just entered `"` and my PS1 command prompt was restored.
    - I had to search the Git documentation to figure this out. I did a text search for "message" on the [git-log page](https://git-scm.com/docs/git-log#git-log---grep-reflogltpatterngt). I found the `--grep=` modifier, enclosed the string in single quotes, and... success! `git log --grep='Set article timestamp color'`. First seven characters of SHA: `5de135a`.
  - `git log --oneline` is more concise.
  - `git log --stat` shows changes. Combine with a search for SHA with `git log 8d3ea36 --stat`
  - Add `-w` to ignore whitespace changes
  - Combine with `git log -p --stat`
- `git show`

[(Back to TOC)](#table-of-contents)

---

## Lesson 4. Add commits to a repo

### Bypass The Editor With The -m Flag

> TIP: If the commit message you're writing is short and you don't want to wait for your code editor to open up to type it out, you can pass your message directly on the command line with the -m flag: `$ git commit -m "Initial commit"`

### What To Include In A Commit

> I've been telling you what files to create, giving you the content to include, and telling you when you should make commits. But when you're on your own, how do you know what you should include in a commit and when/how often you should make commits?
>
> The goal is that each commit has a single focus. Each commit should record a single-unit change. Now this can be a bit subjective (which is totally fine), but each commit should make a change to just one aspect of the project.
>
> Now this isn't limiting the number of lines of code that are added/removed or the number of files that are added/removed/modified. Let's say you want to change your sidebar to add a new image. You'll probably:
>
> - add a new image to the project files
> - alter the HTML
> - add/modify CSS to incorporate the new image
>
> A commit that records all of these changes would be totally fine!
>
> Conversely, a commit shouldn't include unrelated changes - changes to the sidebar and rewording content in the footer. These two aren't related to each other and shouldn't be included in the same commit. Work on one change first, commit that, and then change the second one. That way, if it turns out that one change had a bug and you have to undo it, you don't have to undo the other change too.
>
> The best way that I've found to think about what should be in a commit is to think, "What if all changes introduced in this commit were erased?". If a commit were erased, it should only remove one thing.
>
> Don't worry, commits don't get randomly erased.
>
> In a later lesson, we'll look at using Git to undo changes made in commits and how to manually, carefully remove the last commit that was made.

### Good Commit Messages

> Let's take a quick stroll down Stickler Lane and ask the question:
>
> > How do I write a good commit message? And why should I care?
>
> These are fantastic questions! I can't stress enough how important it is to spend some time writing a good commit message.
>
> Now, what makes a "good" commit message? That's a great question and has been written about a number of times. Here are some important things to think about when crafting a good commit message:
>
> Do
>
> - do keep the message short (less than 60-ish characters)
> - do explain what the commit does (not how or why!)
>
> Do not
>
> - do not explain why the changes are made (more on this below)
> - do not explain how the changes are made (that's what git log -p is for!)
> - do not use the word "and"
>   - if you have to use "and", your commit message is probably doing too many changes - break the changes into separate commits
>   - e.g. "make the background color pink and increase the size of the sidebar"
>
> The best way that I've found to come up with a commit message is to finish this phrase, "This commit will...". However, you finish that phrase, use that as your commit message.
>
> Above all, be consistent in how you write your commit messages!
>
>
> [Udacity Git Commit Message Style Guide](https://udacity.github.io/git-styleguide/)

### Globbing Crash Course

> Let's say that you add 50 images to your project, but want Git to ignore all of them. Does this mean you have to list each and every filename in the .gitignore file? Oh gosh no, that would be crazy! Instead, you can use a concept called globbing.
>
> Globbing lets you use special characters to match patterns/characters. In the .gitignore file, you can use the following:
> ```text
> blank lines can be used for spacing
> # - marks line as a comment
> - - matches 0 or more characters
> ? - matches 1 character
> [abc] - matches a, b, or c
> ** - matches nested directories - a/**/z matches
>   a/z
>   a/b/z
>   a/b/c/z
> ```
> So if all of the 50 images are JPEG images in the "samples" folder, we could add the following line to .gitignore to have Git ignore all 50 images.
> ```text
> samples/*.jpg
> ```
>

---

## Lesson 5. Tagging, branching and merging

This was another helpful lesson.

### Tagging

- Tags are just what you would think, they tag a commit for future reference.
- We used `$ git tag -a v1.0` on the same `new-git-repository`. The `-a` indicates annotated.
- I was able to see the tag simply with `git log --oneline`, even though the tutorial said I shouldn't be able to. There was an addendum in the lesson: `--decorate` Flag Changes in Git 2.13. The lesson should just be updated instead.

  ```bash
  br3ndonland (master *) new-git-project
  $ git log --oneline
  2e104e2 (HEAD -> master, tag: v1.0) Add header to blog
  63afe9d Initial commit
  ```

- If you make a mistake, just delete the tag with `$ git tag -d v1.0` and make a new one

### Branching and merging

- Running `$ git log --oneline --graph --all` will show the branching.
- Switch branches with `git checkout`.
- Switch and create a branch in one step with `git checkout -b <new-branch-name> master`.
- Merge conflicts: we basically created a branch ahead of `master`, modified a line of code and committed, checked out back to `master`, modified the same line of code again and committed, checked out back to `master` again, and attempted to merge. It took me a couple of tries, but I got it to work.
- Final status

  ```text
  $ git log --oneline --graph --all
  -   d8ede3c (HEAD -> master) Merge branch 'heading-mod1'
  |\
  | - 286d83b (heading-mod1) Modify header again to demo merge conflict
  - | 98ec7d0 (heading-mod2) Modify header once again to demo merge conflict
  |/
  - 6cf2cb3 (heading-crusader) Set page heading to Crusade
  - b329862 (heading-update) Set page heading to Quest
  -   6895eb1 Merge branch 'sidebar'
  |\
  | - 254f7e4 (sidebar) Add text to sidebar
  | - f895dd3 Add sidebar.
  - | e385b99 (footer) Add links to social media
  - | 4f7968c Improve site heading for SEO
  - | d6a086f Set background color for page
  |/
  - 27f3cf6 Update for Udacity branching lesson fsnd02_06
  - 2e104e2 (tag: v1.0) Add header to blog
  - 63afe9d Initial commit
  ```

### Feedback on lesson 5

I was able to see the tag simply with `git log --oneline`, even though the tutorial said I shouldn't be able to. There was an addendum in the lesson: `--decorate` Flag Changes in Git 2.13. The lesson should just be updated instead.

---

## Lesson 6. Undoing changes

Major commands used:

- `git commit --amend`
- `git revert`
- `git reset`

### Reset vs Revert

> At first glance, resetting might seem coincidentally close to reverting, but they are actually quite different. Reverting creates a new commit that reverts or undos a previous commit. Resetting, on the other hand, erases commits!
>
> **⚠️ Resetting Is Dangerous ⚠️**
>
> You've got to be careful with Git's resetting capabilities. This is one of the few commands that lets you erase commits from the repository. If a commit is no longer in the repository, then its content is gone.
>
> To alleviate the stress a bit, Git does keep track of everything for about 30 days before it completely erases anything. To access this content, you'll need to use the git reflog command. Check out these links for more info:
>
> - [git-reflog](https://git-scm.com/docs/git-reflog)
> - [Rewriting History](https://www.atlassian.com/git/tutorials/rewriting-history)
> - [reflog, your safety net](http://gitready.com/intermediate/2009/02/09/reflog-your-safety-net.html)

### Relative Commit References

> You already know that you can reference commits by their SHA, by tags, branches, and the special HEAD pointer. Sometimes that's not enough, though. There will be times when you'll want to reference a commit relative to another commit. For example, there will be times where you'll want to tell Git about the commit that's one before the current commit...or two before the current commit. There are special characters called "Ancestry References" that we can use to tell Git about these relative references. Those characters are:
>
> ```text
> ^ – indicates the parent commit
> ~ – indicates the first parent commit
> ```
> Here's how we can refer to previous commits:
>
> - the parent commit – the following indicate the parent commit of the current commit
>   ```text
>   HEAD^
>   HEAD~
>   HEAD~1
>   ```
> - the grandparent commit – the following indicate the grandparent commit of the current commit
>   ```text
>   HEAD^^
>   HEAD~2
>   ```
> - the great-grandparent commit – the following indicate the great-grandparent commit of the current commit
>   ```text
>   HEAD^^^
>   HEAD~3
>   ```
>
> The main difference between the ^ and the ~ is when a commit is created from a merge. A merge commit has two parents. With a merge commit, the ^ reference is used to indicate the first parent of the commit while ^2 indicates the second parent. The first parent is the branch you were on when you ran git merge while the second parent is the branch that was merged in.
>
> It's easier if we look at an example. This what my git log currently shows:
>
> ```text
> - 9ec05ca (HEAD -> master) Revert "Set page heading to "Quests & Crusades""
> - db7e87a Set page heading to "Quests & Crusades"
> -   796ddb0 Merge branch 'heading-update'
> |\
> | - 4c9749e (heading-update) Set page heading to "Crusade"
> - | 0c5975a Set page heading to "Quest"
> |/
> -   1a56a81 Merge branch 'sidebar'
> |\
> | - f69811c (sidebar) Update sidebar with favorite movie
> | - e6c65a6 Add new sidebar content
> - | e014d91 (footer) Add links to social media
> - | 209752a Improve site heading for SEO
> - | 3772ab1 Set background color for page
> |/
> - 5bfe5e7 Add starting HTML structure
> - 6fa5f34 Add .gitignore file
> - a879849 Add header to blog
> - 94de470 Initial commit
> ```
>
> Let's look at how we'd refer to some of the previous commits. Since HEAD points to the 9ec05ca commt:
>
> ```text
> HEAD^ is the db7e87a commit
> HEAD~1 is also the db7e87a commit
> HEAD^^ is the 796ddb0 commit
> HEAD~2 is also the 796ddb0 commit
> HEAD^^^ is the 0c5975a commit
> HEAD~3 is also the 0c5975a commit
> HEAD^^^2 is the 4c9749e commit (this is the grandparent's (HEAD^^) second parent (^2))
> ```
>
> Quiz: *which commit is referenced by HEAD~4^2?*
>
> **f69811c**
>
> > HEAD~4 references the fourth parent commit of the current one and then the ^2 tells us that it's the second parent of the merge commit (the one that got merged in!).

### The git reset Command

> The git reset command is used to reset (erase) commits:
>
> ```bash
> $ git reset <reference-to-commit>
> ```
>
> It can be used to:
>
> - move the HEAD and current branch pointer to the referenced commit
> - erase commits
> - move committed changes to the staging index
> - unstage committed changes
>
>
> #### Git Reset's Flags
>
> The way that Git determines if it erases, stages previously committed changes, or unstages previously committed changes is by the flag that's used. The flags are:
>
> - `--mixed`
> - `--soft`
> - `--hard`
>
> It's easier to understand how they work with a little [animation](https://youtu.be/UN7ki2G2yKc).
>
>
> #### 💡 Backup Branch 💡
>
> Remember that using the git reset command will erase commits from the current branch. So if you want to follow along with all the resetting stuff that's coming up, you'll need to create a branch on the current commit that you can use as a backup.
>
> Before I do any resetting, I usually create a backup branch on the most-recent commit so that I can get back to the commits if I make a mistake:
>
> `$ git branch backup`

### Reset Recap

> To recap, the git reset command is used erase commits:
> ```bash
> $ git reset <reference-to-commit>
> ```
> It can be used to:
>
> - move the HEAD and current branch pointer to the referenced commit
> - erase commits with the `--hard` flag
> - moves committed changes to the staging index with the `--soft` flag
> - unstages committed changes `--mixed` flag
>
> Typically, ancestry references are used to indicate previous commits. The ancestry references are:
>
> - `^` – indicates the parent commit
> - `~` – indicates the first parent commit
>
> Further Research
>
> - [git-reset](https://git-scm.com/docs/git-reset) from Git docs
> - [Reset Demystified](https://git-scm.com/blog) from Git Blog
> - [Ancestry References](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#Ancestry-References) from Git Book

[(Back to TOC)](#table-of-contents)