# Learning Notes: Setting Font and Window Preferences

**Part of:** Lesson 1, Getting Started  |  **Read and practise:** about 45 minutes  |  **Dataset:** `auto` (built into Stata)

Professionals spend hours a day looking at Stata. The right font size, a readable colour scheme and a saved window layout make that time faster and kinder to your eyes. Preferences also decide how your **graphs** look by default, which matters when you submit work to a journal or a donor. This guide covers every part of the manual's preferences chapter and adds practical advice for training rooms and shared computers.

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC), chapter 17 ("Setting font and window preferences"). Graph scheme information was checked against the `set scheme` and "Schemes intro" entries of the Stata graphics manual on stata.com. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Change the font and font size of Stata's windows, and explain why some windows allow only fixed-width fonts
- Change colour schemes for the Results window, Viewer and Do-file Editor
- Set graph preferences, including the graph scheme, printing and clipboard options
- Use `set scheme` for one graph, a session, or permanently
- Save, load, overwrite and delete preference sets
- Prepare Stata for a projector, a small laptop, or a shared training PC
- Close and reopen windows and recover from preference problems

## Contents
1. [What "preferences" are](#1-what-preferences-are)
2. [Where preferences live: a map](#2-where-preferences-live-a-map)
3. [Fonts](#3-fonts)
4. [Colour schemes](#4-colour-schemes)
5. [Graph window preferences](#5-graph-window-preferences)
6. [Graph schemes in depth](#6-graph-schemes-in-depth)
7. [Managing multiple sets of preferences](#7-managing-multiple-sets-of-preferences)
8. [Closing and opening windows](#8-closing-and-opening-windows)
9. [Recipes for common situations](#9-recipes-for-common-situations)
10. [Preferences and reproducibility](#10-preferences-and-reproducibility)
11. [Troubleshooting](#11-troubleshooting)
12. [Practice exercises P1 to P12](#12-practice-exercises-p1-to-p12)
13. [Quick reference card](#13-quick-reference-card)
14. [Facilitator notes](#14-facilitator-notes)

---

## 1. What "preferences" are

**Preferences** are the settings that control how Stata *looks and behaves on your screen*: fonts, sizes, colours, window positions, and the default look of graphs. The manual explains the two reasons to change them:

1. **Your screen and your eyes.** Monitor resolution and personal taste differ.
2. **Output requirements.** For example, you may have requirements for fonts or styles when submitting graphs to journals.

Stata handles both by letting you work with **sets of preferences**. By default your preferences are **saved automatically when you exit Stata and reloaded when you start it**.

Preferences affect **appearance only**. They do not change your data, your commands or your numerical results.

## 2. Where preferences live: a map

| What you want to change | Where to do it |
|-------------------------|----------------|
| Font and size of a window | Right-click the window > **Font...** |
| Colours of Results window or Viewer | Right-click the window > pick or design a colour scheme (or **Preferences...**) |
| Syntax-highlighting colours in the Do-file Editor | Do-file Editor preferences |
| Overall colour scheme | **Edit > Preferences > General Preferences...**, **General** tab |
| Graph appearance, printing and clipboard | Right-click the Graph window > **Preferences...** (tabs: Graph, Printer, Clipboard) |
| Save/load/delete a whole set of settings | **Edit > Preferences** (load, save, delete preference set) |
| Reopen a closed window | **Window** menu |

Menu wording varies slightly between versions and operating systems. On a Mac, the Preferences menu is under the Stata menu.

## 3. Fonts

### 3.1 How to change a font
1. **Right-click** inside the window.
2. Choose **Font...**.
3. In the **Font dialog**, pick a font and size, then confirm.

The manual says you can change the font and font size for most types of windows.

### 3.2 Fixed-width fonts only in three windows
The font lists for the **Results**, **Viewer** and **Do-file Editor** windows are restricted to **fixed-width** fonts only. This restriction ensures output and numbers line up properly and are readable. The other windows (such as History, Variables, Properties) can use any font without adverse consequences.

Why it matters: Stata's tables are built with spaces. In a **fixed-width** (monospaced) font every character takes the same width, so columns align:

```
    Variable |        Obs        Mean    Std. dev.
-------------+---------------------------------
       price |         74    6165.257    2949.496
```

In a proportional font (like Times New Roman) the same table becomes ragged. This is also why log files should be printed in a fixed-width font such as Courier.

### 3.3 Choosing sizes
| Situation | Suggested approach |
|-----------|--------------------|
| Laptop in an office | Medium size; keep many lines visible |
| Training room with a projector | Large Results, Command and Do-file Editor fonts; test from the back row |
| Long sessions | A comfortable size and a clear fixed-width font reduce eye strain |
| Very small screens | Reduce History and Variables fonts first; keep Results readable |

**Tip:** change the font size in the **Do-file Editor** and **Results** windows together so that code and output feel consistent.

## 4. Colour schemes

### 4.1 Three places colours are set
| Window | What the colours control |
|--------|--------------------------|
| **Results** | Input (the commands you type), text, results, errors, links, highlighted text |
| **Viewer** | The same categories, for help files, logs and search results |
| **Do-file Editor** | **Syntax highlighting**, so that Stata commands display differently from arbitrary text |

### 4.2 Results and Viewer
Right-click the window and select a built-in scheme or design your own. The default for both is the built-in **Standard** scheme: **white background, dark text**. There are other built-in schemes and **slots for custom schemes**.

Two rules from the manual to remember:
- The **Viewer's settings affect all Viewer windows at once.**
- Choosing an **overall scheme** from the **General** tab of the General preferences **resets all custom settings** to the settings determined by that scheme. If you have carefully designed a custom scheme, apply an overall scheme *before* customising, not after.

### 4.3 Do-file Editor syntax highlighting
In the Do-file Editor you can choose the colours for syntax highlighting. Colours make code easier to read: commands, comments and strings can each have their own colour, and mistakes such as an unclosed quotation mark stand out.

### 4.4 Choosing colours well
- Use **high contrast** between text and background. Dark text on a white background is the default for a reason.
- Avoid relying on **red versus green** alone to mark errors and results: many people cannot tell them apart. Prefer also changing brightness or boldness.
- For projectors, **light backgrounds usually project better** in bright rooms; a dark scheme can suit dim rooms. Test before the session.
- Keep one scheme across Results, Viewer and Do-file Editor so you are not constantly readjusting.

## 5. Graph window preferences

Right-click the **Graph window** and choose **Preferences...**. You will find tabs for:

| Tab | What it controls |
|-----|------------------|
| **Graph** | The **scheme** used for displaying graphs |
| **Printer** | The settings to use when printing graphs |
| **Clipboard** | How graphs behave when copied to the clipboard (for pasting into Word or PowerPoint) |

### 5.1 What a scheme does
Graph **schemes** control the look of graphs. They provide a quick way to optimise graphs for printing or to display on a screen. There are schemes defined for *The Economist* and the *Stata Journal*, so you can get the details for these publications right without much fuss.

### 5.2 Important: schemes apply to future graphs
**Changing the scheme does not change the current graph; it applies the settings to future graphs.** To see a graph in a new scheme, draw it again.

```stata
sysuse auto, clear
scatter price mpg                      // drawn with the current scheme
```
Change the scheme in Preferences, then rerun the command to see the difference.

## 6. Graph schemes in depth

### 6.1 Command-line control
The same choice can be made in code, which is better for reproducibility.

| Goal | Command |
|------|---------|
| Use a scheme for **one graph** only | Add `scheme(name)` to the graph command, for example `scatter price mpg, scheme(economist)` |
| Use a scheme for the **current session** | `set scheme name` |
| Use a scheme **permanently** | `set scheme name, permanently` |
| Restore the factory default | `set scheme default, permanently` |
| Show current graphics settings | `query graphics` |
| List schemes installed | `graph query, schemes` |
| Draw a saved graph with another scheme | `graph use filename, scheme(name)` |

Graphs saved to a file **keep the scheme they were drawn with**.

### 6.2 Built-in schemes
Stata's graphics documentation lists many schemes. The main ones for this course:

| Scheme | Colour | Background | Typical use |
|--------|--------|------------|-------------|
| `stcolor` | Colour | White | Factory default (in recent versions) |
| `s2color` | Colour | White | Factory default before Stata 18 |
| `s2mono` | Monochrome | White | Monochrome version of `s2color`, for black-and-white print |
| `s1color` | Colour | White | Plain look |
| `s1mono` | Monochrome | White | Plain monochrome look |
| `s1rcolor` | Colour | Black | Plain look on a black background |
| `economist` | Colour | White | Resembles graphs in *The Economist* |
| `sj` | Monochrome | White | Earlier official *Stata Journal* style |
| `stsj` | Monochrome | White | Current official *Stata Journal* scheme |
| `stmono1`, `stmono2` | Monochrome | White | Monochrome variants of the default |

Version notes: the default scheme before Stata 18 was `s2color`; check `help scheme` and `graph query, schemes` in your own version to see what is installed. Other schemes can be installed from the community.

### 6.3 Which scheme should I use?
| Purpose | Suggestion |
|---------|------------|
| Reading on screen while exploring | Default colour scheme |
| Journal manuscript | The journal's own instructions first; a monochrome scheme such as `stsj` or `s2mono` if black-and-white figures are required |
| Printed report in greyscale | A monochrome scheme, so that lines remain distinguishable |
| Slides | A colour scheme with large text; test the colours on a projector |
| Black-background slides | `s1rcolor`, only if your room and template suit it |
| Team reports | **Agree one scheme** and set it at the top of the master do-file |

### 6.4 Where to put the scheme in your workflow
For consistent figures across a project, set the scheme in code (the master do-file header from the [working directory guide](working-directory-guide.md)):

```stata
set scheme s2mono            // for this session
```
This documents the choice, whereas a scheme chosen only through the menu is invisible to colleagues.

## 7. Managing multiple sets of preferences

Stata's preferences are saved when you exit and reloaded at launch. Sometimes you want to rearrange the windows and then **revert to your preferred arrangement**. You do this with named **preference sets**.

### 7.1 Menu operations (Edit > Preferences)
| Operation | Menu path | Effect |
|-----------|-----------|--------|
| **Load** | **Load preference set** and choose a set | Applies the set. Several sets come installed with Stata, some meant for small screens and others for presentations. They are worth a look |
| **Save as new** | **Save preference set > New preference set...** | Enter a name, click OK |
| **Overwrite** | **Save preference set** and choose an existing set | Replaces that set with your current preferences |
| **Delete** | **Delete preference set** and choose a set | Click OK to confirm |

**Key rule:** any changes you make to preferences *after* loading a set **do not affect the set**. The set stays untouched unless you deliberately overwrite it.

### 7.2 Command equivalents
```stata
window manage prefs save "teaching"      // save the current preferences under a name
window manage prefs load "teaching"      // load a saved set
window manage prefs default              // return to the factory appearance
```
The command reference says `window manage prefs default` is equivalent to loading the **Widescreen layout (default)** set.

### 7.3 Naming and organising sets
- Name sets by purpose: `office_dual_screen`, `laptop_small`, `projector_large`, `evening_dark`.
- Keep a set named `my_default` that you update only on purpose.
- Before experimenting, save the current state under a temporary name.
- Preference sets are stored on the computer for your user account. On Windows they are kept in the registry, and Stata offers no simple way to export one to a file, so do not expect to email a layout to a colleague. Rebuild it from a written description instead.

## 8. Closing and opening windows

You can close all windows **except the Results and Command windows**. To reopen a closed window, use the **Window** menu and select the one you want.

See the [docking windows guide](docking-windows-guide.md) for arranging windows and `window manage forward` for bringing windows to the front.

## 9. Recipes for common situations

### Recipe A: Projector for a class
1. Save your current preferences: `window manage prefs save "my_default"`.
2. Load an installed presentation set (**Edit > Preferences > Load preference set**).
3. Increase fonts: right-click Results, Command and Do-file Editor > **Font...**
4. Use `set scheme` with a high-contrast graph scheme.
5. Auto-hide History and Properties.
6. After class: `window manage prefs load "my_default"`.

### Recipe B: Small laptop
1. Load an installed small-screen set.
2. Reduce side-window fonts first.
3. Auto-hide docking windows you use rarely.
4. Save as `laptop_small`.

### Recipe C: Journal-ready figures
1. Read the journal's figure instructions (fonts, colour, width).
2. Choose a scheme that matches (for example a monochrome one for black-and-white print).
3. Put `set scheme ...` in the do-file that makes the figures.
4. Export with a command (`graph export`), not by screenshot.

### Recipe D: Shared training PC
1. At the start, save the machine's current set as `before_class`.
2. Make your changes.
3. At the end, `window manage prefs load "before_class"` so the next user finds it as they left it.

### Recipe E: Something went wrong
1. `window manage prefs default`
2. Reload your saved set if you have one.
3. Rebuild step by step.

## 10. Preferences and reproducibility

| Item | Does it affect results? | What to do |
|------|------------------------|------------|
| Window fonts, sizes, colours | No | Personal choice |
| Window layout | No | Personal choice |
| **Graph scheme** | **Affects the look of every graph** | Set it in code so everyone gets the same figures |
| Printer and clipboard graph settings | Affect printed/pasted graphs | Prefer `graph export` in code |

Rule of thumb: **if it affects an output you share, put it in a do-file; if it only affects your comfort, keep it in preferences.**

## 11. Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Cannot choose a proportional font for Results | Results, Viewer and Do-file Editor allow only fixed-width fonts | Pick a fixed-width font (so columns align) |
| Custom colours vanished | An overall scheme was chosen on the General tab, which resets custom settings | Reapply your custom colours afterwards |
| Graph did not change after changing scheme | Schemes apply to future graphs | Run the graph command again |
| Colleague's graphs look different | Different default scheme or version | Set `set scheme` in the shared do-file |
| Graph shows a different scheme when reopened | Saved graphs keep the scheme they were drawn with | `graph use filename, scheme(name)` |
| Layout reverts after restart | Preferences are saved when Stata exits normally | Save a named preference set |
| Lost a window | Closed or auto-hidden | **Window** menu |
| Layout is a mess | Many experiments | `window manage prefs default` |
| Text too small to read on projector | Default font | Right-click > **Font...** or load a presentation set |
| Saved set not available on another PC | Sets are stored per computer/user | Recreate it there |

## 12. Practice exercises P1 to P12

Solutions for the command-based parts are in `exercise-solutions/lesson-01/preferences-practice.do`. Most exercises are point-and-click. Try each first.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**P1 🟢 Safety net.** Save your current preferences as a new preference set named `before_practice`.

**P2 🟢 Bigger text.** Increase the font size of the Results window. Then open the Variables window font dialog. What difference do you notice between the font lists?

**P3 🟢 Fixed-width test.** Run `sysuse auto, clear` and `summarize price mpg weight`. Compare the table with a different fixed-width font. Why is a proportional font not offered for Results?

**P4 🟢 Colour scheme.** Look at the colour schemes available for the Results window. Choose one, run `summarize`, then return to Standard. Which would be easiest to read on a projector? Why?

**P5 🟡 Viewer scope.** Change the Viewer's font size. Open two Viewers. Do both change?

**P6 🟡 Do-file Editor.** Open the Do-file Editor and type `sysuse auto, clear` and a comment starting with `*`. Change the syntax highlighting colour for comments.

**P7 🟡 Graph before and after.** Run `scatter price mpg`. Change the graph scheme in the Graph window's Preferences. Does the existing graph change? Run the command again.

**P8 🟡 One graph only.** Draw the same scatter plot with `scheme(economist)`, then with `scheme(s2mono)`. Does your default scheme change? Check with `query graphics`.

**P9 🟡 Presentation set.** Load one of the installed presentation preference sets. Describe three differences. Then reload `before_practice`.

**P10 🔴 Overwrite carefully.** Create a set `test_set`, change a font, then load `test_set` again. Is your font change kept? Then overwrite the set. What did you learn about the rule "changes after loading do not affect the set"?

**P11 🔴 Scheme in code.** Write a do-file header that sets a monochrome scheme and draws a histogram of `price` from `auto`. Export it as a PNG with a command. Why is this better than clicking Preferences?

**P12 🔴 Your own standard.** Write a half-page "team standard" listing the font size, graph scheme, and the preference sets your team will keep for training days and office work.

## 13. Quick reference card

| Task | How |
|------|-----|
| Change a window's font | Right-click > **Font...** |
| Fixed-width fonts only | Results, Viewer, Do-file Editor |
| Colour scheme (Results/Viewer) | Right-click > choose/design scheme; default is Standard |
| Overall scheme | **Edit > Preferences > General Preferences**, **General** tab (resets custom settings) |
| Do-file Editor colours | Syntax highlighting settings |
| Graph preferences | Right-click Graph window > **Preferences...** (Graph, Printer, Clipboard tabs) |
| Scheme for one graph | `..., scheme(name)` |
| Scheme for the session | `set scheme name` |
| Scheme permanently | `set scheme name, permanently` |
| Factory scheme | `set scheme default, permanently` |
| Show graphics settings | `query graphics` |
| List installed schemes | `graph query, schemes` |
| Save / load / delete a set | **Edit > Preferences** menus |
| Save / load by command | `window manage prefs save "name"` / `load "name"` |
| Factory window layout | `window manage prefs default` |
| Reopen a window | **Window** menu |

## 14. Facilitator notes

**Timing (45-minute session):** 10 min concepts (sections 1 to 3), 10 min colours and graph preferences (4 to 6), 10 min preference sets (7), 15 min exercises P1 to P9. P10 to P12 are take-home.

**Before the session**
- Everyone must complete **P1** before changing anything.
- On shared PCs, preferences may be saved per user or reset between sessions. Ask the IT contact how the training room is configured.
- Check the Stata version, because default schemes and installed preference sets differ between versions.

**Common stumbling blocks**
- Participants change a scheme and expect the open graph to change. Demonstrate redrawing.
- Participants choose an overall scheme after carefully customising colours, and lose them.
- Participants believe preference sets are shareable files. They are not.
- Disagreements over graph appearance within a team: settle with a written standard (P12).

**Teaching tips**
- Run a 5-minute "readability test": project the screen and have participants judge from the back of the room.
- Compare the same figure in three schemes and ask which is best for print, slides and screen.
- Link back to the [Viewer guide](viewer-guide.md) and [docking windows guide](docking-windows-guide.md): together they complete the workspace setup.

**Assessment prompt (5 minutes):** "You carefully customised Results window colours, then chose an overall colour scheme on the General tab and lost them. Why, and how do you avoid it?" Expected: choosing an overall scheme resets custom settings; apply the overall scheme first, then customise; save a preference set.

**Note on versions.** This guide follows the Windows edition of the Getting Started manual and the current Stata graphics documentation. Menu wording, built-in schemes and installed preference sets differ across versions and operating systems. Check `help scheme`, `help set scheme` and `help window manage` on your installation.
