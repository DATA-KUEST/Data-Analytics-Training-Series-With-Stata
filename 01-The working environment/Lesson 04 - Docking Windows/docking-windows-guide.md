# Learning Notes: Docking Windows in Stata

**Part of:** Lesson 1, Getting Started  |  **Read and practise:** about 45 minutes  |  **Dataset:** `auto` (built into Stata)

A tidy workspace saves time and errors. In Stata you spend your day moving between the Command, Results, History, Variables and Properties windows, plus the Do-file Editor, Viewer and Graph windows. Knowing which of them can be docked, linked, tabbed or auto-hidden lets you build a layout that suits your screen, whether that is a laptop in a training room or a wide monitor in the office. This guide is the detailed companion to the short "Arranging your windows" section of the [Stata interface guide](stata-interface-guide.md).

> Adapted in part from the *Getting Started with Stata for Windows* manual (StataCorp LLC): chapter 2 ("Fine control of Stata's windows", "Window types", "Docking windows", "Auto Hide and pinning", "Nondocking windows") and chapter 17 (preferences). The command-line material was checked against the `window manage` reference entry on stata.com. The explanations, examples and exercises are our own. Stata is a registered trademark of StataCorp LLC.

## Learning objectives
By the end of this guide you will be able to:
- Tell docking windows from nondocking windows and name the windows in each group
- Move, resize, link and tab docking windows using the docking guides
- Use Auto Hide and the pushpin, and avoid its common pitfall
- Undock a window and recover a layout you have messed up
- Save, load and reset window layouts with preference sets
- Choose a sensible layout for different tasks (learning, analysing, presenting)
- Troubleshoot a missing or hidden window

