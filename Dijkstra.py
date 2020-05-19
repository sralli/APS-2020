import sys
def Dijkstra(G,i,d):
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
		for j in range(0,len(G[i])):
			if G[i][j]!=0 :
				stack.append(j)
				print("Coordinates:",i,j)
				if dist[i]+G[i][j]<=dist[j]:
					print("Coordinate affecting:",j,"is",i)
					dist[j]=dist[i]+G[i][j]
					index[j]=i
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
for i in range(0,edges):
	node1,node2,distance=map(int,input().split())
	G[node1][node2]=distance
	#G[node2][node1]=distance
Dijkstra(G,0,4)
