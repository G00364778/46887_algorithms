from time import time
from time import sleep
from numpy.random import randint
import numpy as np

cycles=3 # number of test cycles declare globally

def my_fake_sort_routine(stuff_to_sort):
  #delay to create a fake routine time
  val=randint(1, 10)/np.pi
  sleep(val) # sleep one to ten seconds faking sort time
  return stuff_to_sort

if __name__ == '__main__':
  list_to_sort=[5,5,7,9,4,3,7,1,2] 
  sort_times=[] # an e7mpty array to store the times in the loop below
  for cyle in range(cycles): # run a number of test cycles as defined above
    start=time() # set the start time
    # call the sort routine
    my_fake_sort_routine(list_to_sort)
    end=time() #set the end time
    #print(end-start) # print it so you can see the value
    sort_times.append(end-start)# and save it to the array
    print('sort times: ', sort_times) # so you can see the list grow
#then outside of the loop average the list
avg_time=np.average(sort_times) # average using numpy
print('average_time: ', avg_time)

#or manually calculate the average
sumval=0 
for val in sort_times:
    #print(val)
    sumval+=val
average=sumval/cycles
print('manual avg: ',average)
