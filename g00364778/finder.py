def finder(data):
    # call finder_rec function with data array and the length of the array 
    # and return the final answer from finder_rec to the calling function
    return finder_rec(data, len(data)-1)
   
def finder_rec(data, x):
    # if the arra index is zero, return tha value in the first poition for comparison
    if x == 0:
        return data[x]
    # store the curent value  from the array in v1 for comparison
    v1 = data[x]
    # store the biggest of the two variables from the last call to finder_rec in v2 
    # for comparison when the call returns
    v2 = finder_rec(data, x-1)
    # compare the two values stored in v1 and v2 and return the biggest value for 
    # the next comparison step, the biggest of v1 or v2 will be returned to v2 from 
    # previous call to finder when popping off the stack
    if v1 > v2:
        return v1 # if v1 is bigger than v2 return v1
    else:
        return v2 # if v2 is bigger than v1 return v2

if __name__ == '__main__':
    # define the array of values to pass in to finder
    dat = [0, -247, 341, 1001, 741, 22] 
    # call finder with the dataset created above and return the result to retval
    retval = finder(dat)
    # print retval to the console outut
    print('The Value returned is:', retval)