#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    val=min(abs(p-1),abs(n-p))
    if val%2==1:
        if val==abs(n-p):
            if n%2==0:
                ans=(val//2)+1
            else:
                ans=val//2
        else:
            ans=(val//2)+1

    else:
        ans=val//2
    return ans
