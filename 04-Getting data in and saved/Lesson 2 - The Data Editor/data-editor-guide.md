# Learning Notes: The Data Editor

**Part of:** Lesson 2, Importing and Exploring Data  |  **Read and practise:** about 90 minutes  |  **Dataset:** `auto` and `sp500` (built into Stata) and `data/anc_survey.dta` (in this repo)

The Data Editor is the spreadsheet-like window onto your data. It looks friendly, which is exactly why it is dangerous: one stray keystroke can change a value and leave no trace in your do-file. This guide teaches you to use the Data Editor **well**: to look at data safely, to restrict what you see, to make deliberate edits that are recorded, and to turn point-and-click work into reproducible code.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 6 ("Using the Data Editor"), and checked against the `[D] edit` entry on stata.com. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Open the Data Editor in **browse** or **edit** mode and explain why browse is the default for professionals
- Navigate quickly and use the Cursor Location box
- Enter data by hand and understand missing values, strings and types
- Use the Variables, Properties and Snapshots windows with the Data Editor
- Rename, label and format variables, and create value labels
- Copy, paste, sort, find, filter, hide, drop and add data
- Work with dates and the date input mask
- **Limit your exposure** when you must edit, using `edit varlist if ...`
- Recover the commands the Data Editor ran and turn them into a do-file
- Decide when *not* to use the Data Editor

