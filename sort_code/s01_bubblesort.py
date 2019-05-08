# Bubble Sort
verbose = False
def printArray(arr):
  return (' '.join(str(i) for i in arr))


def bubblesort(arr):
  # create an outer loop the size of the array
  totalcycles=0
  actualcycles=0
  for i in range(len(arr)):
    # create an inner loop thep the size of the array
    for j in range(len(arr) - i - 1):
      totalcycles+=1
      # starting at the left compare the two consecutive 
      # elements and swop if the one to the left is bigger. 
      # Skip the elemnts on the right by the outer loop 
      # value to skip already sorted ones
      if arr[j] > arr[j + 1]:
        actualcycles+=1
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
    # Print array after every pass to visualise progress
    if verbose ==True: 
      print (" After pass " + str(i) + " :", printArray(arr))
  if verbose == True:
    return arr, totalcycles, actualcycles
  else:
    return arr

if __name__ == '__main__':
  verbose = True
  #arr = [10, 7, 3, 1, 9, 7, 4, 3, 2,6]
  #arr = [10, 7, 3, 1, 9, 7, 4, 3]
  arr = [3, 7, 3, 1, 9, 7, 4, 10]
  #arr = [1, 3, 3, 4, 7, 7, 9, 10]
  #arr = [10, 9, 7, 7, 4, 3, 3, 1]
  print ("Initial Array :", printArray(arr))
  if verbose == True:
    arrs,t,a = bubblesort(arr)
  else:
    arrs = bubblesort(arr)
  print (" Sorted Array :", printArray(arrs))
  if verbose == True:
    print ('n: {} Cycles: {} Swops: {}'.format(len(arr),t,a))
  