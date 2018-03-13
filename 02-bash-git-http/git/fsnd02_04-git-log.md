# Review a Repo's History

**Udacity Full Stack Web Developer Nanodegree program**

Part 02. Developer Tools

Lesson 04. Review a Repo's History (from [free Git course](https://www.udacity.com/course/version-control-with-git--ud123))

Brendon Smith

br3ndonland

## Notes

* This lesson was helpful. I hadn't worked with `git log` or `git show` much before this.
* `git log`
  - You can search the log by entering a string after `git log`. To search for an entry with SHA containing 8aa6668, type `git log 8aa6668`.
  - Searching by commit message:
    > Use git log to find the commit that has the message Set article timestamp color. Which commit belongs to that SHA? Provide the first 7 characters of the SHA.
    + I got stuck in a secondary prompt when searching `git log æSet article timestamp color"`. After a while, I realized bash was looking for a closing double quotation character. I just entered `"` and my PS1 command prompt was restored.
    + I had to search the Git documentation to figure this out. I did a text search for "message" on the [git-log page](https://git-scm.com/docs/git-log#git-log---grep-reflogltpatterngt). I found the `--grep=` modifier, enclosed the string in single quotes, and... success! `git log --grep='Set article timestamp color'`. First seven characters of SHA: `5de135a`.
  - `git log --oneline` is more concise.
  - `git log --stat` shows changes. Combine with a search for SHA with `git log 8d3ea36 --stat`
  - Add `-w` to ignore whitespace changes
  - Combine with `git log -p --stat`
* `git show`