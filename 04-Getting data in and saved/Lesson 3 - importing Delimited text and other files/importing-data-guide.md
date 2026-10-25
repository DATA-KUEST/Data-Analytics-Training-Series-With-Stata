# Learning Notes: Importing Delimited Text and Files from Other Software

**Part of:** Lesson 2, Importing and Exploring Data  |  **Read and practise:** about 120 minutes  |  **Data:** the `data/import_practice/` files in this repo (fictional primary health centres)

Most real data does not arrive as a Stata `.dta` file. It arrives as a CSV from a database, an Excel workbook from a partner organisation, an SPSS file from a survey agency, or a fixed-width text file from a government system. Importing is where many analyses quietly go wrong: leading zeros vanish, "NA" turns a number column into text, accented names turn into garbage, a title row becomes the header. This guide teaches you to bring data in **correctly, repeatably and with an audit trail**.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 8 ("Importing data"), and checked against the `[D] import delimited`, `[D] import excel`, `[D] import spss` and `[D] import sas` entries on stata.com. The explanations, examples, practice files and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Choose the right import method for any file type
- Import comma-, tab-, semicolon- and space-delimited text with `import delimited`
- Control variable names, header rows, data types, quotes, number formats and encodings
- Import Excel workbooks (sheets, cell ranges, header rows)
- Import SPSS and SAS files and keep their labels
- Read fixed-width text with `infix`, and know when to use `infile`, ODBC and JDBC
- Spot and fix typical import problems *before* analysing
- Export data to CSV and Excel for colleagues
- Write an import do-file that leaves an audit trail

