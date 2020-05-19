import sys
def Dijkstra(G,V,i,d):
	index=[]
	dist=[]
	stack=[]
	stack.append(i)
	for j in range(0,len(G[i])):
		dist.append(sys.maxsize)
	for j in range(0,len(G[i])):
		index.append(0)
	dist[i]=0
	while(len(stack)!=0):
		i=stack.pop()
		minVertex=-1
		if (V[i]==False) and (minVertex==-1 or dist[q]<dist[minVertex]):
				minVertex=i
		V[minVertex]=True
		minVertex=-1
		for j in range(0,len(G[i])):
			if G[minVertex][j]!=0 and V[j]==False:
				stack.append(j)
				print("Coordinates:",i,j)
				if dist[minVertex]+G[minVertex][j]<=dist[j]:
					print("Coordinate affecting:",j,"is",minVertex)
					dist[j]=dist[minVertex]+G[minVertex][j]
					index[j]=minVertex
	print(dist[d])
	print(dist)
	#print(index)
	k=d
	while(k!=0):
		print(index[k])
		k=index[k]
edges=int(input())
N=int(input())
G=[]
for i in range(0,N):
	l=[]
	for j in range(0,N):
		l.append(0)	
	G.append(l)
V=[]
for i in range(0,N):
	V.append(False)
for i in range(0,edges):
	node1,node2,distance=map(int,input().split())
	G[node1][node2]=distance
	#G[node2][node1]=distance
Dijkstra(G,V,0,4)
