# Git practice with a simple python calculator

I created this repository to enhance my understanding of git branching and merging. As part of this exercise, I chose to construct a calculator class in Python, incorporating fundamental operations such as addition, multiplication, division, subtraction, exponentiation, and radical operations. To maintain the privacy of the numbers passed as arguments, I utilized the property decorator in the operation methods.

## Commands practiced and challenges encountered

Typically, I follow the routine of creating a GitHub repository and cloning it to my local machine before initiating a new project. However, for the purpose of practicing new commands, I opted to use `git init` to commence from a local project and attempted to create a new branch from scratch.

Here, I encountered my initial challenge. Realizing that I should commit first on the "main" branch before branching out, I initiated a .gitignore file and committed it to the main branch. Then, I employed `git branch <branch-name>` to create the first branch and `git checkout <branch-name>` to switch to this newly formed branch. Within this branch, I crafted the .py file, introducing the first three operations (addition, multiplication, division). After committing my changes, I returned to the main branch and merged both branches using the `git merge -m "<message>" <other-branch-name>` command.

Moving forward, I created another branch, incorporating the subtraction and exponentiation operations. Upon returning to the main branch, I established yet another branch, integrating the final radical operation. Although the merge of the second branch transpired seamlessly, I encountered a content conflict while attempting to merge the third branch. To resolve this conflict, I removed the markers indicating the modifications made by git in the files and completed the final commit.

## Reflection

As I usually practice own my own, I rarely create new branches. This endeavor provided valuable insights, enabling me to refine my problem-solving skills. Despite the challenges faced, the experience proved to be enriching and educational!
