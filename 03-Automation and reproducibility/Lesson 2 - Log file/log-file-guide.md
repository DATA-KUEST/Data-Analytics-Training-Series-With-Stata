# Learning Notes: Log Files in Stata

**Part of:** Lesson 4, Do-files and Log Files  |  **Read and practise:** about 75 minutes  |  **Dataset:** `auto` (built into Stata) and the ANC survey in `data/`

Your results disappear from the Results window as you work. The numbers you quoted in a report last month, the exact order of your commands, the warning message you saw before the deadline: none of it survives unless you recorded it. A **log file** is Stata's lab notebook. Together with a do-file it makes your analysis auditable: the do-file says what you *did*; the log says what *happened*.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 16 ("Saving and printing results by using logs"), and checked against the *Stata User's Guide* chapter 15 and the `[R] log` reference entry on stata.com. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Explain what a log file is, and what it records
- Start, pause, resume and close a log using the toolbar, menus and commands
- Choose between SMCL and plain-text logs, and convert between them
- Avoid overwriting or losing a log, and append when you intend to
- Run several named logs at once
- Record commands only, with `cmdlog`, and rescue a session you forgot to log
- View, search, copy, print and share logs responsibly
- Build an audit trail: dated logs, versions and checks inside a log
- Add logging to a do-file and a master do-file

