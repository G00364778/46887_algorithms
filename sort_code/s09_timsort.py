# Timsort - using the built in python sort function
def timsort(arr):
    return sorted(arr)

if __name__ == '__main__':
    ar = [10, 7, 8, 9, 1, 5] 
    print('Initial Array: ',ar) 
    sortedAr = timsort(ar) 
    print(' Sorted Array: ',sortedAr) 