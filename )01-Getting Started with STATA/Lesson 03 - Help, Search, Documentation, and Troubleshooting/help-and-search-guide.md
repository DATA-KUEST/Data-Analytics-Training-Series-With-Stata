# Learning Notes: Getting Help in Stata (Help and Search)

**Part of:** Lesson 1, Getting Started  |  **Read and practise:** about 60 minutes  |  **Dataset:** `auto` (built into Stata)

No analyst memorises every Stata command. What separates confident professionals from stuck ones is knowing **how to find the right command, read its documentation, and fix their own errors**. This guide teaches that skill. It also supports exercise **1l** in the [Lesson 1 exercises](README.md).

## Learning objectives
By the end of this guide you will be able to:
- Choose between `help`, `search`, `findit`, `lookfor` and the manuals for any question
- Read a Stata help file, including its syntax line
- Write search keywords that actually find commands
- Use the Viewer, dialogs and examples to learn a command quickly
- Diagnose common error messages
- Find trustworthy learning resources and ask for help effectively

## Contents
1. [The help ecosystem at a glance](#1-the-help-ecosystem-at-a-glance)
2. [Which tool do I use? A decision guide](#2-which-tool-do-i-use-a-decision-guide)
3. [`help` vs `search`: the key difference](#3-help-vs-search-the-key-difference)
4. [Walkthrough: finding a command you've forgotten](#4-walkthrough-finding-a-command-youve-forgotten)
5. [The Viewer window](#5-the-viewer-window)
6. [Anatomy of a help file](#6-anatomy-of-a-help-file)
7. [Reading the syntax line](#7-reading-the-syntax-line)
8. [Search in depth](#8-search-in-depth)
9. [Command-line toolkit](#9-command-line-toolkit)
10. [The reference manuals](#10-the-reference-manuals)
11. [Videos, journal, forums and other resources](#11-videos-journal-forums-and-other-resources)
12. [When something goes wrong: troubleshooting](#12-when-something-goes-wrong-troubleshooting)
13. [Asking for help well](#13-asking-for-help-well)
14. [Hands-on practice](#14-hands-on-practice)
15. [Cheat sheet and self-check](#15-cheat-sheet-and-self-check)
16. [Facilitator notes](#16-facilitator-notes)

---

## 1. The help ecosystem at a glance

Stata comes with more help than most people realise, and much of it works offline.

| Resource | Best for | How to reach it |
|---|---|---|
| **Help files** | Syntax, options and examples for one known command | `help commandname` or **Help > Stata command...** |
| **Search** | Finding a command when you only know the *task* | `search keywords` or **Help > Search...** |
| **The Viewer** | Reading help and search output, with clickable links | Opens automatically; also on the toolbar |
| **Dialogs** | Learning a command by filling in boxes | `db commandname`, or the Dialog button in a help file |
| **PDF reference manuals** | The full story, with theory, worked examples and formulas | "View complete PDF manual entry" link at the top of a help file |
| **Stata Journal** | Articles, tips and programs from the Stata community | Links in search results; stata-journal.com |
| **Stata YouTube channel** | Short video demonstrations, many through the menus | See [section 11](#11-videos-journal-forums-and-other-resources) |
| **FAQs and forums** | Practical answers to real problems | See [section 11](#11-videos-journal-forums-and-other-resources) |

> **Good to know:** the help files in Stata contain only a fraction of what is in the PDF manuals. When a help file leaves you wanting more, follow its link to the manual entry.

---

## 2. Which tool do I use? A decision guide
<img width="364" height="486" alt="Decision making guide" src="https://github.com/user-attachments/assets/ae25bf21-bcf2-4ccb-9e75-fb1da944ab16" />




| If you think... | Use |
|---|---|
| "What's the syntax for `regress`?" | `help regress` |
| "How do I combine two datasets?" | `search combine datasets` |
| "What was that variable about fuel economy?" | `lookfor fuel` |
| "I want the dialog box for this command" | `db commandname` |
| "I want to know if a user-written command exists for this" | `search keywords, net` or `findit keywords` |
| "What's new in my version of Stata?" | `help whatsnew` |

---

## 3. `help` vs `search`: the key difference

These two look similar but do different jobs.

| | **`help`** | **`search`** |
|---|---|---|
| **You know** | The exact command name | A topic or task |
| **Result** | Goes straight to that command's help file | A list of related commands, FAQs, articles and videos |
| **Menu** | **Help > Stata command...** | **Help > Search...** |
| **Command** | `help commandname` | `search keywords` |

**Why the distinction matters:** some words are both a command name *and* a general topic. `logistic` is a good example.
- `help logistic` takes you directly to the help file for the `logistic` command.
- `search logistic` lists the many commands related to logistic regression.

Use `help` when you know the answer and want the details. Use `search` when you want to explore.

---

## 4. Walkthrough: finding a command you've forgotten

**Scenario:** someone gives you a dataset and you need to know what's in it. You vaguely recall a command for this but not its name.

**Step 1.** Load the practice data (the `clear` option wipes anything already in memory):

```stata
sysuse auto, clear
```

**Step 2.** Search by the *task*, using plain, proper terms:

```stata
search dataset contents
```

Equivalent menu route: **Help > Search...**, make sure **Search all** is selected, type `dataset contents`, press **OK**.

**Step 3.** A Viewer window opens with a list of matches. Among them you should see commands such as `codebook`, `describe`, `list` and `edit`. Each result shows a short description and a clickable `help ...` link.

**Step 4.** Click the link for a command that looks right, for example `codebook`, to open its help file.

**Step 5.** Read the description, then scroll to the **Examples** section (or use the **Jump to** button) and try the examples on the `auto` data.

**Step 6.** Run the command yourself in the Command window, or open its dialog from the **Dialog** button.

**Step 7.** If it isn't what you wanted, use the **Back** button or the **Also see** menu to move to related commands, or type new search terms in the Viewer's search box.

> **What you just did** is the core professional workflow: *search by task, identify the command, read the help file, run the examples, adapt to your data.*

---

## 5. The Viewer window

Help and search results appear in the **Viewer**, a window that behaves a little like a web browser.

| Part | Use |
|---|---|
| **Back / Forward / Refresh** | Move through the pages you have seen |
| **Print** | Print the current page |
| **Search box** (top) | Start a new search or jump to a command's help without leaving the Viewer |
| **Magnifying glass** | Choose the *scope* of a search before typing |
| **Tabs** | Keep several help pages open at once |
| **Dialog / Also see / Jump to** | Quick-access menus inside every command help file (see next section) |
| **Blue links** | Open help files, dialogs, manual entries or web pages; some run example commands |

**Tip:** opening a few tabs (one for the command you are using, one for a related command) saves you repeatedly searching.

---

## 6. Anatomy of a help file

Help files for Stata commands share a standard layout. Knowing it makes every command easier to learn.

| Section (top to bottom) | What it gives you |
|---|---|
| **Quick-access toolbar** | **Dialog** (links to the command's dialog), **Also see** (related help files and PDF documentation), **Jump to** (other sections of this help file) |
| **Manual entry link** | "View complete PDF manual entry" opens the full manual page for the command |
| **Syntax** | The rules for writing the command correctly (see [section 7](#7-reading-the-syntax-line)) |
| **Description** | A short, deliberately terse statement of what the command does |
| **Options** | What each option does, in more detail than the short list under the syntax |
| **Examples** | Worked examples, usually on datasets that ship with Stata or can be loaded from the internet |
| **Stored results** | Values the command saves for later use. Mostly of interest to programmers, but useful later when you start automating |

**Example of why options matter:** the `codebook` help file lists an `mv` option that reports the *pattern of missing values*, which is important when you clean data (Lesson 3 will use ideas like this).

> **Make this a habit:** whenever you meet a new command, open its help file and run the first two or three examples *before* using it on your real data.

---

## 7. Reading the syntax line

The syntax line looks cryptic at first, but it follows a small set of conventions. Take the syntax of `codebook`:

```
codebook [varlist] [if] [in] [, options]
```

| Notation | Meaning |
|---|---|
| `codebook` | The command name; type it exactly |
| `[ ... ]` square brackets | **Optional.** Everything in brackets can be left out |
| `varlist` | A list of variable names, separated by spaces |
| `if` | A condition restricting which observations are used, e.g. `if foreign == 1` |
| `in` | A range of observation numbers, e.g. `in 1/10` |
| `[, options]` | The comma starts the options. Options always come **after** a comma |
| **Underlined letters** (in the help file) | The **shortest allowed abbreviation** of a command or option name |

**Reading it aloud:** "Type `codebook`. If you like, add a list of variables, an `if` condition, an `in` range, and, after a comma, any options."

**Worked examples with `codebook`:**

```stata
sysuse auto, clear
codebook                           // all variables
codebook price mpg                 // only two variables
codebook price if foreign == 1     // only foreign cars
codebook price, header             // with an option (note the comma)
```

**A slightly bigger one:** `regress` has a longer syntax line:

```
regress depvar [indepvars] [if] [in] [weight] [, options]
```

- `depvar` is required (it is *not* in brackets) and `indepvars` is optional.
- `weight` is where you would specify survey or frequency weights.

**Common syntax mistakes**
- Forgetting the comma before options: `summarize price detail` instead of `summarize price, detail`.
- Using `=` instead of `==` in an `if` condition.
- Putting the `if` condition *after* the comma.

---

## 8. Search in depth

### 8.1 Three search scopes

The **Help > Search...** dialog asks what to search. Each scope has a command-line equivalent:

| Menu choice | Command | Where results appear | What it covers |
|---|---|---|---|
| **Search all** | `search topic` | Viewer | Official commands, manuals, Stata Journal, FAQs, videos, selected external sites, and community-contributed features |
| **Search documentation and FAQs** | `search topic, local` | Results window | Stata's own keyword database: official commands, Stata Journal articles and software, FAQs and videos |
| **Search net resources** | `search topic, net` | Results window | Community-contributed commands, from the Stata Journal or elsewhere |

`search` has more abilities, such as searching by author. Run `help search` to see them.

### 8.2 Writing good search keywords

Search matches against Stata's keyword index, so use the **proper statistical or data-management term**, not casual phrasing.

| Instead of... | Try... |
|---|---|
| "compare two groups with non-normal data" | `Mann-Whitney` or `rank sum` |
| "line up two tables" | `merge datasets` |
| "find repeats" | `duplicate observations` |
| "average by group" | `summary statistics by group` |
| "residuals" | `regression residuals` |
| "weights from survey" | `survey weights` |

**Tips**
1. Multiple words are fine (`regression residuals`).
2. Use standard English and standard terminology.
3. Start broad, then narrow with a second search.
4. If nothing useful appears, try a synonym (`missing values` vs `incomplete data`).
5. If you already know the command, skip search and use `help commandname`.

### 8.3 Practical search examples for applied research

| Task | Example search | Commands you are likely to meet |
|---|---|---|
| Combine datasets side by side | `search merge datasets` | `merge` |
| Stack datasets | `search append datasets` | `append` |
| Wide-to-long reshaping | `search reshape data` | `reshape` |
| Check for repeated records | `search duplicate observations` | `duplicates` |
| Compare means between two groups | `search t test` | `ttest` |
| Rank-based group comparison | `search Mann-Whitney` | `ranksum` |
| Logistic regression | `search logistic regression` | `logistic`, `logit` |
| Survey data with weights | `search survey data` | `svyset`, `svy` |
| Panel or longitudinal data | `search panel data` | `xtset`, `xtreg` |
| Count missing values | `search missing values` | `misstable`, `mvdecode`, `codebook` |

> Search results are a starting point. Always open the help file and read the description before using a command.

### 8.4 Searching from inside the Viewer

You can search without going back to the Command window:
- Type a command or search terms in the **Viewer's search box** and press **Enter**, or
- Click the **magnifying glass** to select the scope first.

---

## 9. Command-line toolkit

Everything the menus do can be done from the Command window, which is faster and can be saved in a do-file.

| Command | What it does |
|---|---|
| `help commandname` | Opens the help file for a command (same as **Help > Stata command...**) |
| `help commandname##examples` | Opens the help file at its Examples section (the same style of address that the Viewer shows after **Jump to**) |
| `search keywords` | Same as **Help > Search...** with **Search all**; opens in the Viewer |
| `search keywords, local` | Official keyword search; output in the Results window |
| `search keywords, net` | Search net resources for community-contributed commands; output in the Results window |
| `findit keywords` | Searches Stata's official documentation *and* net resources together |
| `hsearch keywords` | Searches the text inside help files |
| `lookfor keyword` | Searches variable names and labels in the **dataset in memory** |
| `db commandname` | Opens the dialog for a command |
| `help whatsnew` | Summarises what is new in your version |

**`lookfor` deserves special attention.** It is the best tool for finding a variable when you only remember what it measures:

```stata
sysuse auto, clear
lookfor mileage     // finds mpg, whose label contains "Mileage"
lookfor price
```

> Your Stata version determines which options and commands exist. If something here doesn't work, run `help search` and `help whatsnew` to see what your version supports.

### Community-contributed commands (use with care)

Stata's community writes thousands of extra commands. You can discover them with `search ..., net` or `findit`, and many live in the SSC archive (`ssc` command; see `help ssc`). Before installing anything on a work computer:
- Check who wrote it and read its help file first.
- Install only on machines where you are allowed to add software.
- Note the command and its version in your do-file comments so others can reproduce your analysis.

---

## 10. The reference manuals

All Stata manuals ship with the software as **PDF files** full of clickable cross-references, so you can read them non-linearly. They are alphabetical, and the **Stata Index** is a combined index to all manuals except *Getting Started*, which has its own. Start with the index when you are looking for information about a command.

**Understanding references like `[D] merge` or `[R] regress`:** the letter in brackets is the manual that covers the command.

| Notation | Manual |
|---|---|
| `[GSW]` | Getting Started with Stata (Windows) |
| `[U]` | User's Guide |
| `[R]` | Base Reference Manual |
| `[D]` | Data Management Reference Manual |
| `[P]` | Programming Reference Manual |
| `[G]` | Graphics Reference Manual |
| `[SVY]` | Survey Data Reference Manual |
| `[XT]` | Longitudinal/Panel Data Reference Manual |
| `[ST]` | Survival Analysis Reference Manual |
| `[TS]` | Time-Series Reference Manual |

The list of all manuals and their abbreviations appears after the table of contents in the *Getting Started* manual.

**How to use the manuals well**
1. Start with the help file for a quick answer.
2. Use the **View complete PDF manual entry** link when you need the formulas, assumptions, worked examples or references.
3. Use **Also see** to jump to related entries.
4. Use the **User's Guide** for broad concepts (it covers how Stata thinks about data, syntax, and more).

---

## 11. Videos, journal, forums and other resources

*Links were correct at the time of writing; websites change, so use a search engine if one has moved.*

| Resource | Why it's useful | Where |
|---|---|---|
| **Stata YouTube channel** | Short videos using the menus; topics from data management and graphics to multilevel and structural equation models. Playlists run in sequence, for example power and sample size, survival analysis, time series, and a refresher playlist for students | https://www.youtube.com/user/statacorp/ |
| **Stata video tutorials index** | Up-to-date list of videos by topic | https://www.stata.com/links/video-tutorials/ |
| **Stata Journal** | Quarterly, peer-reviewed articles, tips and programs; the accompanying programs and datasets can be downloaded by all users; articles older than three years are free to download | https://www.stata-journal.com |
| **Stata website links page** | Pointers to places where you can download programs and datasets for Stata | https://www.stata.com/links/ |
| **Stata FAQs** | Short, practical answers to common problems | https://www.stata.com/support/faqs/ |
| **Statalist forum** | Community Q&A; search it before asking | https://www.statalist.org |
| **UCLA OARC Stata pages** | Free tutorials and annotated output for many methods | https://stats.oarc.ucla.edu/stata/ |
| **SSC archive** | A convenient place to find community-contributed software | via the `ssc` command (`help ssc`) |

---

## 12. When something goes wrong: troubleshooting

A good analyst reads error messages as clues, not insults. Stata prints a message and a **return code** in the form `r(NNN)`. Failed commands also appear in **red** in the History window.

### Common errors

| Message (example) | Return code | Usual cause | Fix |
|---|---|---|---|
| `command sumarize is unrecognized` | r(199) | Typo in a command name, or the command isn't installed | Check spelling; use `search` to find the right name |
| `variable cost not found` | r(111) | Typo in a variable name, or the wrong dataset is loaded | Use `describe` or `lookfor` to find the correct name |
| `invalid syntax` | r(198) | Command written incorrectly (missing comma, wrong order) | Open the help file and compare with the syntax line |
| `file ... not found` | r(601) | Wrong path, or the wrong working directory | Check `pwd`; use quotes around paths with spaces |
| `type mismatch` | r(109) | Mixing text and numbers, for example comparing a string variable with a number | Check variable types with `describe` |

### A repeatable troubleshooting routine
1. **Read** the message and the return code, and check the History window for the exact command that failed.
2. **Check spelling** of the command and variable names. Use the **Tab** key to auto-complete variable names.
3. **Open `help commandname`** and compare your command with the syntax line.
4. **Check your data** with `describe`, `lookfor` and `browse`.
5. **Run an example** from the help file to see if the command works at all.
6. **Shrink the problem** to the smallest set of commands that still fails.
7. **Search** for the error message text (FAQs and Statalist often have it).
8. **Ask for help** if still stuck ([section 13](#13-asking-for-help-well)).

---

## 13. Asking for help well

Colleagues and online communities help far more readily when you make it easy. Before you post or email:
- ✅ State your **goal** in one sentence.
- ✅ Paste the **exact command** and the **exact error message** (copy from the Results window, not a screenshot of a screenshot).
- ✅ State your **Stata version** (run the `about` command, or check **Help > About Stata**).
- ✅ Provide a **small, reproducible example**, ideally on a built-in dataset like `auto` or a few lines of your own data (never share confidential or personal data).
- ✅ Say what you have **already tried**.
- ✅ Check whether the question has been answered in the FAQ or forum archive.

**Template**

```
Goal: I want to compare average mpg between domestic and foreign cars.
Command: ttest mpg, by(foreign)
What happened: [paste the exact output or error]
Stata version: [your version]
Already tried: help ttest; searched "compare means"
```

> **Data protection reminder for professionals:** never paste patient, client or participant data into forums, emails or AI tools. Use synthetic or built-in data to reproduce problems.

---

## 14. Hands-on practice

Do these in order. Create a do-file for each (or put them all in `help-practice.do`). Sample solutions are in [`exercise-solutions/lesson-01/help-practice.do`](../../exercise-solutions/lesson-01/help-practice.do).

### 🟢 H1. Open a help file from the menu
Use **Help > Stata command...** to open the help file for `summarize`. Find its syntax line. Which parts are optional?

**Expected:** `varlist`, `if`, `in`, weights and options are all in square brackets, so `summarize` alone is a valid command.

### 🟢 H2. Open a help file from the Command window
Open the help file for `describe` using a command. Compare the route with H1.

**Expected:** the same help file opens in a Viewer window.

### 🟢 H3. Find an option
In the `summarize` help file, find the option that adds percentiles, then run it on `price` in the `auto` data.

**Expected:** `summarize price, detail` shows percentiles, variance, skewness and kurtosis.

### 🟢 H4. Search by task
Run a search for *dataset contents*. List two commands from the results that could describe a dataset.

**Expected:** results include `codebook` and `describe`, among others.

### 🟡 H5. `help` versus `search`
Run `help logistic` and `search logistic`. Write one sentence on how the output differs.

**Expected:** `help` opens one command's help file; `search` lists many commands and other resources related to logistic regression.

### 🟡 H6. Control the search scope
Run `search merge datasets, local`. Where do the results appear this time, and why?

**Expected:** in the **Results window**, not the Viewer, because `, local` runs the official keyword search with Results-window output.

### 🟢 H7. Find a variable with `lookfor`
Load `auto`, and use `lookfor` to find the variable that records fuel economy, using the word *mileage*.

**Expected:** `mpg`.

### 🟡 H8. Use examples
Open `help codebook##examples`, then run `codebook rep78` on the `auto` data.

**Expected:** the output reports that `rep78` is numeric and has **5 missing values out of 74 observations**.

### 🟢 H9. Use a dialog
Type `db summarize`. Choose `price` and `mpg`, click **Submit**, and look at the Results window.

**Expected:** a normal `summarize price mpg` command appears in the Results window, followed by its output. Compare the command with what you would have typed.

### 🟡 H10. Read three error messages
Run each line and write down the message and return code:

```stata
sysuse auto, clear
sumarize price
summarize cost
use "data/nofile.dta", clear
```

**Expected:** `command sumarize is unrecognized` (r(199)), `variable cost not found` (r(111)), and `file ... not found` (r(601)).

### 🟡 H11. Which manual?
For each command, state the manual letter that documents it: `merge`, `regress`, `svyset`, `xtreg`.

**Expected:** `merge` is in `[D]` (data management), `regress` in `[R]` (base reference), `svyset` in `[SVY]` (survey), `xtreg` in `[XT]` (longitudinal/panel data). Confirm by opening each help file and using the manual link or the **Also see** menu.

### 🔴 H12. Challenge: solve a real task using only help
You need to find *duplicate observations* in your data. Without being told the command name, use `search` to find it, open its help file, find an example, and report how many surplus copies exist in `data/anc_survey.dta` (from Lesson 2) using that command.

**Expected:** you should find the `duplicates` command; applied to the Lesson 2 data with `duplicates report id` it reports a surplus of 12.

---

## 15. Cheat sheet and self-check

### One-page cheat sheet

| I want to... | Type |
|---|---|
| Open a command's help | `help commandname` |
| Find a command for a task | `search keywords` |
| Search official docs only, in Results | `search keywords, local` |
| Look for user-written commands | `search keywords, net` or `findit keywords` |
| Find a variable by name or label | `lookfor keyword` |
| Open a command's dialog | `db commandname` |
| Jump to examples | `help commandname##examples` |
| See what's new | `help whatsnew` |
| Check where I am | `pwd` |

### Self-check questions
1. What is the difference between `help logistic` and `search logistic`?
2. In `codebook [varlist] [if] [in] [, options]`, which parts are required?
3. Where do the results of `search topic, local` appear?
4. What does the notation `[D] merge` tell you?
5. You can't remember the name of the variable containing patients' blood pressure. Which command helps?
6. Name two things you should include when asking someone for help with an error.
7. Why should you open the help file *and* the manual entry for an unfamiliar command?

<details><summary>Answers</summary>

1. `help logistic` opens the help file for the `logistic` command; `search logistic` lists many commands related to logistic regression.
2. None. Everything after `codebook` is in square brackets, so all of it is optional.
3. In the Results window.
4. `merge` is documented in the Data Management Reference Manual, and a manual entry exists for it.
5. `lookfor` (for example `lookfor blood pressure`), which searches variable names and labels in the data in memory.
6. For example the exact command, the exact error message, your Stata version, and a small reproducible example. A statement of what you've already tried is also good.
7. The help file gives quick syntax and examples; the manual gives the underlying method, assumptions, formulas and more worked examples. Use both.

</details>

---

## 16. Facilitator notes

*For trainers delivering this as a live session with a group of professionals.*

### Suggested 75-minute session plan

| Time | Segment | Method |
|---|---|---|
| 0–10 min | Why help skills matter; the ecosystem map ([section 1](#1-the-help-ecosystem-at-a-glance)) | Short talk |
| 10–25 min | `help` vs `search`; walkthrough in [section 4](#4-walkthrough-finding-a-command-youve-forgotten) | Live demo, participants follow along |
| 25–40 min | Anatomy of a help file and reading syntax ([sections 6 and 7](#6-anatomy-of-a-help-file)) | Demo, then pair work on `regress` and `codebook` syntax |
| 40–55 min | Search keywords, `lookfor`, command toolkit ([sections 8 and 9](#8-search-in-depth)) | Practice H4 to H9 |
| 55–65 min | Errors and troubleshooting ([section 12](#12-when-something-goes-wrong-troubleshooting)) | Practice H10; discuss routine |
| 65–75 min | Challenge H12 and wrap-up; point to resources | Individual, then debrief |

### Teaching tips
- **Model the behaviour.** When a participant asks "what command does X?", resist answering directly. Search in front of the group so they see the process.
- **Make errors normal.** Deliberately mistype a command in the demo and walk through the routine.
- **Mixed experience levels.** Pair beginners with experienced users for H8 and H12.
- **Data protection.** Remind participants not to use confidential data in practice or in forum posts. Everything in this guide works with built-in or synthetic data.
- **Reinforce with do-files.** Ask participants to record their practice in a do-file with comments, so they leave with a reusable record.

### Discussion prompts
1. What do you currently do when you get stuck? How could this routine improve it?
2. When is it better to ask a colleague than to search the documentation?
3. How would you decide whether a community-contributed command is trustworthy enough for a work project?

---

*Adapted and summarised for learners from the "Getting help" chapter of the Stata Getting Started manual (StataCorp LLC), with additional material by the course author. Stata is a registered trademark of StataCorp LLC.*

**Next:** return to the [Lesson 1 exercises](README.md), especially exercise 1l.
