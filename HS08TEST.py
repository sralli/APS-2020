x,y=map(float,input().split())
if x%5==0 and y>=x+0.5:
	y-=x
	y-=0.5
print("%.2f" % y)
