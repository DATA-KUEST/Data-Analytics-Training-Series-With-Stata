# Learning Notes: Opening and Saving Stata Datasets (.dta files)

**Part of:** Lesson 2, Importing and Exploring Data  |  **Read and practise:** about 75 minutes  |  **Dataset:** `auto` (built into Stata) and `data/anc_survey.dta` (in this repo)

Every analysis starts by **opening** a dataset and ends by **saving** one. Done carelessly, these two steps cause the most expensive mistakes in data work: the wrong file analysed, a raw file overwritten, a day of cleaning lost because it was never saved. Done well, they make your work safe and repeatable. This guide explains how Stata handles `.dta` files, in menus and in commands.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 5 ("Opening and saving Stata datasets"), with Data Editor details from chapter 6, and checked against the `[D] use`, `[D] save` and `[D] sysuse` entries on stata.com. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Explain the difference between the dataset **in memory** and the file **on disk**
- Open datasets in every way Stata offers, and choose the right one
- Use `use` with paths, `clear`, variable lists, `if` and `in`
- Use `sysuse` and `webuse` for example data
- Understand and respond to Stata's protection against losing changes (`r(4)`)
- Save with `save`, `save, replace` and `saveold`, and avoid overwriting raw data
- Handle version compatibility between Stata releases
- Inspect a dataset immediately after opening it
- Adopt a safe file-naming and backup routine
- Troubleshoot the common errors

