## Menus and dialogs

You can tell Stata what to do with the **Command window** or with **menus and dialogs**. Each has strengths: dialogs help you discover options, commands are faster and can be saved.

**Where to find things**
- The **Data**, **Graphics** and **Statistics** menus give point-and-click access to almost every command.
- The **User** menu starts nearly empty; programmers can add their own items.
- *Example:* a Logistic regression is under **Statistics > Binary outcomes > Logistic regression**, or you can just type `logistic`.

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

# 2. The toolbar

The toolbar gives one-click access to the most-used features. Hover your mouse over a button for a moment to see a tooltip. Buttons with a small arrow open a menu when you click the arrow.

| Button | What it does |
|---|---|
| **Open** ✉️ | Opens a Stata dataset |
| **Save** | Saves the dataset in memory to disk |
| **Print** 🖨️ | Shows a list of windows; pick one to print |
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

