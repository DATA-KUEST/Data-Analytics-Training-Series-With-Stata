# Lesson 1 Exercises: Getting Started with STATA

## ✔️ 1a. Know your interface
- Open Stata and identify these five windows: **Command**, **Results**, **History**, **Variables**, **Properties**.
- Then type this in the Command window and press Enter:
```stata
display "Hello, DATAQUEST"
```

**Expected Display:** `Hello, DATAQUEST` appears in the Results window.

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

