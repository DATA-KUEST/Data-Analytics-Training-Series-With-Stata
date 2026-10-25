# Learning Notes: `describe` and Dataset, Variable and Value Labels

**Part of:** Lesson 3, Cleaning and Labelling Data  |  **Read and practise:** about 90 minutes  |  **Dataset:** `auto` (built into Stata) and `data/anc_survey.dta` (in this repo)

A dataset that nobody can read is a dataset that nobody can trust. `describe` tells you what is *in* a dataset: names, types, formats, labels. Labels tell the next reader what the data *mean*: that `facility_delivery == 1` is "Yes", that `hb` is haemoglobin in g/dL. This guide teaches both, and ends with a complete labelling workflow for the ANC survey. Its companion, the [Variables Manager and notes guide](variables-manager-and-notes-guide.md), covers the point-and-click side.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 9 ("Labeling data"), and checked against the `[D] describe`, `[D] label` and `[D] notes` entries on stata.com. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Read every part of `describe` output, and use its options
- Choose and change storage types sensibly
- Use `describe` results in programs and as a data dictionary
- Add a dataset label and variable labels
- Create value labels and attach them to variables, in the correct two steps
- Add to, change, list, copy, rename, save and drop value labels
- Use `encode`, `decode` and `numlabel`
- Audit labelling with `describe`, `codebook`, `ds` and `labelbook`
- Write a reproducible labelling do-file for the ANC survey

