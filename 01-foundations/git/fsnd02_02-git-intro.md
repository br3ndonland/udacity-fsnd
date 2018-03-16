# What is version control?

**Udacity Full Stack Web Developer Nanodegree program**

Part 02. Developer Tools

Lesson 02. What is version control? (from [free Git course](https://www.udacity.com/course/version-control-with-git--ud123))

Brendon Smith

br3ndonland

## Notes

* The instructor Richard Kalehoff introduced version control with an analogy. If playing a board game, snapping a picture during play is like making a save point.
* Most popular VCS: Git, Subversion, Mercurial
* Centralized vs. Distributed: Git is distributed (DVCS)
  - [Centralized vs. DVCS from the Atlassian Blog](http://blogs.atlassian.com/2012/02/version-control-centralized-dvcs/)
* Version Control in Daily Use
  > Google Docs' Revision history page is incredibly powerful! I've used it on several occasions to salvage text that I'd written at one point, erased, and then realized I actually did want to keep.
  > 
  > But for all its ability, it's not as powerful as we'd like. What's it missing? A few that I can think of are:
  > 
  > * the ability to label a change
  > * the ability to give a detailed explanation of why a change was made
  > * the ability to move between different versions of the same document
  > * the ability to undo change A, make edit B, then get back change A without affecting edit B
  > 
  > The version control tool, Git, can do all of those things - and more!!! (bet you didn't see that coming!) So have I sold you yet on the awesomeness that is Git? I hope so, cause we're about to dive into it in the next section. 
* Terms: see ud123-git-keyterms.pdf
* Mac/Linux setup: 
  - I installed the bash configuration.
  - It took me a few tries to set Sublime Text 3 as the Git editor. Got it to work with `$ git config --global core.editor "'/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl' -n -w"`