verbose = False
# Python code to implement Stable QuickSort. 
# The code uses middle element as pivot. 
def quickSort(ar): 
	
	# Base case 
	if len(ar) <= 1: 
		return ar 

	# Let us choose middle element a pivot 
	else: 
		mid = len(ar)//2
		pivot = ar[mid] 

		# key element is used to break the array 
		# into 2 halves according to their values 
		smaller,greater = [],[] 

		# Put greater elements in greater list, 
		# smaller elements in smaller list. Also, 
		# compare positions to decide where to put. 
		for indx, val in enumerate(ar): 
			if indx != mid: 
				if val < pivot: 
					smaller.append(val) 
				elif val > pivot: 
					greater.append(val) 

				# If value is same, then considering 
				# position to decide the list. 
				else: 
					if indx < mid: 
						smaller.append(val) 
					else: 
						greater.append(val)
		if verbose == True:
			print('{}<--{}-->{}'.format(smaller,pivot,greater)) 
		return quickSort(smaller)+[pivot]+quickSort(greater) 
	
# Driver code to test above 
if __name__ == '__main__':
	verbose=True
	# ar = [1, 3, 5, 9, 8, 3, 4, 6, 7]
	ar = [5, 7 ,6 ,9, 2] 
	print('Initial Array: ',ar) 
	sortedAr = quickSort(ar) 
	print(' Sorted Array: ',sortedAr) 
