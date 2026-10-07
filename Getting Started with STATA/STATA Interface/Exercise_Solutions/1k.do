* 1k. Same analysis, with a log file
* Start recording output
log using lesson01.log, replace

sysuse auto, clear
describe
summarize price mpg
tabulate foreign
bysort foreign: summarize mpg

* Stop recording
log close
