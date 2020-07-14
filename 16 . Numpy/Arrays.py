import numpy

def arrays(arr):
    a=numpy.array(arr,float)
    return(a[::-1])
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)