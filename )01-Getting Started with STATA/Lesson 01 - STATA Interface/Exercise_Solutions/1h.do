* 1h. Three most expensive cars
sysuse auto, clear
gsort -price            // minus sign = descending order
list make price in 1/3
