#!/bin/python3

import math
import os
import random
import re
import sys
def frequencyCount(arr):
    d={} #Dictionary
    for i in range(len(arr)):
        d[arr[i]]=arr.count(arr[i])
    return d
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d=frequencyCount(ar);
    d=list(d.values())
    count=0
    for i in range(len(d)):
        count+=d[i]//2
    return count

