# Jira plan — Laboratory 6 (copy into Jira)

## Project

- **Project type:** Kanban
- **Project name:** Laboratory 6

## Tasks (move each one To Do → In Progress → Done)

### Task 1 — Implement Insertion Sort

- **Type:** Task
- **Title:** Implement Insertion Sort
- **Description:** Write a separate function `insertion_sort(numbers)` in
  `main.py` that sorts a list of integers in ascending order using
  Insertion Sort. Do not use `sorted()` or `list.sort()`.
  The function returns a new sorted list and does not change the
  original list.
- **Status:** Done

### Task 2 — Implement Merge Sort

- **Type:** Task
- **Title:** Implement Merge Sort
- **Description:** Write separate functions `merge_sort(numbers)` and
  `merge(left, right)` in `main.py` that sort a list of integers in
  ascending order using Merge Sort. Do not use `sorted()` or
  `list.sort()`. The function returns a new sorted list.
- **Status:** Done

### Task 3 — Read date.txt, select the algorithm and write the result

- **Type:** Task
- **Title:** Read date.txt, select the algorithm and write the result
- **Description:** In `main.py`, read exactly two lines from `date.txt`:
  line 1 = integers separated by spaces, line 2 = the algorithm name
  (`Insertion` or `Merge`). Check that the file exists, that the
  numbers are valid integers, and that the algorithm is one of the
  implemented ones; print a clear error message for invalid input.
  Run only the selected algorithm, then write the result below the
  two input lines in the same file, labelled with the algorithm name,
  and keep the original input data.
  Example: input `7 8 2 3 4 5` + `Merge` → add the line
  `Merge: 2 3 4 5 7 8`.
- **Status:** Done

## Bug (found while testing)

### Bug 1 — The result line is added again on every run

- **Type:** Bug
- **Title:** Result line is duplicated when the program runs twice
- **Steps to reproduce:**
  1. Create `date.txt` with `7 8 2 3 4 5` on line 1 and `Merge` on line 2.
  2. Run `python3 main.py`.
  3. Run `python3 main.py` a second time.
  4. Open `date.txt`.
- **Expected result:** the file has 3 lines: the two input lines and
  one result line, `Merge: 2 3 4 5 7 8`.
- **Actual result (first version):** the result line was appended again,
  so the file had 4 lines and kept growing with every run.
- **Fix:** instead of appending, the program now rewrites the file with
  only the two original input lines plus one result line.
- **Status:** Done
