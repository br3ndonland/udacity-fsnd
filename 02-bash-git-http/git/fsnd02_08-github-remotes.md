# GitHub intro

**Udacity Full Stack Web Developer Nanodegree program**

Part 02. Developer Tools

Lesson 08. Intro to GitHub Remotes (from [free Git course](https://www.udacity.com/course/version-control-with-git--ud123))

Brendon Smith

br3ndonland


## Notes

* Made a test repo `github-sample-repo` and created the three intro files in one step with `$ touch README.md index.html app.css`. 
* Configured repo to push with ssh: `$ git remote set-url origin git@github.com:br3ndonland/udacity-travel-plans.git`
* Pushed with `$ git push origin master`.
  > One very important thing to know is that this `origin/master` tracking branch is not a live representation of where the branch exists on the remote repository. If a change is made to the remote repository not by us but by someone else, the `origin/master` tracking branch in our local repository will not move. We have to tell it to go check for any updates and then it will move. We'll look at how to do this in the next section.
* Made changes on github, then brought the changes to the local repo with `$ git pull origin master`.
* `Pull` vs. `fetch`: `fetch` just retrieves remote changes, but does not directly merge. It's like half of `pull`. The other half of `pull` is a merge with the local repo.