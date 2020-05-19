#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    val=max(height)
    if val>k:
        return val-k
    else:
        return 0
