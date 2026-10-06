# Lesson 1 Exercises: Getting Started with STATA

**Level:** Beginner  |  **Time:** about 45 minutes  |  **Dataset:** `auto.dta` (built into Stata, no download needed)

## Learning objectives
By the end of this lesson you will be able to:
- Find your way around the Stata interface
- Load a dataset and inspect its structure
- Use `describe`, `list`, `summarize`, `count` and `tabulate`
- Save your work in a do-file and record output in a log file
- Use `help` to look up any command

> **How to work:** create a new do-file for each exercise (`1a.do`, `1b.do`, etc.). Save each one in a folder on your computer, for example `my-dataquest-work/lesson-01/`. Every do-file should start by loading the data, so it runs on its own.

---

## Part 1: Look around

### 🟢 1a. Know your interface
Open Stata and identify these five windows: **Command**, **Results**, **History**, **Variables**, **Properties**.

Then type this in the Command window and press Enter:

```stata
display "Hello, DATAQUEST"
```

**Expected:** `Hello, DATAQUEST` appears in the Results window.

### 🟢 1b. Load a dataset
Load Stata's built-in 1978 automobile dataset.

**Expected:** Stata prints `(1978 automobile data)`.

<details><summary>Hint</summary>
The command to load built-in example data is <code>sysuse</code>. Add <code>, clear</code> at the end so it works even when other data is already in memory.
</details>

### 🟢 1c. Describe the structure
Find out how many observations and variables the dataset has, and what the variables are.

**Expected:** 74 observations and 12 variables.

<details><summary>Hint</summary>
Try <code>describe</code>.
</details>

### 🟢 1d. Look at the data
Show the first 5 rows, displaying only `make`, `price` and `mpg`.

**Expected:** a table of 5 cars, starting with the AMC Concord.

<details><summary>Hint</summary>
<code>list</code> accepts a variable list and an <code>in</code> range, e.g. <code>in 1/5</code>.
</details>

---

## Part 2: Summarise the data

### 🟢 1e. Summary statistics
Get the number of observations, mean, standard deviation, minimum and maximum for `price` and `mpg`.

**Expected:** mean price is about 6165.26 and mean mpg is about 21.30.

### 🟢 1f. Count with a condition
How many cars are foreign (`foreign == 1`)?

**Expected:** 22

<details><summary>Hint</summary>
<code>count if ...</code> (remember that a test for equality uses <code>==</code>, not <code>=</code>).
</details>

### 🟢 1g. Frequency table
Produce a frequency table of `foreign`.

**Expected:** 52 domestic cars (70.27%) and 22 foreign cars (29.73%).

### 🟡 1h. Find the priciest car
Sort the cars from most to least expensive and list the top 3 (`make` and `price`).

**Expected:** the first row is the Cad. Seville at 15,906.

<details><summary>Hint</summary>
<code>gsort -price</code> sorts in descending order. The minus sign means descending.
</details>

### 🟡 1i. Compare groups
Get summary statistics for `mpg` separately for domestic and foreign cars.

**Expected:** mean mpg is about 19.83 for domestic and about 24.77 for foreign.

<details><summary>Hint</summary>
Put <code>bysort foreign:</code> in front of your summarize command.
</details>

---

## Part 3: Work like an analyst

### 🟢 1j. Your first do-file
Combine exercises 1b, 1c, 1e, 1g and 1i into **one** do-file called `1j.do`. Add a comment line (starting with `*`) above each command saying what it does. Run it with the **Do** button or by typing `do 1j.do`.

**Expected:** all the output appears in the Results window in one run.

### 🟢 1k. Record a log
Edit `1j.do` so that it opens a log called `lesson01.log` at the top and closes it at the bottom. Run it again and open the log file in a text editor.

**Expected:** a `lesson01.log` file containing everything that appeared in the Results window.

<details><summary>Hint</summary>
<code>log using lesson01.log, replace</code> at the start and <code>log close</code> at the end.
</details>

### 🟢 1l. Teach yourself with help
Open the help page for `summarize`. Find what the `detail` option adds, then run `summarize price, detail`.

**Expected:** additional statistics, including percentiles, variance, skewness and kurtosis.

### 🔴 1m. Challenge: above-average fuel economy
Count how many cars have `mpg` above the dataset's average, **without typing the average by hand**.

<details><summary>Hint</summary>
After <code>summarize mpg</code>, Stata stores the mean in <code>r(mean)</code>. Use it inside <code>count if</code>. Look at <code>return list</code> to see what else was stored.
</details>

---

## Think about it
Answer in your own words (write a sentence or two in a comment in your do-file):

1. Why is it better to run commands from a do-file than to type them in the Command window?
2. Foreign cars average higher mpg than domestic cars. Can we conclude that being foreign *causes* better fuel economy? What else might explain the difference?

## Solutions
When you've attempted every exercise, compare with [`exercise-solutions/lesson-01`](../../exercise-solutions/lesson-01/).
