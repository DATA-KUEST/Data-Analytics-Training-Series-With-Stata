# Learning Notes: The Working Directory in Stata

**Part of:** Lesson 1, Getting Started (revisited in Lesson 4, Do-files and Log Files)  |  **Read and practise:** about 60 minutes  |  **Dataset:** `auto` (built into Stata) and the ANC survey in `data/`

Almost every "file not found" error a beginner meets comes from one cause: Stata is looking in a different folder from the one the analyst thinks it is. This guide explains what the **working directory** is, how to see and change it, how to write file paths that work on any computer, and how to organise a project folder so your analysis can be rerun by a colleague.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC): chapter 2 (the working directory), chapter 8 (saving a file into the working directory), appendix B (start-in folder, `profile.do`, double-click launching, batch mode) and appendix C (network installs). The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Explain what the working directory is and what it affects (and does not affect)
- Find it with `pwd` and the status bar, and change it with `cd` or the menu
- Write file paths correctly, including paths with spaces, and use relative paths
- List, create and check folders and files from inside Stata
- Set up a standard project folder and a header that makes a do-file portable
- Control where Stata starts, and understand what happens when you double-click a file
- Diagnose and fix path-related errors

## Contents
1. [What is the working directory?](#1-what-is-the-working-directory)
2. [Seeing where you are](#2-seeing-where-you-are)
3. [Changing the working directory](#3-changing-the-working-directory)
4. [What the working directory does and does not control](#4-what-the-working-directory-does-and-does-not-control)
5. [File paths: absolute, relative and quoted](#5-file-paths-absolute-relative-and-quoted)
6. [Looking around and managing folders from Stata](#6-looking-around-and-managing-folders-from-stata)
7. [Organising a project folder](#7-organising-a-project-folder)
8. [The portable do-file header](#8-the-portable-do-file-header)
9. [Where Stata starts: shortcuts, double-clicking and `profile.do`](#9-where-stata-starts-shortcuts-double-clicking-and-profiledo)
10. [Shared computers, networks and batch jobs](#10-shared-computers-networks-and-batch-jobs)
11. [Other folders Stata uses (not your working directory)](#11-other-folders-stata-uses-not-your-working-directory)
12. [Troubleshooting path problems](#12-troubleshooting-path-problems)
13. [Good habits checklist](#13-good-habits-checklist)
14. [Practice exercises W1 to W12](#14-practice-exercises-w1-to-w12)
15. [Quick reference card](#15-quick-reference-card)
16. [Facilitator notes](#16-facilitator-notes)

---

## 1. What is the working directory?

The **working directory** (also called the *current directory*) is the folder Stata treats as "here". When you give Stata a file name **without a full path**, Stata looks for it, or creates it, in the working directory.

```stata
save myfile, replace        // saved into the working directory
use anc_survey              // looked for in the working directory
graph export fig1.png       // written to the working directory
log using mylog.log         // written to the working directory
```

Think of it as the folder you are "standing in" in a file explorer. Typing just a file name means "the file in front of me". Typing a full path means "go to that exact address".

The working directory is set when Stata starts (see section 9) and stays the same until you change it or close Stata. It is **not** saved with your dataset or do-file. Two colleagues running the same do-file can therefore be "standing" in different folders, which is the root of most path errors.

## 2. Seeing where you are

There are three ways to see the working directory.

| Method | How | Notes |
|--------|-----|-------|
| **Status bar** | Look at the bottom-left of the main Stata window | Always visible; Stata displays it so you can tell where files will be saved |
| **`pwd`** | Type `pwd` in the Command window | Prints the path in the Results window |
| **`c(pwd)`** | `display c(pwd)` | Returns the path as text, so you can store it in a macro |

```stata
pwd
display "I am working in: `c(pwd)'"
local here "`c(pwd)'"
```

`pwd` stands for "print working directory", a name borrowed from Unix. Make `pwd` the **first command you type** whenever a file will not open.

## 3. Changing the working directory

### With a command: `cd`
```stata
cd "C:/Users/Amina/Documents/dataquest/lesson01"
cd                                   // with no argument, shows the current directory
cd ..                                // go up one folder
cd "../data"                         // go up one folder, then into data
```
`cd` stands for "change directory". After a successful `cd`, Stata prints the new directory and the status bar updates.

### With the menu
**File > Change working directory...** opens a folder picker. This is handy while exploring. It runs a `cd` for you, and the command appears in the Results and History windows. **Copy that command into your do-file** instead of relying on clicking.

### Practical advice
- Use `cd` **once per project**, near the top of a master do-file or at the start of your session, not scattered through the analysis.
- If the folder name contains spaces, put the path in **double quotes**.
- If you mistype a folder, Stata reports that it is unable to change to it and your working directory stays where it was. Check with `pwd`.

## 4. What the working directory does and does not control

This is the point that confuses many professionals, so read it carefully.

| Action | Uses the working directory? |
|--------|-----------------------------|
| Commands with a bare file name: `save file`, `use file`, `graph export`, `log using`, `import delimited file.csv` | **Yes** |
| Menu actions such as **File > Open...** and **File > Save as...** | **No.** They behave independently; the dialog may open in whatever folder you last used |
| Do-file Editor **Save** button | Opens a dialog; check the folder shown before saving |

The Getting Started manual states this directly: the working directory is where graphs and datasets are saved when you type commands such as `save filename`, and it does not change the behaviour of menu-driven file actions like File > Save or File > Open.

**Lesson:** if you point-and-click to save a file and later cannot find it, it is probably not in the working directory. Typing the command with an explicit path removes the doubt, and also leaves a record in your do-file.

## 5. File paths: absolute, relative and quoted

### 5.1 Absolute paths
A full address from the top of the drive:
```stata
use "C:/Users/Amina/Documents/dataquest/data/anc_survey.dta", clear
```
This works only on the computer that has that exact folder.

### 5.2 Relative paths
An address measured from the working directory:
```stata
cd "C:/Users/Amina/Documents/dataquest"
use "data/anc_survey.dta", clear      // folder data inside the working directory
use "../shared/other.dta", clear      // one level up, then into shared
```
| Symbol | Meaning |
|--------|---------|
| `data/file.dta` | `data` folder inside the working directory |
| `./file.dta` | the working directory itself |
| `../file.dta` | the folder one level above |

Relative paths make a project **portable**: move the whole project folder and, as long as you `cd` to its top once, everything still works.

### 5.3 Use forward slashes
Windows normally writes paths with backslashes (`C:\Users\...`), and Stata accepts those, but **forward slashes (`/`) work on Windows, macOS and Linux**. Use them everywhere. Backslashes can also clash with Stata's macro syntax in some situations.

```stata
* Works on every operating system
use "data/anc_survey.dta", clear
```

### 5.4 Quote every path
Spaces in a path break the command unless the path is in double quotes.

```stata
use C:/Users/Amina/My Documents/data.dta     // fails: Stata reads this as several words
use "C:/Users/Amina/My Documents/data.dta"   // works
```
Quotes cost nothing when there are no spaces, so quote **all** paths.

### 5.5 Avoid trouble in folder names
- Avoid spaces, accents and symbols such as `&`, `#`, `%` in project folder and file names. `anc_survey_clean.dta` is better than `ANC Survey (final) v2.dta`.
- Keep paths reasonably short.
- Use lower-case names with underscores or hyphens. File names are case-sensitive on macOS and Linux, so `Data` and `data` are different folders there.

### 5.6 Extensions
If you omit the extension, Stata assumes the command's usual type (`.dta` for `use` and `save`, `.do` for `do`, `.smcl` for `log using`). Write the extension anyway for CSV, Excel, log and graph files to avoid ambiguity.

## 6. Looking around and managing folders from Stata

| Command | What it does | Example |
|---------|--------------|---------|
| `dir` (or `ls`) | Lists files in the working directory | `dir`, `dir *.dta`, `dir "data/"` |
| `mkdir` | Creates a folder | `mkdir "output"` |
| `copy` | Copies a file | `copy "data/a.csv" "backup/a.csv"` |
| `erase` (or `rm`) | Deletes a file permanently | `erase "temp.dta"` |
| `type` | Shows a text file in the Results window | `type "data/README.md"` |
| `confirm file` | Stops with an error if a file does not exist | `confirm file "data/anc_survey.dta"` |
| `capture` | Prefix that suppresses an error so the do-file carries on | `capture mkdir "output"` |

```stata
dir *.csv                          // which CSV files are here?
capture mkdir "output"             // create folder if it does not already exist
confirm file "anc_survey.csv"      // stops with a clear error if missing
```

**Safety notes**
- `erase` does not use the recycle bin. Use it only on files your do-file created itself, such as temporary files, never on raw data.
- `mkdir` creates one level at a time, so create `output` before `output/figures`.
- `capture` hides **every** error from the command after it, so use it only where failure is harmless (such as a folder that already exists).

## 7. Organising a project folder

Your working directory should be the **top of a project folder** with a predictable structure. A suggested layout for this course:

```
dataquest-project/
├── data/
│   ├── raw/          ← original files, never edited
│   └── clean/        ← datasets your do-files create
├── do/               ← do-files (00_master.do, 01_import.do, ...)
├── logs/             ← log files
└── output/
    ├── tables/
    └── figures/
```

Principles:
1. **Raw data is read-only.** Never save over it. Do-files read from `data/raw` and write to `data/clean`.
2. **Everything is created by code.** If a file in `clean/`, `tables/` or `figures/` can be deleted and regenerated by running the do-files, your project is reproducible.
3. **Numbered do-files** run in order and tell the story: `01_import.do`, `02_clean.do`, `03_analysis.do`.
4. **One master do-file** (`00_master.do`) sets the working directory and runs the others (section 8).
5. **Same layout for every project** so colleagues always know where to look.

You can create the whole structure from Stata:

```stata
cd "C:/Users/Amina/Documents/dataquest-project"   // folder must already exist
foreach d in data do logs output {
    capture mkdir "`d'"
}
foreach d in raw clean {
    capture mkdir "data/`d'"
}
foreach d in tables figures {
    capture mkdir "output/`d'"
}
```

## 8. The portable do-file header

A standard header at the top of your master do-file means the whole project runs on any computer after changing **one line**.

```stata
*------------------------------------------------------------*
* 00_master.do
* Project : DATAQUEST ANC survey analysis
* Author  : <your name>        Date: <date>
*------------------------------------------------------------*
clear all
set more off

* ---- EDIT THIS ONE LINE for each computer --------------------
global root "C:/Users/Amina/Documents/dataquest-project"
* ----------------------------------------------------------------

* Everything below uses $root, so nothing else needs editing
cd "$root"
global raw    "$root/data/raw"
global clean  "$root/data/clean"
global logs   "$root/logs"
global tables "$root/output/tables"
global figs   "$root/output/figures"

* Check that the folder structure is what we expect
confirm file "$raw/anc_survey.csv"

* Start a log
log using "$logs/master.log", replace text

* Run the project
do "$root/do/01_import.do"
do "$root/do/02_clean.do"
do "$root/do/03_analysis.do"

log close
```

Inside `01_import.do`:
```stata
import delimited "$raw/anc_survey.csv", clear
save "$clean/anc_survey.dta", replace
```

**Notes**
- `global root "..."` creates a **global macro**. You refer to it as `$root`. Globals persist for the whole Stata session, which is why the later do-files can use them.
- Wrap paths that contain macros in double quotes: `"$raw/anc_survey.csv"`.
- To avoid editing the path by hand on each machine, you can pick the root by user name:

```stata
if "`c(username)'" == "amina" {
    global root "C:/Users/Amina/Documents/dataquest-project"
}
else if "`c(username)'" == "tunde" {
    global root "/Users/tunde/dataquest-project"
}
else {
    display as error "Unknown user: add your root folder to 00_master.do"
    exit 198
}
```
- `c(os)` returns `Windows`, `MacOSX` or `Unix`, if you need different behaviour per system.
- Individual do-files, run alone, will fail if `$root` is not defined. That is a feature: it forces you to start from the master do-file. The full do-file and log file lessons are in the [course roadmap](../../ROADMAP.md) (Lesson 4).

## 9. Where Stata starts: shortcuts, double-clicking and `profile.do`

### 9.1 The "Start in" folder (Windows)
When you launch Stata from a shortcut, the shortcut's **Properties** sheet decides the first working directory.

1. Right-click the Stata shortcut and choose **Properties**.
2. On the **Shortcut** tab, find **Target** (the command that launches Stata) and **Start in** (the folder Stata starts in).
3. To change the default working directory, delete the parameter `/UseRegistryStartin` from the Target field if it is present, then type your folder into **Start in** and click OK.

This lets you create **one shortcut per project**, each starting in its own folder.

### 9.2 Double-clicking files
Double-clicking a Stata file (`.dta`, `.do` or `.gph`) starts a new Stata session whose working directory is **the folder containing that file**:
- a `.dta` opens as data,
- a `.do` opens in the Do-file Editor,
- a `.gph` graph opens in a graph window.

If you right-click a do-file you also see **Execute (do)** and **Execute quietly (run)**, which run it in a new Stata session. On Windows 11 you may need to choose *Show more options* first. To open a file in your *existing* session, drag it onto the main Stata window.

Practical consequence: double-clicking `01_import.do` inside `do/` makes `do/` the working directory, so relative paths like `data/raw/...` will fail. Start from the master do-file and use `$root`.

### 9.3 `profile.do`: commands that run at every start-up
If Stata finds a file named `profile.do` when it starts, it runs it automatically. Stata searches the folder where Stata is installed, the current directory, the path, the home directory (typically `C:\Users\username`), and the ado-path, in that order, and the manual recommends putting `profile.do` in your **home directory**.

A very simple example that sets a default working folder each time Stata starts:
```stata
* profile.do
cd "C:/Users/Amina/Documents/dataquest-project"
```
Because Stata also looks in the folder a shortcut starts in, you can keep a different `profile.do` for each project by giving each project its own shortcut. The manual's own example uses `profile.do` to start a time-stamped log of every session. `profile.do` is an ordinary do-file that Stata happens to run for you.

> Use `profile.do` sparingly. If it hides settings your do-files depend on, a colleague who lacks that file will get different results. Anything essential to the analysis belongs in the project's master do-file.

System administrators can use a similar file, `sysprofile.do`, which Stata runs first.

## 10. Shared computers, networks and batch jobs

**Training rooms and shared PCs.** The manual suggests that when a workstation is used by more than one person, the shortcut's **Start in** field can be set to the Windows environment variable `%HOMEDRIVE%%HOMEPATH%`, so each user starts in their own home directory. For network installations, set Start in to a local drive where users have write access, because Stata saves datasets and graphs to the working directory and needs permission to write there.

**Batch mode.** Stata can run a do-file without the interface from the Windows command prompt. In the manual's method, you first `cd` to the folder where you want the log file to appear, then run Stata with the `/e` option and the do-file name. Other options include `/b` (batch mode, plain-text log), `/q` (suppress the logo) and `/s` (SMCL log). Scheduled jobs using Windows Task Scheduler work the same way and the **Start in** field is where the log is saved. Here the working directory decides where the log file lands, a good reason to keep it deliberate.

**Cloud or remote sessions.** Wherever Stata runs, `pwd` tells you the truth. Paths on your laptop do not exist on a server, which is another reason to use relative paths and a single `$root` line.

## 11. Other folders Stata uses (not your working directory)

The working directory is only one of several folders Stata knows about. Do not confuse them.

| Folder | Purpose | See it with |
|--------|---------|-------------|
| **Working directory** | Where *your* files are read and saved by default | `pwd` |
| **STATA / BASE** | Where the official Stata files and commands are installed | `sysdir` |
| **PLUS** | Where `ssc install` and `net install` put downloaded commands | `sysdir` |
| **PERSONAL** | Where you can store your own ado-files | `sysdir`, `personal` |
| **TEMP** | Temporary files Stata creates during a session | `display c(tmpdir)` |

Run `sysdir` to list them. Never save your analysis files into the installation folders. Keep them in your project folder.

## 12. Troubleshooting path problems

| Message or symptom | Likely cause | Fix |
|--------------------|--------------|-----|
| `file anc_survey.dta not found` **r(601)** | Stata is not in the folder you think, or the name or extension is wrong | Run `pwd` and `dir`; `cd` to the correct folder, or use a full or relative path |
| `invalid syntax` or `invalid name` on a long path | Path contains spaces and is not quoted | Wrap in double quotes |
| Saved file is "missing" | Used File > Save or a dialog that opened in another folder | Search for the file name; next time use `save "path/file", replace` |
| `file ... already exists` **r(602)** | Saving over an existing file without `replace` | Add `, replace` only when overwriting is intended |
| Do-file works on my PC, fails on yours | Absolute paths or a different working directory | Use the master do-file with `$root` |
| `unable to change to ...` from `cd` | Folder does not exist, is mistyped, or no permission | Check spelling; confirm with a file explorer; use forward slashes |
| Log file or graph appears in the wrong folder | Working directory changed earlier in the session | Use explicit paths such as `"$logs/..."` and `"$figs/..."` |
| Double-clicked do-file cannot find data | Working directory became the do-file's folder | Run from the master do-file |
| Works until you restart Stata | Relied on a `cd` typed interactively or on a global defined in another session | Put `cd` and `global` in the master do-file |

**Debugging routine (five steps):**
1. `pwd`: where am I?
2. `dir`: is the file here?
3. Check spelling, extension and case.
4. Check quotes and slashes.
5. Try the full absolute path once. If that works, the problem is the working directory, not the file.

## 13. Good habits checklist

- [ ] My project folder has `data/raw`, `data/clean`, `do`, `logs`, `output`
- [ ] Raw data is never overwritten
- [ ] There is one master do-file that sets `$root` and runs everything
- [ ] I changed directory with `cd` in code, not only by clicking
- [ ] Every path is in double quotes with forward slashes
- [ ] No spaces or special characters in folder and file names
- [ ] I use relative paths or global macros, not `C:/Users/...` scattered through the code
- [ ] I check `pwd` first when a file is not found
- [ ] `save` has `, replace` only where overwriting is intended
- [ ] I can delete `data/clean`, `logs` and `output` and recreate them by running the master do-file

## 14. Practice exercises W1 to W12

Create a do-file named `W-practice.do` and add each answer as you go. Solutions are in `exercise-solutions/lesson-01/working-directory-practice.do`. Try each one first.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**W1 🟢 Where am I?** Open Stata and read the working directory from the status bar. Then show it with `pwd`. Do both agree?

**W2 🟢 Store it.** Use `c(pwd)` to display the sentence `My working directory is: ...` in the Results window.

**W3 🟢 Make a project.** In a file explorer, create a folder named `dataquest_practice` somewhere you can write to (avoid spaces in the name). Use `cd` to move Stata into it, then confirm with `pwd`.

**W4 🟢 Build the structure.** From Stata, create the folders `data`, `do`, `logs` and `output` inside `dataquest_practice`, then `data/raw`, `data/clean`, `output/tables` and `output/figures`. Use `capture mkdir`. Run the code twice. Why does it not fail the second time?

**W5 🟡 Save with a bare name.** Run `sysuse auto, clear` and then `save auto_copy, replace`. Use `dir *.dta` to find it. In which folder is it?

**W6 🟡 The menu trap.** Use **File > Save as...** and save the data as `auto_menu.dta`, but let the dialog choose its own folder. Is the file in your working directory? How do you check? What would you type next time to be certain?

**W7 🟡 Quotes.** Make a folder named `my data` (with a space) inside the project. Try `cd my data`. Read the error. Then fix the command with quotes. Finally, `cd ..` back out and confirm with `pwd`.

**W8 🟡 Relative paths.** From the project folder, save `auto` into `data/raw` as `auto_raw.dta` using a relative path. Then `cd` into `data` and open it again using a relative path *from there*. Then use `cd` to return to the project root with `..`.

**W9 🟡 Confirm before use.** Write two lines that stop the do-file with a clear error if `data/raw/auto_raw.dta` does not exist, and then load it. Test it by temporarily renaming the file.

**W10 🔴 Globals.** Write a header that defines `global root`, `$raw`, `$clean`, `$logs`, `$figs`. Using only those globals, load `auto_raw.dta`, create a variable `price_k = price/1000`, save as `auto_clean.dta` in the clean folder, and export a histogram of `price_k` to the figures folder.

**W11 🔴 Make it portable.** Add the `c(username)` switch from section 8 so the same header works for two users with different root folders. Add an `else` branch that stops with an error message.

**W12 🔴 Rerun from scratch.** Delete `data/clean`, `logs` and `output` (manually, in a file explorer), then run your master do-file. Does it rebuild everything? What had to change so it could?

**Using the course data (optional follow-on):** copy `anc_survey.csv` from this repo's `data/` folder into your `data/raw` folder. Write `01_import.do` that imports it with `$raw`, runs `describe`, and saves `anc_survey.dta` in `$clean`.

## 15. Quick reference card

| Task | Command |
|------|---------|
| Show working directory | `pwd` |
| Change directory | `cd "path"` |
| Go up one level | `cd ..` |
| List files | `dir` / `ls` |
| Make a folder | `mkdir "name"` |
| Does a file exist? | `confirm file "path"` |
| Store working directory in a macro | `local here "`c(pwd)'"` |
| Define a project root | `global root "path"` |
| Use it | `"$root/data/file.dta"` |
| Show Stata's system folders | `sysdir` |
| Run another do-file | `do "path/file.do"` |
| Start a log in the logs folder | `log using "$logs/name.log", replace text` |
| Menu | **File > Change working directory...** |

**Rules of thumb:** quote every path, use forward slashes, keep raw data untouched, one `cd` per project, and `pwd` first when anything is "not found".

## 16. Facilitator notes

**Timing (90-minute session):** 10 min concepts (sections 1 to 4), 15 min paths and commands (5 and 6), 15 min project structure and header (7 and 8), 35 min exercises W1 to W9 in pairs, 15 min W10 to W12 demo and discussion.

**Common stumbling blocks**
- Participants assume File > Open and the working directory are linked. Demonstrate W6 live.
- Shared training PCs: participants may not have write permission in the default folder. Ask them to create their practice folder on the Desktop or in Documents before the session.
- Backslash habits from Windows Explorer. Show that forward slashes work everywhere.
- Participants copy a master do-file from a colleague without changing `$root`. Make "edit one line" part of the lesson.

**Teaching tips**
- Run W7 as a live "break it, read the error, fix it" exercise.
- Ask participants to swap project folders with a neighbour and run the neighbour's master do-file after editing only the `$root` line. Success proves portability.
- Revisit this guide in Lesson 4 when log files and do-files are covered in depth.

**Assessment prompt (5 minutes):** "A colleague emails you a do-file containing `use "C:/Users/Bola/Desktop/data.dta"`. List three problems and fix each."
Expected answers: absolute path tied to one machine; no `, clear` (if data are already loaded, the command fails); no project structure or master do-file; no check that the file exists.

**Note on versions.** The Windows screens and shortcuts described in sections 9 and 10 follow the Getting Started manual for Windows (the edition supplied shows Stata 19 paths such as `C:\Program Files\Stata19\`). Folder names, menu wording and shortcut steps differ slightly between versions and between Windows, macOS and Linux; the commands in sections 1 to 8 work the same everywhere.

