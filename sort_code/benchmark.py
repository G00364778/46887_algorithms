from time import time
from s01_bubblesort import bubblesort as bs
from s04_merge_sort import mergesort as ms
from s07_counting_sort import countingsort as cs
from s05a_quick_sort_stable import quickSort as qs
from s09_timsort import timsort as ts
from numpy.random import randint
import numpy as np


if __name__ == '__main__':
    # create a dictionary of sort types to loop through 
    types={bs:'  Bubble Sort',ms:'   Merge Sort',cs:'Counting Sort',qs:'   Quick Sort',ts:'      Timsort'}
    headers='ArraySize'
    for key in types:
        headers+=', '+ types[key].strip()
    print(headers)
    valstrArr=[] ##store the rows for saving to a csv file
    # loop through the values in the array t and use the value to create an array of random values
    #for t in (10,20,30,50,100,200,300,500):
    #for t in (100,200,300,400,500,600,700,800,900,1000):
    for t in (100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000): 
    #for t in range(1000,30001,1000):
        test = randint(1,t*2,t)
        #print('  Input len,min,max: ', len(test),',',min(test),',',max(test))
        funcAvgTim=[] # create an emty array for storing the average times
        # read the sort types to complete from the types list
        for sortfunc, funcname in types.items():
            times=[] # create an empty list to store the times in fr the cycles
            for i in range(10): # repeat tests to get better average
                #print('         Test Cycle: ',i)
                start=time() # mark the start time of the test
                arr=test.copy() #copy the test array created above and re-use for every following test
                #print('  input: ', arr)
                ret=sortfunc(arr) # run the sort function and return the sorted result
                #print(' sorted: ', ret)
                end=time() # record the end time of the test
                #print(funcname,' time: ',(end-start)*1000)
                times.append((end-start)*1000) # append the test time to the times list
            print (t, funcname, np.average(times)) # prnt the average time to the screen
            funcAvgTim.append(np.average(times)) # save the avarage time to a list for saviing to file 
        valstr='' # initiate a val string for writing to file
        sep='' # nitiate the seperator for seperation of the values
        for val in funcAvgTim:
            valstr+=sep+str(val) # ppend the values to the string to write out to files
            sep=', ' # add the seperator
        #print('{}{}{}'.format(t,sep,valstr))
        valstrArr.append('{}{}{}'.format(t,sep,valstr)) #append the strin to a list for saving below

    for line in valstrArr:
        #print(line) # print the result to screen for validation purposes
        pass

    #write the cycle test resuts to file
    with open('sort_cycle_times_100-10k_by_10cycles.csv', 'w') as file:
        file.write(headers+'\n') # write a header line
        for line in valstrArr: # loop through the lines in the list
            file.write(line+'\n') # and write them out to the file 
