import math
import os
import random
import re
import sys

# if the condition for "if" is satiesfied, it will do the operation for that block only and ignore the rest of them. 
# if the "if" condition is not true, then it will move on to the next block which is "elif" in this case and execute that block and ignore the rest.
# if any of the condition is not true, then it will execute the code of "else" block.


if __name__ == '__main__':
    n = int(input().strip())

    if n%2==0 and n>=2 and n<=5:
        print("Not Weird")
    elif n%2==0 and n>=6 and n<=20:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")
    else:
        print("Weird")

