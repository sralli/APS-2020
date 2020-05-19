
from itertools import permutations
final = []
perms = [k for k in permutations([0,1,2,3]) if len(set(k))==4]
d= {'A':0, 'B':1, 'C':2, 'D':3, '12': 0, '3':1, '6':2, '9':3}

def find_sum(max_):
    max_ = sorted(max_, reverse = True)
    s1 = 100*max_[0]+75*max_[1]+50*max_[2]+25*max_[3]
    var = max_.count(0)
    s1 = s1-(100*var)
    return s1

for _ in range(int(input())):
    arr = [[0]*4 for i in range(4)]
    for i in range(int(input())):
        char,num = map(str, input().split(' '))
        arr[d[char]][d[num]]+=1

    max_ = [ [arr[i][j] for i, j in zip(k,l)] for k in perms for l in perms]
    sum_ = [find_sum(i) for i in max_]
    final.append(max(sum_))
    print(max(sum_))
print(sum(final))





   
   
   