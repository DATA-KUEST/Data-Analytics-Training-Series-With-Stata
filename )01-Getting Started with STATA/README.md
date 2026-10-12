# Lesson 2 Exercises: Importing and Exploring Data

**Level:** Beginner  |  **Time:** about 75 minutes  |  **Dataset:** `data/anc_survey` (synthetic antenatal care survey, see [`data/README.md`](../../data/README.md) for the data dictionary)

## Learning objectives
By the end of this lesson you will be able to:
- Set a working directory and use relative file paths
- Import data from CSV, Excel and Stata formats
- Inspect a new dataset: structure, variable types, missing values
- Spot common data-quality problems *before* analysing
- Produce frequency tables, two-way tables and group summaries
- Save a working copy without touching the raw data

> **Before you start:** download or clone this repo. Create a new do-file for each exercise (`2a.do`, `2b.do`, ...). Run them with your working directory set to the **repo root** (the folder containing `data/` and `lessons/`), so that paths like `data/anc_survey.csv` work.
>
> **Golden rule:** never overwrite the raw files in `data/`. Always save your own changes under a new name.

---

## Part 1: Getting data into Stata

### 🟢 2a. Set your working directory
Use Stata commands to move into the repo root folder and then confirm where you are.

**Expected:** the confirming command prints the full path to your `dataquest-stata-course` folder.

<details><summary>Hint</summary>
<code>cd "path/to/folder"</code> changes directory, <code>pwd</code> prints it. Always put paths in quotes, especially when they contain spaces.
</details>

### 🟢 2b. Import a CSV file
Import `data/anc_survey.csv`, replacing any data already in memory.

**Expected:** Stata prints `(13 vars, 1,212 obs)`.

<details><summary>Hint</summary>
CSV files are comma-delimited text files: <code>import delimited "path", clear</code>.
</details>

### 🟢 2c. Import an Excel file
Import `data/anc_survey.xlsx`. The first row contains variable names.

**Expected:** `(13 vars, 1,212 obs)`, the same as the CSV.

<details><summary>Hint</summary>
<code>import excel "path", firstrow clear</code>. Add <code>sheet("anc_survey")</code> if there is more than one sheet.
</details>

### 🟢 2d. Open a Stata dataset
Open `data/anc_survey.dta`.

**Expected:** Stata prints nothing at all, which is normal for `use`. Check the Variables window to confirm that 13 variables are loaded.

<details><summary>Hint</summary>
<code>use "path", clear</code>
</details>

---

## Part 2: Explore before you analyse

For all exercises below, start your do-file with `use "data/anc_survey.dta", clear`.

### 🟢 2e. Check the structure
Find out how many observations and variables the data has, and which variables are **strings**.

**Expected:** 1,212 observations and 13 variables. Three variables are strings: `state`, `residence` and `visit_date`.

**Question:** the study has 1,200 women. Why might the data have 1,212 observations? (Keep this in mind for 2k.)

### 🟢 2f. Eyeball the data
Open the Data Browser, then list the first 10 rows of `id`, `state`, `age`, `anc_visits` and `hb`.

**Expected:** a table of 10 rows. Note that some `hb` values show as a dot `.`, which is Stata's symbol for a missing number.

<details><summary>Hint</summary>
<code>browse</code> opens the browser. <code>list varlist in 1/10</code> prints rows.
</details>

### 🟢 2g. Summary statistics
Summarise `age` and `hb`.

**Expected:**
- `age`: 1,212 observations, mean about 27.06, minimum 15, maximum 45
- `hb`: **1,151** observations, mean about 10.78, minimum 5.5, maximum 15.3

**Question:** why does `hb` have fewer observations than `age`?

### 🟢 2h. Count the missing values
Count how many records have a missing `hb`.

**Expected:** 61

<details><summary>Hint</summary>
<code>count if missing(hb)</code>. In Stata, <code>missing()</code> is the safest way to test for missing values.
</details>

### 🟡 2i. Something looks wrong
Summarise `anc_visits`. Look carefully at the maximum. Then tabulate `anc_visits` to see its values, and count how many records hold the suspicious value.

**Expected:** the maximum is 99 and the mean is about 6.95. The suspicious value appears **40** times.

**Question:** can a woman really have 99 antenatal visits? What might 99 stand for in survey data? Do **not** fix it yet; Lesson 3 covers cleaning. Just write your finding as a comment in your do-file.

### 🟡 2j. Check a categorical variable
Tabulate `state`.

**Expected:** the study covers six states, but the table shows **nine** categories, totalling 1,212. Which categories are really the same state?

### 🟡 2k. Hunt for duplicates
Check whether any `id` appears more than once, then list the repeated records.

**Expected:** the report shows 1,188 observations with one copy and 24 observations in pairs, giving a surplus of **12** records.

<details><summary>Hint</summary>
<code>duplicates report id</code> summarises; <code>duplicates list id</code> shows the actual rows.
</details>

---

## Part 3: Describe the data

### 🟢 2l. Frequency table with percentages
Tabulate `residence`.

**Expected:** Rural 529 (43.65%), Urban 683 (56.35%).

### 🟡 2m. Two-way table
Cross-tabulate `residence` against `facility_delivery`, showing **row percentages**.

**Expected:** among rural women, 42.53% delivered in a facility. Among urban women, 79.06% did.

<details><summary>Hint</summary>
<code>tabulate var1 var2, row</code>. Row percentages sum to 100% across each row.
</details>

### 🟡 2n. Compare groups
Produce the mean of `hb` and `age` separately for urban and rural women in one table.

**Expected:** mean `hb` is about 10.53 for rural and 10.97 for urban women. Mean `age` is about 27.1 for both.

<details><summary>Hint</summary>
<code>tabstat hb age, by(residence) statistics(n mean sd)</code>
</details>

### 🔴 2o. Challenge: anaemia and the missing-value trap
A haemoglobin below 11 g/dL is a common cut-off for anaemia in pregnancy.
1. Count the records with `hb` **below** 11.
2. Count the records with a **measured** `hb` of 11 or above.
3. Now run `count if hb >= 11` and compare it with your answer to part 2. Why do they differ?

**Expected:** 620 below 11; 531 measured at 11 or above; the careless version gives **592**.

<details><summary>Hint</summary>
Stata stores a missing number as a very large value, larger than any real number. So <code>hb >= 11</code> is "true" for every missing value. Combine your condition with <code>!missing(hb)</code>.
</details>

---

## Part 4: Save and document

### 🟢 2p. Save your work and make it reproducible
1. Save the data in memory as `data/anc_survey_working.dta` (not over the original!).
2. Write one do-file, `2p.do`, that opens a log called `lesson02.log`, loads the `.dta`, runs `describe`, `summarize age hb`, `tabulate state`, `tabulate residence facility_delivery, row`, and closes the log.

**Expected:** a `lesson02.log` file containing all of that output.

---

## Think about it
Write short answers as comments in your do-file:

1. If you had not noticed the 99s in `anc_visits`, how would your estimate of the average number of ANC visits be misleading? (Try `summarize anc_visits if anc_visits != 99` to see.)
2. Facility delivery is far more common in urban women. Does that prove urban living *causes* facility delivery? What else differs between urban and rural women in this dataset?
3. Why is it important never to edit or overwrite the raw data file?

## Solutions
Compare with [`exercise-solutions/lesson-02`](../../exercise-solutions/lesson-02/) once you've attempted each exercise.

**Next:** Lesson 3 uses the problems you found here (the 99 codes, inconsistent state names, duplicates and missing values) to teach data cleaning.
