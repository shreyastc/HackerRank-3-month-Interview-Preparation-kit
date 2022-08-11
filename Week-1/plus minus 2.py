import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def plusMinus(arr):
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0
    #Initialising the count of positive, negative and zero numbers as 0
    
    for num in arr:
        if num > 0:
            positive_count += 1   #If number is greater than 0, then increase the positive count
        elif num < 0:
            negative_count += 1   #If number is kesser than 0, then increase the negative count
        else:
            zero_count += 1    #Else increase the zero count
            
        
    print(positive_count / len(arr)) #Print the ratio of postive number count by dividing it by length of total size of array
    print(negative_count / len(arr))   #Print the ratio of negative number count by dividing it by length of total size of array
    print(zero_count / len(arr))   #Print the ratio of zero count by dividing it by length of total size of array
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