## Contents
1. [Why `describe` first](#1-why-describe-first)
2. [Reading `describe` output](#2-reading-describe-output)
3. [Options of `describe`](#3-options-of-describe)
4. [Storage types](#4-storage-types)
5. [Stored results and `describe, replace`](#5-stored-results-and-describe-replace)
6. [`describe using`: look before you load](#6-describe-using-look-before-you-load)
7. [Related commands](#7-related-commands)
8. [Three kinds of label](#8-three-kinds-of-label)
9. [Dataset labels](#9-dataset-labels)
10. [Variable labels](#10-variable-labels)
11. [Value labels: the two-step process](#11-value-labels-the-two-step-process)
12. [Maintaining value labels](#12-maintaining-value-labels)
13. [`encode`, `decode` and `numlabel`](#13-encode-decode-and-numlabel)
14. [Labels in the point-and-click tools](#14-labels-in-the-point-and-click-tools)
15. [Labelling workflow for the ANC survey](#15-labelling-workflow-for-the-anc-survey)
16. [Best practices](#16-best-practices)
17. [Troubleshooting](#17-troubleshooting)
18. [Practice exercises DS1 to DS14](#18-practice-exercises-ds1-to-ds14)
19. [Quick reference card](#19-quick-reference-card)
20. [Facilitator notes](#20-facilitator-notes)

---

## 1. Why `describe` first

`describe` is the first command to run on any dataset, before `summarize` or `tabulate`. It answers: how big is it, what variables are there, how are they stored, and are they labelled? It never changes the data.

```stata
sysuse auto, clear
describe
```

## 2. Reading `describe` output

The output has a **header** and a **variable table**.

### The header

| Line | Meaning |
|------|---------|
| **Contains data from** | The file the data came from (or blank for data typed in) |
| **Observations** | Number of rows |
| **Variables** | Number of columns |
| **Dataset label** | Text set by `label data` (appears beside the file name or on its own line) |
| **Last saved / date** | When the dataset was last saved |
| `(_dta has notes)` | The dataset has notes (see the [notes guide](variables-manager-and-notes-guide.md)) |
| **Sorted by** | Variables the data are sorted on, if any |

### The variable table

| Column | Meaning |
|--------|---------|
| **Variable name** | The name you type in commands |
| **Storage type** | `byte`, `int`, `long`, `float`, `double`, `str#`, `strL` |
| **Display format** | How values print, such as `%9.0g`, `%9.2f`, `%td`, `%10s` |
| **Value label** | Name of the label set attached, blank if none |
| **Variable label** | Descriptive text, blank if none |

**Reading it as an auditor.** A numeric categorical variable with a blank *Value label* column is an unlabelled code. A numeric measure stored as `str` is a data-quality problem. A blank *Variable label* is documentation to be written.

## 3. Options of `describe`

Syntax: `describe [varlist] [, options]`

| Command | Effect |
|---------|--------|
| `describe` | Full header and table |
| `describe price mpg` | Only the listed variables |
| `describe, short` | Header only (number of observations and variables, size, sort order) |
| `describe, simple` | Just a list of variable names |
| `describe, fullnames` | Shows full variable names instead of abbreviating long ones |
| `describe, numbers` | Adds the variable's position number |
| `describe, replace` | Replaces the dataset in memory with a dataset *about* the dataset (section 5). Destroys your data in memory: save first |

> Option availability can vary by Stata version. Run `help describe` to confirm.

## 4. Storage types

Stata stores each variable in the smallest type that holds it, to save memory and disk space.

| Type | Holds | Notes |
|------|-------|-------|
| `byte` | Integers from -127 to 100 | Ideal for 0/1 indicators and small codes |
| `int` | Integers from -32,767 to 32,740 | Years, small counts |
| `long` | Integers up to about ±2.1 billion | Large IDs, big counts |
| `float` | Real numbers, about 7 significant digits | Default for new numeric variables |
| `double` | Real numbers, about 15 significant digits | Use for precise values and long ID numbers stored as numbers |
| `str1` to `str2045` | Text of up to that many characters | `strN` where N is the longest string |
| `strL` | Text up to about 2 billion bytes | For very long text |

Why it matters:
- **Precision.** A `float` holds about seven digits, so an 11-digit phone number or national ID should be a string or `double`, never a `float`.
- **Size.** `compress` converts each variable to the smallest type that can hold it without losing information.
- **Strings cannot be summarised.** If `describe` shows `str` for something numeric, fix it (see the [importing guide](../lesson-02-importing-exploring-data/importing-data-guide.md)).

```stata
compress              // shrink storage where it is safe
recast double income  // change a type deliberately
```

## 5. Stored results and `describe, replace`

After `describe`, Stata stores results you can use in programs. List them with `return list`:

| Result | Content |
|--------|---------|
| `r(N)` | Number of observations |
| `r(k)` | Number of variables |
| `r(width)` | Width of the dataset in bytes |
| `r(changed)` | 1 if the dataset has changed since last saved |
| `r(datalabel)` | The dataset label |
| `r(varlist)` and `r(sortlist)` | Variable list and sort variables (when `describe` is given a varlist) |

```stata
describe, short
display "This file has " r(N) " rows and " r(k) " variables."
assert r(N) == 1212          // stop the do-file if the row count is wrong
```

### A data dictionary in one command
`describe, replace` turns the dataset's *metadata* into the dataset itself, with one row per variable and variables such as position, name, type, whether it is numeric, format, value label name and variable label.

```stata
use "data/anc_survey.dta", clear
preserve
    describe, replace
    list, clean noobs
    export delimited using "data/anc_dictionary.csv", replace
restore
```
`preserve` and `restore` bring your data back afterwards. The exact names of the created variables are listed in `help describe`; check them before using them.

## 6. `describe using`: look before you load

```stata
describe using "data/anc_survey.dta"
describe using "data/anc_survey.dta", short
```
This describes a `.dta` file **on disk without loading it**, useful for big files or when you need to check what a colleague sent. Only `short` and `simple` apply.

## 7. Related commands

| Command | Use |
|---------|-----|
| `codebook` | Detailed per-variable summary: type, range, unique values, missing, labels |
| `ds` | List variable names, optionally by type or property (e.g. `ds, has(type string)`) |
| `lookfor` | Search names **and labels** for a word: `lookfor haemoglobin` |
| `labelbook` | Detailed report on value labels |
| `notes` | Read documentation notes |
| `cf`, `compare` | Compare variables or datasets |

To list variables with no variable label, try `ds, not(varlabel *)`. This is our suggestion and the syntax of `ds` varies by version: confirm it with `help ds`. The Variables Manager (group by label) gives the same answer without code.

## 8. Three kinds of label

| Label | Attaches to | Command | Where it shows |
|-------|-------------|---------|----------------|
| **Dataset label** | The whole dataset | `label data` | Header of `describe`; Open dialog |
| **Variable label** | One variable | `label variable` | Column in `describe`; table and graph titles; Variables window |
| **Value label** | The *values* of a variable | `label define` then `label values` | `tabulate`, `list`, `browse`, graph axes |

Labels never change the underlying numbers. A variable coded 0/1 with a label "No/Yes" is still 0/1 in every calculation. Labels are saved inside the `.dta` file.

## 9. Dataset labels

```stata
label data "Antenatal care survey, synthetic, 1,212 women (DATAQUEST)"
describe, short
```
Maximum length: 80 characters. Clear it with `label data` and no text.

## 10. Variable labels

```stata
label variable age "Age in completed years"
label variable hb "Haemoglobin (g/dL)"
label variable facility_delivery "Delivered in a health facility"
```
Maximum 80 characters. To remove: `label variable hb`.

Good variable labels:
- state the **concept and the unit** ("Systolic blood pressure (mmHg)")
- are short enough to appear in output without wrapping
- use consistent wording and capitalisation across the dataset
- do not repeat the variable name

## 11. Value labels: the two-step process

Value labels are stored separately from variables. This is how one label set (such as Yes/No) can serve many variables.

**Step 1: define the label set**
```stata
label define yesno 0 "No" 1 "Yes"
```
**Step 2: attach it to one or more variables**
```stata
label values facility_delivery yesno
```

Now `tabulate facility_delivery` shows words, while `summarize facility_delivery` still works on the 0/1 values.

The manual's `auto` example:
```stata
label define repairs 1 "atrocious" 2 "bad" 3 "OK" 4 "good" 5 "stupendous"
label values rep78 repairs
tabulate rep78
```

Key rules:
- The label **name** (`yesno`) and the variable name are different things. You can reuse one name for many variables.
- Defining a label does nothing until you **attach** it.
- Value labels apply to **integers** (and the extended missing values `.a` to `.z`). Non-integer values cannot be labelled.
- Label text should be short; it appears in tables.
- Label names follow the same rules as variable names.

### Detaching
```stata
label values facility_delivery .      // detach (the label set remains defined)
```

## 12. Maintaining value labels

`label define` refuses to overwrite an existing set unless you say how:

| Option | Effect |
|--------|--------|
| `add` | Add new value-text pairs; error if a value already has text |
| `modify` | Add new pairs **and** change existing ones |
| `replace` | Throw away the whole set and define it again |
| `nofix` | Do not widen existing label displays automatically (rarely needed) |

```stata
label define education 0 "None"
label define education 1 "Primary" 2 "Secondary" 3 "Higher", add
label define education 0 "No formal education", modify
```

Other `label` subcommands:

| Command | Does |
|---------|------|
| `label dir` | Names of all value-label sets in memory |
| `label list` | Contents of all sets, or `label list education` |
| `label copy old new` | Copy a set under a new name |
| `label rename old new` | Rename a set |
| `label drop name` | Delete a set (variables using it become unlabelled) |
| `label save name using file.do` | Write `label define` commands to a do-file |
| `label language` | Hold labels in several languages |

**Reproducibility tip.** `label save` writes the `label define` commands for sets you have built, so labelling can be replayed on new data:

```stata
label save yesno education using "do/labels_anc.do", replace
```

### Labels and `use`
When you `use` a dataset, its labels come with it, replacing those in memory. Labels are stored in the file, so **save after labelling** or the work is lost.

### Extended missing values
You can label `.a` to `.z`:
```stata
label define hbmiss .a "Not measured" .b "Refused"
```

## 13. `encode`, `decode` and `numlabel`

### `encode`: text to labelled numbers
```stata
encode residence, generate(residence_n)
tabulate residence_n
```
`encode` creates a numeric variable with a value label built from the text. Codes follow alphabetical order of the text, unless you supply your own with `label(name)`. Clean string variants first: `encode` treats "Lagos" and "lagos" as different.

### `decode`: labelled numbers to text
```stata
decode education, generate(education_str)
```

### `numlabel`: show codes beside text
```stata
numlabel education, add       // "1. Primary"
numlabel education, remove
```
This helps when you need to see both the code and the words in a table.

## 14. Labels in the point-and-click tools

| Tool | What it does |
|------|--------------|
| **Data > Data utilities > Label utilities** | Dialogs for define, list, copy, drop and attach |
| **Properties window** | Edit label and value label of the selected variable |
| **Variables Manager** | Edit properties of many variables at once (see the [guide](variables-manager-and-notes-guide.md)) |
| **Data Editor** | Shows labels in blue (labelled values) |

Whatever you click issues a command in the Results window. Copy those commands into a do-file.

## 15. Labelling workflow for the ANC survey

`anc_survey.dta` has **no labels**. Load it and audit:

```stata
use "data/anc_survey.dta", clear
describe
codebook education wealth_quintile facility_delivery, compact
```

Known facts about the data: 1,212 observations and 13 variables; `residence` is text ("Urban" 683, "Rural" 529); `education` is coded 0 to 3 (counts 217, 283, 455, 257); `wealth_quintile` is 1 to 5; `facility_delivery` is 0/1 (447 and 765); `hb` has 61 missing values; `visit_date` is text; `state` has spelling variants.

A starting do-file (`03_labels.do`). **Check the data dictionary in `data/README.md` for the meaning of each code before using these wordings.**

```stata
*--- dataset label
label data "ANC survey (synthetic), DATAQUEST training"

*--- variable labels
label variable age               "Age in completed years"
label variable parity            "Number of previous births"
label variable hb                "Haemoglobin (g/dL)"
label variable systolic_bp       "Systolic blood pressure (mmHg)"
label variable weight_kg         "Weight (kg)"
label variable education         "Highest education level"
label variable wealth_quintile   "Household wealth quintile"
label variable facility_delivery "Delivered in a health facility"

*--- value labels
label define yesno 0 "No" 1 "Yes"
label define edu   0 "None" 1 "Primary" 2 "Secondary" 3 "Higher"
label define wq    1 "Poorest" 2 "Poorer" 3 "Middle" 4 "Richer" 5 "Richest"

label values facility_delivery yesno
label values education         edu
label values wealth_quintile   wq

*--- residence: text to labelled numeric
encode residence, generate(residence_n)
label variable residence_n "Place of residence"

*--- verify
describe
tabulate education
tabulate wealth_quintile
tabulate facility_delivery
tabulate residence_n

*--- document and save under a new name
notes: Labels added by 03_labels.do
save "data/anc_labelled.dta", replace
```

Ask in the verification step: did every `tabulate` show words? Do the counts match the numbers above? The code `education` 0-3 mapping to None/Primary/Secondary/Higher is our assumption for the exercise; confirm it against your data documentation.

## 16. Best practices

1. **Run `describe` first** on every new dataset and keep the output in your log.
2. **Label in a do-file**, never only by clicking.
3. **Label before analysing**, so tables and graphs are readable.
4. **Reuse label sets** (one `yesno` for all yes/no variables).
5. **Keep codes and text in step** with the questionnaire or data dictionary.
6. **Never recode by relabelling.** To change values use `replace` or `recode`, then fix the label.
7. **Store identifiers as strings or `double`**, never `float`.
8. **Compress** before sharing.
9. **Save under a new name** and keep the raw file unchanged.
10. **Add a note** recording who labelled the data and when.

## 17. Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `label already defined` | Set exists | Use `add`, `modify` or `replace` |
| Table still shows numbers | Label defined but not attached | `label values var setname` |
| Wrong words on a value | Label text wrong or codes shifted | `label define set # "text", modify` |
| `encode` gives two codes for one place | Spelling variants in text | Clean the string first (see Lesson 3 cleaning exercises) |
| Labels lost after `use` | Saved before labelling | Re-run the labelling do-file and save |
| Variable label truncated | Longer than 80 characters | Shorten |
| `describe, replace` destroyed my data | Memory replaced | Use `preserve` / `restore` |
| Cannot label 1.5 | Value labels need integers | Recode or leave unlabelled |
| `summarize` fails on a variable | It is a string | Convert with `destring` or fix at import |
| Long ID looks wrong | Stored as `float` | `recast double` or keep as string |

## 18. Practice exercises DS1 to DS14

Solutions are in `exercise-solutions/lesson-03/describe-labels-practice.do`. Use `auto` unless told otherwise.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**DS1 🟢 Read the header.** Run `describe`. How many observations and variables? Is there a dataset label? Are there notes?

**DS2 🟢 Options.** Run `describe, short`, `describe, simple` and `describe price mpg`. What does each show?

**DS3 🟢 Types.** Which variables in `auto` are strings? Which are `byte`? Why can `foreign` be a `byte`?

**DS4 🟢 Stored results.** After `describe, short`, run `return list`. Display a sentence containing `r(N)` and `r(k)`.

**DS5 🟡 Variable labels.** Add a dataset label to `auto`. Change the label of `mpg` to "Mileage (miles per US gallon)". Check with `describe`.

**DS6 🟡 Two-step labels.** Create the `repairs` set from section 11 and attach it to `rep78`. Run `tabulate rep78`. Then detach it and tabulate again.

**DS7 🟡 Add and modify.** Define a set `size` with 1 "Small" and 2 "Large". Add 3 "Medium" using `add`. Then correct 1 to "Compact" using `modify`. Show the result with `label list size`.

**DS8 🟡 Describe on disk.** Without loading it, describe `data/anc_survey.dta` using `describe using`. How many observations does it report?

**DS9 🟡 Audit the ANC survey.** Load it. Which variables are string? Which numeric variables look categorical? List three problems visible from `describe` alone.

**DS10 🟡 Label the ANC survey.** Write `03_labels.do` as in section 15 up to the variable labels. Verify with `describe`.

**DS11 🟡 Value labels for ANC.** Add the `yesno`, `edu` and `wq` sets. Tabulate each variable. Do the counts match 447/765 for `facility_delivery` and 217/283/455/257 for `education`?

**DS12 🔴 Encode.** Encode `residence` and verify against 683 urban and 529 rural. Then try encoding `state` as it is. What goes wrong, and what would you do first?

**DS13 🔴 Data dictionary.** Use `preserve`, `describe, replace` and `export delimited` to produce a dictionary of the labelled ANC data. Open it in a spreadsheet. What is missing that a reader would want (hint: units, source, code meanings)?

**DS14 🔴 Reproduce.** Use `label save` to write the label sets to a do-file. Restart Stata, load the raw `anc_survey.dta`, run the labelling do-files, and show that `describe` matches your earlier output.

## 19. Quick reference card

| Task | Command |
|------|---------|
| Describe the dataset | `describe` |
| Header only / names only | `describe, short` / `describe, simple` |
| Describe a file on disk | `describe using file.dta` |
| Dataset label | `label data "text"` |
| Variable label | `label variable var "text"` |
| Define value label | `label define name # "text" # "text"` |
| Attach value label | `label values var name` |
| Detach | `label values var .` |
| Add / change entries | `label define name # "text", add` / `, modify` |
| Redefine set | `label define name ..., replace` |
| List | `label dir`, `label list [name]` |
| Copy / rename / drop | `label copy`, `label rename`, `label drop` |
| Save labels as code | `label save name using file.do` |
| Text to numeric | `encode var, generate(new)` |
| Numeric to text | `decode var, generate(new)` |
| Show codes with text | `numlabel name, add` |
| Shrink storage | `compress` |
| Change type | `recast type var` |
| Search labels | `lookfor word` |
| Detailed report | `codebook`, `labelbook` |

## 20. Facilitator notes

**Timing (90-minute session):** 15 min `describe` (sections 1 to 7), 10 min label concepts (8 to 10), 20 min value labels (11 to 13), 10 min tools (14), 35 min ANC workflow and exercises DS1 to DS11. DS12 to DS14 are take-home.

**Before the session**
- Participants should have worked through the [do-file guide](../lesson-04-do-files-and-log-files/do-file-guide.md) basics, or be told to type commands in the Command window first.
- Copy `data/anc_survey.dta` to each participant's `data/` folder.
- Agree the code meanings for `education` and `wealth_quintile` with the group (the data README is the authority).

**Common stumbling blocks**
- Defining a value label but forgetting to attach it.
- Expecting `label define` to overwrite an existing set silently.
- Believing labels change the numbers.
- Running `describe, replace` without `preserve`.
- Storing IDs as `float`.

**Teaching tips**
- Show the same `tabulate` before and after labelling; the effect is immediate.
- Let participants find the three problems in the ANC `describe` output before you reveal them.
- Insist that every labelling step goes into a do-file.

**Assessment prompt (5 minutes):** "You ran `label define yesno 0 "No" 1 "Yes"` and then `tabulate facility_delivery`. It still shows 0 and 1. Why, and what is the fix?" Expected: the label set was defined but not attached; run `label values facility_delivery yesno`.

**Caveats.** The code in this guide was written against the manual and reference entries, and has not been run in Stata in the authoring environment. Run each block yourself before teaching, and check option names with `help describe`, `help label`, `help ds` and `help encode` in your version.
