from itertools import combinations
def getSubString(s):
  res = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2)]
  return res
s=input()
print(getSubstring(s))
