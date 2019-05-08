# Bucket sort
def bucketsort(arr):
  N = len(arr)
  bucket = [[]for i in range(0, N)]
  for i in range(0, N):
    index = (int)(N * arr[i])
    bucket[index].append(arr[i])
  print ("After sorting " + str(N) + " buckets")
  for i in range(0, N):
    bucket[i].sort()
    print (bucket[i])
  k = 0
  print ("After concatenating " + str(N) + " buckets")
  for i in range(0, N):
    for j in range(0, len(bucket[i])):
      arr[k] = bucket[i][j]
      k += 1
  print (arr)

if __name__ == '__main__':
    arr = [0.987, 0.678, 0.123, 0.887, 0.665, 0.432, 0.342]
    print ("Initial Array  :" + str(arr))
    bucketsort(arr)