#########
# Dalston Ward
# Homework 3 - Functions
#########

###### selection sort
def selectionSort(List):
	for item in range(len(List) - 1): # - 1  in the loop because the last element has already been compared to everything and thus must be the largest item.
		min = item
		item_val = List[item] #for use in swapping, if necessary 
		for comparison in range(item + 1, len(List)): # + 1 because we don't need to compare an element to itself
			if List[min] > List[comparison]: #where the actual comparison occurs.  min is equal to item on the first iteration of the loop 
				min = comparison
		if item != min: #if item isn't still the minimum we swap it with the current minimum (item and min are indicies!)
			List[item] = List[min]
			List[min] = item_val
	return List

###### merge sort 
def mergeSort(List):
	#these first few lines are just like from class the other day.  
	if len(List) <= 1:
		return List
	left = List[ : len(List) / 2 ]
	right = List[len(List) / 2 : ]
	left = mergeSort(left) #recursive element here and the next line.  
	right = mergeSort(right)
		#its quicker if we don't define a separate function for the merging. 
	i = 0
	j = 0
	merged = []
	while len(merged) < len(left) + len(right): #when this fails, everything is sorted
		if i < len(left) and j < len(right): #make sure that there are still items left in both of them to sort.  If so, then compare and sort 
			if left[i] < right[j]:
				merged.append(left[i])
				i += 1
			else:
				merged.append(right[j])
				j += 1
		elif i < len(left): #these elifs kick in when we've already entirely sorted one of the two lists.  Then we just append the rest of the other list one item at a time. 
			merged.append(left[i])
			i += 1
		elif j < len(right):
			merged.append(right[j])
			j += 1
	return merged 
	