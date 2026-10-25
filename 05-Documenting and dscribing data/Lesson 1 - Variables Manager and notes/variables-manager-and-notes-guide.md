# Learning Notes: The Variables Manager and Notes

**Part of:** Lesson 3, Cleaning and Labelling Data  |  **Read and practise:** about 75 minutes  |  **Dataset:** `auto` (built into Stata) and `data/anc_survey.dta` (in this repo)

Once a dataset has more than a few dozen variables, you can no longer keep it in your head. Which variables have no label? Which are stored as text but should be numbers? Which have a display format that hides decimals? What did the last analyst learn about the `income` variable and forget to tell you? The **Variables Manager** is Stata's control panel for exactly these questions, and **notes** are the memory that stays inside the dataset. This guide covers both. Its companion, the [describe and labels guide](describe-and-labels-guide.md), covers the command-line side.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 7 ("Using the Variables Manager"), with related material from chapters 6 and 9, and checked against the `[D] notes` and `[D] label` entries on stata.com. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Open the Variables Manager and explain what it is for
- Filter, sort, group and rearrange the variable list, and use grouping to find unlabelled variables
- Use the right-click menu to keep, drop, copy and send variable lists
- Edit the properties of one variable, or of many variables at once
- Add, edit, list, search and delete notes on the dataset and on variables, with time stamps
- Use the equivalent commands (`notes`, `rename`, `label`, `format`, `recast`) so that your work is reproducible
- Record Variables Manager actions in a do-file
- Use the Variables Manager and notes as part of a data-quality and documentation routine

