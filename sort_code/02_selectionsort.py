# selection sort
def printArray(arr):
  return (' '.join(str(i) for i in arr))


def selectionsort(arr):
  N = len(arr)
  for i in range(0, N):
    small = arr[i]
    pos = i
    for j in range(i + 1, N):
      if arr[j] < small:
        small = arr[j]
        pos = j
    temp = arr[pos]
    arr[pos] = arr[i]
    arr[i] = temp
    print ("After pass " + str(i) + "  :", printArray(arr))

if __name__ == '__main__':
    arr = [10, 7, 3, 1, 9, 7, 4, 3]
    print ("Initial Array :", printArray(arr))
    selectionsort(arr)