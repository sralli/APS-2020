#!/bin/python3

import math
import os
import random
import re
import sys

def number(n):
    num=n
    num1=str(num)
    n=n**2
    n=str(n)
    val2=0
    if len(n)!=1:
        val=n[:len(n)-len(num1)]
        val2=int(val)
        if len(str(num))<len(n):
            val1=n[len(n)-len(num1):]
            val2+=int(val1)
    else:
        if num!=1:
            return False
        else:
            return True
    if val2==num:
        return True
    else:
        return False
# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    flag=0
    for i in range(p,q+1):
        if number(i):
            print(i,end=' ')
            flag=1
    if flag==0:
        print("INVALID RANGE")
