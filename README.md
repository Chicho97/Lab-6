# Laboratory 6 — Sorting Algorithms and Task Management in Jira

## What the program does

`main.py` sorts numbers using the algorithm written in `date.txt`.
It never uses `sorted()` or `list.sort()`.

`date.txt` has exactly two lines:

```
7 8 2 3 4 5
Merge
```

- Line 1: the integers, separated by spaces.
- Line 2: the algorithm name — `Insertion` or `Merge`.

After the run, the program writes the result **below** those two lines,
in the same file, and keeps the original input:

```
7 8 2 3 4 5
Merge
Merge: 2 3 4 5 7 8
```

Running the program again does **not** add the result a second time.

## How to run it

```
python3 main.py
```

To try the other algorithm, change line 2 of `date.txt` to `Insertion`
and run it again.

## If the input is wrong, the program says so clearly

- `date.txt` does not exist → `Error: file 'date.txt' does not exist.`
- Fewer than two lines → error asking for two lines.
- Line 1 has something that is not an integer (for example `7 a 3`) →
  `Error: line 1 must contain only integers separated by spaces.`
- Line 2 is not `Insertion` or `Merge` (for example `Quick`) →
  `Error: unknown algorithm 'Quick'. Use 'Insertion' or 'Merge'.`

In all these cases the file is **not** changed.

## The two algorithms (simple version)

- **Insertion Sort** (`insertion_sort`): take each number, one by one,
  and insert it in the right place among the numbers before it.
- **Merge Sort** (`merge_sort` + `merge`): split the list in half,
  sort each half, then merge the two sorted halves.

## Files

- `main.py` — the program (Python, no extra libraries needed)
- `date.txt` — the input file (example from the lab)
- `jira-tasks.md` — the Jira project, tasks and Bug, ready to copy into Jira
- `README.md` — this file

## Jira — what to do (details in `jira-tasks.md`)

1. Create a **Kanban project** in Jira named **Laboratory 6**.
2. Create 3 tasks: *Implement Insertion Sort*, *Implement Merge Sort*,
   *Read date.txt, select the algorithm and write the result*.
   Each task has a title and a description.
3. Move each task **To Do → In Progress → Done** while you work.
4. Create 1 **Bug** item for a problem found while testing
   (the duplicate-result bug — see `jira-tasks.md`):
   steps to reproduce, expected result, actual result.

## GitHub — what to do

1. On GitHub, create a **public** repository named **`hicham_lab_06`**
   (the lab asks for `nume_lab_06`, with `nume` replaced by your own name).
2. Upload these files: `main.py`, `date.txt`, `README.md`
   (and `jira-tasks.md` if you want).
3. The repository must contain Python code — `main.py` is the program.

## Tested

- Example from the lab: `7 8 2 3 4 5` + `Merge` → `Merge: 2 3 4 5 7 8`
- `5 3 8 1` + `Insertion` → `Insertion: 1 3 5 8`
- Second run does not duplicate the result line.
- Invalid numbers, unknown algorithm, missing file and one-line file
  all print a clear error and leave the file unchanged.
