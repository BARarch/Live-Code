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
def isValid(s):
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
