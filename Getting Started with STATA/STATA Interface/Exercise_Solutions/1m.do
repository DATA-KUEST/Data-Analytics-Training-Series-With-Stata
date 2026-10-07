* 1m. Cars with above-average mpg, without hard-coding the mean
sysuse auto, clear
summarize mpg
display "Stored mean: " r(mean)
count if mpg > r(mean)

* See everything summarize stored
return list
