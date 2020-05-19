#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    val=2
    while(val!=n):
        t3=t1+(t2**2)
        t1=t2
        t2=t3
        val+=1
    return t3