## Contents
1. [Why layout matters](#1-why-layout-matters)
2. [Docking and nondocking windows](#2-docking-and-nondocking-windows)
3. [The default layout](#3-the-default-layout)
4. [Moving and resizing: the basics](#4-moving-and-resizing-the-basics)
5. [Docking guides: linking and tabbing](#5-docking-guides-linking-and-tabbing)
6. [Auto Hide and the pushpin](#6-auto-hide-and-the-pushpin)
7. [Nondocking windows](#7-nondocking-windows)
8. [Closing, reopening and bringing windows forward](#8-closing-reopening-and-bringing-windows-forward)
9. [Preference sets: save, load, reset](#9-preference-sets-save-load-reset)
10. [Fonts and colours](#10-fonts-and-colours)
11. [Suggested layouts](#11-suggested-layouts)
12. [Troubleshooting](#12-troubleshooting)
13. [Practice exercises D1 to D12](#13-practice-exercises-d1-to-d12)
14. [Quick reference card](#14-quick-reference-card)
15. [Facilitator notes](#15-facilitator-notes)

---

## 1. Why layout matters

- **Speed:** the History window lets you click to rerun a command; the Variables window pastes names into the Command window. If they are hidden, you type more and mistype more.
- **Screen space:** on a small laptop, every pane competes with the Results window. Auto Hide gives the space back.
- **Presentations:** a projected screen needs big fonts and fewer panes.
- **Comfort:** a layout that suits you reduces strain over a long session.

None of this changes your results. Layout is purely about how comfortable and efficient you are.

## 2. Docking and nondocking windows

The Stata for Windows interface has two types of windows, and the difference decides what you can do with each.

| | **Docking windows** | **Nondocking windows** |
|---|---|---|
| **Windows** | History, Command, Variables, Properties | Results, Graph, Data Editor, Do-file Editor, Viewers, dialogs |
| **Linked** to other windows with a divider (splitter) | Yes | No |
| **Tabbed** together in one window | Yes | No |
| **Auto-hide** when not in use | Yes | No |
| **Location** | Inside the main Stata window, or placed relative to it | Separate from the main window (Results excepted) |

The Results window is a special case. It is a nondocking window, but because it is Stata's primary window it **always stays inside the main Stata window** and fills whatever space the docked windows leave.

> **Memory aid:** the four docking windows are the *side panels* (History, Variables, Properties) plus the Command window. Everything else floats.

Docking windows share these three abilities. Section 5 explains linking and tabbing and section 6 explains Auto Hide.

## 3. The default layout

When Stata is first launched, the History, Results, Command, Variables and Properties windows appear in the main window. The History, Command, Variables and Properties windows are initially both docked and linked to one another and attached to the edges of the main window.

```
┌───────────────────────────────────────────────────────────────┐
│ Toolbar                                                        │
├────────────┬────────────────────────────────┬─────────────────┤
│ History    │                                │ Variables       │
│ (docked)   │        Results                 │ (docked)        │
│            │   (nondocking, always inside   ├─────────────────┤
│            │    the main window)            │ Properties      │
│            │                                │ (docked)        │
├────────────┴────────────────────────────────┴─────────────────┤
│ Command (docked)                                               │
├───────────────────────────────────────────────────────────────┤
│ Status bar: working directory                                  │
└───────────────────────────────────────────────────────────────┘
```

The exact arrangement depends on your version and screen. The manual describes this default as simple and familiar. If you are happy with it you can stop here; the rest of this guide is for when you want to customise.

## 4. Moving and resizing: the basics

1. **Resize** a docked window by dragging its edge or the splitter between linked windows. Making one bigger makes its neighbour smaller.
2. **Reposition** a docked window by dragging its **title bar**. Docking guides appear (section 5).
3. **Hide** it as a tab by clicking the **pushpin** (section 6).

Try these in the main window before reading on. The windows are forgiving, and you can always recover the default layout (section 9).

## 5. Docking guides: linking and tabbing

When you drag a docking window by its title bar over the main Stata window or over another docking window, **docking guides** appear: small markers around the target window and in its centre. Move the pointer over a guide **without releasing** and a preview shows where the window will go. Release the mouse button to drop it.

### 5.1 Linking (outer guides)
Dropping a window on one of the **outer** docking guides **links** it to the window under the guide. For example, dragging the History window over the Variables window and dropping it on the **bottom** guide places History in the lower part of the same space as Variables.

When windows are linked, a **splitter** (divider) appears between them. Drag the splitter to resize: increasing one window decreases the other.

*Use linking when you want to see two windows at once.*

### 5.2 Tabbing (centre guide)
Dropping a window on the **centre** guide **combines** it with the window under the guide. Stata creates one docking window with a **tab** for each docked window along the bottom. Click a tab to show that window.

*Use tabbing when you rarely need two windows at the same time and want to save space (for example Variables and Properties).*

### 5.3 Undocking a tabbed window
Click and drag the window's **tab** out of the docking window and drop it on a docking guide. The docking window containing tabbed windows can itself be linked to other docking windows, so you can build combinations such as "History and Variables tabbed together, linked above Command".

### 5.4 Linking versus tabbing at a glance

| | Linked | Tabbed |
|---|--------|--------|
| Drop on | An **outer** docking guide | The **centre** docking guide |
| What you see | Both windows at once, with a splitter | One window at a time, with tabs |
| Resize with | Splitter | The combined window's edges |
| Best when | You use both constantly | You use one often and the other occasionally |
| Undo | Drag the title bar elsewhere | Drag the tab out |

## 6. Auto Hide and the pushpin

Docking windows can hide themselves when you are not using them. Every docked window in the main Stata window has a **pushpin** in its title bar.

| Pushpin | Meaning |
|---------|---------|
| **Vertical** | Auto Hide **off**: the window stays visible |
| **Horizontal** | Auto Hide **on**: the window collapses into a **tab along an edge** of the main window |

**To show** an auto-hidden window, move the pointer over its edge tab. **To hide it again**, move the pointer away. If the window has the focus (its title bar is highlighted), it will also hide when you click on another window. Click the pushpin again to turn Auto Hide off.

### Pitfall: History covering the Command window
If you enable Auto Hide for the History window in its default docked location, it will **obscure the beginning of the Command window** when it slides out. Fix: **dock the History window at the right edge** of the main Stata window first, and then enable Auto Hide.

### When to use Auto Hide
- **Small screens:** hide History and Properties, keep Variables.
- **Presenting:** hide everything except Results and Command.
- **Data work:** keep Variables visible; hide Properties until you need to change a label.

## 7. Nondocking windows

The Graph window, Data Editor, Do-file Editor, Viewers and dialogs are **always independent** of the main Stata window. They can be moved freely and do not link, tab or auto-hide with docking windows. Use your operating system's own window management (snap, tile, second monitor) for these.

Practical arrangements:
- Put the **Do-file Editor** on one half of the screen and the main Stata window on the other.
- Put a **Viewer** with a help file beside the Do-file Editor.
- Keep the **Graph** window on a second monitor if you have one.

See the [Viewer guide](viewer-guide.md) for tabs and split tab groups *inside* a Viewer. Those are a different mechanism from docking windows in the main window, though they look similar.

## 8. Closing, reopening and bringing windows forward

According to the manual, you can close all windows except the Results and Command windows. To open a closed window, use the **Window** menu and select the window you want.

You can also bring a window to the front from the Command window:

```stata
window manage forward results
window manage forward variables
window manage forward viewer
window manage forward doeditor
```
Valid window names for this command are: browser, command, doeditor, editor, graph, help, history, results, review, variables and viewer. If the window is not available, the command does nothing and shows no error. (On Mac and Unix, `command`, `history`, `results` and `variables` all bring the single main Stata window forward.)

The toolbar also helps: the **Viewer**, **Graph** and **Do-file Editor** buttons open or bring forward their windows, and their small arrows let you choose among several open ones.

## 9. Preference sets: save, load, reset

Stata saves your preferences (including window arrangement) when you exit and reloads them on start-up. If you want to experiment safely, or switch between layouts, use **preference sets**.

### 9.1 In the menu
Open **Edit > Preferences** and do any of the following (the manual describes these):
- **Load preference set** and choose from the list. Several sets come installed with Stata; some are meant for small screens and others for giving presentations. They are worth a look.
- **Save preference set > New preference set...** to save the current preferences under a name you type.
- **Save preference set** and choose an existing set to overwrite it with the current preferences.
- **Delete preference set** and choose a set to remove it (you will be asked to confirm).

Changes you make *after* loading a set do not alter the set; it stays untouched unless you deliberately overwrite it.

### 9.2 With commands
The `window manage prefs` commands do the same things:

```stata
window manage prefs save "my_analysis_layout"   // save current preferences under a name
window manage prefs load "my_analysis_layout"   // load a saved set
window manage prefs default                     // back to the factory appearance
```
The reference entry says `window manage prefs default` is equivalent to loading the **Widescreen layout (default)** set, which is the quickest rescue if your layout goes wrong.

### 9.3 Good practice
- **Save a set before experimenting.** One command gets you back.
- Name sets after their use: `small_screen`, `teaching`, `data_cleaning`.
- Put `window manage prefs load "..."` in `profile.do` only for personal convenience. Never rely on it for results (see the [working directory guide](working-directory-guide.md) for `profile.do`).
- Preference sets belong to the computer and user account. A discussion on the Statalist forum indicates that on Windows the settings are kept in the registry and Stata offers no simple export to a file, so do not expect a saved layout to travel to a colleague's machine.

## 10. Fonts and colours

Layout is only half of comfort. The manual explains that you can change the display font and size of most windows by **right-clicking the window and choosing Font...**. The font lists for the Results, Viewer and Do-file Editor windows contain only **fixed-width** fonts so that output and numbers line up. Other windows may use any font.

Colours: the Results window and the Viewer have colour schemes controlling the display of input, text, results, errors, links and highlighted text. The default is the built-in Standard scheme (white background, dark text). In the Do-file Editor you can choose colours for syntax highlighting. An overall scheme can be selected on the **General** tab of the General preferences.

**Training-room tip:** for a projector, load a presentation preference set, increase the font in the Results and Command windows, and auto-hide History and Properties.

## 11. Suggested layouts

| Situation | Layout idea |
|-----------|-------------|
| **Learning (first weeks)** | Keep the default; all five windows visible so you see what each does |
| **Small laptop** | Variables and Properties tabbed together; History auto-hidden at the right edge; Do-file Editor on its own half of the screen |
| **Data cleaning** | Variables visible, Properties tabbed beside it; Data Editor in Browse mode on a second screen; Do-file Editor beside the main window |
| **Writing a do-file** | Do-file Editor and main window side by side; Viewer with help on the third part of the screen |
| **Presenting** | Results and Command only; large fonts; others auto-hidden or closed |
| **Reviewing a log** | A Viewer with a log in one tab group and the corresponding do-file in the Do-file Editor beside it |

Treat these as starting points. Save the ones you like as preference sets.

## 12. Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| A window has disappeared | It was closed or is auto-hidden at an edge | **Window** menu and select it; or look for an edge tab and hover |
| History covers the start of the Command window | Auto Hide on History in its default position | Dock History at the right edge first, then enable Auto Hide |
| Dragged a window and now the layout is odd | Dropped on the wrong docking guide | Drag it out again, or load a saved preference set |
| Cannot tab the Data Editor with Variables | The Data Editor is a nondocking window | Arrange it with operating system tools instead |
| Cannot find the Results window title | The Results window has no name in its title bar | It is the large window that fills the remaining space |
| Pushpin does nothing | The window is not docked in the main Stata window | Dock it first |
| Layout reverts after restart | Preferences are saved at exit; a crash or forced close may skip that | Save a named preference set once you are happy |
| Text unreadable on projector | Small fonts | Right-click > **Font...**, or load a presentation set |
| Colleague's screenshot looks different | Different version, platform, or preference set | Compare **Edit > Preferences** settings |
| Layout lost after reinstalling | Settings stored with the computer or user | Recreate the layout and save it again |

**Rescue sequence:** `window manage prefs default` returns to the factory layout. Then rebuild your own, step by step.

## 13. Practice exercises D1 to D12

Solutions are in `exercise-solutions/lesson-01/docking-windows-practice.do` (command-based parts only; most exercises are point-and-click). Try each one first.

**Difficulty key:** 🟢 basic, 🟡 intermediate, 🔴 challenge

**D1 🟢 Classify.** Without looking back, list the docking windows and the nondocking windows. Check against section 2.

**D2 🟢 Find the Results window.** Which window fills the remaining space in the main window? Why can it not be docked or tabbed?

**D3 🟢 Resize.** Drag the splitter between two linked windows. What happens to the neighbour?

**D4 🟢 Pushpin.** Click the pushpin on the Variables window. Where does the window go? Hover over its tab. Move the pointer away. Then click the pushpin to turn Auto Hide off. Note whether the pin is horizontal or vertical in each state.

**D5 🟡 Link.** Drag the History window by its title bar over the Variables window and drop it on the **bottom** guide. Describe the result. Which element lets you resize the two?

**D6 🟡 Tab.** Drag Properties over Variables and drop on the **centre** guide. How are the two windows now arranged? How do you switch between them?

**D7 🟡 Undock.** Drag the Properties tab out of the tabbed window and put it back where it was.

**D8 🟡 The pitfall.** Turn on Auto Hide for History in the default position and click in the Command window. What do you notice when History slides out? Fix it using the recommended method.

**D9 🟡 Save a layout.** Arrange the windows how you like them. Save the arrangement as a preference set called `my_layout` (use the menu), then run `window manage prefs default`, then reload `my_layout` with `window manage prefs load "my_layout"`.

**D10 🟡 Forward.** Open the Viewer, Do-file Editor and a graph (`sysuse auto, clear`, `scatter price mpg`). Practise bringing each forward with `window manage forward`. What happens if you ask for a window that is not open?

**D11 🔴 Design for a small screen.** Design a layout for a 13-inch laptop to be used for data cleaning. Draw it on paper first, then build it and save it as `small_screen`. What did you auto-hide and why?

**D12 🔴 Teach a colleague.** Write a five-line instruction card for a colleague who has "lost" the Variables window. Include the quickest rescue.

## 14. Quick reference card

| Task | How |
|------|-----|
| Docking windows | History, Command, Variables, Properties |
| Nondocking windows | Results, Graph, Data Editor, Do-file Editor, Viewers, dialogs |
| Move a docked window | Drag its title bar |
| Link windows (side by side or stacked) | Drop on an **outer** docking guide |
| Tab windows together | Drop on the **centre** docking guide |
| Undock a tabbed window | Drag its tab out to a docking guide |
| Resize linked windows | Drag the splitter |
| Auto Hide on / off | Click the pushpin (horizontal = on, vertical = off) |
| Show an auto-hidden window | Hover over its edge tab |
| Reopen a closed window | **Window** menu |
| Bring a window forward | `window manage forward <name>` |
| Save a layout | **Edit > Preferences > Save preference set**, or `window manage prefs save "name"` |
| Load a layout | **Edit > Preferences > Load preference set**, or `window manage prefs load "name"` |
| Factory layout | `window manage prefs default` |
| Change font | Right-click window > **Font...** |

## 15. Facilitator notes

**Timing (45-minute session):** 10 min concepts and demonstration (sections 1 to 3, 5, 6), 25 min hands-on D1 to D9, 10 min discussion of layouts for different tasks. D10 to D12 are optional extension.

**Before the session**
- Make sure every participant can find **Edit > Preferences** and has saved a preference set (a safety net) *before* they start dragging windows.
- On shared training PCs, preferences may be reset between users. Tell participants not to invest effort in a layout they cannot keep.
- Check the version on the training PCs: menu wording and default layouts differ between versions and operating systems (Windows, macOS, Linux).

**Common stumbling blocks**
- Participants try to dock the Data Editor or Do-file Editor. Remind them these are nondocking.
- Participants lose a window and panic. Teach the **Window** menu and `window manage prefs default` first.
- Dropping on the wrong guide. Encourage them to watch the preview before releasing.
- Auto Hide on History in its default position hides the start of the Command window.

**Teaching tips**
- Run a "messy to tidy" race: deliberately scramble the layout, then give two minutes to restore it using only the rescue sequence.
- Have pairs design a layout for a stated scenario (small laptop, projector) and explain their choices.
- Ask for a one-line rule: "Link what I use together, tab what I use in turns, hide what I use rarely."

**Assessment prompt (5 minutes):** "Your colleague's History window keeps covering the beginning of the Command window when it slides out. What is wrong and how do you fix it?" Expected: Auto Hide is on in the default position; dock History at the right edge, then enable Auto Hide.

**Note on versions.** This guide follows the Windows edition of the Getting Started manual. Docking behaviour is described for Stata for Windows; on macOS and Linux the main window arrangement and some `window manage` commands differ (for example, several window names all bring the main window forward). Check `help window manage` in your own installation.
