# Learning Notes: Do-files and the Do-file Editor

**Part of:** Lesson 4, Do-files and Log Files (the basics are used from Lesson 1 onward)  |  **Read and practise:** about 90 minutes  |  **Dataset:** `auto` (built into Stata) and the ANC survey in `data/`

If you remember one habit from this whole course, make it this one: **write your analysis in a do-file**. A do-file is a plain-text list of Stata commands. Run it today, run it next year, give it to a colleague or a reviewer, and you get the same results. That is what *reproducible analysis* means in practice.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 13 ("Using the Do-file Editor—automating Stata"), and checked against the *Stata User's Guide* chapter 16 ("Do-files") and the `do` and comments entries on stata.com. The explanations, examples, template and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Explain what a do-file is and why professionals use them
- Use the Do-file Editor: toolbar, menus, bookmarks, navigator, code folding, autocomplete
- Write, save and run a do-file, and run only part of it
- Use all four comment styles and break long commands over several lines
- Read an error, fix it, and know what happens when a do-file stops
- Choose between `do`, `run` and `include`
- Turn an interactive session into a do-file
- Pass arguments to a do-file and call one do-file from another
- Structure a project with a master do-file and a standard header
- Follow a team style guide so that anyone can read your code

## Contents
1. [What is a do-file?](#1-what-is-a-do-file)
2. [Why use do-files?](#2-why-use-do-files)
3. [A tour of the Do-file Editor](#3-a-tour-of-the-do-file-editor)
4. [Your first do-file: a worked example with deliberate mistakes](#4-your-first-do-file-a-worked-example-with-deliberate-mistakes)
5. [The anatomy of a good do-file](#5-the-anatomy-of-a-good-do-file)
6. [Comments and long lines](#6-comments-and-long-lines)
7. [Running a do-file: do, run, include and partial runs](#7-running-a-do-file-do-run-include-and-partial-runs)
8. [Errors and debugging](#8-errors-and-debugging)
9. [Arguments, nested do-files and the master do-file](#9-arguments-nested-do-files-and-the-master-do-file)
10. [From interactive work to a do-file](#10-from-interactive-work-to-a-do-file)
11. [Navigating long do-files](#11-navigating-long-do-files)
12. [Other Do-file Editor features](#12-other-do-file-editor-features)
13. [A team style guide](#13-a-team-style-guide)
14. [Running do-files without the interface (batch mode)](#14-running-do-files-without-the-interface-batch-mode)
15. [Troubleshooting](#15-troubleshooting)
16. [Practice exercises DO1 to DO12](#16-practice-exercises-do1-to-do12)
17. [Quick reference card](#17-quick-reference-card)
18. [Facilitator notes](#18-facilitator-notes)

---

## 1. What is a do-file?

A **do-file** is a text file, usually ending in `.do`, containing Stata commands. When you tell Stata to run it, Stata executes the commands in order, exactly as if you had typed them one by one. In other software the same thing is called a *script* or a *batch file*.

```stata
* myjob.do
use "data/anc_survey.dta", clear
tabulate state
summarize anc_visits
```
Run it by typing:
```stata
do myjob
```
If you leave off the extension, Stata assumes `.do`.

Do-files are plain text, so you can write them in Stata's Do-file Editor or in any text editor. Do not use a word processor, which adds hidden formatting.

## 2. Why use do-files?

| Without do-files | With do-files |
|------------------|---------------|
| Results come from clicking and typing; nobody can tell how | Every step is written down |
| A mistake at step 3 means redoing steps 4 to 30 by hand | Fix one line and rerun |
| A colleague cannot repeat your analysis | They run the same file |
| Reviewers ask "how did you clean this?" and you cannot say | The cleaning code is the answer |
| Raw data gets overwritten "just this once" | Raw data stays untouched; code creates clean copies |
| New data arrives and the work starts over | Rerun the file on the new data |

The User's Guide recommends do-files for all research projects: they make your work reproducible, ease debugging, and let you change one step without redoing everything interactively.

**Interactive versus do-file work.** Use the Command window to *explore* ("what does this variable look like?"). Once a command is worth keeping, put it in a do-file. A good habit: try it in the Command window, then paste the version that worked into your do-file.

## 3. A tour of the Do-file Editor

Open the Do-file Editor by clicking the **Do-file Editor** button on the main toolbar or by typing `doedit` in the Command window.

### 3.1 The toolbar (15 buttons)
| Button | Purpose |
|--------|---------|
| **New** | New do-file in a new tab |
| **Open** | Open a do-file from disk in a new tab |
| **Save** | Save the current file |
| **Print** | Print the contents |
| **Find** | Open the Find dialog |
| **Cut / Copy / Paste** | The usual clipboard actions |
| **Undo / Redo** | Undo the last change; undo the last undo |
| **Toggle bookmark** | Turn the bookmark on the current line on or off |
| **Previous bookmark / Next bookmark** | Jump between bookmarks |
| **Show file in Viewer** | Show the file in a Viewer; useful for files with SMCL tags such as logs and help files |
| **Execute (do)** | Run the do-file, showing all commands and output. If text is highlighted, it becomes **Execute selection (do)** and runs only the selected lines |

Hover over any button for a tooltip. The Execute button is often called the **Do button**.

### 3.2 Menus at a glance
| Menu | Useful items |
|------|--------------|
| **File** | New > Do-file, New > Window, New > Document from template, New > Project...; Open; Save; Save as...; Print |
| **Edit** | Undo, Redo, Cut, Copy, Paste, Delete, Find; Insert file...; Select line; Delete line; Find > Go to line...; Match bracket; Balance brackets; **Advanced** submenu (below) |
| **View** | Zoom, Show whitespace, Code folding (Toggle, Fold all, Unfold all), Show Navigator |
| **Tools** | Execute (do), Execute (do) nostop, Execute (do) from top, Execute (do) to bottom, Execute (do) line, Execute quietly (run), Execute (include), Show file in Viewer |
| **Language** | Choose Stata, Markdown, Python or Java syntax highlighting |

**Edit > Advanced** is a programmer's toolbox:

| Item | Effect |
|------|--------|
| Shift right / Shift left | Indent / unindent the selection by one tab |
| Shift line up / down | Move the current line |
| Re-indent | Indent the selection according to its nesting in blocks and programs |
| Fold selection | Turn selected code into a foldable block with indentation and curly braces |
| **Toggle comment** | Toggle `//` comments at the start of the selected lines |
| **Add / Remove block comment** | Put `/*` before and `*/` after the selection, or undo it |
| Make selection uppercase / lowercase | Change case |
| Complete word | Complete the current word from words already in the file |
| Convert to UTF-8... | Convert encoding (section 12) |
| Convert line endings (macOS/Unix or Windows) | Fix line endings when files move between systems |
| Convert tabs to spaces, leading spaces to tabs, all spaces to tabs | Normalise whitespace |
| Convert Unicode spaces and curly quotes to ASCII | Fix text pasted from Word or the web |

**Tip:** click the left margin beside a line number to select the whole line, including its end-of-line characters. Drag in the line-number column to select a range of lines.

### 3.3 Tabs and windows
**New > Do-file** opens a new tab in the current editor window; **New > Window** opens a new editor window. Having your master do-file and the one you are working on in separate tabs is a good way to work.

## 4. Your first do-file: a worked example with deliberate mistakes

This follows the Getting Started manual's own example, in which you purposely make common mistakes and see the solutions. Work along at your computer.

### 4.1 Type this into a new Do-file Editor tab
```stata
* an example do-file
sysuse auto
generate gp100m = 100/mpg
label var gp100m "Gallons per 100 miles"
regress gp100m weight foreing
```
Notice that the text changes colour as you type. That is **syntax highlighting**: commands, comments, strings and other elements get different colours.

Also notice: `foreing` is misspelled on purpose.

### 4.2 Mistake 1: a misspelled variable
Click the **Do** button. The Results window shows something like:

```
. do C:\Users\...\Temp\STD08000000.tmp
. * an example do-file
. sysuse auto
(1978 automobile data)
. generate gp100m = 100/mpg
. label var gp100m "Gallons per 100 miles"
. regress gp100m weight foreing
variable foreing not found
r(111);
end of do-file
```
What happened:
- Stata saved your unsaved commands to a temporary file and ran it with a `do` command.
- The first three commands worked.
- The fourth failed with **r(111)** ("variable not found"). **A do-file stops at the first error.** Everything after it is skipped.

Fix the spelling to `foreign` and click **Do** again.

### 4.3 Mistake 2: data already in memory
Now the failure is on the first command:
```
. sysuse auto
no; dataset in memory has changed since last saved
r(4);
```
Stata protects you from throwing away changed data without warning. Your earlier run created `gp100m`, so the data in memory differ from the file. You have two choices:

1. Start the do-file with `clear` (or add the `clear` option to the loading command): convenient but "dangerous because it defeats Stata's protection against throwing away changes without warning".
2. Type `clear` in the Command window before each run: safe but aggravating while building a complicated do-file.

The manual's advice is worth memorising:
> Automatically clear Stata's memory while debugging the do-file. Once the do-file is in its final form, decide the context in which it will be used. If it will be used in a highly automated environment, the do-file should still automatically clear memory. If it will be used rarely, do not clear memory.

Add `, clear` to the load command:
```stata
* an example do-file
sysuse auto, clear
generate gp100m = 100/mpg
label var gp100m "Gallons per 100 miles"
regress gp100m weight foreign
```
Click **Do**. The regression table appears. Save the file (**File > Save as...**) as `gp100m.do` in your project's `do/` folder (see the [working directory guide](../lesson-01-getting-started/working-directory-guide.md)). From now on you can rerun it by typing `do gp100m` from the folder it is in, or `do "path/to/gp100m.do"` from anywhere.

### 4.4 What you learned
| Observation | Lesson |
|-------------|--------|
| Do-files stop at the first error | Read the *last* lines of output first |
| `r(111)` | Variable (or similar) not found: check spelling |
| `r(4)` | Data in memory have changed: clear on purpose |
| Re-running changes the state | A do-file should work from a clean start, every time |

## 5. The anatomy of a good do-file

A readable do-file has a header, setup commands, and then logically ordered sections.

```stata
*------------------------------------------------------------------*
* 01_import_explore.do
* Project : DATAQUEST ANC survey
* Purpose : Import the ANC survey and describe it
* Author  : <your name>                       Date: <date>
* Input   : data/anc_survey.csv
* Output  : data/anc_survey.dta, logs/01_import.log
*------------------------------------------------------------------*

version 17              // use the release you teach with
clear all
set more off

* ---- 1. Paths ---------------------------------------------------
* (run from the project root; see the working directory guide)
local raw "data"

* ---- 2. Log -----------------------------------------------------
capture mkdir "logs"
log using "logs/01_import.log", replace text

* ---- 3. Import --------------------------------------------------
import delimited "`raw'/anc_survey.csv", clear
describe

* ---- 4. Explore -------------------------------------------------
summarize
tabulate state

* ---- 5. Save ----------------------------------------------------
save "data/anc_survey_working.dta", replace

log close
```
A ready-made version is in [`templates/do-file-template.do`](../../templates/do-file-template.do).

### Line-by-line notes
| Line | Why |
|------|-----|
| `version 17` | Declares the Stata release the code was written for, so the file keeps working as Stata changes. Stata restores the previous version setting when the do-file ends. Use the version you are teaching with; recent releases allow e.g. `version 19` |
| `clear all` | Starts from an empty session (clears data, macros and more). Be careful: it also clears things you set up before running |
| `set more off` | Stops Stata pausing with `--more--` when the screen fills. It is restored when the do-file ends |
| `log using ... , replace` | Records output; `replace` lets you rerun the file. Without it, an existing log makes the do-file stop |
| `log close` | Closes the log at the end |

The master do-file in the [working directory guide](../lesson-01-getting-started/working-directory-guide.md) sets `$root` and calls these step files in order.

## 6. Comments and long lines

### 6.1 Four comment styles
| Style | Rule | Example |
|-------|------|---------|
| `*` | Must start the line. Works interactively too | `* Calculate the BMI` |
| `//` | Starts a line or follows code; **must be preceded by at least one space** | `generate bmi = wt/ht^2   // kg per m squared` |
| `/* ... */` | Can go anywhere, even in the middle of a line, and can span lines | `/* old code below */` |
| `///` | Treats the rest of the line as a comment **and joins the next line to this one** (line continuation) | see below |

Comments with `//`, `///` and `/* */` work only in do-files (and ado-files), not when typed in the Command window.

```stata
* This works
generate bmi = weight/height^2     // space before the double slash

* This does NOT work: no space before //
generate bmi = weight/height^2// comment
```

**What to comment:** *why* you did something, not *what* the code does. `* Exclude 12 duplicate records found in Lesson 2` is useful; `* drop observations` is not.

**Disable code temporarily:** select lines and use **Edit > Advanced > Toggle comment** (adds `//`) or **Add block comment** (`/* */`). Be careful with block comments that already contain `*/`.

### 6.2 Breaking long commands
Use `///` at the end of a line:
```stata
tabstat hb anc_visits age, ///
    by(state) ///
    statistics(n mean sd min max) ///
    columns(statistics)
```
Stata reads this as one command. Indent continuation lines so the structure is visible.

An older alternative is `#delimit ;`, which makes a semicolon end each command until you switch back with `#delimit cr`:

```stata
#delimit ;
tabstat hb anc_visits age,
    by(state)
    statistics(n mean sd);
#delimit cr
```
`#delimit` works only in do-files, and Stata resets the delimiter when the do-file ends. For most users `///` is simpler and less error-prone. Learn to recognise `#delimit ;` because you will meet it in other people's code.

## 7. Running a do-file: do, run, include and partial runs

### 7.1 Whole-file commands
| Command | What it does |
|---------|--------------|
| `do file` | Runs the file, **showing each command and its output** |
| `run file` | Runs the file **silently**: neither the commands nor the output appear |
| `include file` | Runs the file as if its commands had been typed at that point; **local macros defined in your current session can be used** by the included commands |

```stata
do "do/01_import.do"
run "do/helpers.do"        // e.g. a file that only defines programs
include "do/setup.do"
```
`run` is handy for a file that only defines programs. For everything else, use `do` so you can see what happened.

The Do-file Editor equivalents are **Tools > Execute (do)**, **Execute quietly (run)** and **Execute (include)**.

### 7.2 Partial runs from the Do-file Editor
Often you want to run just a piece:

| Action | How |
|--------|-----|
| Run selected lines | Highlight them, then click **Execute selection (do)** (the Do button changes) |
| Run from the first line to the cursor | **Tools > Execute (do) from top** |
| Run from the cursor to the end | **Tools > Execute (do) to bottom** |
| Run one line at a time | **Tools > Execute (do) line**; the cursor moves to the next executable line, skipping blanks and comments |
| Continue past errors | **Tools > Execute (do) nostop**; use with caution |

**Important:** local macros exist only while a do-file (or the lines you run) is executing. If you run a selection that uses `` `raw' `` but the line that defines it was not selected, the macro is empty and you will see strange errors. Run the definition and the use *together*, or use globals set in the master do-file, or choose **Execute (include)**.

### 7.3 Stopping a do-file
A do-file stops when:
- it reaches the end of the file,
- it reaches an `exit` command,
- any command produces an error (a nonzero return code), or
- you press the **Break** button (this counts as an error with return code `r(1)`).

`do file, nostop` continues past errors. It is not recommended, because a failed command can cause later commands to do the wrong thing.

### 7.4 Quiet commands and `set more`
`set more off` prevents `--more--` pauses. For one noisy command use the `quietly` prefix:
```stata
quietly regress price mpg weight
```

## 8. Errors and debugging

### 8.1 Reading the output
Stata prints each command, then the error message, then the return code in parentheses (for example `r(111);`). The **last command shown before the error** is the one that failed.

### 8.2 Common return codes
| Code | Message | Typical cause |
|------|---------|---------------|
| r(111) | variable ... not found | Misspelled or missing variable |
| r(198) | invalid syntax / ... | Typo, missing comma, wrong option |
| r(199) | unrecognized command | Misspelled command, or a user-written command not installed |
| r(601) | file ... not found | Wrong working directory or path |
| r(4) | no; dataset in memory has changed | Loading data without `clear` |
| r(109) | type mismatch | Text where a number was expected |
| r(1) | (Break) | You pressed Break |

See the [help and search guide](../lesson-01-getting-started/help-and-search-guide.md) for more.

### 8.3 A debugging routine
1. Read the **last lines** of the Results window.
2. Look at the failing command. Compare it with `help commandname`.
3. Run the do-file **up to the line before** the failure (**Execute (do) from top** on the previous line) and inspect the data (`describe`, `browse`).
4. Fix one thing at a time.
5. Rerun from the top to confirm the whole file runs from a clean start.

### 8.4 Making a do-file fail early and clearly
```stata
confirm file "data/anc_survey.csv"        // stops with an error if missing
assert !missing(id)                        // stops if any id is missing
isid id                                    // stops if id is not unique
```
`assert` and `isid` are your **tests**. They turn silent data problems into loud errors, which is what you want in a reproducible pipeline.

## 9. Arguments, nested do-files and the master do-file

### 9.1 Passing arguments
A do-file can accept arguments after its name. They are stored in local macros `` `1' ``, `` `2' ``, and so on.

```stata
* describe_data.do
args dsname
use "`dsname'", clear
describe
summarize
```
Run it with:
```stata
do describe_data "data/anc_survey.dta"
```
`args` gives the numbered arguments readable names. It does **not** validate the input; `syntax` (see `help syntax`) can do that. Arguments with spaces must be in double quotes. When the do-file ends, the previous macro definitions are restored.

### 9.2 Nesting
A do-file can call other do-files. This is how a **master do-file** works:

```stata
* 00_master.do
do "do/01_import.do"
do "do/02_clean.do"
do "do/03_analysis.do"
```
Nesting can go 64 levels deep. Calling many do-files one after another does not count as deep nesting. Calling them in sequence is exactly what a master do-file does.

### 9.3 Ending a do-file
`exit` stops a do-file at that point. For unattended runs on Unix, ending with `exit, STATA clear` makes Stata quit rather than wait for another command.

### 9.4 A project pattern
```
do/
├── 00_master.do        ← sets paths, starts a log, runs the rest
├── 01_import.do
├── 02_clean.do
├── 03_analysis.do
└── 04_figures.do
```
Rules: **each step file starts from data on disk and ends by saving data on disk**, so any step can be rerun alone. Only the master file defines paths.

## 10. From interactive work to a do-file

Often you start by experimenting, then wish you had recorded it. Stata gives you several ways to rescue the work.

| Method | How |
|--------|-----|
| **History window** | Select commands (right-click > **Select all**, or click and shift-click), then **Send selected to Do-file Editor**. Or right-click and choose **Save all...**/**Save selected...** to write a do-file |
| **Remove failed commands first** | Filter the History window to hide commands that gave errors, then save |
| **`cmdlog`** | `cmdlog using filename.do` starts recording only the commands you type (and comments); `cmdlog close` stops it. The result can be used as a do-file |
| **Dialogs** | Instead of **OK**, use **Copy**/**Submit** options (see the interface guide) to paste the generated command into the Do-file Editor |

The History window stores the last 5,000 commands, so a session can usually be rescued. Always **review and tidy** a saved history: remove exploratory commands, add comments, and add the header.

```stata
cmdlog using "do/my_session.do", replace
* ... work ...
cmdlog close
```

## 11. Navigating long do-files

### 11.1 Bookmarks
Bookmarks let you jump between parts of a long file.

| Type | Behaviour | How to add |
|------|-----------|-----------|
| **Permanent** | Saved with the do-file; reappears when you reopen it. Shown with a vertical bookmark icon | **Edit > Toggle bookmark** or click in the bookmark margin beside the line number; or type a line starting with `//#` |
| **Temporary** | Lost when the file is closed. Horizontal icon | **Edit > Toggle temporary bookmark**, or **Alt+click** in the margin |

A line beginning `//#` (or `**#`) becomes a permanent bookmark, and **the rest of the line is its title**:

```stata
//# 2. Clean the haemoglobin variable
replace hb = . if hb == 99
```
`//#` is preferable because it is also valid in Mata and Java. The line must not contain code, or the bookmark comment is ignored. Permanent bookmarks cannot be added inside multi-line comments or multi-line commands. Delete the line to remove the bookmark. Use **Next bookmark** and **Previous bookmark** to move among them.

### 11.2 The Navigator
**View > Show Navigator** lists permanent bookmarks and programs (and Java and Python blocks) in your file. Double-click an entry to jump to it. Right-click a permanent bookmark to indent or delete it. Toggle **View > Show Navigator** off to hide it.

A do-file with `//#` section titles gives you a clickable table of contents.

### 11.3 Code folding
Fold blocks to hide detail: **View > Code folding > Toggle / Fold all / Unfold all**. **Edit > Advanced > Fold selection** turns selected code into a foldable block. This works best with loops and `if` blocks.

### 11.4 Brackets
Matching brackets are highlighted as you move around. **Edit > Find > Match bracket** jumps to the partner of a bracket; **Balance brackets** selects the narrowest enclosing pair, and a second use expands to the next level. Useful for `foreach`, `forvalues` and `if` blocks.

## 12. Other Do-file Editor features

| Feature | Notes |
|---------|-------|
| **Syntax highlighting** | Colours and text properties can be changed under **Edit > Preferences...** in the Do-file Editor, on the **Colors** tab. You can define your own keyword list. See the [font and window preferences guide](../lesson-01-getting-started/font-and-window-preferences-guide.md) |
| **Languages** | The **Language** menu switches highlighting among Stata, Markdown, Python and Java. Stata chooses by file extension; for an unsaved file you must choose |
| **Autocomplete** | Pause while typing and suggestions appear for command names, words already in the file, and variable names, macros and stored results. Use the arrow keys, keep typing to narrow, press **Enter** to accept. Preferences control what and where it completes |
| **Word and selection highlighting** | The editor highlights all occurrences of the word under the cursor (case-sensitive) and of the current selection (case-insensitive). Settings are under **Preferences... > Highlighting** |
| **Show whitespace** | **View > Show whitespace** displays dots for spaces and arrows for tabs. **Preferences... > General > Always show whitespace in a selection** shows them only when you select text |
| **Templates** | **File > New > Document from template** opens a stored template. To add your own, create a document templates folder inside your PERSONAL directory (see `help sysdir`) and save plain-text template files there. Each file with an extension appears in the menu |
| **Projects** | **File > New > Project...** (Project Manager) keeps track of do-files, data files, graph files and others in a project |
| **Encoding (UTF-8)** | Stata strings use UTF-8. If you open an older file with accented, Cyrillic, CJK or other non-ASCII characters in another encoding, Stata asks you to specify its encoding and converts it. You can undo with **Undo** until you save. Retry with **Convert to UTF-8...** |
| **Line endings** | Convert between Windows and macOS/Unix when files cross systems |

**A template for your team.** Save `templates/do-file-template.do` from this repo in your PERSONAL `templates` directory, and every team member starts new do-files with the same header.

## 13. A team style guide

Agree a short style guide and keep to it. A starting point:

1. **Header** on every file: purpose, author, date, inputs, outputs.
2. **`version`** line first.
3. **One job per file**, numbered in order (`01_`, `02_`, ...).
4. **Master do-file** runs everything; step files do not set paths.
5. **Never change raw data.** Read from `data/raw`, write to `data/clean`.
6. **Lowercase** variable names with underscores: `anc_visits`, not `ANCvisits`.
7. **Comment the why**, and mark sections with `//#` titles.
8. **Indent** loops and `if` blocks consistently (4 spaces, no tabs, or the reverse; choose one).
9. **Keep lines short**; break with `///`.
10. **Quote file paths**; use forward slashes.
11. **Use `assert`/`isid`** to test your assumptions.
12. **Log** every analysis run; log name matches the do-file.
13. **Test from a clean start**: `clear all` then run the master do-file.
14. **No hard-coded results** in text: let code produce the numbers.
15. **Save with `replace` only where overwriting is intended.**

## 14. Running do-files without the interface (batch mode)

Do-files can run in the background, which is useful for long jobs and scheduled tasks.

| System | Command (example) |
|--------|-------------------|
| Windows | `"C:\Program Files\Stata19\StataSE-64.exe" /e do "C:\project\do\00_master.do"` (run from a command prompt) |
| Mac | `/Applications/Stata/Stata.app/Contents/MacOS/Stata -b do myjob` |
| Unix | `stata -b do myfile &` |

Notes from the manuals: `/b` (or `-b`) runs in batch mode and writes a **plain-text** log; `/s` (or `-s`) writes a **SMCL** log; `/e` is batch mode that does not prompt when the command has completed on Windows. The log goes to the **current directory** when the job starts, so `cd` to the folder where you want the log first (see the [working directory guide](../lesson-01-getting-started/working-directory-guide.md), section 10). Batch jobs ignore `--more--` and other interactive stopping conditions. If the do-file also opens its own log, you will get two copies of the output. File names depend on your edition and version, so check your installation.

## 15. Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| `r(601)` file not found | Wrong working directory or path | `pwd`; `dir`; check quotes and slashes |
| `r(4)` on the first line | Data changed since load | Add `clear` while developing |
| `r(199)` unrecognized command | Typo, or add-on not installed | `help`/`search`; `ssc install` where appropriate |
| Works when I run all, fails when I run a selection | A macro or earlier step was not run | Run definitions with the lines that use them, or use **Execute (include)** |
| Nothing prints | Used `run` or `quietly` | Use `do` |
| `--more--` appears | `set more` is on | Add `set more off` |
| Comment breaks the line | No space before `//` | Add a space |
| Long command splits wrongly | Missing `///` or stray space after it | Make `///` the last characters on the line |
| Log will not open | A log is already open, or the file exists without `replace` | `log close` (use `capture log close` at the top), add `replace` |
| Works on my PC, not yours | Absolute paths, different working directory, different version | Master do-file with `$root`; add `version` |
| Weird characters in comments or strings | File encoding or pasted curly quotes | **Edit > Advanced > Convert Unicode spaces and curly quotes to ASCII** or **Convert to UTF-8...** |
| Do-file ran but results differ from yesterday | Different data, version, or random seed | `set seed`; log versions; test with `assert` |

A line worth putting at the top of every do-file that opens a log:
```stata
capture log close         // closes a log left open by an earlier failed run
```

## 16. Practice exercises DO1 to DO12

Solutions are in `exercise-solutions/lesson-04/do-file-practice.do`. Try each first. Use `auto` unless told otherwise.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**DO1 🟢 First run.** Open the Do-file Editor. Type the manual's example (section 4.1) exactly as given, including the misspelling. Click **Do**. Which command failed, and what is the return code?

**DO2 🟢 Fix and re-run.** Fix the spelling. Run again. What new error appears, and why? Fix it two ways and explain which you would choose for a final analysis.

**DO3 🟢 Save and run by name.** Save the working file as `gp100m.do` in a `do` folder. Close the editor. Run it by typing `do gp100m` in the Command window. What do you have to check first?

**DO4 🟢 Comments.** Add a header with purpose, author and date. Add one `*` comment, one `//` comment after code, and one `/* */` comment. Then deliberately remove the space before `//` and see what happens.

**DO5 🟡 Long commands.** Rewrite this as three lines with `///`:
`tabstat price mpg weight, by(foreign) statistics(n mean sd min max) columns(statistics)`

**DO6 🟡 Partial runs.** Highlight only the first two lines and click **Execute selection (do)**. Then place the cursor on a line and use **Execute (do) from top**, then **Execute (do) line** repeatedly. When would you use each?

**DO7 🟡 `do`, `run`, `include`.** Create `setup.do` containing `local cutoff 5000`. In the Command window run `do setup.do`, then display `` `cutoff' ``. Repeat with `include setup.do`. What do you see, and why?

**DO8 🟡 History to do-file.** In the Command window run `sysuse auto, clear`, `summarize price`, a misspelled command, and `tabulate foreign`. Use the History window to remove the error and send the rest to the Do-file Editor. Add a header and save.

**DO9 🟡 Bookmarks and Navigator.** In a do-file with four sections, add `//# 1. Setup` and similar lines. Open the Navigator. Jump between sections. Fold a `foreach` loop with code folding.

**DO10 🔴 Arguments.** Write `describe_data.do` that takes a dataset path as an argument, loads it, and runs `describe` and `summarize`. Run it on `data/anc_survey.dta`. What happens if you give a path that does not exist?

**DO11 🔴 Master do-file.** Write `00_master.do` that sets `$root`, starts a log, runs three step files in order and closes the log. Make the third step fail on purpose (for example `use "missing.dta"`). What does the log look like? Fix it and rerun from a clean start.

**DO12 🔴 Peer review.** Swap a do-file with a neighbour. Using the style guide in section 13, give three specific improvements. Then apply the improvements you receive.

## 17. Quick reference card

| Task | How |
|------|-----|
| Open Do-file Editor | Toolbar button or `doedit` |
| Run the whole file | **Do** button or `do filename` |
| Run silently | `run filename` |
| Run with access to session macros | `include filename` |
| Run selection | Highlight, then **Execute selection (do)** |
| Run from top to cursor | **Tools > Execute (do) from top** |
| Run line by line | **Tools > Execute (do) line** |
| Ignore errors (careful) | `do file, nostop` or **Execute (do) nostop** |
| Comment a line | `*` or `//` (space before `//`) |
| Comment a block | `/* ... */` or **Edit > Advanced > Add block comment** |
| Continue a command | End the line with `///` |
| Section bookmark | `//# Title` |
| Declare version | `version 17` (use your release) |
| Quiet a command | `quietly command` |
| Stop paging | `set more off` |
| Start / close log | `log using file, replace` / `log close` |
| Pass arguments | `do file arg1 arg2`, then `args name1 name2` |
| Stop a do-file | `exit` or the **Break** button |
| Record commands only | `cmdlog using file.do` / `cmdlog close` |

## 18. Facilitator notes

**Timing (90-minute session):** 15 min concepts and editor tour (sections 1 to 3), 20 min worked example with deliberate errors (4), 15 min structure, comments and running (5 to 7), 10 min arguments and master file (9), 30 min exercises DO1 to DO9. DO10 to DO12 are take-home or an advanced group task.

**Before the session**
- Participants should have completed the [working directory guide](../lesson-01-getting-started/working-directory-guide.md) (project folder and `$root`).
- Have the template file ready for everyone.
- Check each PC's Stata version to choose a sensible `version` line.

**Common stumbling blocks**
- Expecting a do-file to continue after an error. Show that it stops.
- Running a selection that uses a local macro defined on a line they did not select.
- `r(4)` after the second run. Teach `clear` while developing, and explain the trade-off.
- Pasting from Word, which brings curly quotes and odd spaces.
- Forgetting the space before `//`.
- Copying a colleague's do-file with absolute paths.

**Teaching tips**
- Run the manual's "deliberate mistakes" example live and let participants predict each error before clicking Do.
- Hold a "clean start test": everyone restarts Stata and runs their master do-file. Whoever fails first explains why.
- Pair work: one person reads the do-file aloud, the other predicts the output.
- End with the style guide: have the group vote on which three rules they will adopt.

**Assessment prompt (5 minutes):** "Your colleague's do-file ran fine yesterday but today fails at line 1 with r(4). What changed, and what are two ways to prevent it?" Expected: data in memory changed since it was loaded; use `clear` on the load command or `clear all` at the top (with the trade-off explained).

**Note on versions.** This guide follows the Windows edition of the Getting Started manual and the current User's Guide. Menu names, available toolbar buttons and file names for batch mode differ across versions and systems. Check `help doedit`, `help do` and `help version` in your own installation.
