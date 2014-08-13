from timeit import Timer

##############
# Dalston Ward
# Homework 3 - timing
##############

#These two for loops create dictionaries recording how long it takes the functions to sort some random data.  

time_selection = {} #output is stored here
for size in range(1,251): #the range defines how large our set of numbers to sort is
	setup = "import sort; import numpy; import random; data = list(numpy.random.normal(size="+str(size)+"))" #we create a setup objet that our timer will call to initialize the timed runs
	t = Timer("sort.selectionSort(List = data)", setup) #creates an object saying how to initialized a timed run and what to run while timing
	time_selection[size] = t.timeit(number = 100) #does the timing.  number says "do this function 100 times".  This is to avoid basing conclusions of the speed of our function on random disturbances.  
print time_selection

#same as above but with merge 
time_merge = {}
for size in range(1,251):
	setup = "import sort; import numpy; import random; data = list(numpy.random.normal(size="+str(size)+"))"
	t = Timer("sort.mergeSort(List = data)", setup)
	time_merge[size] = t.timeit(number = 100) 
print time_merge