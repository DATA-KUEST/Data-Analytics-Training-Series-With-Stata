* 1n. Command equivalents of the toolbar actions
sysuse auto, clear

* Do-file Editor button
doedit

* Data Editor (Browse) button
browse

* Log button: start, then close
log using toolbar_practice.log, replace
summarize price mpg
log close

* Toolbar clicks leave no record; these commands do, so they are reproducible.
