# Git Flow Guide

## 1. Start with a repository
- Clone a GitHub repo:
  ```powershell
  git clone https://github.com/<owner>/<repo>.git
  cd <repo>
  ```
- Or create a new local repo:
  ```powershell
  git init
  ```

## 2. Check repo status
- See current changes and branch status:
  ```powershell
  git status
  ```

## 3. Use branches for work
- Create and switch to a new branch:
  ```powershell
  git checkout -b my-feature
  ```
- Switch branches:
  ```powershell
  git checkout main
  ```

## 4. Make changes
- Edit code, add files, or update tests.
- Review changes before staging:
  ```powershell
  git diff
  ```

## 5. Stage changes
- Stage specific files:
  ```powershell
  git add file1.py file2.py
  ```
- Stage everything:
  ```powershell
  git add .
  ```

## 6. Commit changes
- Save your changes with a useful message:
  ```powershell
  git commit -m "Describe the fix or feature"
  ```

## 7. Sync with the remote repository
- Pull updates from remote first:
  ```powershell
  git pull origin main
  ```
- Push your branch to remote:
  ```powershell
  git push origin my-feature
  ```

## 8. Merge with Pull Request
- Open a pull request on GitHub from `my-feature` into `main`.
- Review the code and merge when ready.

## Common commands
- `git branch` — list branches
- `git branch -a` — list local and remote branches
- `git checkout <branch>` — switch to a branch
- `git checkout -b <branch>` — create and switch to a branch
- `git merge <branch>` — merge another branch into the current branch
- `git fetch` — download remote changes without merging
- `git pull` — fetch and merge from remote
- `git push` — upload commits to remote
- `git log --oneline` — view commit history

## Simple workflow example
1. Clone repo:
   ```powershell
   git clone https://github.com/owner/repo.git
   cd repo
   ```
2. Create a feature branch:
   ```powershell
   git checkout -b fix-create-order
   ```
3. Make changes.
4. Stage and commit:
   ```powershell
   git add .
   git commit -m "Fix createOrder call with credentials"
   ```
5. Push branch:
   ```powershell
   git push origin fix-create-order
   ```
6. Open a PR on GitHub.

## Notes
- Keep commits small and clear.
- Use branches for features and bug fixes.
- Pull often to stay updated.
- Resolve merge conflicts carefully.
