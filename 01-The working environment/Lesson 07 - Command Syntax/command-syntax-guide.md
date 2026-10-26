# Learning Notes: Stata Command Syntax

**Part of:** Lesson 3, Cleaning and Labelling Data  |  **Read and practise:** about 90 minutes  |  **Dataset:** `auto` (built into Stata) and `data/anc_survey.dta` (in this repo)

Every Stata command follows the same grammar. Once you can read that grammar, you can pick up any new command in minutes: open `help commandname`, read the syntax line, and build the command. This guide uses `list` as the teaching vehicle, as the manual does, then applies the same rules to `summarize`, `tabulate` and `count` on the ANC survey. Its companion, the [generate and replace guide](generate-and-replace-guide.md), applies the grammar to creating and changing variables.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 10 ("Listing data and basic command syntax"), with pointers to `[U] 11 Language syntax`. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Read a Stata syntax line: square brackets, underlined abbreviations, required and optional parts
- Build commands with a `varlist`, `if`, `in` and `options`
- Use variable-list shorthand: `*`, `?`, `-` and `~`
- Write correct logical expressions, and avoid the six classic errors
- Handle missing values safely inside `if`
- Choose between `if` and `in`, and between the value and the label of a variable
- Control the appearance of `list` output with options
- Interrupt a command with Break
- Understand `by`, `bysort` and prefix commands at an introductory level
- Read and fix common error messages and `r()` codes

