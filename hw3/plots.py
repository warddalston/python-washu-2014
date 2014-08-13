import matplotlib.pyplot as plt
import timer

###################
# Dalston Ward
# Homework 3 - plotting functions
####################

#using the output from the timer file, create lines.  Selection sort is red. Only need one argument, because the default is to treat the given argument as y and let x =  range(1:len(y)+1).  "r-" instructs python to make a red line.  Labels are used in the legend.  
plt.plot(timer.time_selection.values(), "r-", label = "Selection Sort") 
plt.plot(timer.time_merge.values(), "g-", label = "Merge Sort")
plt.ylabel("Time (in seconds)") 
plt.xlabel("Number of Items to Sort")
plt.title("Runtime of Two Sorting Algorithms")
plt.legend(loc='upper left') #gets label information from the plt.plot calls. 
plt.show()