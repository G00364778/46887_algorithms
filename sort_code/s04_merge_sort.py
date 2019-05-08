# Merge sort
debug = False
def mergesort(arr):
  # create a top level function with a single parameter and calculate the 
  # merge sort parameters so that the function is similar to the other sort 
  # functions and can be called from the benchmark fucntion 
  return mergesort_p(arr, 0, len(arr)-1)

def mergesort_p(arr, i, j):
  # main merge sort function
  # this splits the array in left and right untill there are just a single pair 
  # of values left and the pass the vales to merge to put together is a sorted way. 
  # This section also creates the stacked space complexity by calling itself and 
  # placing sections of the stack unitill it cannot be split further. Coming off 
  # the stack left and right are then merged by reference. 
  mid = 0
  if i < j:
    mid = int((i + j) / 2)
    # split part down the middle and stack untill one 
    mergesort_p(arr, i, mid)
    # split right down the middle and stach untill one
    mergesort_p(arr, mid + 1, j)
    r_arr=merge(arr, i, mid, j)
    return r_arr

def merge(arr, i, mid, j):
  # this code merges the referenced sections on the stack back together in sorted 
  # order and return it to the calling function
  if debug == True: # display this if debugging is enabled
    print ("Left: " + str(arr[i:mid + 1]), "Right: " + str(arr[mid + 1:j + 1]))
  N = len(arr)
  temp = [0] * N
  l = i
  r = j
  m = mid + 1
  k = l
  while l <= mid and m <= r:
    if arr[l] <= arr[m]:
      temp[k] = arr[l]
      l += 1
    else:
      temp[k] = arr[m]
      m += 1
    k += 1

  while l <= mid:
    temp[k] = arr[l]
    k += 1
    l += 1
  while m <= r:
    temp[k] = arr[m]
    k += 1
    m += 1
  for i1 in range(i, j + 1):
    arr[i1] = temp[i1]
  if debug == True: # display this if debugging is enabled
    print (" After Merge: " + str(arr[i:j + 1]))
  return arr

if __name__ == '__main__':
    # debug = True # default disabled, uncomment to enable
    # diffrent arrays for testing and comparison purposes
    arr1 = [0, 1, 2, 3, 4, 5, 6]
    arr2 = [0, 1, 2, 3, 4, 5, 6, 7]
    arr3 = [9, 4, 8, 3, 1, 2, 5]
    arr4 = [4, 8, 3, 1, 2, 5, 9]
    arr5 = [i for i in range(100,0,-1)]
    
    # a list of the arrays to loop through is the test 
    #s = [arr1,arr2,arr3,arr4,arr5]
    s = [arr3]
    for arr in s:
      print ("Initial Array: " + str(arr))
      arrs=mergesort(arr)
      print (" Sorted Array: " + str(arrs)+"\n")