## Contents
1. [What the Variables Manager is for](#1-what-the-variables-manager-is-for)
2. [Opening it](#2-opening-it)
3. [The Variable pane](#3-the-variable-pane)
4. [The right-click menu on the Variable pane](#4-the-right-click-menu-on-the-variable-pane)
5. [The Variable Properties pane](#5-the-variable-properties-pane)
6. [Working on many variables at once](#6-working-on-many-variables-at-once)
7. [Notes: documentation that travels with the data](#7-notes-documentation-that-travels-with-the-data)
8. [Managing notes in the Variables Manager](#8-managing-notes-in-the-variables-manager)
9. [The `notes` command in depth](#9-the-notes-command-in-depth)
10. [From clicks to code](#10-from-clicks-to-code)
11. [A documentation routine for a new dataset](#11-a-documentation-routine-for-a-new-dataset)
12. [Variables Manager, Variables window or Properties window?](#12-variables-manager-variables-window-or-properties-window)
13. [Troubleshooting](#13-troubleshooting)
14. [Practice exercises VM1 to VM12](#14-practice-exercises-vm1-to-vm12)
15. [Quick reference card](#15-quick-reference-card)
16. [Facilitator notes](#16-facilitator-notes)

---

## 1. What the Variables Manager is for

The manual describes the Variables Manager as a tool for managing the properties of variables **both individually and in groups**. You can use it to:
- create variable labels and value labels,
- rename variables,
- change display formats,
- manage notes,
- filter and group variables, and
- create variable lists.

The manual says users find these features especially useful for managing **large datasets**.

**Every action you take in the Variables Manager results in a command being issued to Stata, as though you had typed it in the Command window.** This is the key safety property: the command appears in the Results window, in the History window and in any log, so you can keep good records and learn commands as you go.

What the Variables Manager changes is the **data in memory**. As always, nothing is permanent on disk until you save (see the [opening and saving guide](../lesson-02-importing-exploring-data/opening-and-saving-dta-guide.md)).

| Use the Variables Manager to... | ...but prefer a do-file to... |
|---------------------------------|-------------------------------|
| Survey a dataset you have just received | Apply the same labels to next month's data |
| Find unlabelled variables quickly | Document and repeat the labelling |
| Change a property of many variables at once | Make a change that must be reproduced |
| Build a variable list for a command | Run that command in a script |
| Read and add notes | Keep a permanent record of why |

## 2. Opening it

Load a dataset first:

```stata
sysuse auto, clear
```
Then open the Variables Manager by either:
- selecting **Data > Variables Manager**, or
- clicking the **Variables Manager** button on the main toolbar.

(The command `varmanage` also opens it from the Command window.)

The Variables Manager is a separate window. Like the Data Editor, it is a *nondocking* window; but inside it, the **Variable Properties pane** is a docking window (section 5).

## 3. The Variable pane

The left pane of the Variables Manager shows the **list of variables in the dataset**. It has no explicit title on the screen, but the manual calls it the **Variable pane**. The columns show information such as the variable's position (#), name, label, type, format and value label.

### 3.1 Filtering
Type text into the **filter box** in the upper-left corner. The list narrows to variables whose names or labels match. This is a good way to zoom in on similarly named or labelled variables. Example: type `price` or `mileage`.

### 3.2 Sorting
Click a **column title** to sort the list:
1. The first click sorts **ascending**.
2. A second click on the same title sorts **descending**.
3. Clicking the **hash mark (#)** restores the original variable order.

**The sort affects only how variables appear in the Variables Manager. The dataset itself stays the same.**

### 3.3 Rearranging columns
Drag the column titles to change their order. To restore the original headings, right-click the column titles and select **Restore column defaults**.

### 3.4 Grouping
You can **group** variables by the values in one or more columns:
1. Drag a column title into the **grouping bar** above the list.
2. The variables are gathered into collapsible groups.
3. To cancel the grouping, drag the title back into the column titles row.

Examples (the manual shows grouping `auto.dta` by variable type):

| Group by... | What you learn |
|-------------|----------------|
| **Type** | Which variables are strings, which are `byte`, `int`, `float`... |
| **Format** | Which variables display with which format |
| **Value label** | Which variables share a label set, and which have none |
| **Label** | **A good way to find unlabelled variables**: they gather in one group with an empty label |

> **Quality tip:** when you receive a new dataset, group by label and by type. Variables without labels and numeric variables stored as `str` stand out in seconds.

## 4. The right-click menu on the Variable pane

Right-clicking in the Variable pane displays a menu of common tasks:

| Item | What it does |
|------|--------------|
| **Edit variable properties** | Moves focus to the Variable Properties pane (and shows it if it was auto-hidden) |
| **Keep only selected variables** | Keeps the selected variables in the dataset and **drops all the others** |
| **Drop selected variables** | Drops the selected variables from the dataset |
| **Manage notes for selected variable...** | Opens a window to add and delete notes for **one** variable. Disabled if several variables are selected |
| **Manage notes for dataset...** | Opens a window to add and delete notes for the dataset as a whole |
| **Copy varlist** | Copies the names of the selected variables to the Clipboard |
| **Select all** | Selects all **visible** variables (variables hidden by the filter are not selected) |
| **Send varlist to Command window** | Inserts the names of the selected variables into the Command window |
| **Print...** | Prints the Variable pane; change the printed column widths by changing the widths in the Variables Manager |

### Building variable lists
The combination of **filter, sort, group and Send varlist to Command window** is a fast way to create variable lists in large datasets. For example:
1. Filter for `Q1`.
2. Select all.
3. Choose **Send varlist to Command window**.
4. Type your command in front: `summarize ` and press Enter.

You can then paste the list into a do-file. Better still, use wildcards and ranges (`Q1*`, `price-weight`) in code.

### Caution on Keep/Drop
Both **Keep only selected variables** and **Drop selected variables** alter the data in memory. They are not recorded as something you can undo. The commands issued (`keep ...` and `drop ...`) appear in the Results window; take a snapshot or save first (see the [Data Editor guide](../lesson-02-importing-exploring-data/data-editor-guide.md)).

## 5. The Variable Properties pane

The **Variable Properties pane** is where you change properties of the variable(s) selected in the Variable pane.

- With **one variable** selected, you can manipulate **all** its properties.
- With **many variables** selected, you can change their **formats or types** and assign **value labels** all at once.

The fields work the same way as in the Properties window described in the [Data Editor guide](../lesson-02-importing-exploring-data/data-editor-guide.md):

| Property | What it is | Command equivalent |
|----------|-----------|--------------------|
| **Name** | The variable's name | `rename old new` |
| **Label** | Descriptive text | `label variable name "text"` |
| **Type** | Storage type (`byte`, `int`, `long`, `float`, `double`, `str#`) | `recast type name` (or `compress`) |
| **Format** | How values are displayed | `format name %fmt` |
| **Value label** | The label set attached | `label values name labelname` |
| **Notes** | Notes attached to the variable | `notes name: text` |

### A docking window
The Variable Properties pane is in fact a **docking window**, like those in the main Stata window (see the [docking windows guide](../lesson-01-getting-started/docking-windows-guide.md)). Click its **pushpin** to make it auto-hide when not in use, or drag it by its title bar to another docking guide to reposition it within the Variables Manager.

### Rules for variable names
(As in the Data Editor guide.) Names are case sensitive, 1 to 32 characters, letters/digits/underscores, must not start with a digit, and should not start with an underscore. Use lowercase.

## 6. Working on many variables at once

This is where the Variables Manager beats the Data Editor. Typical bulk jobs:

| Job | How |
|-----|-----|
| Give the same value label to all yes/no variables | Filter or group; select them; set **Value label** to the shared label |
| Set a common display format | Select; set **Format** (e.g. `%9.2f` for all lab values) |
| Change storage type for a group | Select; set **Type** |
| Create a variable list | Select; **Send varlist to Command window** |
| Drop a set of temporary variables | Filter on the prefix; **Select all**; **Drop selected variables** |
| Keep a working set | Select; **Keep only selected variables** |

**Example with the ANC survey.** `anc_survey.dta` stores `education`, `wealth_quintile`, `facility_delivery` as numbers without labels. In the Variables Manager you can select `facility_delivery` and set a value label; for several variables sharing the same coding (such as 0 = No, 1 = Yes), define one label and attach it to all of them.

**Good practice.** For repeated work, bulk commands in a do-file are better than clicking:
```stata
label define yesno 0 "No" 1 "Yes"
label values facility_delivery yesno
```
The Variables Manager creates the same commands, so use it to learn them.

## 7. Notes: documentation that travels with the data

Stata allows you to attach **notes** to both variables and the dataset as a whole. The manual calls them *simple text notes that you can use to document whatever you like*: the source of the dataset, data-collection quirks associated with a variable, what you need to investigate about a variable, or anything else.

Why notes are valuable:
- **They are stored in the `.dta` file** and come back when you `use` it. Documentation cannot get separated from the data.
- They answer later questions: "Why is this variable missing for Kano?" "Who recoded `hb`?"
- They survive hand-offs between colleagues.
- Manual: *Notes can be an invaluable memory aid when working on projects that last a long time.*

What belongs in a note:

| Dataset notes | Variable notes |
|---------------|----------------|
| Source and date received | Units and collection method |
| Who cleaned it, and when | Known problems (e.g. `99` means "not recorded") |
| The version and the do-file that produced it | Recoding decisions and who authorised them |
| Key decisions (duplicates removed) | Questions to follow up |

What does **not** belong in a note: long reports (use a separate document), personal data, passwords.

## 8. Managing notes in the Variables Manager

### 8.1 For a variable
1. Select the variable in the Variable pane (for example `price`).
2. In the **Variable Properties** pane, click the **Manage...** button next to the **Notes** field. (Or right-click the variable > **Manage notes for selected variable...**.)
3. The notes dialog appears.
4. Click **Add** to add a note.
5. Type your text. Typing **`TS `** (the letters TS followed by a trailing space) inserts a **timestamp** in the note. For example: `TS - started working`.
6. Add more notes, and experiment with editing and deleting.

### 8.2 For the dataset
Right-click in the Variable pane > **Manage notes for dataset...** and use the same dialog.

The manual adds: *Anytime you manipulate notes in the Notes Manager, you create Stata commands.*

### 8.3 What it looks like
After adding notes to `price` you can see them in the Results window as commands such as:

```
. note price: TS - started working
```
and read them back with `notes price` or `describe`.

## 9. The `notes` command in depth

`note` and `notes` are synonyms.

### 9.1 Adding notes
```stata
notes: Data obtained from the State Ministry of Health, 2026-10-25.     // dataset note
notes price: TS - recorded in 1978 US dollars.                          // variable note
notes hb: 99 means "not measured"; recode to missing in 02_clean.do.
```
The syntax is `notes [varname]: text`. With no variable name the note is attached to the **dataset** (stored internally as `_dta`).

### 9.2 Time stamps
If the text contains **`TS`** in capital letters, surrounded by blanks, Stata replaces it with the **current date and time**. This documents *when* the note was written without typing the date.

### 9.3 Listing and searching
```stata
notes                       // list all notes (dataset and variables)
notes list price            // notes for price
notes list price in 2       // note number 2 for price
notes search hb             // search all notes for the text "hb"
```
`describe` also tells you if there are notes: the header line shows `(_dta has notes)` for dataset notes (and `describe` flags variable notes in its listing).

### 9.4 Numbering
Notes are numbered from 1 for each variable and for the dataset.
- **Dropping a note does not renumber the others**, and new notes are added after the highest-numbered existing note.
- Use `notes renumber varname` to close the gaps.

### 9.5 Replacing and dropping
```stata
notes replace price in 2: TS - corrected currency note.
notes drop price in 1       // delete note 1 for price
notes drop price            // delete all notes for price
notes drop _dta             // delete all dataset notes
notes drop all              // delete everything (note: plain "notes drop" does not do this)
```
**Typing `notes drop` alone does not delete everything**; to delete all notes you must specify `all`. That is a safety feature.

### 9.6 Saving
**Notes are part of the dataset.** Additions and deletions take effect on disk only when you `save` the dataset. If you add a note and then reload the file without saving, the note is lost.

### 9.7 Limits
Up to 9,999 notes for the dataset and 9,999 notes per variable; each note can be very long (tens of thousands of characters in the standard editions). In practice, keep notes short.

### 9.8 Formatting notes
Notes may contain SMCL directives, such as `{cmd:...}`, which display formatted when listed. Use sparingly.

### 9.9 Notes and characteristics
Notes are stored as *characteristics* of the dataset and variables. Characteristics (`char`) are a more general tool for attaching information; see `help char`. For routine documentation, notes are sufficient.

## 10. From clicks to code

Everything you do in the Variables Manager appears in the Results and History windows. To make your work reproducible:

1. Do the changes in the Variables Manager.
2. In the **History** window select the commands that came from it (click the first, Shift-click the last).
3. **Right-click > Send selected to Do-file Editor**.
4. Add a header, comments and `, clear` on the load line; save as `03_labels.do`.
5. Restart Stata and run the do-file from a clean start. Do you get the same dataset? (See the [do-file guide](../lesson-04-do-files-and-log-files/do-file-guide.md).)

For a log of what you did, start a log first (see the [log file guide](../lesson-04-do-files-and-log-files/log-file-guide.md)).

Typical commands you will see:

```stata
rename var2 price
label variable price "Price in US dollars"
format price %9.0fc
label define repairs 1 "atrocious" 2 "bad" 3 "OK" 4 "good" 5 "stupendous"
label values rep78 repairs
notes price: TS - started working
drop trunk
keep make price mpg weight
```

## 11. A documentation routine for a new dataset

When a dataset arrives, spend 15 minutes on this routine, in the Variables Manager and then in a do-file:

1. **Open** it and `describe`. How many variables? What types?
2. **Variables Manager:** group by **Label**. Which variables have none?
3. **Group by Type:** are any numeric variables stored as strings?
4. **Group by Value label:** which categorical variables are unlabelled?
5. **Sort by Name:** do names follow a pattern? Any with capitals or odd characters?
6. **Add dataset notes:** source, date received, who sent it.
7. **Add variable notes** where you know a quirk (a `99` code, a unit, a filter).
8. **Write the labels in a do-file** (`label variable`, `label define`, `label values`).
9. **Save** under a new name; keep the raw file untouched.
10. **Re-run** the do-file from a clean start to prove it works.

Apply it to `anc_survey.dta`: group by label and you will find that **every** variable is unlabelled. That is your Lesson 3 job.

## 12. Variables Manager, Variables window or Properties window?

| Tool | Where | Best for |
|------|-------|----------|
| **Variables window** | Main Stata window | Quick list of names; double-click to paste a name |
| **Properties window** | Main Stata window | Viewing/editing properties of the one selected variable |
| **Variables Manager** | Separate window | Survey and edit **many** variables; filter, sort, group; notes; varlists |
| **Data Editor** | Separate window | Seeing values; entering data |
| **Commands** (`describe`, `label`, `notes`) | Do-files | **Reproducible** work |

## 13. Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Properties cannot be edited | Properties window locked (main window) | Unlock, or use the Variables Manager |
| "Manage notes for selected variable" is greyed out | More than one variable selected | Select one variable |
| Some variables not selected by **Select all** | Hidden by the filter | Clear the filter |
| Sorted list but dataset order unchanged | The sort affects only the display | Expected. Use `order` in a do-file to change dataset order |
| Notes disappeared after reloading | Not saved | `save, replace` after adding notes |
| Notes appear to be missing numbers (1, 3, 4) | A note was dropped; numbering is not changed | `notes renumber varname` |
| `notes drop` did not delete everything | Needs an argument | `notes drop all` |
| TS did not become a timestamp | Not capitals or no surrounding blanks | Type ` TS ` with spaces |
| Label not applied to a group | Mixed types selected | Select variables with the same coding |
| Cannot find a variable | Filter active | Clear the filter text |
| Changed my mind after **Keep only selected** | Variables dropped from memory | Restore a snapshot, or reload the file |

## 14. Practice exercises VM1 to VM12

Solutions for the command-based parts are in `exercise-solutions/lesson-03/variables-manager-practice.do`. Use `auto` unless told otherwise.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**VM1 🟢 Open it.** Load `auto` and open the Variables Manager by the menu, then by the toolbar button. How many variables are listed? What columns are shown?

**VM2 🟢 Filter and sort.** Filter for `mpg`, then for `weight`. Clear the filter. Sort by name (ascending, then descending), then by type. Restore the original order with the hash mark. Open the Data Editor in browse mode: has the order of columns changed?

**VM3 🟢 Group.** Group the variables by **type**. How many `int` variables? Cancel the grouping. Group by **label**. Are there any unlabelled variables in `auto`?

**VM4 🟢 Right-click tour.** Select three variables and use **Copy varlist**. Paste into a do-file. Then **Send varlist to Command window**, type `summarize ` in front, and press Enter.

**VM5 🟡 One variable.** Select `price`. Change its label to `Price (US dollars)`. Change its format so it shows commas. What commands appear in the Results window?

**VM6 🟡 Many variables.** Select `price`, `weight` and `length`. Set the same display format for all three in one step. How would you do this in one command? (Hint: `format price weight length %9.0fc`.)

**VM7 🟡 Notes on a variable.** Add three notes to `price`. Use `TS ` in one. Edit one and delete one. Run `notes price` and `notes list price`. Are the remaining notes still numbered 1, 2, 3?

**VM8 🟡 Dataset notes.** Add two dataset notes (source and cleaning date). Then run `describe, short`. What does the header say about notes? Save the dataset as `auto_notes.dta` and reload it. Are the notes still there?

**VM9 🟡 Searching.** Add notes to three variables, each mentioning "check". Use `notes search check`. Then use `notes drop` on one variable and `notes renumber`. Explain the difference between `notes drop` and `notes drop all`.

**VM10 🟡 Find the unlabelled variables.** Load `data/anc_survey.dta`. In the Variables Manager group by label. Write the names of the unlabelled variables. How many are there? Which five would you label first, and why?

**VM11 🔴 From clicks to code.** On `anc_survey.dta`, use the Variables Manager to: label `age` ("Age in completed years"), format `weight_kg` with one decimal, add a note to `hb` that blank means "not measured", and add a dataset note about the source. Send the commands from History to the Do-file Editor, save as `03_vm_changes.do`, and run it from a clean start.

**VM12 🔴 Design a notes policy.** Write half a page for your team: what must dataset notes contain, what must variable notes contain, who writes them, and when? Include the exact `notes` commands you expect.

## 15. Quick reference card

| Task | How |
|------|-----|
| Open the Variables Manager | **Data > Variables Manager**, toolbar button, or `varmanage` |
| Filter the list | Filter box (upper left) |
| Sort the list | Click a column title (again for descending); `#` restores original order |
| Group | Drag a column title to the grouping bar |
| Restore columns | Right-click titles > **Restore column defaults** |
| Copy names | Right-click > **Copy varlist** |
| Paste names into the Command window | Right-click > **Send varlist to Command window** |
| Keep / drop selected | Right-click > **Keep only selected variables** / **Drop selected variables** |
| Edit one variable | Variable Properties pane |
| Edit many | Select several; change **Format**, **Type**, **Value label** |
| Variable notes | **Manage...** next to Notes; or right-click > **Manage notes for selected variable...** |
| Dataset notes | Right-click > **Manage notes for dataset...** |
| Time stamp in a note | Type `TS ` (capitals, with blanks) |
| Add a note (command) | `notes [varname]: text` |
| List / search notes | `notes`, `notes list varlist`, `notes search text` |
| Replace / drop | `notes replace varname in #: text`, `notes drop varlist in #`, `notes drop all` |
| Renumber | `notes renumber varname` |
| Keep notes | `save, replace` |
| Make it reproducible | History > **Send selected to Do-file Editor** |

## 16. Facilitator notes

**Timing (75-minute session):** 10 min why and how to open (sections 1 to 2), 15 min Variable pane and right-click menu (3 to 4), 10 min Variable Properties and bulk edits (5 to 6), 15 min notes (7 to 9), 25 min exercises VM1 to VM9. VM10 to VM12 are take-home or a group task.

**Before the session**
- Participants should be comfortable with the Data Editor ([Data Editor guide](../lesson-02-importing-exploring-data/data-editor-guide.md)) and with saving files.
- Have the Variables and Properties windows visible (see the [docking windows guide](../lesson-01-getting-started/docking-windows-guide.md)).
- Make sure everyone saves `anc_survey.dta` under a new name before experimenting.

**Common stumbling blocks**
- Thinking sorting the Variables Manager list changes the dataset.
- Expecting notes to survive without saving.
- Selecting several variables and wondering why "Manage notes" is disabled.
- Dropping variables with **Keep only selected** and not realising it.
- Believing changes made by clicking will be repeated automatically next time.

**Teaching tips**
- Start with a "mystery dataset": a dataset with unlabelled, oddly named variables. Ask the group to find three problems in two minutes using only grouping.
- Run the notes demo twice: once with a save, once without, to show why `save` matters.
- Have pairs trade datasets and read each other's notes. The reader should be able to say where the data came from and what was done to them.

**Assessment prompt (5 minutes):** "You added five notes to `hb`, then saved nothing and reloaded the file. What do you find, and what does `notes drop` with no argument do?" Expected: the notes are gone because they are part of the data and need a `save`; `notes drop` alone does not delete anything, you need `notes drop all` or a varlist.

**Note on versions.** This guide follows the Windows edition of the Getting Started manual and the current reference entries. Dialog names and the layout of the Variables Manager differ slightly across versions and systems. Check `help varmanage`, `help notes` and `help label` in your own installation.