## Contents
1. [What a log file is](#1-what-a-log-file-is)
2. [Why every serious analysis should be logged](#2-why-every-serious-analysis-should-be-logged)
3. [Starting a log](#3-starting-a-log)
4. [Anatomy of a log](#4-anatomy-of-a-log)
5. [SMCL or plain text?](#5-smcl-or-plain-text)
6. [Replace, append and never overwriting by accident](#6-replace-append-and-never-overwriting-by-accident)
7. [Pausing, resuming and closing](#7-pausing-resuming-and-closing)
8. [Checking the status of your logs](#8-checking-the-status-of-your-logs)
9. [Multiple (named) logs](#9-multiple-named-logs)
10. [Command logs with `cmdlog`](#10-command-logs-with-cmdlog)
11. [Rescuing a session you forgot to log](#11-rescuing-a-session-you-forgot-to-log)
12. [Working with logs: view, search, copy, print, translate](#12-working-with-logs-view-search-copy-print-translate)
13. [Logging inside do-files](#13-logging-inside-do-files)
14. [An audit trail inside your log](#14-an-audit-trail-inside-your-log)
15. [Logs, privacy and GitHub](#15-logs-privacy-and-github)
16. [Troubleshooting](#16-troubleshooting)
17. [Practice exercises L1 to L12](#17-practice-exercises-l1-to-l12)
18. [Quick reference card](#18-quick-reference-card)
19. [Facilitator notes](#19-facilitator-notes)

---

## 1. What a log file is

The manual defines a log file as **a record of your Results window**. It records **all commands and all textual output as it happens**. Because Stata writes the file to disk while it writes to the Results window, it also protects you from disastrous failures such as power cuts or computer crashes: what has been logged is already on disk.

The manual's analogy: behave like a bench scientist and keep a lab notebook so that your work can be replicated. The feeling of complete omniscience while you work is "wonderful but fleeting". The next day the small details needed for perfect duplication have become obscure.

What a log **does** record:
- Every command you type or run from a do-file (the echoed lines starting with `.`)
- Every line of text output, including error messages
- Comments you type with `*`

What a log **does not** record:
- Graphs (save them with `graph export`)
- The data themselves
- Anything that happens before you start the log or after you close it
- Changes made by clicking inside the Data Editor, apart from the commands Stata echoes

## 2. Why every serious analysis should be logged

| Reason | Example |
|--------|---------|
| **Reproducibility** | A reviewer asks how you got a figure; the log shows the commands and output |
| **Crash protection** | The laptop dies at 4 p.m.; the log holds everything up to the crash |
| **Quality assurance** | A colleague checks the numbers in the report against the log |
| **Debugging** | You compare yesterday's working log with today's failing one |
| **Documentation** | Your thinking is in the comments: why you excluded 12 duplicates |
| **Auditing** | A funder or ethics board asks for evidence of analysis steps |
| **Teaching** | Participants send the log instead of describing "an error" |

The manual recommends that you **start a log file whenever you begin any serious work in Stata**.

## 3. Starting a log

### 3.1 With the toolbar or menu
Click the **Log** button on the main toolbar. A standard file dialog opens so you can choose a folder and a file name. If you give no extension, Stata adds `.smcl`. The Log button's menu also lets you close, suspend or resume the current log. The **File > Log** menu has the same choices, including **View...** and **Translate...**.

If you pick a file that already exists, you are asked whether to **append** the new log to the file or **overwrite** it.

### 3.2 With a command (recommended)
```stata
log using "logs/session1.smcl", replace
```
This is better than clicking because the command can sit at the top of your do-file. It is recorded, repeatable and consistent.

```stata
log using mylog                  // SMCL format, saved as mylog.smcl
log using mylog, text            // plain text, saved as mylog.log
log using "logs/mylog.log", replace
```

**Where does the log go?** In the working directory unless you give a path. See the [working directory guide](../lesson-01-getting-started/working-directory-guide.md) and use `"$logs/name.smcl"` as in the master do-file.

## 4. Anatomy of a log

The manual's example session produces a log like this:

```
      name:  <unnamed>
       log:  C:\Users\Stata User\Documents\base.smcl
  log type:  smcl
 opened on:  24 Mar 2025, 15:50:27

. sysuse auto
(1978 automobile data)

. by foreign, sort: summarize price mpg
 ... output ...

. * be sure to include the above stats in report!
. * now for something completely different
. corr price mpg
 ... output ...

. log close
      name:  <unnamed>
       log:  C:\Users\Stata User\Documents\base.smcl
  log type:  smcl
 closed on:  24 Mar 2025, 15:50:27
```

| Part | Meaning |
|------|---------|
| **Header** (name, log path, log type, opened on) | Identifies the log. It is part of the log file and helps when you have several logs |
| Lines starting with `. ` | The commands Stata ran |
| Output underneath | The results |
| Lines starting with `. *` | **Comments.** Stata ignores everything after the asterisk, so you can write any note. Comments are a good way to document your thinking and mark sections of the log for later |
| **Footer** (closed on) | Shows when logging stopped |

You can hide the header and footer with the `nomsg` option, or with `set logmsg off`.

> Closing the log with `log close` is good practice but not strictly necessary: logs are closed automatically when you exit Stata. In a do-file, close it anyway, so the log is complete and so a rerun can reopen the file.

## 5. SMCL or plain text?

Stata can save a log in two formats.

| | **SMCL** (`.smcl`) | **Plain text** (`.log`) |
|---|---|---|
| Full name | Stata Markup and Control Language | Plain text |
| Default? | **Yes** | No; use `text` or a `.log` extension |
| Preserves formatting, colour and links | **Yes** | No |
| Opens correctly in Stata's Viewer | Yes | Yes |
| Opens correctly in Notepad/Word | **No**: shows markup such as `{smcl}` and `{com}` | **Yes** |
| Easy to translate to other formats | **Yes** (to text, PDF, and so on) | Already text |
| Best for | Your own working record; printing from Stata | Sharing, editing, version control, emailing |

The manual recommends SMCL because it can be translated into a variety of formats readable by other applications with **File > Log > Translate...** (see `translate`).

**How the format is chosen**
- A `.smcl` extension forces SMCL; a `.log` extension forces text.
- With no extension, the format follows the default setting, which starts as SMCL.
- Change the default with `set logtype text, permanently`.

### Converting a log
```stata
translate "logs/session1.smcl" "logs/session1.log", replace
translate "logs/session1.smcl" "logs/session1.pdf", replace     // on Windows and Mac
```
Add `replace` to overwrite an existing target.

### Recommendation for this course
- During **interactive work**, log in **SMCL** for convenience.
- In **do-files** meant to be shared and kept in version control, log as **text** (`log using file.log, replace text`) so colleagues can open the log with any editor.
- Keep the log's name matched to the do-file's name: `02_clean.do` writes `02_clean.log`.

## 6. Replace, append and never overwriting by accident

Stata never overwrites an existing log by accident. If the file exists and you give neither option, the command fails and the do-file stops.

| Option | Effect | Use when |
|--------|--------|----------|
| `replace` | Overwrites the existing file | Rerunning a do-file that always rewrites its log |
| `append` | Adds to the end of the existing file (or creates it if none exists) | Continuing a long piece of work across sessions |
| *(neither)* | Error if the file exists | Protecting a log you must not lose |

```stata
log using "logs/analysis.smcl", replace      // fresh log each run
log using "logs/analysis.smcl", append       // add to the same log
```
Or use a different name for each run, such as a date: see section 14.

**Rule of thumb:** a do-file that you rerun again and again uses `replace`. Hand-run, exploratory sessions use `append`, or a new dated file.

## 7. Pausing, resuming and closing

| Command | Effect |
|---------|--------|
| `log off` | Suspends recording but keeps the file open |
| `log on` | Resumes recording |
| `log close` | Stops logging and closes the file |

```stata
log using "logs/session.smcl", replace
sysuse auto, clear
summarize price
log off                      // routine work here is not recorded
regress price mpg weight
log on                       // back on: capture the key command
regress price mpg weight
log close
```
The User's Guide offers this practical advice: log only the interesting parts. Run with `log off` during routine work, then `log on` and rerun the key command to capture its output. Be careful with this style: a log with gaps is a weaker audit trail. For formal analysis, log everything.

## 8. Checking the status of your logs

```stata
log query                    // status of the unnamed log
log query _all               // status of every open log
```
`log query` reports whether a log is on, off or closed, its file name and its format. After `log query _all`, the number of open logs is stored in `r(numlogs)`.

`log` on its own also reports status. The results are stored in `r()` (name, file name, status and type) so you can use them in code:

```stata
log query
return list
```
(If you are unsure of the exact form for "all logs" in your version, check `help log`.)

## 9. Multiple (named) logs

Stata allows more than one log open at once **only if the logs are named**. Use the `name()` option.

```stata
log using "logs/full.smcl", replace name(full)           // everything
log using "logs/results_only.log", replace text name(tables)
* ... work ...
log off tables                                          // pause just one
log on tables
log close tables                                        // close just one
log close full
```
Notes from the reference entry:
- The default name is `<unnamed>`.
- You can have up to **five SMCL logs and five text logs** open at once.
- `log close _all` closes every open log together.

Use cases: a complete log plus a smaller log of just the tables for the report; a log per analysis section.

## 10. Command logs with `cmdlog`

A **command log** records **only the commands you type**, as plain text, not the output. It is a quick way to build a do-file as you work.

```stata
cmdlog using "do/my_session.do", replace
sysuse auto
by foreign, sort: summarize price mpg
* be sure to include the above stats in report!
corr price mpg
cmdlog close
```
The result contains only commands and comments, so it can be used as a do-file:

```stata
sysuse auto
by foreign, sort: summarize price mpg
* be sure to include the above stats in report!
corr price mpg
```
Facts to remember:
- `cmdlog using file` records typed commands; `cmdlog close` stops; `cmdlog off` and `cmdlog on` suspend and resume.
- Command logs are **always plain text**. The default extension is `.txt`, so they do not overwrite your do-files by accident; give a `.do` extension yourself if you want that.
- Only **one** command log can be open at a time. You can run it **alongside** full logs.
- It records everything you type, including mistakes, so tidy the file before reuse.

| | `log` | `cmdlog` |
|---|-------|----------|
| Records commands | Yes | Yes |
| Records output | **Yes** | No |
| Format | SMCL or text | Text only |
| Typical use | Evidence of what happened | Building a do-file |
| Several at once | Yes, if named | One only |

## 11. Rescuing a session you forgot to log

You started working and then wish you had logged. Do not panic.

1. **History window.** It stores your last 5,000 commands. Right-click and use **Save all...** (or **Save selected...**) to write a do-file. The manual advises first filtering out the commands that gave errors. To move the commands straight into the Do-file Editor, **Select all** and then **Send selected to Do-file Editor**.
2. **`#review`.** The command `#review 100` lists your last 100 commands in the Results window. If a log is on, that list is recorded too.
3. **Re-run and log.** Put the rescued commands in a do-file, start a log, and run it again. You now have both the do-file and the log.

What you cannot recover is the *output* of the original session. That is why you log from the start.

## 12. Working with logs: view, search, copy, print, translate

### 12.1 Viewing
The manual says logs are best viewed in Stata's **Viewer**.

- **File > Log > View...** and locate the log file, or type `view logs/session1.smcl`.
- To view the **current** log, choose **File > Log > View...**; the path of the current log is already filled in, so click OK.

**Important:** the Viewer shows a **snapshot** of the log. It does not scroll as you keep working. If you need to see more recent results, click **Reload page**. This is an advantage over scrolling back in the Results window: what you are reading stays fixed. See the [Viewer guide](../lesson-01-getting-started/viewer-guide.md).

### 12.2 Searching
Use the Viewer's **Find** bar. Useful searches: `r(` to find error codes, `error`, a variable name, a comment such as `* CHECK`.

### 12.3 Copying
You can copy text from the Viewer and paste it into a word processor or text editor. You can even paste into the Command window or the Do-file Editor, but **copy only commands, not output**. It is fine to include the `.` prompt at the start of an echoed command, because Stata ignores it in the Command window. In a word processor, pasted text is unformatted: use a **fixed-width font** such as Courier or Courier New so the columns line up.

### 12.4 Printing
Open the log in the Viewer, then use the **Print** toolbar button, right-click > **Print...**, or **File > Print...**. A print settings dialog lets you fill in optional **Header**, **Name** and **Project** items and choose whether to print line numbers, a header and a logo. **Prefs...** sets the font (fixed-width fonts only), margins and colour scheme (monochrome, colour, or custom). You can also use `translate` to make a PostScript or PDF copy.

### 12.5 Plain-text logs in other programs
A plain `.log` can be opened, edited, formatted and printed in a text editor or word processor. Add headings and comments if you wish. Use a fixed-width font. You may want to associate the `.log` extension with a text editor in Windows.

### 12.6 Reading a log with a purpose
| Question | Look for |
|----------|----------|
| Did it finish? | The last lines: a `log close` footer or an error |
| What failed? | `r(` followed by a number; the line above it is the failing command |
| Which data were used? | The `use`/`import` line and the observation count |
| Why do two runs differ? | Compare the two logs side by side in Viewer tab groups |

## 13. Logging inside do-files

A do-file should look after its own log.

```stata
capture log close                         // closes a log left open by a failed earlier run
log using "logs/02_clean.log", replace text
* ... all your commands ...
log close
```

| Practice | Why |
|----------|-----|
| `capture log close` at the top | If an earlier run failed before `log close`, the log is still open and `log using` would fail |
| `replace` | So the do-file can be rerun; otherwise it stops if the log exists |
| `log close` at the end | Complete, closed log |
| Log name matches do-file name | Easy to match evidence to code |
| `set more off` | Avoids `--more--` pauses |

**An error stops the do-file before `log close`.** The log stays open and contains the error. That is helpful: read the end of the log. Add `capture log close` at the top of the next run.

**Master do-file pattern** (from the [do-file guide](do-file-guide.md)):
```stata
* 00_master.do
global root "C:/path/to/project"           // EDIT
cd "$root"
capture log close
capture mkdir "logs"
log using "logs/master.log", replace text
do "do/01_import.do"
do "do/02_clean.do"
do "do/03_analysis.do"
log close
```
If every step file also opens its own log, you get one log per step plus the master. Decide which design you want: **one master log for everything** (then step files do not open logs), or **one log per step** (then the master does not). Do not nest unnamed logs: Stata allows several logs only if they are named.

## 14. An audit trail inside your log

A log is more useful if it carries its own context. Put a block like this near the top of each analysis do-file after the log opens:

```stata
display "Date and time : `c(current_date)' `c(current_time)'"
display "Stata version : `c(stata_version)'"
display "Operating sys : `c(os)'"
display "User          : `c(username)'"
display "Working dir   : `c(pwd)'"
about
```
Also useful:

| Command | Adds to the log |
|---------|-----------------|
| `about` | Stata version, edition and licence information |
| `describe, short` | Observations, variables and size of the loaded data |
| `datasignature` | A compact fingerprint of the data, to prove the same data were used |
| `set seed 12345` | Makes random operations repeatable; record it |
| `assert` / `isid` | Tests that fail loudly and appear in the log |
| `* comments` | Reasons for decisions |
| `display "Step 3 done"` | Section markers |

### Dated log names
```stata
local today = string(date("`c(current_date)'", "DMY"), "%tdCCYY-NN-DD")
log using "logs/analysis_`today'.log", replace text
```
This gives `analysis_2026-10-24.log` style names that sort neatly. (The Getting Started manual shows a similar, more elaborate idea in its `profile.do` example, which starts a time-stamped log automatically every time Stata starts.)

## 15. Logs, privacy and GitHub

Logs contain whatever Stata printed, and that can include **data values**. In health, migration or survey work that can mean personal information.

**Do**
- Avoid `list` and `browse`-style output of identifiable records in logs you will share.
- Use `describe`, `summarize`, `tabulate` and counts instead of printing rows.
- Review a log before emailing it.
- Store logs in the project's `logs/` folder, outside any shared public folder.

**Do not**
- Put logs containing individual records on GitHub or in an email.

In this repository, `.gitignore` already contains `*.log` and `*.smcl`, so logs created while you practise are not uploaded by accident. If you deliberately want to publish an example log, give it a different name and add an exception, as done for `data/viewer_demo.smcl`. The Lesson 2 data are synthetic, so logs from them are safe to share.

## 16. Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| `log file already open` | An earlier log is still open (often after an error) | `log close`, or `capture log close` at the top |
| `file ... already exists` when starting a log | A log with that name exists and you gave no option | Add `replace` or `append`, or change the name |
| `file ... could not be opened` / path error | Folder does not exist, or no permission | `capture mkdir "logs"`; check the path and working directory |
| Log opens in Notepad as strange `{smcl}` text | It is an SMCL log | `view` it in Stata, or `translate` to text, or log as text |
| Log is empty or very short | Started late, or `log off` left on | Check `log query`; start at the top of the do-file |
| Log does not show the newest results in the Viewer | It is a snapshot | Click **Reload page** |
| Two copies of the output in batch runs | The do-file opens its own log and batch mode also logs | Use one or the other |
| `--more--` appears in the log | `set more on` | `set more off` |
| Table columns misaligned when pasted into Word | Proportional font | Use Courier New |
| Log has no graph | Logs record text only | `graph export "figs/name.png", replace` |
| Cannot open a second log | Both are unnamed | Give each a `name()` |
| Log filled the disk | Very large output | Use `quietly` for routine steps; avoid listing large datasets |

## 17. Practice exercises L1 to L12

Solutions are in `exercise-solutions/lesson-04/log-file-practice.do`. Try each first. Create a folder `logs` first (see the working directory guide).

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**L1 🟢 Start and stop.** Using the toolbar **Log** button, start a log called `first_log` in your `logs` folder. Run `sysuse auto, clear` and `summarize price mpg`. Add a comment starting with `*`. Close the log from the toolbar. What extension did Stata add?

**L2 🟢 By command.** Repeat L1 with commands only: `log using` ... `log close`. Open the result with **File > Log > View...** and identify the header, a command, an output block and a comment.

**L3 🟢 Replace.** Run your `log using` line from L2 a second time. What happens? Fix it with `replace`. Now try `append` and look at the log in the Viewer. What changed?

**L4 🟢 Text versus SMCL.** Create `plain.log` with `log using "logs/plain.log", text replace` (or with a `.log` extension) and `rich.smcl`. Open both in a text editor such as Notepad. Describe the difference.

**L5 🟡 Convert.** Use `translate` to turn `rich.smcl` into `rich.log`. Open it in a text editor. If your system supports it, also produce a PDF.

**L6 🟡 Pause and resume.** Start a log. Run three commands, `log off`, run two more, `log on`, run one more, `log close`. Which commands are in the log? Check with `log query` at each stage.

**L7 🟡 Snapshot.** Start a log, run `summarize price`, and open the current log in the Viewer. Run `summarize mpg`. Does it appear? What do you click to see it?

**L8 🟡 Two logs.** Open a full log named `full` and a text log named `tables`. Use `log off tables`, run a command, `log on tables`, and run another. Which log contains which commands? Close both with one command.

**L9 🟡 Command log.** Use `cmdlog using` to record a short session, including a comment, then `cmdlog close`. Open the result in the Do-file Editor. Is it ready to run? What did you need to tidy?

**L10 🟡 Rescue.** Without a log running, run six commands (one with a typing error). Use the History window and `#review 10`. Create a do-file from the good commands.

**L11 🔴 Self-logging do-file.** Write `log_demo.do` using the pattern in section 13: `capture log close`, a text log with `replace`, the audit block from section 14, and one deliberate error halfway. Run it. Where does the log end? What would you do before rerunning?

**L12 🔴 Master with one log.** Write a master do-file that runs two step files and records everything in one log. Run it. Then change it so that each step file has its own log. Compare. Which design would you choose for your team, and why?

## 18. Quick reference card

| Task | Command or menu |
|------|-----------------|
| Start a log (SMCL) | `log using file, replace` |
| Start a plain-text log | `log using file.log, replace text` |
| Add to a log | `log using file, append` |
| Close | `log close` |
| Pause / resume | `log off` / `log on` |
| Status | `log query` or `log` |
| Name a log | `log using file, name(x)` |
| Close one / all | `log close x` / `log close _all` |
| Quiet header and footer | `log using file, nomsg` or `set logmsg off` |
| Default format | `set logtype text, permanently` |
| Record commands only | `cmdlog using file.do` / `cmdlog close` |
| Last commands | `#review 100` |
| View a log | `view file.smcl` or **File > Log > View...** |
| Convert a log | `translate in.smcl out.log, replace` |
| Print | Open in the Viewer, **Print** |
| Log in a do-file | `capture log close` then `log using ..., replace` ... `log close` |
| Add a note | `* comment` |

## 19. Facilitator notes

**Timing (75-minute session):** 10 min why and what (sections 1 to 2), 15 min starting, anatomy and formats (3 to 5), 10 min replace, append, pause (6 to 8), 10 min named logs and cmdlog (9 to 11), 30 min exercises L1 to L10. L11 to L12 are take-home.

**Before the session**
- Participants should have a project folder with `logs/` (working directory guide) and know how to use the Viewer ([Viewer guide](../lesson-01-getting-started/viewer-guide.md)).
- Check write permission on the training PCs.
- Decide whether the group will log as SMCL or text in do-files and say so.

**Common stumbling blocks**
- `log using` fails because the file exists or a log is already open. Teach `replace` and `capture log close` together.
- Expecting graphs in logs.
- Opening SMCL in Notepad and thinking the file is corrupt.
- Forgetting `log close`, then finding the next run fails.
- Printing identifiable records into a log that will be shared.

**Teaching tips**
- Run a "crash" demonstration: log a session, force an error halfway through a do-file, and show that the log still contains everything up to the error.
- Ask pairs to swap logs and answer three questions from the log alone: what data were used, how many observations, and what failed.
- Compare the History window, `cmdlog` and a full log in a three-way table.

**Assessment prompt (5 minutes):** "Your do-file stops with an error before it reaches `log close`. The next day you rerun it and it stops at the first line with a log-related error. Why, and what two lines at the top prevent it?" Expected: the log is still open from the failed run; `capture log close` before `log using ..., replace`.

**Note on versions.** This guide follows the Windows edition of the Getting Started manual and the current reference entry for `log`. Menu names, the exact form for closing all logs, and the availability of PDF conversion differ across versions and systems. Check `help log`, `help cmdlog` and `help translate` in your own installation.
