# def heap(h):
#     n=len(h)
#     i = (n//2)-1
#     while i!=1:
#         k = i
#         v = h[i]
#         heap1=False
#         while heap1!=True and 2*k<=n:
#             j = 2*k
#             if j<n:
#                 if h[j]<h[j+1]:
#                     j= j+1
                
#             if v>=h[j]:
#                 heap1=True
#             else:
#                 h[k] = h[j]
#                 k=j
#         h[k]=v
#     print(h)


# h=[0,2,9,7,6,5,8]
# heap(h)


import heapq
h=[]

for _ in range(int(input())):
    n = list(map(int, input().split()))
    m = []
    heapq.heapify(h)
    if len(n)==2:
        j,k = n[0], n[1]
        if j==1:
            heapq.heappush(h,k)
            m.append(k)
        if j==2:
            m.remove(h.index(k))
    else:
        if n[0]==3:
            while heap[0] not in m:
                heappop(h)
            
            print(h[0])