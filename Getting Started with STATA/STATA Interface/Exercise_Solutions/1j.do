* 1j. Lesson 1 analysis in a single do-file
* Load the data
sysuse auto, clear

* Structure of the dataset
describe

* Summary statistics for price and mpg
summarize price mpg

* Frequency table of origin
tabulate foreign

* mpg by origin
bysort foreign: summarize mpg