## Contents
1. [The key idea: memory versus disk](#1-the-key-idea-memory-versus-disk)
2. [What is a .dta file?](#2-what-is-a-dta-file)
3. [Seven ways to open a dataset](#3-seven-ways-to-open-a-dataset)
4. [The `use` command in depth](#4-the-use-command-in-depth)
5. [Example data: `sysuse` and `webuse`](#5-example-data-sysuse-and-webuse)
6. [Stata's protection against losing changes](#6-statas-protection-against-losing-changes)
7. [Inspect every dataset as soon as you open it](#7-inspect-every-dataset-as-soon-as-you-open-it)
8. [Saving datasets](#8-saving-datasets)
9. [Version compatibility: sharing with other Stata users](#9-version-compatibility-sharing-with-other-stata-users)
10. [Saving safely: a routine for professionals](#10-saving-safely-a-routine-for-professionals)
11. [Saving smaller and richer files](#11-saving-smaller-and-richer-files)
12. [Several datasets at once: frames](#12-several-datasets-at-once-frames)
13. [Opening and saving in a do-file](#13-opening-and-saving-in-a-do-file)
14. [Troubleshooting](#14-troubleshooting)
15. [Practice exercises F1 to F12](#15-practice-exercises-f1-to-f12)
16. [Quick reference card](#16-quick-reference-card)
17. [Facilitator notes](#17-facilitator-notes)

---

## 1. The key idea: memory versus disk

When you open a dataset, Stata makes **a copy in memory (RAM)**. Everything you do (`generate`, `drop`, `replace`, `recode`) changes the copy in memory. The file on disk does not change until you **save**.

```
   file on disk                  Stata's memory
  ┌──────────────┐   use        ┌──────────────┐
  │ anc_survey   │ ───────────▶ │ working copy │ ← you edit this
  │   .dta       │ ◀─────────── │              │
  └──────────────┘   save       └──────────────┘
```

The manual puts it plainly: **changes you have made to a dataset are not permanent until you save them. You work with a copy of the dataset in memory, not with the data file itself.**

Two consequences:
1. If Stata closes (or the power fails) before you save, the changes are gone.
2. If you save over the original, the original is gone too. The manual warns that once you overwrite a dataset there is no way to recover the original, and recovering from an inadvertent save is nearly impossible.

A second point: Stata has **one active dataset at a time**. It is possible to hold several datasets in memory using *frames* (section 12), but only one is active. Keeping this in mind explains why Stata is careful when you open a new dataset.

## 2. What is a .dta file?

A `.dta` file is Stata's own data format. It stores more than numbers:

| Stored in a .dta file | Example |
|-----------------------|---------|
| The data | 1,212 rows and 13 columns |
| Variable names | `anc_visits` |
| Variable labels | "Number of ANC visits" |
| Value labels | 1 = "Urban", 2 = "Rural" (the course's `anc_survey.dta` stores text and has no labels yet; adding them is Lesson 3) |
| Storage types | `byte`, `int`, `float`, `double`, `str#` |
| Display formats | `%9.2f`, `%td` |
| Dataset label and notes | "Synthetic ANC survey" |
| Sort order | Which variable the data are sorted by |

This is why `.dta` is better than CSV for work in progress: the labels and types travel with the data, and Stata opens the file fast. CSV and Excel files lose labels and may be misread (see the import sections of Lesson 2).

**File extension.** If you give no extension, Stata assumes `.dta`. Your operating system may hide extensions; turn on "file name extensions" in your file explorer to avoid confusion between `anc_survey.dta` and `anc_survey.dta.csv`.

## 3. Seven ways to open a dataset

The manual lists these ways to open a Stata dataset.

| # | Method | When to use it |
|---|--------|----------------|
| 1 | **Double-click** a `.dta` file | Quick look. Starts Stata with the working directory set to the file's folder. May open a new Stata session |
| 2 | **File > Open...** or the **Open** toolbar button | Occasional, one-off opening by browsing |
| 3 | **File > Open data subset...** | Large files: choose the observation range and the variables |
| 4 | **File > Recent files** | Re-open something you used recently |
| 5 | **`use filename`** | **Best practice**: recorded in your do-file, repeatable |
| 6 | **`sysuse filename`** | Example datasets that ship with Stata or sit on the adopath |
| 7 | **`webuse filename`** | Datasets used in the Stata manuals, fetched from the internet |

The Data Editor's **Open** button also opens a dataset, and Stata warns you if your current dataset has unsaved changes.

**Rule for professionals:** use the menus to *explore*, but use `use` in a do-file for anything that matters. A menu click leaves no record of which file you opened.

### 3.1 What happens to the data already in memory?
Opening a dataset in the current frame **replaces** the dataset in memory. If the data have unsaved changes, Stata refuses to discard them unless you force it:
- Through **menus**, Stata **prompts** you.
- In the **Command window or a do-file**, you get an error, unless you add `clear` (section 6).

## 4. The `use` command in depth

### 4.1 Basic forms
```stata
use anc_survey                       // looks for anc_survey.dta in the working directory
use "data/anc_survey.dta"            // path relative to the working directory
use "C:/Users/Amina/Documents/dataquest/data/anc_survey.dta", clear
```
- If you omit the extension, Stata assumes `.dta`.
- Stata looks for the file in the **current working directory** unless you give a path. See the [working directory guide](../lesson-01-getting-started/working-directory-guide.md).
- **If there is a space anywhere in the path or file name, put the whole name in double quotes.** Quote every path as a habit, and use forward slashes.

### 4.2 The `clear` option
```stata
use "data/anc_survey.dta", clear
```
`clear` tells Stata: "replace whatever is in memory, even if it has unsaved changes." It is convenient and dangerous in equal measure.

| Situation | Use `clear`? |
|-----------|-------------|
| First line of a do-file that starts from raw files on disk | **Yes**: nothing worth protecting is in memory |
| Interactively, after you have saved your work | Yes |
| Interactively, when you have unsaved changes you care about | **No**: save first |

### 4.3 Opening only part of a file
You do not have to load a whole dataset. This is useful for large files and for focus.

```stata
use id state age hb using "data/anc_survey.dta", clear      // selected variables
use id state age hb in 1/100 using "data/anc_survey.dta", clear   // first 100 observations
use if state == "Lagos" using "data/anc_survey.dta", clear  // selected observations
use id age hb if age >= 18 using "data/anc_survey.dta", clear
```
Note the form: `use [varlist] [if] [in] using filename`. The word `using` is required when you select variables or observations. The `if` and `in` conditions are applied while reading, so rows that do not match never enter memory.

The menu equivalent is **File > Open data subset...**, where you specify the observation range and select variables.

> Be sure you really want a subset: if you then `save` it over the original file name, you will have thrown away the rest of the data. Use a new name (section 10).

### 4.4 `nolabel`
```stata
use "data/anc_survey.dta", clear nolabel
```
`nolabel` prevents value labels from loading, so you see the underlying codes. You are unlikely to need it routinely.

### 4.5 Opening a file from the internet
`use` accepts a web address (URL) too:
```stata
use https://www.stata-press.com/data/r19/union, clear
```
`webuse union` is a shorthand for the same dataset (section 5).

**Caution with data from the internet:** use only sources you trust, and always inspect the file after opening it.

### 4.6 Looking inside a file without opening it
```stata
describe using "data/anc_survey.dta"
```
shows the variables, types and labels in the file without loading it. This is useful before opening a large dataset.

## 5. Example data: `sysuse` and `webuse`

### 5.1 `sysuse`
```stata
sysuse auto, clear         // 1978 automobile data, 74 cars
sysuse dir                 // list the example datasets available
```
`sysuse` looks across the **adopath**, a set of folders where Stata keeps its files, for `.dta` files. Datasets that ship with Stata sit in system folders. Datasets installed from the internet through `net` or `ssc` can appear there too.

You can store **your own** datasets in your personal ado folder (see `help sysdir`) and they will appear in `sysuse dir`. This is handy for a training team's shared practice data. `sysuse dir all` includes names with underscores, which are normally hidden. After `sysuse dir`, the list is stored in `r(files)`; after `sysuse filename`, the full path is stored in `r(fn)`.

### 5.2 `webuse`
`webuse` fetches the datasets used in the Stata manuals from the internet. For example `webuse lbw` loads the dataset used in the documentation of the `logistic` command. This lets you follow the manual examples exactly. It needs an internet connection.

### 5.3 Which to use
| Command | Source | Needs internet? |
|---------|--------|-----------------|
| `use file` | Your file system | No |
| `sysuse file` | Stata's installed examples and your adopath | No |
| `webuse file` | Stata's web-hosted examples | **Yes** |

## 6. Stata's protection against losing changes

Try this:
```stata
sysuse auto, clear
generate gp100m = 100/mpg        // the data in memory now differ from the file
sysuse auto
```
The last line fails:
```
no; dataset in memory has changed since last saved
r(4);
```
This is Stata protecting you from mistakenly losing data. You have three choices:

| Choice | Command | Effect |
|--------|---------|--------|
| Save first, then open | `save "work.dta", replace` then `use ...` | Nothing lost |
| Discard the changes deliberately | `use ..., clear` | Changes lost |
| Cancel | (do nothing) | Nothing changes |

**In a do-file:** put `clear` on the loading line when the do-file starts from raw files, as the do-file guide explains. During development, keep `clear` so you can rerun repeatedly; decide what is appropriate in the final version.

**Check whether the data have changed:**
```stata
display c(changed)        // 1 if the data in memory changed since last save, 0 if not
display "`c(filename)'"   // the name of the file last loaded or saved
```

## 7. Inspect every dataset as soon as you open it

Never assume you opened what you meant to. A five-command habit:

```stata
use "data/anc_survey.dta", clear
describe                  // variables, types, labels, file name, size
count                     // number of observations
codebook, compact         // quick summary of each variable
list in 1/5               // first few rows (avoid listing identifiable data in shared logs)
summarize                 // numeric variables
```
Questions to ask:
1. Is it the **right file**? (check the title in the Results window, `c(filename)`, and the observation count)
2. Does it have the **expected number of observations and variables**?
3. Are variable **types** sensible (numbers stored as numbers, not text)?
4. Are there **labels**? Is anything unlabelled?
5. Is there a **unique identifier**? (`isid id` stops with an error if not; `duplicates report id` shows how many repeats)
6. How much is **missing**?

The Data Editor in **browse mode** is a safe way to look: the manual highly recommends using it in browse mode and switching to edit mode only when you want to make changes.

```stata
browse                    // opens the Data Editor in browse mode
```

For a record of the exact data used, create a data fingerprint:
```stata
datasignature             // a compact checksum of the data
```
Compare signatures to confirm two people have identical data.

## 8. Saving datasets

### 8.1 The three situations (from the manual)

| Situation | Menu | Command |
|-----------|------|---------|
| Save an **unnamed** dataset, or an old dataset under a **new name** | **File > Save as...** | `save filename` |
| Save for use with **Stata 13** | **File > Save as...**, then choose "Stata 13 Data (*.dta)" | `saveold filename` |
| Save a **changed dataset, overwriting** the original file | **File > Save**, the **Save** button | `save, replace` |

### 8.2 `save`
```stata
save "data/anc_survey_working.dta"             // new file
save "data/anc_survey_working.dta", replace    // overwrite if it exists
save, replace                                  // save under the name last used
```
- If you give no extension, Stata adds `.dta`.
- If you give no file name, Stata uses the name last known (`c(filename)`).
- Names with spaces need double quotes.

### 8.3 Overwrite protection
`save` **refuses to overwrite an existing file**:
```
file anc_survey_working.dta already exists
r(602);
```
To overwrite deliberately, add `replace`. This is the reason `replace` appears in so many do-files: they rewrite their own output each run. Stata also checks that data are saved when you exit; `exit, clear` overrides that, so use it with care.

> **Golden rule:** use `replace` only on files your code created. Never use it on raw data.

### 8.4 Options of `save`
| Option | Effect |
|--------|--------|
| `replace` | Allow overwriting an existing file |
| `nolabel` | Omit value labels (variable labels, dataset label and the connections between variables and value labels are still saved) |
| `orphans` | Also save value labels that are not attached to any variable |
| `all` | Programmer's option: save `e(sample)` |
| `emptyok` | Programmer's option: allow a dataset with no observations and no variables |

### 8.5 `saveold`
```stata
saveold "data/for_colleague.dta", version(13) replace
```
Saves in an earlier `.dta` format for colleagues with older Stata. See section 9.

### 8.6 Saving through the menus
**File > Save as...** opens a dialog; choose the **folder** carefully (the dialog may not open in your working directory; see the [working directory guide](../lesson-01-getting-started/working-directory-guide.md)) and the **file type**. After saving, check the file name in Stata's title bar and with `display "`c(filename)'"`.

## 9. Version compatibility: sharing with other Stata users

| Direction | Works? |
|-----------|--------|
| Newer Stata opens a file saved by **older** Stata | **Yes** |
| Older Stata opens a file saved by **newer** Stata | **May fail**, with `file ... not Stata format`, `r(610)` |

If a colleague uses an older Stata, save a copy for them with `saveold`. According to the reference entry:
- `saveold` takes `version(#)`, where `#` can be 11 to 18; the default is 13.
- Stata 14 through 17 share a file format when a dataset has 32,767 or fewer variables.
- Stata 18 and 19 share a format unless the data contain *alias variables* (which need a newer format). To save for older versions, drop them or convert them first.
- Stata/MP 15 and later can handle more than 32,767 variables using a slightly different format.
- Stata/MP and Stata/SE can read Stata/BE files, and Stata/BE can read MP and SE files that fit within its limits.

**Practical advice**
1. Find out which Stata version your recipients use before sending.
2. Keep your own master copy in the format of your current Stata, and make an old-format copy only for sending.
3. Mention the format in the file name if you keep several: `anc_survey_v13.dta`.
4. Remember that features introduced in newer versions (long strings, many variables, some labels) may not survive in an older format. Test by opening the copy.

## 10. Saving safely: a routine for professionals

### 10.1 Keep raw data raw
```
data/
├── raw/       ← original files, read only; never saved over
└── clean/     ← datasets your do-files create
```
A do-file reads from `raw/` and writes to `clean/`:
```stata
use "data/raw/anc_survey.dta", clear
* ... cleaning ...
save "data/clean/anc_survey_clean.dta", replace
```
You can make the raw file **read only** in your operating system to add a second layer of protection.

### 10.2 Save under a new name
Whenever you change the structure of a dataset (dropping observations or variables, collapsing, reshaping, merging), save the result under a **new name** so the earlier stage still exists:
```
anc_survey_raw.dta   →   anc_survey_clean.dta   →   anc_survey_analysis.dta
```
The manual's advice: with important datasets, keep a backup copy of the original, or save changes under a new name.

### 10.3 Naming conventions
| Good | Bad |
|------|-----|
| `anc_survey_clean.dta` | `ANC Survey FINAL (2).dta` |
| `anc_survey_2026-10-25.dta` | `new data.dta` |
| `01_import.do` | `import.do` |

Use lowercase, underscores or hyphens, no spaces, and a short description of the stage. Dates in `YYYY-MM-DD` order sort correctly. Avoid "final": there is always a later one.

### 10.4 Save as you go, but keep your history
- In a do-file, put a `save` at the end of each stage so the next stage can start from disk.
- Between sessions, **never rely on the data in memory**.
- Back up the project folder (cloud or external drive), and keep code in version control such as GitHub. Data that include personal information must **not** be uploaded to public repositories.

### 10.5 Temporary changes: `preserve` and `restore`
To try something without altering your working dataset:
```stata
preserve
keep if state == "Lagos"
summarize hb
restore                     // back to the full data
```
`preserve` saves a temporary copy, and `restore` brings it back.

### 10.6 Add documentation inside the file
```stata
label data "Synthetic ANC survey, cleaned 2026-10-25"
note: Duplicates removed in 02_clean.do; hb 99 recoded to missing.
notes                         // list the notes stored with the dataset
```
Labels and notes travel with the `.dta` file.

## 11. Saving smaller and richer files

```stata
compress                      // store each variable in the smallest type that holds it without loss
save "data/anc_survey_clean.dta", replace
```
`compress` shrinks the file without losing information. Run it before saving large datasets. Also drop variables you do not need, and label what you keep, so that the next person understands the file.

## 12. Several datasets at once: frames

Stata can hold more than one dataset in memory in separate **frames**, though only one is the active (current) frame. Opening a dataset replaces only the dataset **in the current frame**; datasets in other frames are unaffected. When multiple frames are present, the current frame is shown in the title bar.

A set of frames can be saved as one file with the extension **`.dtas`**:
```stata
frames save "project.dtas"       // save all frames (a frameset)
frames use "project.dtas"        // open a frameset
```
Frames are an advanced topic; for this course, work with one dataset at a time and use `merge` or `append` to combine files. See `help frames intro`.

## 13. Opening and saving in a do-file

A reliable pattern:

```stata
*--------------------------------------------------------------*
* 02_clean.do : clean the ANC survey
*--------------------------------------------------------------*
version 17
clear all
set more off
capture log close
log using "logs/02_clean.log", replace text

* 1. Check the input exists, then open it
confirm file "data/raw/anc_survey.dta"
use "data/raw/anc_survey.dta", clear
describe
duplicates report id                  // are ids unique? (the course data are not: see Lesson 2)
* isid id                            // use once the duplicates are resolved: stops if id is not unique

* 2. ... cleaning steps ...

* 3. Save the result under a NEW name
compress
save "data/clean/anc_survey_clean.dta", replace

log close
```
Why this works: it **confirms** the file exists, **opens** with `clear`, **tests** assumptions, and **saves** under a new name in a different folder. See the [do-file guide](../../lessons/lesson-04-do-files-and-log-files/do-file-guide.md) and the [log file guide](../../lessons/lesson-04-do-files-and-log-files/log-file-guide.md).

## 14. Troubleshooting

| Message or symptom | Cause | Fix |
|--------------------|-------|-----|
| `file ... not found` **r(601)** | Wrong working directory, path, spelling or extension | `pwd`, `dir`, check the name; use quotes |
| `no; dataset in memory has changed since last saved` **r(4)** | Unsaved changes in memory | `save, replace` first or `use ..., clear` |
| `file ... already exists` **r(602)** | Saving over an existing file without `replace` | Add `replace` only if intended |
| `file ... not Stata format` **r(610)** | File saved by a newer Stata, or not a Stata file | Ask the sender for a `saveold` copy; check the file type |
| Opened a file but it is the wrong one | Name confusion, hidden extension, wrong folder | Check `c(filename)` and `describe` |
| Saved file cannot be found | Menu dialog used another folder | `display "`c(filename)'"`; search by name |
| Variables show numbers instead of labels | Opened with `nolabel`, or labels lost in CSV/Excel | Reopen without `nolabel`; re-label (Lesson 3) |
| `no variables defined` on `save` | Nothing in memory | Open or create data first |
| File opens but a colleague cannot open it | Version mismatch | `saveold` copy |
| Out-of-memory type errors on big files | File too large | Use `use varlist ... in ... using ...`; close other programs |
| `r(4)` appears every time you rerun a do-file | Previous run changed the data | Add `, clear` on the load line while developing |
| Changes vanished after restarting Stata | Never saved | Save at the end of every stage |

## 15. Practice exercises F1 to F12

Solutions are in `exercise-solutions/lesson-02/dta-files-practice.do`. Try each first. Run from the repo's top folder (or adjust paths). Use `auto` or the ANC survey as stated.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**F1 🟢 Memory versus disk.** Run `sysuse auto, clear`, then `generate gp100m = 100/mpg`. Use `display c(changed)`. Then `save "auto_gp.dta"`. Run `display c(changed)` again. What changed, and why?

**F2 🟢 Open three ways.** Open `data/anc_survey.dta` by (a) File > Open, (b) File > Recent files, (c) the `use` command. Which leaves a record in a do-file?

**F3 🟢 Quotes and paths.** Create a folder called `my data` inside your project. Save a dataset into it with a path that includes the space. What happens without quotes?

**F4 🟢 The r(4) message.** Reproduce the "dataset in memory has changed" error with `sysuse auto`. Then recover three ways: `save`, `clear`, and cancelling. What does each do to your work?

**F5 🟢 Inspect.** Open `data/anc_survey.dta` and run the five-command habit from section 7. Write down: number of observations, number of variables, and one thing you want to check. (Expected: 1,212 observations and 13 variables. Does the file carry any variable labels?)

**F6 🟡 Look without loading.** Run `describe using "data/anc_survey.dta"` with a clean memory (`clear`). Is anything in memory afterwards?

**F7 🟡 Subsets.** From `data/anc_survey.dta`, load (a) only `id state age hb`, (b) only the first 50 observations, (c) only women recorded as `Lagos` aged 18 or over. Confirm the counts (expected: 50 observations for (b) and 212 for (c)). Why might (c) miss some Lagos records? Run `tabulate state` on the full data to find out.

**F8 🟡 Overwrite protection.** Save the data as `test_copy.dta`. Run the same `save` again. What happens? Fix it. When would you not want to use `replace`?

**F9 🟡 Raw and clean.** Create `data/raw` and `data/clean` in your practice project. Copy `anc_survey.dta` into `raw`. Write a do-file that reads from `raw`, runs `compress`, and saves to `clean` under a new name.

**F10 🟡 Old-format copy.** Save a copy for a colleague with Stata 13 using `saveold`. Then try opening the file again in your Stata. Why do you keep your own master copy in the current format?

**F11 🔴 Preserve and restore.** Using `preserve`, `keep` and `restore`, compute the mean `hb` for Lagos only and then confirm the full dataset is back in memory with the original number of observations.

**F12 🔴 Safe-start do-file.** Write a do-file `open_check.do` that (a) confirms the input file exists, (b) opens it with `clear`, (c) checks that `id` is unique with `isid` (what happens on the raw ANC file, and why?), (d) asserts that the number of observations equals a number you expect, and (e) saves a working copy under a new name. Test it with a wrong file name and a wrong expected count.

## 16. Quick reference card

| Task | Command or menu |
|------|-----------------|
| Open a Stata dataset | `use "file.dta", clear` |
| Open a subset of variables | `use var1 var2 using "file.dta", clear` |
| Open selected observations | `use if cond using "file.dta", clear` or `use in 1/100 using ...` |
| Look inside a file | `describe using "file.dta"` |
| Example data shipped with Stata | `sysuse auto, clear`, `sysuse dir` |
| Manual datasets from the web | `webuse name, clear` |
| Menu: open / subset / recent | **File > Open...** / **Open data subset...** / **Recent files** |
| Save under a new name | `save "new.dta"` |
| Overwrite | `save "file.dta", replace` or `save, replace` |
| Save for older Stata | `saveold "file.dta", version(13) replace` |
| Has the data changed? | `display c(changed)` |
| Current file name | `display "`c(filename)'"` |
| Shrink storage | `compress` |
| Safe look | `browse` (browse mode) |
| Temporary changes | `preserve` ... `restore` |
| Save a set of frames | `frames save "x.dtas"` / `frames use "x.dtas"` |
| Discard and clear | `clear`, or `use ..., clear` |

## 17. Facilitator notes

**Timing (75-minute session):** 10 min memory versus disk and the .dta format (sections 1 to 2), 15 min opening (3 to 5), 10 min r(4) and inspection (6 to 7), 15 min saving and versions (8 to 9), 25 min exercises F1 to F9. F10 to F12 are take-home.

**Before the session**
- Participants should have a project folder (see the [working directory guide](../lesson-01-getting-started/working-directory-guide.md)) and a copy of this repo's `data/` folder.
- Find out which Stata versions are on the training PCs.
- If the room has no internet, skip `webuse`.

**Common stumbling blocks**
- Believing that data are saved automatically.
- Using `replace` on the raw file "just once".
- Using `clear` reflexively and throwing away work.
- File > Save as dialog opening in an unexpected folder.
- Not looking at the data after opening.
- Sending a file to a colleague on an older Stata.

**Teaching tips**
- Run the "lost work" demonstration: make a change, deliberately close Stata without saving, and reopen. Then do the same with a do-file, and show how little is lost.
- Pair exercise: swap USB sticks or shared folders with a neighbour and try to open each other's `.dta` files; discuss version problems.
- Ask: "Which file in this folder is the raw one? Which is the latest? How can you tell?" If the answer needs guessing, the naming scheme needs work.

**Assessment prompt (5 minutes):** "A colleague writes `use rawdata.dta, clear` and, after cleaning, `save rawdata.dta, replace`. What is wrong, and what should they do instead?" Expected: the raw file is overwritten and the original cannot be recovered; read from `raw/` and save the cleaned data under a new name in `clean/`.

**Note on versions.** This guide follows the Windows edition of the Getting Started manual and the current reference entries. Menu names and the supported `saveold` versions differ across Stata releases and systems. Check `help use`, `help save` and `help saveold` in your own installation. Use only the synthetic course data when sharing logs or screenshots.
