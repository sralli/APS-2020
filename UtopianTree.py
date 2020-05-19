#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    val=1
    for i in range(n):
        if i%2==0:
            val*=2
        else:
            val+=1
    return val
