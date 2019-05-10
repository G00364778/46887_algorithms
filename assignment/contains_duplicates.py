import time

def contains_duplicates(elements):
    for i in range (0, len(elements)):
        for j in range(0, len(elements)):
            steps=(i+1)*(j+1)
            if i == j: # avoid self comparison
                continue
            if elements[i] == elements[j]:
                #return True, steps
                return steps
    #return False, steps
    return steps

if __name__ == '__main__':
    #testarr=[i for i in range(0,5001)]
    #testarr[0]=1000
    test1=[10,0,5,3,-19,5]
    test2=[0,1,0,-127,346,125]
    start = time.time()
    result = contains_duplicates(test2)
    end = time.time()
    #print("Duplicates found:", result, "- Execution Time:", (end-start)*1000, "ms")
    print("Duplicates found in stepcount:", result, "- Execution Time:", (end-start)*1000, "ms")