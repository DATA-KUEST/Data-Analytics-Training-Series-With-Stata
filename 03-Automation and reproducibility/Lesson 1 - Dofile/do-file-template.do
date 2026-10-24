*------------------------------------------------------------------*
* NN_name.do
* Project : DATAQUEST <project name>
* Purpose : <one sentence>
* Author  : <your name>                       Date: <date>
* Input   : <files read>
* Output  : <files written>
*------------------------------------------------------------------*

version 17              // change to the release you are using
clear all
set more off

* ---- Paths (defined in 00_master.do; shown here for stand-alone use) --
* global root "C:/path/to/project"
* cd "$root"

* ---- Log --------------------------------------------------------
capture log close
capture mkdir "logs"
log using "logs/NN_name.log", replace text

//# 1. Load data
* use "data/..." , clear

//# 2. Checks
* confirm file "..."
* assert !missing(id)
* isid id

//# 3. Main work

//# 4. Save
* save "data/..." , replace

log close
