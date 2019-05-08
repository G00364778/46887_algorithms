# insertion sort
def printArray(arr):
  return(' '.join(str(i) for i in arr))


def insertionsort(arr):
  N = len(arr)
  for i in range(1, N):
    j = i - 1
    temp = arr[i]
    while j >= 0 and temp < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = temp
    print ("After pass " + str(i) + "  :", printArray(arr))

if __name__ == '__main__':
    arr = [10, 7, 3, 1, 9, 7, 4, 3]
    print ("Initial Array :", printArray(arr))
    insertionsort(arr)