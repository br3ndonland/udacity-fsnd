# Add Commits To A Repo

**Udacity Full Stack Web Developer Nanodegree program**

Part 02. Developer Tools

Lesson 05. Add Commits To A Repo (from free course [Version Control with Git](https://www.udacity.com/course/version-control-with-git--ud123))

Brendon Smith

br3ndonland

## Notes

* Bypass The Editor With The -m Flag
  - TIP: If the commit message you're writing is short and you don't want to wait for your code editor to open up to type it out, you can pass your message directly on the command line with the -m flag: `$ git commit -m "Initial commit"`

### What To Include In A Commit

I've been telling you what files to create, giving you the content to include, and telling you when you should make commits. But when you're on your own, how do you know what you should include in a commit and when/how often you should make commits?

The goal is that each commit has a single focus. Each commit should record a single-unit change. Now this can be a bit subjective (which is totally fine), but each commit should make a change to just one aspect of the project.

Now this isn't limiting the number of lines of code that are added/removed or the number of files that are added/removed/modified. Let's say you want to change your sidebar to add a new image. You'll probably:

    add a new image to the project files
    alter the HTML
    add/modify CSS to incorporate the new image

A commit that records all of these changes would be totally fine!

Conversely, a commit shouldn't include unrelated changes - changes to the sidebar and rewording content in the footer. These two aren't related to each other and shouldn't be included in the same commit. Work on one change first, commit that, and then change the second one. That way, if it turns out that one change had a bug and you have to undo it, you don't have to undo the other change too.

The best way that I've found to think about what should be in a commit is to think, "What if all changes introduced in this commit were erased?". If a commit were erased, it should only remove one thing.

    Don't worry, commits don't get randomly erased.

    In a later lesson, we'll look at using Git to undo changes made in commits and how to manually, carefully remove the last commit that was made.

### Good Commit Messages

Let's take a quick stroll down Stickler Lane and ask the question:

    How do I write a good commit message? And why should I care?

These are fantastic questions! I can't stress enough how important it is to spend some time writing a good commit message.

Now, what makes a "good" commit message? That's a great question and has been written about a number of times. Here are some important things to think about when crafting a good commit message:

Do

    do keep the message short (less than 60-ish characters)
    do explain what the commit does (not how or why!)

Do not

    do not explain why the changes are made (more on this below)
    do not explain how the changes are made (that's what git log -p is for!)
    do not use the word "and"
        if you have to use "and", your commit message is probably doing too many changes - break the changes into separate commits
        e.g. "make the background color pink and increase the size of the sidebar"

The best way that I've found to come up with a commit message is to finish this phrase, "This commit will...". However, you finish that phrase, use that as your commit message.

Above all, be consistent in how you write your commit messages!


[Udacity Git Commit Message Style Guide](https://udacity.github.io/git-styleguide/)


### Globbing Crash Course

Let's say that you add 50 images to your project, but want Git to ignore all of them. Does this mean you have to list each and every filename in the .gitignore file? Oh gosh no, that would be crazy! Instead, you can use a concept called globbing.

Globbing lets you use special characters to match patterns/characters. In the .gitignore file, you can use the following:

    blank lines can be used for spacing
    # - marks line as a comment
    * - matches 0 or more characters
    ? - matches 1 character
    [abc] - matches a, b, or c
    ** - matches nested directories - a/**/z matches
        a/z
        a/b/z
        a/b/c/z

So if all of the 50 images are JPEG images in the "samples" folder, we could add the following line to .gitignore to have Git ignore all 50 images.

samples/*.jpg