## Contents
1. [What the Data Editor is, and the case for caution](#1-what-the-data-editor-is-and-the-case-for-caution)
2. [Opening it: edit mode versus browse mode](#2-opening-it-edit-mode-versus-browse-mode)
3. [The window and its toolbar](#3-the-window-and-its-toolbar)
4. [Moving around](#4-moving-around)
5. [The right-click menu](#5-the-right-click-menu)
6. [Entering data by hand](#6-entering-data-by-hand)
7. [Missing values, strings and types](#7-missing-values-strings-and-types)
8. [Renaming, labelling and formatting variables](#8-renaming-labelling-and-formatting-variables)
9. [Value labels](#9-value-labels)
10. [Copying and pasting](#10-copying-and-pasting)
11. [Changing data: find, sort, replace, drop, add](#11-changing-data-find-sort-replace-drop-add)
12. [Dates in the Data Editor](#12-dates-in-the-data-editor)
13. [Filtering and hiding: limiting your exposure](#13-filtering-and-hiding-limiting-your-exposure)
14. [Snapshots: temporary safety nets](#14-snapshots-temporary-safety-nets)
15. [From clicks to code: recovering the commands](#15-from-clicks-to-code-recovering-the-commands)
16. [When not to use the Data Editor](#16-when-not-to-use-the-data-editor)
17. [Troubleshooting](#17-troubleshooting)
18. [Practice exercises E1 to E12](#18-practice-exercises-e1-to-e12)
19. [Quick reference card](#19-quick-reference-card)
20. [Facilitator notes](#20-facilitator-notes)

---

## 1. What the Data Editor is, and the case for caution

The Data Editor gives a **spreadsheet-like view of the data currently in memory**. You can use it to enter new data, edit existing data, search the data, and edit attributes of the data such as variable names, labels, display formats and value labels. Two companion windows, the **Variables** window and the **Properties** window, sit beside it and work like their namesakes in the main Stata window.

**Every action you take in the Data Editor is issued to Stata as a command, as though you had typed it in the Command window.** The command appears in the Results window and the History window. This means you can keep a record and learn commands from what the Data Editor does.

Now the caution, in the manual's words: *a small mistake in the Data Editor can cause large problems in your dataset.*

| Spreadsheet habit | Why it is risky in Stata |
|-------------------|--------------------------|
| Type over a cell to "fix" it | The change is made to the data in memory, with no explanation, and may not be in your do-file |
| Sort by clicking | Changes the order of rows; can affect reproducibility of anything that depends on order |
| Paste over cells | **Overwrites existing data**, and is not recorded as a normal command |
| Delete a column | The variable is gone from memory |
| Scroll with the keyboard in edit mode | A keypress can enter a value |

Rule of this course: **explore in browse mode; change data in a do-file.** When you must edit by hand, limit your exposure (section 13) and keep the record (section 15).

## 2. Opening it: edit mode versus browse mode

| | **Edit mode** | **Browse mode** |
|---|---------------|-----------------|
| Toolbar button | **Data Editor (Edit)** | **Data Editor (Browse)** |
| Command | `edit` | `browse` |
| Changes by typing | Allowed | **Disabled** |
| Menu items that alter data, labels or formats | Enabled | **Disabled** (you can still view a variable's properties) |
| Filter observations / hide variables | Yes | Yes |
| Sorting | Yes | Allowed, unless an `if` or `in` restricts the data |
| Pasting | Yes | **Not available** |

The manual's recommendation: **use the Data Editor in browse mode and switch to edit mode only when you want to make changes.** You can switch modes with the **Edit mode** and **Browse mode** buttons on the Data Editor's own toolbar.

Note: browse mode only restricts the Data Editor *itself*. You can still type commands in the Command window and use other menus, so you can watch the effect of your commands on the data.

### Command syntax
```stata
browse                          // all variables, all observations
browse make price mpg           // only these variables
browse make price if price > 10000
edit make rep78 if missing(rep78)
browse in 1/20                  // only the first 20 observations
browse, nolabel                 // show underlying numbers instead of value labels
```
General form: `edit [varlist] [if] [in] [, nolabel]` and `browse [varlist] [if] [in] [, nolabel]`. The varlist limits **columns**; `if` and `in` limit **rows**.

### Three working states
- **Full-edit:** `edit` or `edit varlist` with nothing omitted. All features available.
- **Filtered:** entered when `if` or `in` actually leaves out data, or when you filter inside the editor. Sorting and pasting are turned off.
- **Browse:** typing changes are disabled.

## 3. The window and its toolbar

The Data Editor toolbar contains:

| Button | Purpose |
|--------|---------|
| **Edit mode** | Switch to edit mode |
| **Browse mode** | Switch to safe browse mode |
| **Open** | Open a Stata dataset. Stata warns you if the current dataset has unsaved changes |
| **Save** | Save the dataset shown in the editor |
| **Print** | Print the data |
| **Copy** | Copy the selection to the Clipboard |
| **Paste** | Paste the Clipboard; only if one cell is selected, which becomes the upper-left corner of the pasted block. **Warning: this pastes over existing data** |
| **Find** | Open the Find bar |
| **Filter observations** | Show only observations meeting a condition |

Other parts of the window:
- **Cursor Location box:** shows the active cell as `varname[obsnum]`, for example `price[4]`, and doubles as a navigation tool.
- **Time/Date input mask:** a field in the upper-right corner (DMY, MDY or YMD) that controls how you type dates (section 12).
- **Variables, Properties and Snapshots windows:** beside the data table.
- **Colour coding:** string values, value labels and all other values are shown in different colours. (The `edit` reference lists red for strings, blue for value labels and black for other values.) Change colours via right-click > **Preferences...**

## 4. Moving around

| To move | Press |
|---------|-------|
| Right | **Tab** or right arrow |
| Left | **Shift+Tab** or left arrow |
| Down | **Enter** or down arrow |
| Up | **Shift+Enter** or up arrow |
| To a specific cell | Type `varname obsnum` in the Cursor Location box, for example `rep78 74`, and press Enter |
| Select a column | Click the variable name / column heading |
| Select a row | Click the observation number / row heading |
| Select a range | Click and drag |
| Cancel an entry in progress | **Esc** |
| Edit inside a cell | Double-click the cell; then left/right arrows move within the text |

**Context-sensitive arrows:** if you select a cell and type new data, an arrow key *accepts* the change and moves on. If you double-click and edit inside the cell, the arrows move within the text. Be aware which state you are in.

## 5. The right-click menu

Right-clicking in the Data Editor gives a menu of common tasks.

| Item | What it does |
|------|--------------|
| **Copy / Paste / Paste special...** | Clipboard actions; *Paste special* gives control of delimiters with a preview |
| **Select all** | Selects all data *displayed*, which may differ from the dataset if data are filtered or variables hidden |
| **Data > Insert variable...** | Create a variable at the current cursor position |
| **Data > Add variable...** | Create a variable at the beginning or end |
| **Data > Replace contents of variable...** | Replace the values of the selected variable |
| **Data > Insert observations... / Add observations...** | Insert empty observations at the cursor / at the end |
| **Data > Sort data...** | Sort by the selected variable |
| **Data > Value labels** and **Manage value labels...** | Work with value labels |
| **Data > Keep only selected data** | Keep the selection; **all remaining data are dropped from memory** (not from disk) |
| **Data > Drop selected data** | Drop the selection; possible only if the selection consists of entire variables (columns) or observations (rows) |
| **Data > Convert variables from string to numeric... / numeric to string...** | Convert types (useful when strings contain formatting characters such as commas) |
| **Data > Encode string variable to labeled numeric... / Decode labeled numeric variable to string...** | Convert categories between text and labelled numbers |
| **Pin selected row or column** | Keep rows or columns visible while scrolling |
| **Reset selected column widths** | Restore default widths |
| **Hide selected variables / Show only selected variables / Show entire dataset** | Control what is displayed; **Show entire dataset** turns off all filters and unhides all variables |
| **Preferences... / Font...** | Display settings |

## 6. Entering data by hand

The Data Editor is a handy place to key in a **small** table. Follow the manual's example (work through it yourself):

| Make | Price | MPG | Weight | Gear ratio |
|------|-------|-----|--------|-----------|
| VW Rabbit | 4697 | 25 | 1930 | 3.78 |
| Olds 98 | 8814 | 21 | 4060 | 2.41 |
| Chev. Monza | 3667 | *(unknown)* | 2750 | 2.73 |
| AMC Concord | 4099 | 22 | 2930 | 3.58 |
| Datsun 510 | 5079 | 24 | 2280 | 3.54 |
| *(unknown)* | 5189 | 20 | 3280 | 2.93 |
| Datsun 810 | 8129 | 21 | 2750 | 3.55 |

1. Save your current dataset if needed, then type `clear` in the Command window. (As a check on whether your data have changed, type `describe, short` or `d,s`.)
2. Open the Data Editor in **edit mode**: click **Data Editor (Edit)** or type `edit`. The active cell is `var1[1]`.
3. Enter the data **observation by observation**: type a value, press **Tab**, and continue across the row. After the **first** observation is complete, Stata knows the number of variables, so **Tab at the end of a row jumps to the first cell of the next row.**
4. Alternatively enter **variable by variable** by pressing **Enter** between values down a column. Press Enter twice to skip a missing value.
5. Skip missing values by tabbing (or pressing Enter) through them.

### Notes on data entry
- **No blank columns or rows in the middle.** Always begin new variables or observations in the first empty column or row. If you skip, Stata fills the gap with missing values.
- **Strings and value labels are colour-coded.**
- **A period (`.`) is the system missing value** for numbers.
- **The Tab key is smart** after the first observation (above).
- **No quotes needed for strings** once Stata knows a variable is text. For a first value that looks like a number but should be text (such as a ZIP or ID code with a leading zero), use quotes on the first entry: `"02173"`.
- **Esc** throws away an entry in progress.
- The cell editor for strings can be **resized** to show more text.

## 7. Missing values, strings and types

### 7.1 Missing values
| Symbol | Meaning |
|--------|---------|
| `.` | System missing value (default) |
| `.a` to `.z` | Extended missing values, to record *why* a value is unknown (for example `.a` = refused, `.b` = not applicable) |

Key facts, illustrated in the manual by sorting `rep78` in `auto`:
- Stata treats missing values as **larger than every nonmissing number**: `. < .a < .b < ... < .z`, and all of them are greater than any real number.
- Therefore `rep78 >= .` is equivalent to `missing(rep78)`.
- The consequence is the trap from Lesson 2: **`if hb >= 11` includes observations with missing `hb`.** Use `if hb >= 11 & !missing(hb)`.

### 7.2 Storage types change as you type
According to the `edit` reference, typing a value that needs more storage **changes the variable's type**: an `int` receiving `22.5` becomes a `float`; a `str4` receiving `"alpha"` becomes a `str5`. A new variable's type is set by its **first entry** (a quoted number creates a string). Numeric variables are not converted to strings unless they contain only missing values.

Practical lesson: if you type text in a numeric column by accident, the data may refuse it or behave unexpectedly. Check types with `describe`.

### 7.3 Strings
- `strL` values can be edited only if 2,045 characters or fewer, and binary `strL` cannot be edited.
- Never type spaces at the start or end of a text value by accident; they make values look the same but not match.

## 8. Renaming, labelling and formatting variables

New variables arrive as `var1`, `var2`, and so on. Fix them with the **Properties** window.

Steps (for `var2`, which will become `price`):
1. Click the variable in the **Variables** window; its properties appear in the **Properties** window.
2. Double-click the **Name** field and type `price`.
3. Under **Label**, type a description such as `Price in dollars`.
4. Click the **Format** field (`%9.0g`), then the **ellipsis (...)** button: the **Create format** dialog opens. Tick **Use commas in numeric output**, then **OK**.
5. In **Notes**, click the ellipsis, then **Add**, type a note, **Submit**, then **Close**. Expand the disclosure control to see the note.

Behind the scenes these steps issue commands you can reuse:

| Click action | Command |
|--------------|---------|
| Change the name | `rename var2 price` |
| Enter a label | `label variable price "Price in dollars"` |
| Change the format | `format price %9.0fc` |
| Add a note | `note price: text of the note` |

### Rules for variable names
- Stata is **case sensitive**: `Make`, `make` and `MAKE` are different names. **Use lowercase** to avoid trouble.
- A name must be **1 to 32 characters**.
- Characters can be letters, digits, underscores, or Unicode characters that are not symbols.
- **No spaces or other characters.**
- The first character must be a letter, an underscore, or a Unicode character. **Do not start with an underscore**: such names are used for temporary variables in Stata.

For example: `gear_ratio`, not `gear ratio`.

## 9. Value labels

A **value label** attaches words to numeric codes (1 = "atrocious", 2 = "bad", and so on), so tables show readable text while the data stay numeric.

Following the manual's example with `rep78` in `auto`:
1. Select `rep78` in the Variables window.
2. In Properties, click the **Value label** field, then the ellipsis: **Manage value labels** opens.
3. Click **Create label**; name it `repairs`.
4. Type a **value** (1), press **Tab**, type its **label** (`atrocious`), press **Enter** to create the pair. Repeat: 2 `bad`, 3 `OK`, 4 `good`, 5 `stupendous`. Click **OK**.
5. Expand the disclosure control to check; **Edit label** to correct.
6. Close the dialog. In the **Value label** drop-down, choose `repairs` to attach it to `rep78`.

Commands behind the scenes:
```stata
label define repairs 1 "atrocious" 2 "bad" 3 "OK" 4 "good" 5 "stupendous"
label values rep78 repairs
```

Also helpful: for a cell with a missing value, right-click and choose **Data > Value labels > Assign value from value label "repairs"** to choose from a list. This helps when a label has many values.

**Copy with labels or numbers.** When copying variables with value labels you can copy the **text** (default) or the **underlying numbers**. For the latter select **View > Show all value labels**. See also `browse, nolabel`.

> Value labels are covered in full in Lesson 3 (Cleaning and Labelling).

## 10. Copying and pasting

A simple way to get a small table into Stata from a spreadsheet or database.

1. **Select** the data: click a column heading for a column, a row number for a row, or drag across a range.
2. **Copy**: right-click inside the selection > **Copy**.
3. **Paste**: right-click the **top-left cell** of the target area > **Paste**.

Example from the manual: click the observation number of the first observation (selecting the row), copy it, click the first cell in row 8, and paste: the observation is duplicated.

Notes:
- The external application must copy tables in a **delimited** form, as spreadsheets and many databases do. Easiest test: try it.
- If a simple paste does not give what you expect, use **Edit > Paste special...**, which gives flexibility and a preview of delimiters.
- **Pasting overwrites existing data** and is disabled in browse and filtered modes. Pasted data are **not recorded** as an ordinary command in the Results window, unlike other edits.
- Pasting text into a numeric variable leaves those cells unchanged and shows a warning. Take a **snapshot** first (section 14).
- For a spreadsheet-sourced paste, remove blank rows, blank columns, repeated headers and merged cells first.
- For anything beyond small tables, use `import excel` or `import delimited` (Lesson 2): they are repeatable.

## 11. Changing data: find, sort, replace, drop, add

This walkthrough follows the manual's `auto` example.

```stata
sysuse auto, clear
browse            // or edit, if you intend to change something
```

| Task | Data Editor | Command it runs |
|------|-------------|-----------------|
| Find a car | **Edit > Find...**, type `Toronado`, Enter | (search only) |
| Sort by mileage | Right-click `mpg` heading > **Data > Sort data...** (or **Tools > Sort data...**) | `sort mpg` |
| Jump to the last observation | Cursor Location box: `rep78 74` | (navigation only) |
| Change one value | Select the cell, type, Enter | `replace mpg = 22.5 in 5` |
| Delete a variable | Right-click heading > **Data > Drop selected data** (confirm) | `drop trunk` |
| Create a variable | Right-click a cell > **Data > Add variable...**: name `gp100m`, expression `100/mpg`, position at the end | `generate gp100m = 100/mpg` |

Notes:
- **Sorting:** Stata asks how to sort (ascending by default) because sort order can affect reproducibility, for example when using resampling. This is a good thing.
- **Drop** asks for confirmation, because it can lead to data loss. Remember it affects only the data in memory, not the file on disk.
- **Create a variable:** the **Create...** button opens the Expression Builder, which lists functions.
- Throughout, **look in the Results window**: the commands and output appear there, and in the History window.
- When you finish, **save under a new name** (File > Save as...) to avoid overwriting the original dataset.

## 12. Dates in the Data Editor

The Data Editor has two special tools for dates. Use the `sp500` dataset:

```stata
sysuse sp500, clear
browse
```

### 12.1 Display format
1. Select `date` in the Variables window.
2. In Properties, click **Format**, then the ellipsis: the **Create format** dialog opens. It tells you these are **daily** dates and that the default format is `%td`, displayed like `07apr2024`.
3. Choose a pre-made format from the **Samples** pane, for example "April 7, 2024". The format string appears at the bottom.
4. Click **OK**. The display changes; the stored numbers do not.

The equivalent command is `format date %tdMonth_dd,_CCYY` (check the string in the dialog). See `help datetime` for details.

### 12.2 Input mask
In the upper-right corner of the Data Editor is the **Time/Date input mask** field, showing **DMY** by default. It tells Stata how to read dates you *type*. With DMY you can type `18jan2024` or `30042024` (no separators) and Stata understands. Change the mask to **MDY** and `March 15, 2024` works. This is the fastest way to edit dates by hand.

Safe date habits:
- Store dates as real Stata dates (numbers with a date format), not text. Text dates cannot be sorted or subtracted.
- Choose the mask that matches the dates you will type, and **check the Results window** to see the command Stata actually ran.
- The ANC survey stores `visit_date` as text (`YYYY-MM-DD`), a Lesson 3 task: convert it with `date()`.

## 13. Filtering and hiding: limiting your exposure

The manual's central safety advice: *if you must edit your data, protect yourself by limiting the dataset's exposure.* If you need to change `rep78` only when it is missing, look **only** at the missing values and the variables you need to identify them. Then a stray keystroke cannot damage other variables or observations.

### 13.1 Hiding variables (columns)
In the Data Editor's **Variables** window:
- **Drag variables** up or down to change their order *in the Data Editor only*. This does not change their order in the dataset.
- **Untick** the checkboxes to hide variables.
- Use the **Filter variables here** box to search variable names and labels (the default ignores case and finds any of the words). The wrench icon lets you change this behaviour and add or remove information columns. Filtering this list affects the list, not which data are displayed.
- **Select all** from the right-click menu, then click one checkbox to deselect all, then tick only the variables you want, for example `make` and `rep78`.

No command is issued when you do this: hiding variables does not affect the dataset, only the display. **Show entire dataset** (right-click menu) undoes it.

### 13.2 Filtering observations (rows)
1. Click **Filter observations** on the toolbar.
2. In **Filter by expression**, enter `missing(rep78)`.
3. Click **Apply filter**. (The ellipsis opens the Expression Builder, listing functions.)

Now you see only cars with missing repair records.

### 13.3 The command-line way
```stata
edit make rep78 if missing(rep78)
```
`varlist` restricts the **columns**; `if` and `in` restrict the **rows**. This is the cleanest way to limit exposure and it is reproducible: you can put the line in a do-file. The `edit` reference gives the same advice, with examples such as `edit model mpg` and `edit model mpg if mpg>=.`.

### 13.4 Browse the same way
```stata
browse id state age hb if missing(hb)
browse id state if inlist(state, "lagos", "LAGOS", "kano")
```
(Using the ANC survey: women with no haemoglobin measurement; and the inconsistent state spellings that Lesson 3 will fix.)

## 14. Snapshots: temporary safety nets

A **snapshot** is a temporary saved copy of the dataset in memory, taken from the **Snapshots** tab beneath the Variables window. Snapshots are deleted when you exit Stata, so treat them as temporary.

Uses:
- Save a temporary copy so another dataset can be opened and viewed.
- Save stages of work so you can recover from a disaster.
- Save pieces of datasets during analyses.
- Take one **before pasting** (recommended by the `edit` reference).

Snapshots toolbar:
| Button | Action |
|--------|--------|
| **Add** | Save a new snapshot with a timestamp and label (for example `Start`) |
| **Remove** | Erase a snapshot's temporary file; does not affect the data in memory |
| **Change label** | Edit the label |
| **Restore** | Replace the data in memory with the selected snapshot (you confirm) |

Workflow: add `Start`; make changes; add `Changed`; restore `Start` to see where you began (double-click it); restore `Changed` to go back.

Command-line equivalents exist (`snapshot save`, `snapshot restore`, `snapshot list`, `snapshot erase`; see `help snapshot`).

**Snapshots are not a substitute for saving.** They disappear when Stata closes.

## 15. From clicks to code: recovering the commands

Everything the Data Editor did appears in the **Results** and **History** windows. To make it reproducible:

1. In the **History** window, click the last command that came from the Data Editor.
2. Scroll up to the first one (for example `sort mpg`) and **Shift-click** it.
3. **Right-click** the highlighted commands.
4. Choose **Send selected to Do-file Editor**.
5. Add a header and comments, then save as a do-file.

Tips from the manual and the reference:
- **Log your session** so that you have a permanent record of the changes and can check that they are the changes you intended. See the [log file guide](../lesson-04-do-files-and-log-files/log-file-guide.md).
- Filter out commands that produced errors before saving the history.
- **Pasted data are not recorded** as a normal command, so document pastes by hand with a comment.
- The best habit: perform the change with a command in a do-file in the first place, such as `replace hb = . if hb == 99`.

## 16. When not to use the Data Editor

| Situation | Better approach |
|-----------|-----------------|
| Just looking at data | `browse` (browse mode) |
| Correcting many values | A do-file with `replace ... if ...` |
| Anything you will need to repeat | A do-file |
| Bringing in a file | `import delimited` / `import excel` / `use` |
| Large datasets | Use `if`/`in` and a varlist, or `summarize`/`tabulate`/`codebook` |
| Auditable corrections (health records, surveys) | Written correction rules in a do-file, with comments saying who authorised each |
| Finding problems | `assert`, `duplicates`, `tabulate`, `codebook` |

The Data Editor is an excellent **microscope** and a poor **assembly line**.

## 17. Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Cannot type in cells | Browse mode | Switch to edit mode, deliberately |
| Cannot paste | Browse or filtered mode | Show the whole dataset in edit mode |
| Cannot sort | Filtered mode, or browse with `if`/`in` | Remove the filter (**Show entire dataset**) |
| Some variables are missing from view | Hidden or filtered | **Show entire dataset** |
| A value changed and I do not know when | Edit-mode keystroke | Check the Results/History windows and your log; restore a snapshot or reload the file |
| `Select all` does not select everything | Data filtered or variables hidden | It selects only what is displayed |
| Variable became a string or float unexpectedly | Typed text or decimals | `describe`; fix with `destring`, `recast` or reload |
| `r(4)` or an unsaved-changes prompt | Unsaved changes in memory | Save, or `clear` deliberately |
| Date typed was misread | Wrong input mask | Check the mask (DMY/MDY/YMD) and the Results window |
| Wrong name rejected | Space, symbol, or leading digit | Follow the naming rules (section 8) |
| Edits not in my do-file | Made by hand | History > Send selected to Do-file Editor |

## 18. Practice exercises E1 to E12

Solutions to the command-based parts are in `exercise-solutions/lesson-02/data-editor-practice.do`. Most steps are point-and-click, so write down your observations. Use `auto` unless told otherwise.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**E1 🟢 Two modes.** Open `auto` and start the Data Editor with the **Edit** button, then with the **Browse** button (or `browse`). Compare the right-click menus. Which items are disabled in browse mode? Which would you want on while exploring a new file?

**E2 🟢 Navigate.** In browse mode, jump to `rep78[74]` using the Cursor Location box. Then move with Tab, Shift+Tab, Enter and Shift+Enter. What do the dots at the end of `rep78` mean?

**E3 🟢 Find and sort.** Use **Edit > Find...** to locate the Toronado. Sort by `mpg` using the right-click menu. Which command appeared in the Results window?

**E4 🟢 Enter a small table.** Clear the data and key in the manual's seven-car table (section 6) observation by observation. Skip the two missing values. What happens at the end of the second row when you press Tab? Why not at the end of the first?

**E5 🟡 Name, label, format.** Rename `var1` to `make`, `var2` to `price`, and so on. Add a label and a comma format to `price`, and a note. List the commands that ran. Which variable name would Stata reject: `gear_ratio`, `gear ratio`, `1st_gear`, `Gear`?

**E6 🟡 Value labels.** Reload `auto`. Create the `repairs` value label and attach it to `rep78`. Then use `browse, nolabel`. What do you see? Why is this useful?

**E7 🟡 Limited exposure.** Use the Data Editor's own controls to show only `make` and `rep78` for cars where `rep78` is missing. Then do the same with one command. Why is the command better?

**E8 🟡 Missing values.** Using `auto`, run `count if rep78 >= .`, `count if missing(rep78)` and `count if rep78 > 3`. Why does the third not equal the number of cars with good records? How would you fix the condition?

**E9 🟡 Dates.** Open `sp500`. Change the display format of `date` to "April 7, 2024" style. Type a new date in the first row with the DMY mask (`18jan2024`), then switch to MDY and type `March 15, 2024`. What commands ran? Then `clear`.

**E10 🟡 Snapshots.** Take a snapshot called `Start`. Drop the `trunk` variable and create `gp100m`. Take a snapshot called `Changed`. Restore `Start`, then restore `Changed`. Why are snapshots not a substitute for saving?

**E11 🔴 ANC survey: look before you touch.** Open `data/anc_survey.dta`. Using only `browse` with a varlist and `if`, find (a) respondents with missing `hb`, (b) rows whose `state` is not spelled with a leading capital letter, (c) respondents with `anc_visits` equal to 99. Write the three commands. (Expected counts: 61, 19 and 40. The 19 covers `lagos`, `LAGOS` and `kano` only; there may be other spelling variants to look for.)

**E12 🔴 From clicks to a do-file.** Make five changes in the Data Editor on `auto` (a rename, a label, a sort, a drop, a new variable). Use the History window to send them to the Do-file Editor. Add a header, add `, clear` on the load line, save as `de_changes.do`, restart Stata and run it. Do you get the same data?

## 19. Quick reference card

| Task | How |
|------|-----|
| Safe look | `browse` or **Data Editor (Browse)** |
| Edit deliberately | `edit` or **Data Editor (Edit)** |
| Limit columns / rows | `browse varlist if cond in range` |
| Go to a cell | Type `varname obs` in the Cursor Location box |
| Move | Tab, Shift+Tab, Enter, Shift+Enter |
| Cancel an entry | Esc |
| Find | **Edit > Find...** |
| Sort | Right-click heading > **Data > Sort data...** |
| Add / drop a variable | **Data > Add variable...** / **Drop selected data** |
| Rename / label / format | Properties window |
| Value labels | Properties > **Value label** > ellipsis; `label define`, `label values` |
| Hide variables | Untick in the Variables window; **Show entire dataset** restores |
| Filter rows | **Filter observations** button |
| Snapshots | Snapshots tab: Add, Remove, Change label, Restore |
| Date input mask | Field at upper right (DMY, MDY, YMD) |
| Recover commands | History window > **Send selected to Do-file Editor** |
| Missing numeric value | `.` (and `.a` to `.z`) |
| Missing test | `missing(x)` |
| Variable names | 1 to 32 characters, letters, digits, underscore; do not start with a digit or underscore; case sensitive |

## 20. Facilitator notes

**Timing (90-minute session):** 10 min why caution and the two modes (sections 1 to 3), 15 min entering, missing values and properties (6 to 9), 15 min changing, dates and copy/paste (10 to 12), 15 min exposure and snapshots (13 to 14), 10 min recovering commands (15), 25 min exercises E1 to E10. E11 and E12 are take-home or an advanced task.

**Before the session**
- Participants should know how to open and save datasets (see the [opening and saving guide](opening-and-saving-dta-guide.md)).
- Make sure everyone has a dataset saved before they start editing, since several exercises change data in memory.
- Have the Variables and Properties windows visible (see the [docking windows guide](../lesson-01-getting-started/docking-windows-guide.md)).

**Common stumbling blocks**
- Typing in a cell by mistake in edit mode.
- Assuming that hidden variables or filtered rows have been deleted, or the opposite.
- Pasting over data.
- Not noticing that sorting changed the row order.
- Forgetting that changes are in memory only.
- Date input masks: participants type a US-style date with a DMY mask.

**Teaching tips**
- Demonstrate a "silent error": in edit mode, change one value, then ask the group to find it using the Results window and the log. Everyone sees how little trace there is without logging.
- Pair exercise: one participant makes five secret changes in the editor; the other reconstructs them from the History window.
- Ask the group to produce their own two-line rule: "browse to look; do-file to change".

**Assessment prompt (5 minutes):** "A colleague says: 'I fixed 30 wrong ages by typing over them in the Data Editor, then saved.' List three risks and what they should have done." Expected: no record of what changed or why; cannot be repeated if new data arrive; no review possible; may have overwritten raw data. Better: a do-file with `replace age = . if age > 49` and comments, run on a copy, logged.

**Note on versions.** This guide follows the Windows edition of the Getting Started manual and the `[D] edit` reference. Menu names, toolbar buttons and some features (such as frame support in the `edit` and `browse` commands in newer releases) differ across Stata versions and systems. Check `help edit` and `help snapshot` in your own installation. Use only the synthetic course data in screenshots and logs you share.
