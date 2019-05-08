# Counting sort
debug = False
def printArray(arr):
  # create a nice looking output of the array seperated by spaces
  return(' '.join(str(i) for i in arr))


def countingsort(arr):
  N = len(arr)
  maxval=max(arr) + 1
  # create an array for every possible number from 0 to the biggest 
  # number in the list passed in to the function
  count = [0] * maxval  # can store the count of positive numbers <= maxval
  # count and catalog the occurance count for every number in the list
  for i in range(0, N):
    count[arr[i]] += 1
  if debug == True:
    print ("         Counting Array :", printArray(count))
  # sum the count by adding the countvalues to the sum of the previous column 
  # this  reates the positional index for the values
  for i in range(1, len(count)):
    count[i] += count[i - 1]
  if debug == True:
    print ("  Counting Array summed :", printArray(count))
  # initialise the output array
  output = [0] * N
  if debug == True:
    print ("       Output inisiated :", printArray(output))
  # move the input array values to the positions in the output array based on 
  # the indexes created in the summed count array above. Decrement the positional index 
  # value for positioning of duplicates
  for i in range(len(arr)):
    output[count[arr[i]] - 1] = arr[i]
    count[arr[i]] -= 1
    if debug == True:
      print('    loop:',i,' Output Arr :',printArray(output))
      print('              Count Arr :',printArray(count))
  if debug == True:
    print ("  Output Array arranged :", printArray(count))
    print ("Counting Array less one :", printArray(output))
  if debug == True:
    print ("         After Sorting  :", printArray(output))
  # return the sorted list to the calling function
  return output

if __name__ == '__main__':
  debug = True
  a1 = [6, 7, 3, 1, 9, 7, 4, 3]
  a2 = [7, 3, 1, 9, 7, 4, 3, 6]
  
  sorts=[a1,a2]
  for arr in sorts:
    print ("         Initial Array  :", printArray(arr))
    arrs=countingsort(arr)
    print ("          Sorted Array  :", printArray(arrs))
