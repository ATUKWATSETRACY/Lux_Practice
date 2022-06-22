#!/bin/python3

import math
import os
import random
import re
import sys



## Python 3 code to find sum of elements in given array
 
def simpleArraySum(ar):
    
    
    sum=0
    
    
    for i in ar:
        sum = sum + i
        
    return(sum)

# driver function
ar=[]
# input values to list
ar = [30,40,50,60]

# calculating length of array
n = len(ar)

ans = simpleArraySum(ar)

# display sum
print ('Sum of the array is ', ans)





