def return_the_biggest(data):
    # assign the first item in the list to the vaiable "largest"
    largest=data[0]
    # now iterate through the list assigning one value at a time to testval
    for testval in numlist:
        # compare the values and assign the biggest to the variable "largest" if bigger 
        if testval > largest:
            largest=testval
    #finally return the result 
    return largest
    
if __name__ == '__main__':
    # define the list of number to process
    numlist=[0, -247, 341, 1001, 741, 22] 
    retval = return_the_biggest(numlist)
    print('The biggest value in the list is:',retval)