## Contents
1. [The import mindset](#1-the-import-mindset)
2. [Which command for which file?](#2-which-command-for-which-file)
3. [The quickest route: copy and paste](#3-the-quickest-route-copy-and-paste)
4. [`import delimited`: the workhorse](#4-import-delimited-the-workhorse)
5. [Variable names and header rows](#5-variable-names-and-header-rows)
6. [Types: numbers, text, leading zeros and "NA"](#6-types-numbers-text-leading-zeros-and-na)
7. [Delimiters, quotes and decimal marks](#7-delimiters-quotes-and-decimal-marks)
8. [Encoding: accents and special characters](#8-encoding-accents-and-special-characters)
9. [Importing part of a file](#9-importing-part-of-a-file)
10. [Excel files with `import excel`](#10-excel-files-with-import-excel)
11. [SPSS and SAS files](#11-spss-and-sas-files)
12. [Fixed-width and other text formats: `infix` and `infile`](#12-fixed-width-and-other-text-formats-infix-and-infile)
13. [Databases and other sources](#13-databases-and-other-sources)
14. [After every import: a checklist](#14-after-every-import-a-checklist)
15. [Exporting data](#15-exporting-data)
16. [An import do-file with an audit trail](#16-an-import-do-file-with-an-audit-trail)
17. [Troubleshooting](#17-troubleshooting)
18. [Practice exercises I1 to I14](#18-practice-exercises-i1-to-i14)
19. [Quick reference card](#19-quick-reference-card)
20. [Facilitator notes](#20-facilitator-notes)

---

## 1. The import mindset

Three principles:

1. **Never trust an import until you have looked at it.** Stata guesses variable types and header rows; guesses can be wrong.
2. **Import by command, not by clicking.** The manual makes the point: copying and pasting is a great way to bring data in, but if you need a *clear audit trail* for your data, you need another way. A command in a do-file is that audit trail.
3. **Keep the original file untouched** in `data/raw/`, import it, and save the result as a `.dta` file in `data/clean/` (see the [opening and saving guide](opening-and-saving-dta-guide.md)).

## 2. Which command for which file?

The manual's summary of choices, extended:

| If you have... | Use |
|----------------|-----|
| A CSV or tab-delimited text file exported from a spreadsheet or database | **`import delimited`** |
| A Microsoft Excel `.xls` or `.xlsx` file | **`import excel`** |
| An IBM SPSS Statistics `.sav` file (or compressed `.zsav`) | **`import spss`** |
| A SAS `.sas7bdat` file | **`import sas`** |
| A SAS V5 or V8 Transport file | `import sasxport5` / `import sasxport8` |
| A fixed-format text file (data aligned in columns) | **`infix`**, or `infile` with a dictionary |
| Simple data separated by spaces | `infile` |
| A database with an ODBC driver | `odbc` |
| A database accessible with JDBC | `jdbc` |
| Economic data from the Federal Reserve | `import fred` |
| Haver Analytics databases | `import haver`, `import haverdirect` |
| A dBASE file | `import dbase` |
| A small table you can see on screen | Copy and paste into the Data Editor |
| Something else | A third-party transfer program, or ask the source for CSV |

The full list is in `help import`. **Rule of thumb:** if the source can give you either a native file or a CSV, a *well-formed CSV* is often the safest, because it is plain text you can inspect.

## 3. The quickest route: copy and paste

For a small table, copy and paste works. Steps from the manual:

1. `clear` any current data.
2. Copy the data (from a spreadsheet, database, or even a comma-separated text file).
3. Open the Data Editor in **edit** mode.
4. Choose **Edit > Paste special...**. Stata detects the column delimiters and shows a preview of how the data would look.
5. Click **OK**.

Cautions from the manual:
- Spreadsheets can contain formatting that ruins the rectangular form. Make sure there are **no blank rows, blank columns, repeated headers or merged cells**.
- Pasting leaves no command in your do-file. **Use it for exploration, not for production work.** See the [Data Editor guide](data-editor-guide.md).

## 4. `import delimited`: the workhorse

`import delimited` reads text files in which each line is an observation and the values are separated by a delimiter such as a comma, tab or semicolon. It was developed for files created by spreadsheet or database programs.

### 4.1 The simplest case
```stata
import delimited "data/import_practice/phc_comma.csv", clear
describe
list in 1/5
```
- Give the file name. **Quote it** if it has spaces. Include the path if it is not in the working directory (see the [working directory guide](../lesson-01-getting-started/working-directory-guide.md)).
- If you omit the extension, `.csv` is assumed.
- By default the command works out the delimiter itself (comma or tab, from the first line of data), decides whether there is a header, and guesses each column's type.
- The `clear` option replaces any data in memory. Without it, Stata refuses if data are loaded.

On success Stata reports something like `(9 vars, 12 obs)`, and may also report `(encoding automatically selected: ...)`.

### 4.2 Practice files
The repo's `data/import_practice/` folder holds the same fictional data in different shapes, each with its own quirk:

| File | Format | The quirk |
|------|--------|-----------|
| `phc_comma.csv` | Comma-delimited, header | Ids with leading zeros (`001`), quoted names containing commas, `NA` for a missing number, dates as `dd/mm/yyyy` |
| `phc_semicolon.csv` | Semicolon-delimited | Decimal **commas** in `rating` (`3,5`) |
| `phc_tab.txt` | Tab-delimited | Auto-detected |
| `phc_noheader.csv` | Comma-delimited | **No header row** |
| `phc_latin1.csv` | Comma-delimited | **ISO-8859-1** encoding with accented letters |
| `phc_fixed.txt` | Fixed-width | Columns by position |
| `phc_workbook.xlsx` | Excel, 3 sheets | Title rows above the header in `Q1_2025` |
| `phc_survey.sav` | SPSS | Variable labels and value labels |

All records are fictional. The generator script `make_import_practice.py` is in the same folder.

### 4.3 What the manual's own example teaches
The manual imports a small comma-separated file with no variable names in it. Stata assigns its own names (`v1`, `v2`, ...). You can give better names by listing them *before* the filename, which requires the `using` keyword:

```stata
import delimited make price mpg weight gear_ratio using "a few cars.csv"
```
The same idea applies to our practice files:

```stata
import delimited facility_id name state beds staff deliveries pop rating opened ///
    using "data/import_practice/phc_noheader.csv", clear
```
Note the continuation `///` (see the [do-file guide](../../lessons/lesson-04-do-files-and-log-files/do-file-guide.md)).

## 5. Variable names and header rows

| Situation | What to do |
|-----------|-----------|
| File **has** a header row | Default; Stata detects it. Names are converted to valid Stata names; the original header text is kept as the **variable label** |
| File has **no** header | `varnames(nonames)`, or give names yourself before `using` |
| Header is **not** on the first line | `varnames(#)`, where `#` is the line number of the header |
| Names come in **capitals** | `case(preserve)` keeps the file's case; the default is lowercase; `case(upper)` for capitals |
| You want your **own names** | List them before `using`; they override the header |

```stata
import delimited "data/import_practice/phc_comma.csv", clear
describe          // the column "facility name" becomes a valid name; the original is the label
rename facilityname facility_name        // adjust to the name that describe shows
```
Variable names in Stata must be 1 to 32 characters, with letters, digits and underscores only, not starting with a digit. Names with spaces are not allowed. Always check with `describe` how Stata converted yours.

## 6. Types: numbers, text, leading zeros and "NA"

Stata decides the type of each column from its contents. This causes the most common import surprises.

| Symptom | Cause | Fix |
|---------|-------|-----|
| `001` becomes `1` | Column looked numeric, leading zeros dropped | `stringcols(1)` (column number) or `stringcols(_all)` for all text |
| A number column becomes text | A non-numeric entry such as `NA`, `-`, `n/a`, `*` appears in it | `numericcols(#)` forces numeric; non-numeric entries become missing (`.`) |
| Large identifiers get duplicated or rounded | Not enough precision in `float` | `asdouble` |
| Dates arrive as text (`14/03/2015`) | Stata does not guess dates | Convert after import: `generate opened_d = date(opened, "DMY")` then `format opened_d %td` |
| Thousand separators (`1,234`) become text | Group separator not understood | `groupseparator(",")` |
| Decimal commas (`3,5`) become text | Number format differs | `decimalseparator(",")` |

Example on `phc_comma.csv`:
```stata
import delimited "data/import_practice/phc_comma.csv", ///
    stringcols(1) numericcols(6) asdouble clear
describe
generate opened_d = date(opened, "DMY")
format opened_d %td
```
Column numbers refer to the position in the file: `facility_id` is 1, `facility name` is 2, `state` 3, `beds` 4, `staff` 5, `monthly_deliveries` 6, `catchment_pop` 7, `rating` 8, `opened` 9.

Other type options:
- `asfloat` and `asdouble` choose the storage type for non-integer data (otherwise the default follows `set type`).
- `favorstrfixed` stores strings as fixed-length `str#` where possible; by default Stata may use `strL` when that saves space.

**Missing-value codes.** Many sources use special codes for "missing": `NA`, `.`, `-`, `-9`, `99`, `999`. After import, convert to proper missing values (`mvdecode`, `replace ... = .`) as covered in Lesson 3. Never leave `99` in a numeric variable and calculate with it.

## 7. Delimiters, quotes and decimal marks

### 7.1 Delimiters
Stata detects commas and tabs automatically. For other delimiters:

```stata
import delimited "data/import_practice/phc_semicolon.csv", delimiters(";") clear
import delimited "report.txt", delimiters("whitespace") clear
import delimited "report.txt", delimiters(" ", collapse) clear     // repeated spaces count as one
import delimited "tab_file.txt", delimiters("\t") clear
```
- `delimiters("chars")` sets the separator.
- `collapse` treats consecutive delimiters as one (good for space-aligned files).
- `asstring` treats a whole multi-character string as a single delimiter.

### 7.2 Decimal commas
```stata
import delimited "data/import_practice/phc_semicolon.csv", ///
    delimiters(";") decimalseparator(",") clear
summarize rating
```
Without `decimalseparator(",")`, the `rating` column stays as text. An alternative is `parselocale()`, which parses numbers using a stated locale.

### 7.3 Quotes
Fields containing the delimiter must be quoted in the file (`"St. Mary's, Ikeja"`). Stata recognises these *binding quotes* so the comma inside is not treated as a separator. Options:

| Option | Meaning |
|--------|---------|
| `bindquotes(loose)` (default) | Quotes must match on the same line |
| `bindquotes(strict)` | Keep looking across lines for the closing quote; use when a quoted field contains line breaks |
| `bindquotes(nobind)` | Ignore quotes for binding |
| `stripquotes(yes | no | default)` | Remove all quotes, keep them, or remove only binding quotes |
| `maxquotedrows(#)` | How many lines a quoted field may span under `strict` (default 20) |

In `phc_comma.csv` the name `Rafin Zurfi "Model" Clinic` contains doubled quotes. The default handling turns two adjacent quotes into a single literal quote. Check with `list facility_name if facility_id == "004"`.

### 7.4 Blank lines
`emptylines(skip)` (default) ignores blank lines; `emptylines(include)` turns them into rows of missing values.

## 8. Encoding: accents and special characters

Text files store characters in an **encoding**. Modern files are usually UTF-8, but files from older Windows systems are often ISO-8859-1 (Latin-1) or similar. If the encoding is wrong, accented letters appear as strange symbols.

```stata
import delimited "data/import_practice/phc_latin1.csv", clear
list
```
Stata tries to detect the encoding and reports `(encoding automatically selected: ...)`. If the result looks wrong, state it yourself:

```stata
import delimited "data/import_practice/phc_latin1.csv", encoding("ISO-8859-1") clear
```
Facts from the reference:
- ASCII and UTF-8 strings display correctly in the Data Editor and Results window.
- Extended ASCII may display incorrectly unless you give `encoding()` so Stata converts it to UTF-8.
- Exported files are always UTF-8.
- `charset()` is a synonym for `encoding()`.
- After import, `return list` shows the encoding used (`r(encoding)`).

## 9. Importing part of a file

For large files, or files with notes at the end:

```stata
import delimited "data/import_practice/phc_comma.csv", rowrange(2:6) clear      // rows 2 to 6
import delimited "data/import_practice/phc_comma.csv", colrange(1:4) clear      // columns 1 to 4
```
`rowrange()` counts the header line as row 1 and still reads the header. Bounds are optional: `rowrange(10:)` means "from row 10 to the end". Check with `count` that you have the rows you meant.

## 10. Excel files with `import excel`

`import excel` reads `.xls` and `.xlsx` files directly, on Windows, Mac and Linux. The file extension determines the format. If you give no extension, Stata looks for `.xls` first, then `.xlsx`.

### 10.1 Look before you load
A workbook can contain several sheets. List them without loading anything:
```stata
import excel "data/import_practice/phc_workbook.xlsx", describe
return list              // number of sheets, names and ranges
```
This stores the number of worksheets in `r(N_worksheet)` and each sheet's name and cell range in `r(worksheet_#)` and `r(range_#)`.

### 10.2 Basic import
```stata
import excel "data/import_practice/phc_workbook.xlsx", sheet("Q2_2025") firstrow clear
```
| Option | Meaning |
|--------|---------|
| `sheet("name")` | Which worksheet (default: the first) |
| `firstrow` | Use the first row as variable names; names are converted to valid Stata names and the originals kept as variable labels |
| `cellrange(A4:F16)` | Only this block of cells |
| `case(preserve | lower | upper)` | Case of names when using `firstrow` (default preserve) |
| `allstring` | Import everything as text (useful to inspect messy cells) |
| `clear` | Replace data in memory |

### 10.3 When the header is not in row 1
The `Q1_2025` sheet has three title rows above the header. Start the range at the header row:
```stata
import excel "data/import_practice/phc_workbook.xlsx", ///
    sheet("Q1_2025") cellrange(A4) firstrow clear
```
(A range such as `A4:F16` also works.) If you forget this, the title text becomes the header and every column turns into text.

### 10.4 Picking columns
```stata
import excel facility_id=A state=C beds=D using "data/import_practice/phc_workbook.xlsx", ///
    sheet("Q2_2025") cellrange(A2) clear
```
This `extvarlist` form names columns by letter. It cannot be combined with `firstrow`.

### 10.5 Types and dates
- If a column contains **any** non-numeric text, the **whole column** is imported as a string.
- A numeric column formatted as dates becomes a Stata date (or a datetime if times are present).
- Excel stores dates using the 1900 or 1904 date system; Stata handles both.
- Cells with text such as `001` stay text, which preserves leading zeros. Cells where someone typed `1` and formatted it as `001` are numbers, and the zeros are lost.

### 10.6 Limits and advice
- `.xls`: 65,536 rows and 256 columns. `.xlsx`: 1,048,576 rows and 16,384 columns, with a 40 MB limit applied by `import excel` for performance reasons.
- Workbooks with merged cells, colours-as-data, notes in cells, totals rows or several tables on a sheet are not data tables. Clean the layout, or save each table as CSV, or select exact ranges.
- Avoid formulas, hidden rows and merged cells in files you will import regularly.
- Excel will happily turn identifiers into numbers or dates (such as `1-2` becoming a date). Inspect the source if values look odd.

## 11. SPSS and SAS files

### 11.1 SPSS (`import spss`)
```stata
import spss using "data/import_practice/phc_survey.sav", clear
describe
label list
```
- Reads `.sav` files from SPSS version 16 or later, and compressed `.zsav` files from version 21 or later (add the `zsav` option).
- **Variable labels** are kept (labels over 256 characters are truncated and the original stored as a characteristic).
- **Value labels** for numeric variables are attached as value label sets named `labels#`. Value labels for string variables are ignored.
- Variable names that are not valid in Stata become `v#`, with the original stored as a characteristic.
- Options: `case(lower | upper | preserve)` (default preserve), `clear`, `encoding()` to override a wrong file header.
- Import only some variables: `import spss facility_id beds using "phc_survey.sav", clear`.
- Export with `export spss`.

### 11.2 SAS (`import sas`)
```stata
import sas using "survey.sas7bdat", clear
import sas using "survey.sas7bdat", bcat(formats) clear      // with value labels from formats.sas7bcat
```
- Reads SAS version 7 or higher `.sas7bdat` files. (The manual's summary says files created on a Windows machine; check `help import sas` for your platform.)
- **SAS does not attach value labels to variables.** Load the catalogue with `bcat()`, then use `label list` and `label values` to attach a set to a variable.
- Options: `case()`, `clear`, `encoding()`.
- Variable names invalid in Stata become `v#`; labels longer than 80 characters are truncated and the original stored as a characteristic.
- Transport files: `import sasxport5`, `import sasxport8`.

### 11.3 Limits
`import spss` and `import sas` can bring in up to 32,766 variables at once (2,048 in Stata/BE). Larger files must be split into more than one Stata dataset.

### 11.4 Why labels matter
The SPSS file arrives with labels. A CSV does not. This is one reason to ask a survey agency for the **native file** as well as a CSV: you keep their variable and value labels.

## 12. Fixed-width and other text formats: `infix` and `infile`

Some government and legacy systems export **fixed-width** files with no delimiters: each field occupies fixed character positions. `phc_fixed.txt` is an example:

```
001Ajegunle PHC                  Lagos    12 18
002St. Mary's, Ikeja             Lagos    30 41
```
Here the id is in columns 1 to 3, the name in 4 to 33, state 34 to 41, beds 42 to 44, staff 45 to 47.

```stata
infix str3 id 1-3 str30 name 4-33 str8 state 34-41 int beds 42-44 int staff 45-47 ///
    using "data/import_practice/phc_fixed.txt", clear
list in 1/3
```
- `infix` is for data aligned in columns, even if split across several lines per observation.
- `infile` is for simple data separated by spaces, or for rigidly formatted data using a **dictionary** file that describes the layout. See `help infile` and `help infix`.
- You need the **codebook or layout description** from the data provider. Without it, you cannot know the column positions. Always keep it with the raw file.

## 13. Databases and other sources

- **ODBC:** `odbc` pulls data directly from any data source for which you have ODBC drivers, without an interim file. Handy for hospital or survey databases. See `help odbc`.
- **JDBC:** `jdbc` loads data from a database, executes SQL statements, and inserts data, using JDBC drivers.
- **Other specialised importers:** `import fred`, `import haver`, `import dbase`.
- **From the web:** `use` and `webuse` read `.dta` files from URLs. `import delimited` can also read from a URL; see `help import delimited`.

For this course, the CSV, Excel, SPSS and SAS routes cover almost everything you will meet.

## 14. After every import: a checklist

Make this a habit; put it in your import do-file.

```stata
describe                     // variable names, types, labels
count                        // is the number of observations what the source says?
codebook, compact            // quick profile of every variable
summarize                    // ranges: any impossible values?
list in 1/10                 // does it look right?
duplicates report facility_id    // are identifiers unique?
tabulate state               // categories: any spelling variants?
misstable summarize          // how much is missing?
```
Questions to ask:

| Check | Why |
|-------|-----|
| Number of rows and columns match the source? | Truncated or extra rows from blank lines or notes |
| Are numeric variables numeric? | A single "NA" can turn a number column into text |
| Did leading zeros survive? | Identifiers must remain text |
| Do dates look like dates? | Text dates cannot be sorted or subtracted |
| Do special characters look right? | Encoding problems |
| Are there impossible values (`99`, `-9`, `999`)? | Missing-value codes |
| Are labels present? | CSV has none; plan to add them (Lesson 3) |
| Did the header row import as names, not as data? | Title rows or a header not on line 1 |

Then save the imported data as `.dta` (section 16) so you do not repeat the import every time.

## 15. Exporting data

You will often hand data to others.

### 15.1 To CSV
```stata
export delimited using "output/phc_export.csv", replace
export delimited facility_id state beds using "output/phc_small.csv", replace
export delimited using "output/phc_export.csv" if beds >= 15, replace
```
- Default delimiter is a comma; `delimiter(tab)` for tab-delimited.
- `novarnames` omits the header row.
- `nolabel` writes numeric codes rather than value labels; by default value labels are written.
- `quote` puts double quotes around all strings (by default only strings that contain spaces or the delimiter are quoted).
- `datafmt` writes values using display formats.
- Exported files are always UTF-8.

### 15.2 To Excel
```stata
export excel using "output/phc_export.xlsx", firstrow(variables) replace
```
- `firstrow(variables)` writes variable names in the first row; `firstrow(varlabels)` writes labels.
- `sheet("name", modify | replace)` chooses the sheet; `cell(B2)` sets where to start.
- `missing("NA")` writes missing values as text instead of leaving the cells empty.

### 15.3 Good practice
- Export from a do-file and keep the do-file.
- Do not export identifiable personal data unless you are authorised to.
- Prefer CSV for long-term exchange: any software can read it.

## 16. An import do-file with an audit trail

```stata
*------------------------------------------------------------------*
* 01_import_phc.do : import the PHC practice file
* Input  : data/import_practice/phc_comma.csv   (original, never edited)
* Output : data/phc_imported.dta
*------------------------------------------------------------------*
version 17
clear all
set more off
capture log close
capture mkdir "logs"
log using "logs/01_import_phc.log", replace text

* ---- 1. Import ------------------------------------------------------
confirm file "data/import_practice/phc_comma.csv"
import delimited "data/import_practice/phc_comma.csv", ///
    stringcols(1) numericcols(6) asdouble clear
display "Imported: " r(N) " observations, " r(k) " variables, encoding " r(encoding)

* ---- 2. Tidy the obvious -------------------------------------------
rename facilityname facility_name        // use the name that describe shows
generate opened_d = date(opened, "DMY")
format opened_d %td
label variable opened_d "Date facility opened"

* ---- 3. Check ------------------------------------------------------
assert _N == 12
isid facility_id
codebook, compact

* ---- 4. Save -------------------------------------------------------
compress
save "data/phc_imported.dta", replace
log close
```
Why this works: it **confirms** the source exists, **records** what was imported, **checks** it, and **saves** it. The original file is never changed. See the [log file guide](../../lessons/lesson-04-do-files-and-log-files/log-file-guide.md).

## 17. Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `file ... not found` **r(601)** | Wrong working directory, path or extension | `pwd`, `dir`; quote the path |
| `no; dataset in memory has changed since last saved` **r(4)** | Data loaded and changed | Save, or add `clear` |
| Everything lands in one column | Wrong delimiter | `delimiters(";")` etc. |
| Variable names are `v1`, `v2`... | No header, or header not detected | `varnames(1)`, or give names before `using` |
| Header text appears as the first observation | Header not detected | `varnames(1)` |
| Number column is text | Non-numeric entry such as `NA` | `numericcols(#)`, then check |
| Leading zeros lost | Numeric guess | `stringcols(#)` |
| Decimals are wrong or numbers are text | Decimal comma | `decimalseparator(",")` |
| Strange characters | Wrong encoding | `encoding("ISO-8859-1")` and similar |
| Fewer rows than the source | Blank lines, `rowrange`, or quoted line breaks | Check `emptylines()`, `bindquotes(strict)` |
| More rows than expected | Notes or totals at the bottom of the file | `rowrange()` or clean at the source |
| Excel import: wrong header | Title rows above the header | `cellrange(A4)` etc. |
| Excel import: all text | Mixed content in columns | Clean the sheet, or `allstring` and convert |
| Value labels missing | CSV carries none | Ask for the native file, or label in Lesson 3 |
| SAS labels missing | Catalogue not loaded | `bcat()` |

## 18. Practice exercises I1 to I14

Solutions are in `exercise-solutions/lesson-02/import-practice.do`. Run from the repo's top folder. Expected values come from the practice files and are listed in `data/README.md`.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**I1 🟢 Paste special.** Copy the first five rows of `phc_comma.csv` (open it in a text editor) and paste them into the Data Editor with **Edit > Paste special...**. What does the preview show? Why is this not suitable for your master analysis?

**I2 🟢 Default import.** Import `phc_comma.csv` with no options. How many variables and observations? Run `describe`. Which variables are text? What happened to `facility_id`?

**I3 🟢 Fix the identifier.** Re-import using `stringcols(1)`. Confirm `facility_id` shows `001`, `002`, and so on.

**I4 🟢 The NA problem.** What type is `monthly_deliveries` after the default import? Why? Re-import with `numericcols(6)`. What is the mean? How many are missing?

**I5 🟡 Semicolons and decimal commas.** Import `phc_semicolon.csv` (a) without options, (b) with `delimiters(";")`, (c) with `delimiters(";") decimalseparator(",")`. What changes? What is the mean `rating` in (c)?

**I6 🟡 Tab file.** Import `phc_tab.txt`. Did you need to say it is tab-delimited? Check with `return list` (`r(delimiter)`).

**I7 🟡 No header.** Import `phc_noheader.csv` (a) default, (b) naming the variables yourself. What are the default names?

**I8 🟡 Encoding.** Import `phc_latin1.csv`. Do the accents look right? Re-import with `encoding("ISO-8859-1")`. What does `r(encoding)` report?

**I9 🟡 Dates.** In the `phc_comma.csv` import, convert `opened` to a Stata date. Which facility opened first? How many opened before 2012?

**I10 🟡 Excel.** Use `import excel, describe` on the workbook. List the sheets. Import `Q2_2025` with `firstrow`. How many observations? Then import `Q1_2025` correctly, skipping the title rows.

**I11 🟡 SPSS.** Import `phc_survey.sav`. List the value labels. How does `tabulate state` look compared with the CSV version?

**I12 🔴 Fixed width.** Import `phc_fixed.txt` with `infix`. Compare the result with the CSV import: are all names, states and numbers identical?

**I13 🔴 Compare sources.** Import the same data from the CSV, the Excel `Q2_2025` sheet and the SPSS file. Use `compare` or `cf` to see which variables differ (`help cf`). What differences come from the import method itself?

**I14 🔴 A full import do-file.** Write the import do-file in section 16 for `phc_comma.csv`. Add an `assert` for the expected number of observations and a `duplicates report`. Run it from a clean start twice. Is the second run identical? Check the log.

## 19. Quick reference card

| Task | Command |
|------|---------|
| CSV or tab file | `import delimited "file.csv", clear` |
| Semicolon file | `import delimited "file.csv", delimiters(";") clear` |
| Decimal commas | `decimalseparator(",")` |
| No header | `varnames(nonames)` |
| Header on line # | `varnames(#)` |
| Own names | `import delimited a b c using "file.csv", clear` |
| Keep text (leading zeros) | `stringcols(#)` |
| Force numbers | `numericcols(#)` |
| Large ids | `asdouble` |
| Encoding | `encoding("ISO-8859-1")` |
| Part of file | `rowrange(2:100)` / `colrange(1:4)` |
| List sheets | `import excel "f.xlsx", describe` |
| Excel sheet, header | `import excel "f.xlsx", sheet("name") firstrow clear` |
| Excel from a cell | `cellrange(A4)` |
| SPSS | `import spss using "f.sav", clear` |
| SAS (+ labels) | `import sas using "f.sas7bdat", bcat(fmt) clear` |
| Fixed width | `infix str3 id 1-3 ... using "f.txt", clear` |
| Database | `odbc` / `jdbc` |
| Export CSV | `export delimited using "f.csv", replace` |
| Export Excel | `export excel using "f.xlsx", firstrow(variables) replace` |
| Check after import | `describe`, `count`, `codebook, compact`, `summarize`, `list in 1/10` |

## 20. Facilitator notes

**Timing (two 60-minute sessions or one 120-minute session):** Session A: sections 1 to 8 and exercises I1 to I9. Session B: sections 9 to 17 and exercises I10 to I14.

**Before the session**
- Participants should have the repo's `data/import_practice/` folder (see `data/README.md`) and a working directory set (see the [working directory guide](../lesson-01-getting-started/working-directory-guide.md)).
- Check the Stata version: `import spss` and `import sas` require a version that includes them, and some options differ by release.
- Open `phc_comma.csv` in a text editor beforehand so participants *see* the raw file before importing it.

**Common stumbling blocks**
- Importing and never looking at the result.
- Losing leading zeros in identifiers.
- A single `NA` making a number column text.
- Confusing the Excel title rows with the header.
- Garbled accents.
- Copy-paste imports that cannot be reproduced.

**Teaching tips**
- "Predict, then run": ask what each import will do before running it.
- Have participants break each file on purpose (remove `stringcols`, remove `delimiters`) and read the symptom.
- Ask each pair to write a one-line "import recipe" for a file their own organisation sends regularly.
- Emphasise: a CSV carries no labels; a native SPSS or SAS file does. Ask the data owner for both.

**Assessment prompt (5 minutes):** "A colleague imports a CSV and gets `facility_id` values 1, 2, 3 instead of 001, 002, 003, and `monthly_deliveries` as a string variable. Explain both problems and the options that fix them." Expected: leading zeros lost because the column looked numeric, fix with `stringcols()`; non-numeric `NA` made the column text, fix with `numericcols()` which turns `NA` into missing.

**Note on versions.** This guide follows the Windows edition of the Getting Started manual and the current reference entries for the import commands. Options, supported file versions and platform notes differ across Stata releases. Check `help import delimited`, `help import excel`, `help import spss` and `help import sas` in your own installation. The practice files are fictional and safe to share.
