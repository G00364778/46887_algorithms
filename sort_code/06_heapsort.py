# Heap Sort
class MaxHeap:
  len
  arr = []

  def __init__(self, len, arr):
      self.len = len
      self.arr = arr
# Sorting in non decreasing order


def printArray(arr):
  return ' '.join(str(i) for i in arr)


def heapsort(arr):
  N = len(arr)
  # creating a heap
  heap = createHeap(arr, N)
  # Repeating the below steps till the size of the heap is 1.
  while heap.len > 1:
      swap(heap, 0, heap.len - 1)
      heap.len -= 1
    # Replacing largest element with the last item of the heap
      heapify(heap, 0)
  return heap.arr
# creating a heap


def createHeap(arr, N):
  maxheap = MaxHeap(N, arr)
  i = (int)((maxheap.len - 2) / 2)
  while i >= 0:
      maxheap = heapify(maxheap, i)
      i -= 1
  return maxheap


def heapify(maxheap, N):
  largest = N
  left = 2 * N + 1  # index of left child
  right = 2 * N + 2  # index of right child
  if left < maxheap.len and maxheap.arr[left] > maxheap.arr[largest]:
      largest = left
  if right < maxheap.len and maxheap.arr[right] > maxheap.arr[largest]:
      largest = right
  if largest != N:
      swap(maxheap, largest, N)
      heapify(maxheap, largest)
  return maxheap


def swap(maxheap, i, j):
  temp = maxheap.arr[i]
  maxheap.arr[i] = maxheap.arr[j]
  maxheap.arr[j] = temp

if __name__ == '__main__':
    arr = [9, 4, 8, 3, 1, 2, 5]
    print ("Initial Array  :", printArray(arr))
    arr = heapsort(arr)
    print ("After Sorting  :", printArray(arr))