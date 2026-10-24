# Learning Notes: The Stata Viewer

**Part of:** Lesson 1, Getting Started  |  **Read and practise:** about 60 minutes  |  **Dataset:** `auto` (built into Stata) and `data/viewer_demo.smcl` (in this repo)

The Viewer is the window you meet every time you type `help`, `search` or `findit`, yet most beginners never learn to use it well. It is also where you read log files, open text files, and manage add-on commands. A confident Viewer user finds answers faster, keeps reference material on screen while working, and can review earlier output without scrolling through the Results window.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC): chapter 3 (Using the Viewer), plus the passages on logs in chapter 16 and on preferences in chapter 17. The [R] `view` reference entry on stata.com was used to check the `view` commands. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Explain what the Viewer is for and open one in several ways
- Use its toolbar, command box, search box and Find bar
- Work with links, tabs and split tab groups
- View log files, SMCL files, text files and remote text files
- Print and export Viewer content
- Use the Viewer's own commands, including `view`, `ado` and `net`
- Read and write a small SMCL file with clickable links
- Customise the Viewer and troubleshoot common problems

## Contents
1. [What the Viewer is, and why it matters](#1-what-the-viewer-is-and-why-it-matters)
2. [Opening a Viewer](#2-opening-a-viewer)
3. [Anatomy of the Viewer window](#3-anatomy-of-the-viewer-window)
4. [Links: how the Viewer behaves like a web browser](#4-links-how-the-viewer-behaves-like-a-web-browser)
5. [The Find bar](#5-the-find-bar)
6. [Tabs and tab groups](#6-tabs-and-tab-groups)
7. [Using the Viewer for help and search](#7-using-the-viewer-for-help-and-search)
8. [Viewing log files, SMCL files and text files](#8-viewing-log-files-smcl-files-and-text-files)
9. [Viewing files over the internet](#9-viewing-files-over-the-internet)
10. [Managing community-contributed commands](#10-managing-community-contributed-commands)
11. [Printing and saving Viewer content](#11-printing-and-saving-viewer-content)
12. [A short introduction to SMCL](#12-a-short-introduction-to-smcl)
13. [Preferences, fonts and colours](#13-preferences-fonts-and-colours)
14. [Viewer or Results window? Choosing the right place](#14-viewer-or-results-window-choosing-the-right-place)
15. [Troubleshooting](#15-troubleshooting)
16. [Practice exercises V1 to V12](#16-practice-exercises-v1-to-v12)
17. [Quick reference card](#17-quick-reference-card)
18. [Facilitator notes](#18-facilitator-notes)

---

## 1. What the Viewer is, and why it matters

The Viewer is a separate window that works much like a small web browser. The manual describes it as the first place to turn for help within Stata, but it does much more:

| Use | Example |
|-----|---------|
| **Reading help** | `help summarize` opens the help file in a Viewer |
| **Showing search results** | `search regression` lists commands, FAQs, articles and add-ons |
| **Reading log files** | Review the output of this or a previous session |
| **Reading any SMCL or plain-text file** | Output files, readme files, `.sthlp` help files |
| **Installing and managing add-on commands** | Browse, install, review and uninstall community-contributed commands |
| **Following links** | Open a web page in your browser |

Why professionals should care:
- **It stays still.** Output in the Results window scrolls away as you work. A Viewer holds a fixed page, so you can read a help file while you type commands.
- **It is searchable.** The Find bar locates any word on the page.
- **It is interactive.** Links run commands, open help files, or install software with a click.
- **It supports reproducible work.** Logs are best read in the Viewer.

## 2. Opening a Viewer

There are several ways to open one.

| Method | How |
|--------|-----|
| Toolbar | Click the **Viewer** button on the main toolbar. Click the small **arrow** beside it to choose among open Viewers and bring one to the front |
| Menu | **Window > Viewer > New Viewer** |
| Commands | Any `help`, `search`, `findit` or `view` command opens one automatically |
| Help menu | **Help > Search...**, **Help > Stata command...** |
| File menu | **File > Log > View...** (for log files) |

To **bring a Viewer to the front**, use **Window > Viewer** and pick it from the list, or use the arrow beside the toolbar button. **Window > Viewer > Close all Viewers** closes every Viewer window and tab.

Typing a `help` command from the Command window opens a new Viewer showing the requested help.

## 3. Anatomy of the Viewer window

```
┌────────────────────────────────────────────────────────────┐
│ [◀ Back] [▶ Forward] [⟳ Reload] [🖨 Print] [Find] [🔍 ▾]    │ ← toolbar
│ Command box: ___________________________   Search: ______  │
├────────────────────────────────────────────────────────────┤
│ [ tab 1 ] [ tab 2 ] [ + ]                                   │ ← tabs
├────────────────────────────────────────────────────────────┤
│                                                            │
│   Page content (help file, log, search results ...)        │
│   with blue links                                          │
│                                                            │
├────────────────────────────────────────────────────────────┤
│ Find bar (appears only when opened)                         │
│ Status bar: shows the action behind the link under mouse    │
└────────────────────────────────────────────────────────────┘
```

### Toolbar buttons
| Button | What it does |
|--------|--------------|
| **Back** | Goes back one step in your viewing trail |
| **Forward** | Goes forward one step, after you have gone back |
| **Reload page** | Refreshes the page, in case what you are viewing has changed (for example, a log file that is still growing) |
| **Print** | Prints the Viewer contents |
| **Find text in page** | Opens the Find bar at the bottom |
| **Search (magnifying glass)** | Chooses the scope of help searches |

### The command box
Everything you can do by clicking in the Viewer you can also do by typing in the command box at the top, or in the main Command window. Typical entries are `contents`, a command name, a search keyword, or `view` followed by a file name.

### The search box
Click the magnifying glass, choose a scope, type a word or phrase and press Enter. The three scopes are:

| Scope | Looks in |
|-------|----------|
| **Search all** | Official documentation, FAQs, Stata Journal articles, videos, selected external sites, and add-ons |
| **Search documentation and FAQs** | Official Stata commands, Journal articles and software, FAQs and videos |
| **Search net resources** | Community-contributed commands, whether from the Stata Journal or elsewhere |

### The status bar
Hover over any link and the status bar at the bottom of the Viewer shows the action attached to it, for example `help logistic`. **Read this before clicking** when the link is an installation link.

## 4. Links: how the Viewer behaves like a web browser

Links appear in blue by default. What happens depends on how you click:

| Click | Result |
|-------|--------|
| **Click** | Opens the link in the current tab |
| **Middle-click** (or **Ctrl+click** if you have no three-button mouse) | Opens the link in a **new tab** in the same Viewer window |
| **Shift+click** | Opens the link in a **new Viewer window** |

A link can do different things: show another help file, run a search, open a dialog box, run a command in the main window, install software, or open your web browser. The viewing trail built as you click is what **Back** and **Forward** navigate.

Practical tip: when reading a help file, Ctrl+click the interesting links rather than clicking them. You keep your place and can compare pages in tabs.

## 5. The Find bar

Long help files are easier to read if you jump to the part you need.

1. Click **Find text in page** to reveal the Find bar at the bottom.
2. Type the text in the **Find** field.
3. Use **Next** and **Previous** to move between matches. Both wrap around the document, so you never hit a dead end.
4. **Highlight all** (on by default) marks every match in yellow; if off, only the current match is highlighted in black.
5. **Match case** (off by default) makes the search case-sensitive: searching for `This` would not find `this`.
6. **Close** hides the bar.

Useful searches inside a help file: `Options`, `Example`, `Stored results`, `Also see`. In a long log: `r(`, `error`, or a variable name.

## 6. Tabs and tab groups

A single Viewer window can hold several tabs, each showing a different file or a different place in the same file.

- **New tab:** click the **Open new tab** button, or Ctrl/middle-click a link.
- **Reorder tabs:** drag them along the tab bar.
- **Split the window:** drag a tab and drop it inside the body of the same window. A menu appears:
  - **New Horizontal Tab Group** splits the window top and bottom, useful for two views of the same file at different places (the syntax at the top, an example at the bottom).
  - **New Vertical Tab Group** splits side by side, useful for **comparing two similar files**, such as two logs from different runs.
- If you drop a tab inside an existing group you can create a similar new group or move the tab to the selected group.

Plan your screen: a common arrangement is the Viewer on one side with the help file for the command you are using, and the Do-file Editor on the other.

## 7. Using the Viewer for help and search

The detailed treatment is in the [help and search guide](help-and-search-guide.md). The Viewer-specific points are:

| Task | In the Viewer | From the Command window |
|------|---------------|-------------------------|
| Help for a command | Type the command name in the command box | `help summarize` |
| Search a topic | Magnifying glass, choose scope, type topic | `search regression` |
| Search documentation and FAQs only | Scope: Search documentation and FAQs | `search regression, local` |
| Search net resources only | Scope: Search net resources | `search regression, net` |
| Help contents | Type `contents` | `help contents` |

According to the manual, `search topic, local` and `search topic, net` display their results in the **Results window** rather than a Viewer, while plain `search topic` opens a Viewer.

Typical workflow with the Viewer:
1. Search for a topic.
2. Click a command name to open its help file.
3. Use the **Also see** menu or the **Back** button to move around.
4. Use the **Dialog** link in the help file to open the command's dialog, or type the command in the Command window.
5. For more depth, follow the link to the PDF documentation.

## 8. Viewing log files, SMCL files and text files

### 8.1 Viewing a log
A **log file** is a record of your commands and results. By default, Stata logs in a format called SMCL (extension `.smcl`). Plain-text logs have the extension `.log`.

- To **view a log**: **File > Log > View...** and select the file.
- To **view the log currently being written**: **File > Log > View...** shows the current log's path already filled in. Click OK.

Two important points from the manual:
- The Viewer shows a **snapshot** of the log. It will not scroll as you continue to work. This is an advantage over the Results window because **what you are reading stays fixed**.
- To see newer output, click **Reload page**.

You can copy text from a log in the Viewer and paste it into a word processor or the Command window. If you paste into the Command window or a do-file, **copy only the commands, not the output**. The leading prompt (`.`) is ignored by the Command window, so you may include it.

### 8.2 Viewing other files
Use **File > Open...** (the exact menu wording differs between versions) or type:

```stata
view mylog.smcl          // SMCL file
view notes.txt           // plain text file
view mylog.log           // text log
view "path/with spaces/file.smcl"
```

The `view` command displays `.smcl` and `.sthlp` files as SMCL by default. Add the option `asis` to display any file as plain text, whatever its extension:

```stata
view script.do, asis
```

### 8.3 `view` versus `type`
Both show text files, in different places.

| Command | Shows the file in |
|---------|-------------------|
| `view file` | The **Viewer** (formatted, searchable, with working links) |
| `type file` | The **Results window** (as plain text; SMCL codes may appear for SMCL files) |

Use `view` for logs and help files and `type` when you want the text inside the Results window.

## 9. Viewing files over the internet

You can look at a remote file by typing its URL in place of a local path:

```stata
view https://www.stata.com/man/readme.smcl
```

The manual gives a warning: use this **only for text or SMCL files**. If you enter the address of an ordinary web page, you will see the page's **HTML source**, not the page as a browser would show it.

To open a normal web page in your web browser from Stata, use:

```stata
view browse https://www.stata.com
```

> The manual's command list refers to this as `browse URL`; the full form documented in the `view` reference entry is `view browse URL`. Use the full form.

## 10. Managing community-contributed commands

The Viewer is also Stata's built-in "app store" for add-ons (user-written commands). The manual lists these Viewer tasks:

| Task | Command |
|------|---------|
| Browse the Stata Journal and community-contributed commands | `net from https://www.stata.com` |
| Review installed community-contributed packages | `ado` |
| Uninstall a package | `ado uninstall` |

The `view` family displays the output of these commands in the Viewer:

| Command | Purpose |
|---------|---------|
| `view net` | Runs `net` commands and shows the output in the Viewer |
| `view ado` | Runs `ado` commands (such as the list of installed files) and shows the output in the Viewer |
| `view update` | Runs `update` commands in the Viewer; `view update query` skips the first step and shows the comparison directly |
| `view help topic` / `view search keywords` | Help and search results in the Viewer |

**Safety habits for installing add-ons**
1. Read the package description page in the Viewer first.
2. Hover over the install link and check the status bar.
3. Prefer well-known sources (Stata Journal, SSC) and check the author.
4. Record what you installed in your master do-file as a comment, so colleagues can install the same commands.
5. Use `ado` regularly to review what is installed.

Full details of installing add-ons belong in the chapter on updating and extending Stata (chapter 19 of the manual), planned for a later lesson.

## 11. Printing and saving Viewer content

### Printing
Any of these prints the Viewer contents:
- Click the **Print** button on the Viewer toolbar
- Right-click in the Viewer and select **Print...**
- **File > Print > [name of the Viewer]**

For SMCL logs, the manual notes that a print settings dialog follows, where you can fill in optional **Header**, **Name** and **Project** items, choose whether to print line numbers, a header and a logo, and set fonts, margins and the colour scheme (monochrome, colour, or custom). Printed logs look best in a fixed-width ("typewriter") font such as Courier.

### Making a PDF or other copy of a log
The manual points to the `translate` command to convert a SMCL log into another format such as PostScript or PDF. Check its options with `help translate`.

```stata
translate mylog.smcl mylog.pdf, replace
```
Test this on your own system, because available output formats depend on your Stata version and platform.

### Plain-text logs
If you choose a plain-text `.log`, you can open it in any text editor or word processor, edit it, add headings and comments, and print it. Use a fixed-width font so columns line up.

### Copying
Select text, then copy and paste into a document. Pasted text is unformatted, so use a fixed-width font such as Courier for tables.

## 12. A short introduction to SMCL

**SMCL** (Stata Markup and Control Language) is the formatting language behind the Viewer. Help files and log files are SMCL. You rarely write it, but recognising it explains what you see in the Viewer and why raw SMCL looks strange in a text editor.

SMCL codes are written in curly braces. A few basic ones you can try (the commands are listed in `help smcl`):

| Code | Effect |
|------|--------|
| `{smcl}` | First line of a SMCL file; tells Stata to interpret it |
| `{title:Some title}` | A heading |
| `{hline}` | A horizontal line |
| `{bf:text}` | **Bold** |
| `{it:text}` | *Italic* |
| `{help summarize}` | A clickable link to a help file |
| `{help summarize:click here}` | A link whose displayed text differs |
| `{stata "sysuse auto, clear":Load auto data}` | A link that runs a command when clicked |
| `{browse "https://www.stata.com":Stata website}` | A link that opens your web browser |

The repo file [`data/viewer_demo.smcl`](../../data/viewer_demo.smcl) contains a small example. Open it with:

```stata
view "data/viewer_demo.smcl"
```
Then use the file in exercises V8 to V10. For more on the language, type `help smcl`.

> Be careful with `{stata ...}` links in files from people you do not know. A click runs a command on your computer. Read the status bar before clicking, as with any link.

## 13. Preferences, fonts and colours

Right-click anywhere in a Viewer for the contextual menu:

| Item | Use |
|------|-----|
| **Select all** | Select all text, ready to copy |
| **Preferences...** | Edit the Viewer's preferences |
| **Font...** | Change the font |
| **Print...** | Print |

(Some contexts add more items.)

- The Results window and the Viewer each have a **colour scheme** controlling the display of input, text, results, errors, links and highlighted text. The default is the built-in **Standard** scheme (white background, dark text). There are other built-in schemes and slots for custom schemes.
- The Viewer's settings affect **all Viewer windows at once**. Choosing an overall scheme from the General tab of the preferences resets custom settings to that scheme.
- Preferences are saved when Stata closes and reloaded on start-up. You can store several named **preference sets** under **Edit > Preferences** (for example a larger-font set for presentations) and load them later.

**Training-room tip:** before presenting, increase the Viewer font and choose a high-contrast scheme so the back row can read the screen.

## 14. Viewer or Results window? Choosing the right place

| Question | Viewer | Results window |
|----------|--------|----------------|
| Does it scroll when new output arrives? | No, fixed snapshot | Yes |
| Can I use links? | Yes | Only some |
| Can I find text easily? | Yes (Find bar) | Limited |
| Best for | Help, search, logs, reference text | Running commands and seeing live output |
| Can I keep it beside my work? | Yes, in tabs or separate windows | It is the main window |

A good habit is to keep **the Viewer for reading** and the **Results window for doing**.

## 15. Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| A help file did not open | Command name misspelled, or the command is not installed | Use `search` instead of `help`; check `ado` for add-ons |
| The Viewer is hidden behind other windows | Window not in front | **Window > Viewer** and pick it, or use the arrow beside the toolbar button |
| Log in the Viewer is out of date | It is a snapshot | Click **Reload page** |
| A web address shows strange code | The Viewer shows HTML source for ordinary web pages | Use `view browse URL` instead |
| `file ... not found` **r(601)** when using `view` | Wrong working directory or path | `pwd`, `dir`; see the [working directory guide](working-directory-guide.md) |
| Too many Viewer windows | Each help command opened a new one | Use tabs (Ctrl+click) or **Window > Viewer > Close all Viewers** |
| Text too small to read | Default font | Right-click > **Font...**, or load a presentation preference set |
| A SMCL file looks like code in a text editor | SMCL is markup | Open it with `view` |
| SMCL log cannot be edited easily | It is formatted | Log as plain text (`log using name, text`) or use `translate` |

## 16. Practice exercises V1 to V12

Create a do-file named `V-practice.do` for the command-based parts. Solutions are in `exercise-solutions/lesson-01/viewer-practice.do`. Try each one first.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**V1 🟢 Open three ways.** Open a Viewer using (a) the toolbar button, (b) the menu **Window > Viewer > New Viewer**, (c) the command `help summarize`. How many Viewer windows do you now have? How do you bring a particular one to the front?

**V2 🟢 Tour the toolbar.** In a Viewer showing `help summarize`, hover over each toolbar button and read its tooltip. Click a link, then use **Back** and **Forward**. Write down what each does in one line.

**V3 🟢 Find in page.** In the `summarize` help file, use the Find bar to locate the word `detail`. Count the matches by pressing **Next**. Switch **Match case** on and repeat. Does the count change? Turn **Highlight all** off and see the difference.

**V4 🟢 Three kinds of click.** In the `summarize` help file, find a link to another command. Open it by a plain click, then again with Ctrl+click (or middle-click), then with Shift+click. Describe the three results.

**V5 🟡 Compare in tabs.** Open help for `summarize` and `tabstat` in separate tabs. Drag one tab into the body of the window and create a **New Vertical Tab Group** so both appear side by side. Which options does `tabstat` offer that `summarize` does not?

**V6 🟡 Scope of search.** Search for `missing values` using each of the three scopes in the search box. Then run `search missing values, local` and `search missing values, net` from the Command window. Where does each result appear (Viewer or Results window)?

**V7 🟡 Live log.** Start a log with `log using viewer_test, replace`. Run `sysuse auto, clear` and `summarize price`. Open **File > Log > View...** and click OK. Run `summarize mpg`. Does the new output appear in the Viewer? What must you click to see it? Close the log with `log close`.

**V8 🟡 Open a SMCL file.** Open `data/viewer_demo.smcl` in the Viewer (using `view`). Click the **Load auto data** link and then the `summarize` link. What happens in the main window? Why should you check the status bar before clicking such links?

**V9 🟡 View versus type.** Run `view data/viewer_demo.smcl` and then `type data/viewer_demo.smcl`. Compare. When would you choose each?

**V10 🟡 Plain text.** Run `view data/README.md, asis`. Why is `asis` needed? Try without it.

**V11 🔴 Installed commands.** Run `ado` to list the community-contributed packages installed on your machine. Pick one and view its description. How would you uninstall a package you no longer need? (Do not uninstall anything today.)

**V12 🔴 Review a log.** Using a log from an earlier lesson, open it in the Viewer, use Find to locate the first error (search for `r(`), and write a one-sentence diagnosis. Then use `translate` to produce a PDF copy if your installation supports it.

## 17. Quick reference card

| Task | How |
|------|-----|
| Open a Viewer | Toolbar **Viewer** button or **Window > Viewer > New Viewer** |
| Bring a Viewer to front | **Window > Viewer** list, or the arrow beside the toolbar button |
| Close all Viewers | **Window > Viewer > Close all Viewers** |
| Open link in new tab | Ctrl+click or middle-click |
| Open link in new window | Shift+click |
| Search inside a page | **Find text in page** (Find bar) |
| Scroll | Up/Down arrows (line), Page Up/Page Down (screen) |
| Refresh | **Reload page** |
| Help for a command | `help command` |
| Search a topic | `search topic` |
| View a file | `view file.smcl`, `view file.txt`, `view file.log` |
| View any file as plain text | `view file, asis` |
| Show a file in Results | `type file` |
| Open a web page in your browser | `view browse URL` |
| List installed add-ons | `ado` |
| Uninstall an add-on | `ado uninstall` |
| Print | Toolbar Print, right-click > **Print...**, or **File > Print** |
| Change font/colours | Right-click > **Font...** / **Preferences...** |

## 18. Facilitator notes

**Timing (60-minute session):** 10 min concepts (sections 1 to 3), 10 min links, Find bar and tabs (4 to 6) with live demo, 10 min logs and files (8 and 9), 25 min exercises V1 to V9, 5 min wrap-up. V10 to V12 are take-home.

**Common stumbling blocks**
- Participants open a new Viewer for every help command and end up with a cluttered screen. Teach Ctrl+click and tabs early.
- Participants expect the log in the Viewer to update live. Demonstrate V7 once, then ask them what the **Reload** button is for.
- Reading a web page in the Viewer and seeing HTML. Demonstrate `view browse`.
- `view` versus `type`: show both on the same file.

**Teaching tips**
- Project the Viewer with a larger font; use a presentation preference set.
- Pair up for V5: one participant predicts which options differ, the other checks.
- Set a 3-minute challenge: "Find, using only the Viewer, how to display only the 10 largest values of a variable." (Possible routes: search `list`, `gsort`, or `sort`; there is more than one answer.)

**Assessment prompt (5 minutes):** "A colleague says: 'I ran my analysis yesterday but the Results window only shows today's output. Where can I read yesterday's results, and how do I get a copy I can edit?'" Expected: open yesterday's log in the Viewer (File > Log > View, or `view`), copy the text, or use a plain-text log in future.

**Note on versions.** This guide follows the Windows edition of the Getting Started manual. Menu wording and some Viewer features differ across Stata versions and between Windows, macOS and Linux; the commands work in all of them. Always check `help view` and `help smcl` in your own version.
