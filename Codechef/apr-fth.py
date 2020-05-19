
def checker(arr, i, ind):
    global odd, n, answer
    if i&1:
        add_1()
    if i%4==0:
        increment_2(n,ind)
    if i%4==2:
        next_index=n
        for j in range(ind+1, n):
            if arr[j]%2==0:
                next_index=j
                break
    
        counter_3(n,int(next_index))

def add_1():
    global odd
    odd+=1

def make_zero():
    global odd
    odd =0
    

def increment_2(n,i):
    global answer,odd
    answer+= (n-i) + ((odd * (odd + 1)) / 2) + (odd * (n-i))
    make_zero()

def counter_3(n,nxt_idx):
    global answer, odd
    answer += (n-nxt_idx) + ((odd * (odd + 1)) / 2) + (odd * (n-nxt_idx))
    make_zero()




for t in range(int(input())):
    answer, odd = 0 ,0 
    n =  int(input())
    arr = list(map(int, input().split(' ')))
    for ind in range(n):
        checker(arr, arr[ind], ind)
    
    answer += (odd * (odd + 1)) / 2
    print(int(answer))

   


