# Github

### Useful Links
[Git Tagging](https://stackoverflow.com/questions/35979642/what-is-git-tag-how-to-create-tags-how-to-checkout-git-remote-tags)

[Git Stashing](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
```
# stashes all of the work in your current working branch
git stash

# lists all of your stashed work and indexed
git stash list

# if you don’t specify a stash, Git assumes the most recent stash and tries to apply it
git stash apply

# apply the stash and then immediately drop it from your stack
git stash pop

# drops your stash from the stack
git stash drop stash@{0}

# creates a new branch for you with your selected branch name, checks out the commit you were on when you stashed your work, reapplies your work there, and then drops the stash if it applies successfully
git stash branch testchanges
```