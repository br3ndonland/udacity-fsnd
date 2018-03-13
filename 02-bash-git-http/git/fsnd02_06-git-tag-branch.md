# Tagging, Branching and Merging

**Udacity Full Stack Web Developer Nanodegree program**

Part 02. Developer Tools

Lesson 06. Tagging, Branching and Merging (from [free Git course](https://www.udacity.com/course/version-control-with-git--ud123))

Brendon Smith

br3ndonland


## Notes

This was another helpful lesson.

### Tagging

* Tags are just what you would think, they tag a commit for future reference.
* We used `$ git tag -a v1.0` on the same `new-git-repository`. The `-a` indicates annotated.
* I was able to see the tag simply with `git log --oneline`, even though the tutorial said I shouldn't be able to. There was an addendum in the lesson: `--decorate` Flag Changes in Git 2.13. The lesson should just be updated instead.
  ```bash
  br3ndonland (master *) new-git-project
  $ git log --oneline
  2e104e2 (HEAD -> master, tag: v1.0) Add header to blog
  63afe9d Initial commit
  ```
* If you make a mistake, just delete the tag with `$ git tag -d v1.0` and make a new one


### Branching and merging

* Running `$ git log --oneline --graph --all` will show the branching.
* Switch branches with `git checkout`. 
* Switch and create a branch in one step with `git checkout -b <new-branch-name> master`.
* Merge conflicts: we basically created a branch ahead of `master`, modified a line of code and committed, checked out back to `master`, modified the same line of code again and committed, checked out back to `master` again, and attempted to merge. It took me a couple of tries, but I got it to work.
* Final status
```
$ git log --oneline --graph --all
*   d8ede3c (HEAD -> master) Merge branch 'heading-mod1'
|\
| * 286d83b (heading-mod1) Modify header again to demo merge conflict
* | 98ec7d0 (heading-mod2) Modify header once again to demo merge conflict
|/
* 6cf2cb3 (heading-crusader) Set page heading to Crusade
* b329862 (heading-update) Set page heading to Quest
*   6895eb1 Merge branch 'sidebar'
|\
| * 254f7e4 (sidebar) Add text to sidebar
| * f895dd3 Add sidebar.
* | e385b99 (footer) Add links to social media
* | 4f7968c Improve site heading for SEO
* | d6a086f Set background color for page
|/
* 27f3cf6 Update for Udacity branching lesson fsnd02_06
* 2e104e2 (tag: v1.0) Add header to blog
* 63afe9d Initial commit
```

## Feedback on lesson 6

I was able to see the tag simply with `git log --oneline`, even though the tutorial said I shouldn't be able to. There was an addendum in the lesson: `--decorate` Flag Changes in Git 2.13. The lesson should just be updated instead.