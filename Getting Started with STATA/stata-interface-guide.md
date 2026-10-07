# Learning Notes: The Stata User Interface

**Part of:** Lesson 1, Getting Started  |  **Read time:** about 15 minutes  |  **Do this before the exercises**

Stata gives you two ways to work: **typing commands** and **pointing and clicking** through menus. Both lead to the same place, and this guide shows you where everything lives. The details below follow the Windows version of Stata, so small differences may appear on other systems.

## Contents
1. [The five main windows](#1-the-five-main-windows)
2. [The toolbar](#2-the-toolbar)
3. [The Command window](#3-the-command-window)
4. [The Results window](#4-the-results-window)
5. [The Variables window](#5-the-variables-window)
6. [The Properties window](#6-the-properties-window)
7. [The History window](#7-the-history-window)
8. [Menus and dialogs](#8-menus-and-dialogs)
9. [The working directory](#9-the-working-directory)
10. [Arranging your windows](#10-arranging-your-windows)
11. [Cheat sheet and self-check](#11-cheat-sheet-and-self-check)

---

## 1. The five main windows

When Stata opens, five windows are in use for the whole session:

| Window | What it's for |
|---|---|
| **History** | A record of the commands you've run (failed ones appear in red) |
| **Results** | All commands and their output |
| **Command** | Where you type commands |
| **Variables** | The list of variables in your dataset |
| **Properties** | Details about the selected variable and the dataset |

The main title bar shows the **name of the current dataset** (and the current *frame*, if you are using more than one). Stata also has specialised windows that you open when needed, such as the Viewer, Data Editor, Variables Manager, Do-file Editor and Graph windows.

**Finding a window:** choose it from the **Window** menu or the toolbar. To flip between windows from the keyboard, use **Ctrl+Tab** (cycles through windows *inside* Stata) or **Alt+Tab** (cycles through *all* open programs).

**Right-click is your friend.** Most windows have a right-click menu for copying text, changing preferences, or printing. When you copy or print, right-click inside the window you want, so you know exactly what is being copied.

---

## 2. The toolbar

The toolbar gives one-click access to the most-used features. Hover your mouse over a button for a moment to see a tooltip. Buttons with a small arrow open a menu when you click the arrow.

| Button | What it does |
|---|---|
| **Open** | Opens a Stata dataset |
| **Save** | Saves the dataset in memory to disk |
| **Print** | Shows a list of windows; pick one to print |
| **Log** | Starts a log, or closes, pauses or resumes the current one |
| **Viewer** | Opens or brings forward a Viewer (help and log output) |
| **Graph** | Brings a Graph window to the front |
| **Do-file Editor** | Opens or brings forward a do-file editor |
| **Data Editor (Edit)** | Opens the Data Editor so you can view and change values |
| **Data Editor (Browse)** | Opens the Data Editor in view-only mode |
| **Variables Manager** | Opens the Variables Manager for managing variable properties |
| **Show more results** | Tells Stata to continue when long output has paused |
| **Break** | Stops the task Stata is currently running |

> **Habit to build:** use **Browse** rather than **Edit** when exploring, so you can't change data by accident.

---

## 3. The Command window

This is where you type and submit commands. It supports basic editing, copy and paste, command recall, and shortcuts:

| Key | Action |
|---|---|
| **Page Up** | Step back through earlier commands |
| **Page Down** | Step forward through commands |
| **Tab** | Auto-complete a variable name (or show matching names). If you start with a double quote `"`, it completes **file names** instead |

The command history also records commands sent by menus and dialogs, so you can recall one, edit it and run it again without reopening the dialog.

---

## 4. The Results window

Everything you run, and everything Stata replies, appears here. It's the only main window without a name in its title bar, and it always fills the space left over.

- **Search it:** the find bar is hidden by default. Show it with **Edit > Find...**.
- **Clear it:** right-click inside and choose **Clear results**. This cannot be undone.
- **Scroll while typing:** with the cursor in the Command window, use **Shift + up/down arrow** to scroll by a line, or **Shift + Page Up/Down** to scroll by a page.

---

## 5. The Variables window

It lists the variables in the current dataset along with their labels. You can control what's shown by right-clicking a column header.

**Selecting and using variables**
- Click a variable to select it. **Ctrl-click** adds non-adjacent variables; **Shift-click** selects a range.
- **Double-click** a variable to paste its name into the Command window.
- The leftmost **one-click paste column** also sends a variable to the Command window when you click the arrow that appears on hover.

**Filtering and sorting**
- Type in the **Filter variables here** box to show only matching variables. By default it ignores case and matches any of the words you type, in any visible column. The wrench icon changes this behaviour.
- Click a **column header** to sort: first click ascending, second descending, third back to dataset order.
- Sorting changes the **display only**, never the order of variables in your dataset.

**Right-click menu on a variable**

| Item | Effect |
|---|---|
| Keep only selected variables | Keeps just those variables **in memory** (you are asked to confirm) |
| Drop selected variables | Removes them **from memory** (you are asked to confirm) |
| Copy varlist | Copies the selected names to the clipboard |
| Select all | Selects every variable that passes the current filter |
| Send varlist to Command window | Pastes the selected names into the Command window |
| Font... | Changes the display font |

Keep and drop affect only the data in memory, not the file on disk, unless you save over it. These menu items run ordinary Stata commands, so clicking is the same as typing.

To hide the window, click its close button. To bring it back: **Window > Variables**.

---

## 6. The Properties window

It shows properties of the **selected variable** (or those shared by several selected variables) and of the **dataset**.

- The **padlock icon** in its title bar locks and unlocks editing. It is **locked by default**.
- The **< and > arrows** move to the previous or next variable in the Variables window.
- Every change you make here produces a **command** that appears in the Results window, the Command window and any log, so the change is reproducible.
- It is one of the easiest ways to manage **notes**, **variable and value labels**, and **display formats**.

Hide it with its close box and reveal it with **Window > Properties**. The **Variables Manager** extends these abilities and is worth exploring.

---

## 7. The History window

It lists commands you've entered, with **failed commands and their error codes in red**.

**Filtering:** the **Filter** button in the title bar shows or hides the search tools. Typing in *Filter commands here* narrows the list (ignoring case by default). The **Filter errors** button hides commands that failed.

**Reusing a command**
- **Click once** to copy it into the Command window (replacing what's there).
- **Double-click** to run it again (it is added to the bottom of the list).

**Right-click menu**

| Item | Effect |
|---|---|
| Cut / Copy | Remove or copy selected commands to the clipboard |
| Delete | Removes selected commands from the window |
| Select all / Clear all | Selects or clears every command, including ones hidden by a filter |
| **Do selected** | Re-runs the selected commands, even if some cause errors |
| **Send selected to Do-file Editor** | Puts them in a new do-file editor |
| **Save all... / Save selected...** | Saves the commands as a **do-file** |
| Font... | Changes the display font |

> **Tip:** if you have been experimenting with the point-and-click tools and now want a reproducible script, select the commands in the History window and send them to the Do-file Editor.

---

## 8. Menus and dialogs

You can tell Stata what to do with the **Command window** or with **menus and dialogs**. Each has strengths: dialogs help you discover options, commands are faster and can be saved.

**Where to find things**
- The **Data**, **Graphics** and **Statistics** menus give point-and-click access to almost every command.
- The **User** menu starts nearly empty; programmers can add their own items.
- *Example:* a Poisson regression is under **Statistics > Count outcomes > Poisson regression**, or you can just type `poisson`.

**Inside a dialog**
- Variable boxes show only variables of a suitable type (for example, numeric only).
- Tabs hold the options. Many dialogs have **by/if/in** (choose which observations to use) and **Weights** tabs. Estimation dialogs usually add a **Maximization** tab for optimiser settings.
- Look through every tab the first time you use a dialog to see what it can do.

**The six standard buttons**

| Button | Action |
|---|---|
| **OK** | Runs the command and closes the dialog |
| **Cancel** | Closes without doing anything |
| **Submit** | Runs the command and **keeps the dialog open**, handy for tweaking a graph |
| **Help** (?) | Opens the help file for the command |
| **Reset** | Returns the dialog to its default state (dialogs remember your last entries) |
| **Copy command to Clipboard** | Copies the command instead of running it, so you can paste it into a do-file |

**Learn from your clicks.** A dialog just builds an ordinary command and submits it. You can see that command in the Results and History windows, so reading it teaches you Stata's syntax.

**Open any dialog by command:** type `db` followed by a command name, for example:

```stata
db summarize
```

---

## 9. The working directory

The **status bar** at the bottom of the Stata window always shows the **current working directory**. This is the folder where files go when you use commands such as `save filename` (and where graphs are saved).

- It does **not** change the behaviour of menu actions such as **File > Open** or **File > Save**, which use their own dialogs.
- Change it with the `cd` command, for example `cd "C:/Users/yourname/Documents"`.

---

## 10. Arranging your windows

The default layout works well, so you can skip this section until you want to customise.

**Two kinds of windows**

| Docking windows | Non-docking windows |
|---|---|
| History, Command, Variables, Properties | Results, Graph, Data Editor, Do-file Editor, Viewers, dialogs |
| Can link to each other, share a tabbed window, and auto-hide | Always independent of the main window (except Results, which stays inside it) |

**Rearranging docking windows**
- **Drag** a window by its title bar over the Stata window or another docked window. Docking guides appear and preview where it will land.
- Drop on an **outer guide** to **link** two windows. A splitter appears between them so you can resize.
- Drop on the **centre guide** to **tab** them together, with one tab per window at the bottom. To separate them, drag a tab back out.

**Auto Hide:** click the **pushpin** in a docked window's title bar. Horizontal pin = auto-hide on (the window collapses to a tab on the edge; hover to show it). Vertical pin = off. If you auto-hide the History window in its default place it can cover the start of the Command window, so dock it on the right edge first.

---

## 11. Cheat sheet and self-check

### Quick reference

| I want to... | Do this |
|---|---|
| Re-run an earlier command | Double-click it in History, or press **Page Up** in the Command window |
| Paste a variable name | Double-click it in the Variables window, or type a few letters and press **Tab** |
| Find text in my output | **Edit > Find...** |
| See where my files will go | Look at the status bar, or run `pwd` |
| Change folder | `cd "folder path"` |
| Open a dialog for a command | `db commandname` |
| Turn clicks into a script | History: select commands, then **Save selected...** or **Send selected to Do-file Editor** |
| View data safely | **Data Editor (Browse)**, or the command `browse` |
| Stop a long-running task | **Break** button |

### Self-check questions
1. Name the five main windows. Which one has no name in its title bar?
2. What is the difference between **OK** and **Submit** in a dialog?
3. You drop a variable using the Variables window right-click menu. Is the variable gone from the file on disk? Why or why not?
4. Why is the Properties window locked by default, and what happens to a change you make once it is unlocked?
5. What does `db summarize` do?
6. What is the difference between the Data Editor's **Edit** and **Browse** modes, and which should you use while exploring?

<details><summary>Answers</summary>

1. History, Results, Command, Variables, Properties. The Results window has no name in its title bar.
2. OK runs the command and closes the dialog; Submit runs it and leaves the dialog open.
3. No. The drop only affects the data in memory. The file on disk changes only if you save over it.
4. The lock prevents accidental changes. Once unlocked, each change creates a command that shows up in the Results window, Command window and any log, so it is reproducible.
5. It opens the dialog for the `summarize` command.
6. Edit lets you change values; Browse is view-only. Use Browse while exploring.

</details>

---

*Adapted and summarised for learners from the interface chapter of the Stata Getting Started manual (StataCorp LLC). Stata is a registered trademark of StataCorp LLC.*

**Next:** return to the [Lesson 1 exercises](README.md).