## Contents
1. [Why learn the syntax](#1-why-learn-the-syntax)
2. [Reading a syntax line](#2-reading-a-syntax-line)
3. [The anatomy of a command](#3-the-anatomy-of-a-command)
4. [Variable lists](#4-variable-lists)
5. [The `if` qualifier](#5-the-if-qualifier)
6. [Missing values in `if`: the big trap](#6-missing-values-in-if-the-big-trap)
7. [Common mistakes with `if`](#7-common-mistakes-with-if)
8. [The `in` qualifier](#8-the-in-qualifier)
9. [Options](#9-options)
10. [Controlling `list` output](#10-controlling-list-output)
11. [Break](#11-break)
12. [Prefixes: `by`, `bysort` and `quietly`](#12-prefixes-by-bysort-and-quietly)
13. [Abbreviations and style](#13-abbreviations-and-style)
14. [Error messages and return codes](#14-error-messages-and-return-codes)
15. [Applying the grammar to the ANC survey](#15-applying-the-grammar-to-the-anc-survey)
16. [Troubleshooting](#16-troubleshooting)
17. [Practice exercises CS1 to CS16](#17-practice-exercises-cs1-to-cs16)
18. [Quick reference card](#18-quick-reference-card)
19. [Facilitator notes](#19-facilitator-notes)

---

## 1. Why learn the syntax

Menus and dialogs are a good way to start. But the manual notes that, with practice, the Command window is often much faster because of the **clean and regular syntax** of Stata commands. More importantly, only typed commands can be saved in a do-file, re-run, shared and audited. Every dialog you use ends by issuing a command; reading that command is the quickest way to learn the grammar.

## 2. Reading a syntax line

Open `help list`. The first syntax line is:

```
list [varlist] [if] [in] [, options]
```

How to read it, following the manual:

| Notation | Meaning |
|----------|---------|
| `[ ... ]` square brackets | **Optional.** Anything inside is not required |
| Anything **not** in brackets | **Required.** For `list`, only the command word itself |
| `varlist` | A list of variable names (optional for `list`) |
| `if` | Restrict to observations for which an expression is true |
| `in` | Restrict to a range of observation numbers |
| `,` and `options` | Options come after a comma, separated from the rest |
| Underlined part of a word (shown underlined in the Viewer) | The **minimum abbreviation**. For `list`, the `l` is underlined, so `l`, `li` and `lis` all work |

Two more rules:
- Optional pieces do not exclude each other unless the help says so. `list` can have a `varlist`, an `if` **and** an `in`.
- Items in the syntax line shown in plain text (like `list`) are typed exactly; items in italics (like *varlist*) are replaced by your own content.

For the details, `help language` has more examples and `[U] 11 Language syntax` has the full rules.

> **Training habit:** before using any new command, read its first syntax line aloud and say which parts are required. This takes ten seconds and prevents most errors.

## 3. The anatomy of a command

```
command  varlist  if expression  in range  ,  options
```

A worked example, all pieces present:

```stata
list make price mpg if foreign == 0 in 1/10, sepby(foreign) abbreviate(10)
```

| Piece | Text |
|-------|------|
| Command | `list` |
| Variable list | `make price mpg` |
| `if` qualifier | `if foreign == 0` |
| `in` qualifier | `in 1/10` |
| Options (after the comma) | `sepby(foreign) abbreviate(10)` |

The order is fixed: **varlist, then `if`, then `in`, then a comma, then options.** Stata is not forgiving about the order.

Commands generally differ in which pieces they accept. `summarize` takes a varlist, `if`, `in` and options (and weights). `tabulate` takes one or two variables. `generate` takes an equation instead of a varlist. The syntax line tells you.

## 4. Variable lists

A varlist saves typing. The manual's points:
- The varlist is **optional for `list`**: with none given, the command runs on all variables.
- Name variables explicitly: `list make mpg price`.
- Use shorthand:

| Shorthand | Meaning | Example |
|-----------|---------|---------|
| `m*` | All variables **starting** with `m` | `list m*` |
| `*e` | All variables **ending** in `e` | `list *e` |
| `ma?e` | `ma`, any one character, `e` | `list ma?e` |
| `price-weight` | All variables from `price` through `weight`, **in dataset order** | `li price-weight` |
| `gear r~o` (tilde) | A unique abbreviation with `~` standing for the omitted characters | `l gear_r~o` |
| `_all` | All variables | `summarize _all` |

The manual's `afewcars` examples use `list m*` (gives `mpg`... plus others starting with `m`), `li price-weight` and `list ma?e` (which finds only `make`).

Cautions:
- The range `price-weight` depends on the **order in the dataset**. Check it with `describe` or `describe, numbers`. If the order changes (for example after `order`), the same range means something different.
- If an abbreviation is **not unique**, Stata returns an error. Use more characters.
- Wildcards can quietly pick up variables you did not intend (a new `mpg2`). In a long-lived do-file, name important variables explicitly.

## 5. The `if` qualifier

`if` runs the command only on observations for which the expression is **true**; others are skipped.

### Operators
| Operator | Meaning |
|----------|---------|
| `<` | less than |
| `<=` | less than or equal |
| `==` | **equal** (two equals signs) |
| `>` | greater than |
| `>=` | greater than or equal |
| `!=` | not equal |
| `&` | and |
| `\|` | or |
| `!` | not |
| `( )` | grouping, to set order of evaluation |

`&` is evaluated before `|`, like multiplication before addition. The manual advises **using parentheses** so that the order of evaluation is clear.

### Examples (from the manual's `afewcars` data and `auto`)
```stata
list if mpg > 22
list if (mpg > 22) & !missing(mpg)
list make mpg price gear_ratio if (mpg > 22) | (price > 8000 & gear_ratio < 3.5)
list if mpg == 21 & weight > 4000
list if make == "Datsun 510"
```

### Strings need quotes
`list if make == "Datsun 510"`. Without the quotation marks Stata assumes `Datsun` is a variable and reports `Datsun not found`.

### Numeric values versus value labels
Value labels *look* like strings but the variable underneath is numeric. If `foreign` is stored as 0 and 1 with labels "Domestic" and "Foreign":

```stata
list if foreign == 0                    // the number
list if foreign == "Domestic":origin    // the label, using the "value":labelname form
list if foreign == "Domestic"           // WRONG: type mismatch, r(109)
```
In the third line, Stata reads `foreign` as numeric and cannot compare it with text. In the second, `"Domestic":origin` means "the number that the label set `origin` calls Domestic". To see the codes behind a labelled variable use `label list`, `codebook foreign`, or `tabulate foreign, nolabel`.

## 6. Missing values in `if`: the big trap

In Stata a numeric missing value (`.`) is stored as a **very large number**, larger than any real value. So:

| Expression | Includes missing? |
|------------|-------------------|
| `mpg > 22` | **Yes**: `.` counts as larger than 22 |
| `mpg >= 22` | **Yes** |
| `mpg < 22` | No |
| `mpg != 22` | **Yes** |
| `mpg > 22 & !missing(mpg)` | No |
| `mpg > 22 & mpg < .` | No |

The manual shows the symptom: `list if mpg > 22` lists the two cars with missing `mpg` as well as the two with `mpg` over 22; the safe version adds `!missing(mpg)`.

On the ANC survey:
- `hb` has **61 missing** values and 620 observations with `hb < 11` (verified with pandas).
- `count if hb < 11` gives **620**.
- `count if hb >= 11` gives **592**, because it includes the 61 missing. The true number of women with `hb >= 11` is **531**: use `count if hb >= 11 & !missing(hb)`.

**Rule:** whenever the variable in your `if` might have missing values, either check with `misstable summarize` first, or add `!missing(var)` when using `>`, `>=` or `!=`.

For text variables a missing value is the empty string `""`; there is no "large number" effect.

## 7. Common mistakes with `if`

The manual walks through a series of errors. Try to spot each before reading the fix.

| Typed | Message | Problem | Correct |
|-------|---------|---------|---------|
| `list if mpg=21` | `=exp not allowed`, r(101) | `=` is assignment; equality is `==` | `list if mpg==21` |
| `list if mpg==21 if weight>4000` | `invalid syntax`, r(198) | Only one `if` is allowed | `list if mpg==21 & weight>4000` |
| `list if mpg==21 and weight>4000` | `invalid 'and'`, r(198) | Stata does not use the word `and` | Use `&` |
| `list if make==Datsun 510` | `Datsun not found`, r(111) | String not in quotes | `list if make=="Datsun 510"` |
| `list if foreign=="Domestic"` | `type mismatch`, r(109) | Comparing a numeric variable with text | `list if foreign==0` or `list if foreign=="Domestic":origin` |
| `list if mpg > 22` | no error, but extra rows | Missing counts as large | `list if mpg > 22 & !missing(mpg)` |

**Lesson:** a command that runs without an error can still be wrong. Always check the number of observations selected.

## 8. The `in` qualifier

`in` selects observations **by position** (row number) using the form `first/last`. Negative numbers count from the end.

| Command | Selects |
|---------|---------|
| `list in 1` | The first observation |
| `list in -1` | The **last** observation |
| `list in 2/4` | Observations 2 through 4 |
| `list in -3/-2` | The third-last and second-last |
| `list in 1/10` | The first ten rows (a quick peek) |

`in` and `if` can combine: `list make mpg if mpg <= 22 in 2/4` first restricts to rows 2 to 4, then applies the condition. The row numbers in the output remain the dataset's row numbers (2 and 4 in the manual's example).

**`if` or `in`?** `if` selects by *value*; `in` selects by *position*. Position changes whenever the data are sorted, so use `in` for peeking and `if` for analysis.

> A common idiom is to `sort` first, then use `in` to see extremes: `sort hb` then `list id hb in 1/5` (the five lowest). Missing values sort to the end.

## 9. Options

Options follow a comma. The comma appears **once**, and everything after it is an option.

```stata
list make price, nolabel
summarize hb, detail
tabulate residence education, row
```

Types of options:
- **Switches**: just the word, e.g. `detail`, `nolabel`, `clean`.
- **With arguments in parentheses**: `sepby(foreign)`, `abbreviate(10)`, `separator(3)`, `level(90)`.
- Many options can be **abbreviated** (underlined in help), e.g. `det` for `detail`.

Common mistakes: putting options before the comma, using two commas, and putting spaces between an option name and its parentheses.

## 10. Controlling `list` output

The manual illustrates these options for fine control of `list`:

| Option | Effect |
|--------|--------|
| `sepby(varname)` | Draws a separator line between groups of `varname` (sort first) |
| `abbreviate(#)` | Minimum number of characters before a variable name is abbreviated in the header |
| `divider` | Draws a vertical line between the variables |
| `separator(#)` | Draws a horizontal line every `#` rows. The default is 5; `separator(0)` turns separators off |

Examples:
```stata
sort foreign make
list make price gear_ratio foreign, sepby(foreign)
list make weight gear_ratio, abbreviate(10)
list, divider
list, separator(3)
```

Other useful `list` options (check `help list`): `clean` (no borders), `noobs` (no observation numbers), `nolabel` (show codes instead of value labels), and `table`.

For a quick look at a large dataset, combine `in`, `clean` and `noobs`:
```stata
list id age hb in 1/8, clean noobs
```

## 11. Break

To interrupt a running command click the **Break** button on the toolbar. The manual stresses: **it is always safe to click Break.** After Break, the state of the system is the same as if the command had never been issued. Use it if you accidentally run `list` on a million observations.

## 12. Prefixes: `by`, `bysort` and `quietly`

A *prefix* goes in front of a command and changes how it runs. An introduction:

| Prefix | Meaning | Example |
|--------|---------|---------|
| `by var:` | Repeat the command for each group; **data must be sorted by `var`** | `by state: summarize hb` |
| `bysort var:` | Sorts, then repeats for each group | `bysort state: summarize hb` |
| `quietly` or `qui` | Run but suppress output | `quietly summarize hb` |
| `capture` | Run, and do not stop if it errors | `capture drop oldvar` |

`by` puts a colon after the variable and **comes before** the command, unlike options. The `by` prefix is central to `generate` with `_n` and `_N` and to `egen`; see the [generate and replace guide](generate-and-replace-guide.md#13-by-and-the-system-variables-_n-and-_n).

## 13. Abbreviations and style

- Many commands can be abbreviated: `l` for `list`, `g` for `generate`, `su` for `summarize`, `tab` for `tabulate`. But **`replace` cannot be abbreviated**, because it alters existing data.
- Abbreviations save typing at the Command window; in **do-files** write full words so colleagues can read them.
- Use `//` for comments at the end of a line, `*` for a whole-line comment, and `/* ... */` for blocks.
- Use `///` to continue a long command onto the next line in a do-file.
- Stata is **case sensitive**: `Mpg` and `mpg` are different variables, and commands are lower case.

## 14. Error messages and return codes

When a command fails Stata prints a message and a **return code** `r(#)`. The ones you will meet most:

| Code | Typical message | Usual cause |
|------|-----------------|-------------|
| `r(100)` | `varlist required` | Command needs at least one variable |
| `r(101)` | `=exp not allowed` | `=` used in place of `==` |
| `r(109)` | `type mismatch` | String compared with numeric |
| `r(110)` | `variable ... already defined` | `generate` on an existing name; use `replace` |
| `r(111)` | `... not found` | Misspelled variable, or missing quotes on a string |
| `r(198)` | `invalid syntax` | Wrong order, double `if`, `and` instead of `&` |
| `r(199)` | `unrecognized command` | Typo, or a user-written command not installed |
| `r(601)` | `file not found` | Wrong path or working directory |
| `r(2000)` | `no observations` | The `if` or `in` selected nothing |

Look up any code with `search rc 111`, or click the blue `r(#);` in the Results window. When you are stuck, read the **first** line of the message and the command above it.

## 15. Applying the grammar to the ANC survey

```stata
use "data/anc_survey.dta", clear

summarize age hb systolic_bp, detail                 // varlist + option
count if hb < 11 & !missing(hb)                      // if, with missing guard
tabulate residence                                   // one variable
tabulate residence education, row                    // two variables + option
list id state age hb in 1/8, clean noobs             // in + options
list id age hb if age < 18 & !missing(age), clean noobs   // 88 women under 18
count if systolic_bp >= 140                          // 12 women
bysort residence: summarize hb                       // prefix
```

Expected, from our pandas check of the CSV: 88 women with `age < 18`; 12 with `systolic_bp >= 140`; 620 with `hb < 11`; `hb` missing in 61.

`anc_visits` contains the code **99** 40 times (a "not recorded" code). `summarize anc_visits` is therefore badly distorted, and `count if anc_visits >= 4` would wrongly include the 99s. The safe count is `count if anc_visits >= 4 & anc_visits != 99`. The [generate and replace guide](generate-and-replace-guide.md#9-recoding-codes-to-missing-with-replace) shows how to fix the variable properly.

## 16. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `invalid syntax` | Wrong order of pieces, two `if`, or two commas | Reorder: varlist, `if`, `in`, comma, options |
| `Datsun not found` | Unquoted string | Add double quotes |
| `type mismatch` | Using the label text on a numeric variable | Use the code, or `"label":labelname` |
| Too many rows selected | Missing values counted as large | Add `!missing(var)` |
| `variable not found` | Typo, case, or abbreviation not unique | Check with `describe`; Stata is case sensitive |
| `price-weight` shows unexpected variables | Dataset order differs from what you think | `describe, numbers`, or name variables explicitly |
| Wildcard picked extra variables | New variable matched the pattern | Name the variables |
| Command seems to hang | Large output | Click **Break** (it is safe) |
| `by` gives `not sorted` | Data not sorted on the by-variable | Use `bysort` |
| `in` selects the wrong rows | Data were re-sorted | Use `if`, or sort first |

## 17. Practice exercises CS1 to CS16

Solutions are in `exercise-solutions/lesson-03/command-syntax-practice.do`. Use `auto` unless told otherwise.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**CS1 🟢 Read the syntax.** Type `help list`. Which parts of the first syntax line are optional? What is the minimum abbreviation of `list`?

**CS2 🟢 Varlists.** Load `auto`. List `make`, `price`, `mpg`. Then list `m*`. Then `price-weight`. Then `ma?e`. Explain what each does.

**CS3 🟢 In.** List the first five observations, the last observation, and observations 10 to 15. How does `in -3/-1` differ?

**CS4 🟢 If.** List cars with `mpg > 30`. Then cars with `price < 4000`. Count each with `count if`.

**CS5 🟡 Two conditions.** List cars that are `foreign` and have `mpg >= 25`. Then cars that are either `price > 12000` or `weight < 2000`. Use parentheses even where not needed.

**CS6 🟡 Strings.** List the car whose `make` is "VW Rabbit". Which error do you get without quotation marks?

**CS7 🟡 Labels and values.** `foreign` has value labels. Write two correct ways to list the foreign cars, and one wrong way. What error does the wrong way give?

**CS8 🟡 Spot the errors.** Fix each: (a) `list if mpg=20`, (b) `list if mpg>20 and price<5000`, (c) `list if mpg>20 if price<5000`, (d) `list if make==Buick Regal`.

**CS9 🟡 Missing trap.** In `auto`, `rep78` has missing values. Compare `count if rep78 > 3` and `count if rep78 > 3 & !missing(rep78)`. By how many do they differ and why?

**CS10 🟡 Output options.** `sort foreign make`, then list with `sepby(foreign)`. Then `list, divider`, then `list in 1/9, separator(3)`.

**CS11 🟡 Break.** Run `list` on the full ANC survey. Interrupt it with Break. What state is the data in?

**CS12 🟡 ANC counts.** Load the ANC survey. Count women with `age < 18`, with `systolic_bp >= 140`, with `hb < 11`. Do you match 88, 12 and 620?

**CS13 🔴 The trap on `hb`.** Count `hb >= 11`, then `hb >= 11 & !missing(hb)`. Explain 592 versus 531.

**CS14 🔴 The 99s.** Count `anc_visits >= 4`, then `anc_visits >= 4 & anc_visits != 99`. How many 99s are there? (Expect 40.) Which count is correct?

**CS15 🔴 By prefix.** Run `bysort residence: summarize hb` and `bysort state: count if hb < 11`. What does each produce? Why do the state results look untidy?

**CS16 🔴 Write a syntax cheat card.** For `summarize`, `tabulate` and `count`, copy the first syntax line from `help`, mark what is required, and give one ANC example of each.

## 18. Quick reference card

| Part | Rule |
|------|------|
| Order | `command varlist if ... in ... , options` |
| Square brackets in help | Optional |
| Underlined letters in help | Minimum abbreviation |
| Equal / not equal | `==` / `!=` |
| And / or / not | `&` / `\|` / `!` |
| Strings | Always in double quotes |
| Missing numeric | `.` is larger than any number; use `!missing(var)` |
| Varlist shorthand | `*`, `?`, `a-b`, `abbr~` |
| Rows by position | `in 1/10`, `in -1` |
| Value label comparison | `var == "text":labelname` |
| Options | After one comma |
| Prefix | `by var:`, `bysort var:`, `quietly` |
| Interrupt | **Break** button, always safe |
| Look up an error | `search rc #` |
| More on syntax | `help language`, `[U] 11 Language syntax` |

## 19. Facilitator notes

**Timing (90-minute session):** 10 min reading syntax (sections 1 to 3), 15 min varlists and `in` (4, 8), 25 min `if`, missing values and mistakes (5 to 7), 10 min options and output (9 to 11), 30 min exercises CS1 to CS12. CS13 to CS16 are take-home.

**Before the session**
- Have `auto` and `anc_survey.dta` ready; participants should be able to run commands from a do-file.
- Prepare slides or a handout of the error table in section 7; let participants try to find the fix before showing it.

**Common stumbling blocks**
- Writing `=` instead of `==`.
- Forgetting that missing is a large number.
- Typing `and`/`or` in words.
- Trying to compare a labelled variable with its label text.
- Expecting `in` to follow the original order after a sort.

**Teaching tips**
- Run section 7 as a "bug hunt": show the bad command, ask for the error before running it.
- Make the missing-value trap memorable with the 592 versus 531 example on real data.
- Ask participants to say the syntax line of a new command out loud before using it.

**Assessment prompt (5 minutes):** "`count if hb >= 11` returns 592 but you expected 531. Why, and what is the fix?" Expected: `hb` has 61 missing values, which Stata treats as large numbers, so they pass `>= 11`; use `count if hb >= 11 & !missing(hb)`.

**Caveats.** The command examples follow the manual and were checked against the ANC counts in the CSV, but were not run in Stata in the authoring environment. Test each block before teaching, and check option names with `help list`, `help summarize`, `help tabulate` and `help language` in your version.
