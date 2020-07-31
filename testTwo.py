#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200730

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def highestValuePalindrome(s, n, k):
    return str(len(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
