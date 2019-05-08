from numpy.random import randint
from time import time

def Bubble_Sort(array):
  # your sort code
  sorted=array
  return sorted

def Merge_Sort(array):
  # your sort code
  sorted=array
  return sorted

def Counting_Sort(array):
  # your sort code
  sorted=array
  return sorted

def Quick_Sort(array):
  # your sort code
  sorted=array
  return sorted

def Timsort(array):
  # your sort code
  sorted=array
  return sorted

# The actual names of your sort functions in your code somewhere, notice no quotes
sort_functions_list = [Bubble_Sort, Merge_Sort, Counting_Sort, Quick_Sort, Timsort]

# The prescribed array sizes to use in the benchmarking testst
for ArraySize in (100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000):
  # create a randowm array of values to use in the tests below
  testArray = randint(1,ArraySize*2,ArraySize)
  # iterate throug the list of sort functions to call in the test
  for sort_type in sort_functions_list:
    # and test every function ten times
    for i in range(10):
      start=time()
      sort_type(testArray)
      stop=time()
      print('{} {} {} {}'.format(sort_type, ArraySize, i, (stop-start)*1000))
      