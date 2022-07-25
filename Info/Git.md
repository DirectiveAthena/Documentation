---
copyright: "Andreas Sas 2022"
created: "2022-07-24 22:39"
cssclass: metaDataHide
aliases: [Git]
---

# Git stuff
A place to house all types of git stuff
## Branch conventions
- **The default branch name for every git repo is : `core`**
  This was a neutral name that didn't hold any weight like the old `master` name had or the personal inconsistency I saw with the name `main`. 
  It simply refers to the "core" of a tree where all branches diverge from. I know that for Git this doesn't quite make sense, as branches can converge again, but it is the closest I can come to a comprehensive name.

- **A branch name should not hold the name of the upcoming version, but simply state what the branch is there for.**
  I have been guilty of this rule in the past which lead to version bumps being related to a single feature or no feature at all sometimes. It's a stupid habit and I should refrain from doing it in the future

## Commit conventions

A set of convention rules to follow to make lookups easier and bring order to some chaos I have created in the past.

| convention     | explanation                                              |
|:-------------- |:-------------------------------------------------------- |
| `Feat : ...`   | An addition to the code base                             |
| `Fix : ...`    | A fix to the code base that doesn't change the behaviour |
| `Change : ...` | A change to the code base that does change the behaviour |
| `Remove : ...` | A removal of a piece of the code base                    |
| `Docu : ...`   | A documentation change (addition / fix / ....)                                                         |
