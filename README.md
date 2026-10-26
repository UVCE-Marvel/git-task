# UVCE Marvel - Task 3: Working with GitHub

Familiarize yourself with **GitHub Issues**, **Branching**, **Pull Requests**, **GitHub Actions (CI/CD)**, and **Resolving Merge Conflicts** through this hands-on beginner Python exercise.


---

## Before You Start

Make sure **Git** and **Python 3** are installed on your computer by running:
```bash
git --version
python --version
```
*(Tip for Windows users: if `python` opens the Microsoft Store, use `py` instead of `python` in the commands below.)*

No external Python libraries (`pip install`) are needed -- standard Python 3 works out of the box.

---

## Overview

This repository contains **300 short beginner Python functions** spread across **10 campus scenario files**:
1. `campus_academics.py` - Attendance, internal marks, grade points & lab hours
2. `canteen_and_mess.py` - Dosa orders, filter coffee, mess rebates & chai bills
3. `metro_and_commute.py` - Namma Metro fares, BMTC passes & shuttle trips
4. `marvel_makerspace.py` - 3D printer filament, battery voltages & sensors
5. `fest_and_clubs.py` - Impetus/Kagada events, hackathons & volunteer shifts
6. `hostel_and_facilities.py` - Laundry loads, Wi-Fi usage & room electricity
7. `sports_and_fitness.py` - Cricket runs, badminton rallies & football points
8. `library_and_labs.py` - Library loans, titration readings & pendulum trials
9. `placements_and_internships.py` - Aptitude scores, stipends & notice periods
10. `digital_campus.py` - Portal logins, student IDs & timetable slots

You only need to inspect the **5 functions assigned to your GitHub username**. Every function includes a English description and a concrete `Example:` showing what it should return for a sample input:

```python
def laundry_ordered_pair(pair: list):
    """
    Given a 2-element list `pair`, return a new 2-element list with the smaller number
    first and the larger number second.

    Example:
        laundry_ordered_pair([9, 3]) -> [3, 9]
    """
    first, second = pair[0], pair[1]
    if first < second:
        return [second, first]
    return [first, second]
```

---

## Instructions

### Step 1: Fork & Clone the Repository
1. Click the **Fork** button at the top-right of this GitHub page.
   *(Tip: On the Fork page, uncheck **"Copy the `main` branch only"** so that the `merge-conflict-practice` branch is also copied to your fork.)*
2. Clone your fork to your computer and add the main repository as `upstream`:
   ```bash
   git clone https://github.com/<your-github-username>/git-task.git
   cd git-task
   git remote add upstream https://github.com/UVCE-Marvel/git-task.git
   git fetch upstream
   ```

### Step 2: View Your 5 Assigned Functions
Run the assignment script with your **exact GitHub username**:
```bash
python my_task.py <your-github-username>
```
This prints the **5 functions** assigned to your GitHub username along with their file names and exact line numbers.

### Step 3: Open a GitHub Issue
1. Open the 5 files at the line numbers shown by `my_task.py`.
2. Trace each function using the `Example:` in its docstring to see which functions have a bug.
3. Go to the **Issues** tab of `UVCE-Marvel/git-task` and create a new Issue:
   - **Title:** `Task 3 Bug Report - @<your-github-username>`
   - **Description:** List the buggy functions you found in your 5-function assignment and briefly state what was wrong with each one.

### Step 4: Create a Branch & Fix the Bugs
1. Create and switch to a new branch:
   ```bash
   git checkout -b fix/<your-github-username>
   ```
2. Edit the broken functions so their code matches their docstrings and `Example:` outputs.
3. Test each function you edit using:
   ```bash
   python ci_check.py --func <function_name>
   ```
   - `[UNCHANGED]` means you have not edited that function yet.
   - `[PASS]` means your fix passed all test cases.
   - `[FAIL]` shows what your function returned so you can adjust your fix.

### Step 5: Practice Resolving a Merge Conflict
1. Merge the `merge-conflict-practice` branch into your branch:
   ```bash
   git fetch upstream
   git merge upstream/merge-conflict-practice
   ```
   *(If you unchecked "Copy the `main` branch only" when forking, `git merge origin/merge-conflict-practice` also works.)*
2. Git will report a **Merge Conflict** in `campus_registry.py` and add conflict markers that look like this:
   ```python
   <<<<<<< HEAD
       return ["MARVEL", "IEEE"]
   =======
       return ["GDSC", "SAE"]
   >>>>>>> upstream/merge-conflict-practice
   ```
3. Open `campus_registry.py` in your editor, read the instructions at the top of the file, combine the data from both branches so both functions return the complete combined values, and delete the `<<<<<<<`, `=======`, and `>>>>>>>` marker lines.
4. Run the full progress check locally:
   ```bash
   python ci_check.py --user <your-github-username>
   ```
   Make sure both **Part 1** and **Part 2** pass and you see:
   `SUCCESS: All tasks for @<your-github-username> are complete and ready to commit/push!`

### Step 6: Commit, Push & Open a Pull Request
1. Stage, commit, and push your changes to your fork:
   ```bash
   git add .
   git commit -m "Complete Task 3 fixes and resolve merge conflict for @<your-github-username>"
   git push origin fix/<your-github-username>
   ```
2. On GitHub, open a **Pull Request** from your `fix/<your-github-username>` branch to `UVCE-Marvel/git-task` (`main` branch), and mention your Issue number in the description.
3. **GitHub Actions** will automatically run on your Pull Request and turn green once all checks pass.

---

## Notes & Troubleshooting
- **Do all 5 assigned functions have a bug?** Not necessarily -- some functions in your 5-function list already work as described in their docstring. Only edit a function if its code does not match its docstring and `Example:`.
- **`git merge` says `not something we can merge`:** Run `git remote add upstream https://github.com/UVCE-Marvel/git-task.git` followed by `git fetch upstream`, then run `git merge upstream/merge-conflict-practice`.
- **Do not modify** `testing.py`, `ci_check.py`, `my_task.py`, or functions outside your 5-function assignment.

## References
- [GitHub Quickstart: Contributing to Projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
- [Resolving a Merge Conflict Using the Command Line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)
