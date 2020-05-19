x,y = map(int, input().split(' '))
print("Min is", (y^(x^y)& -(x<y)))

print("Max is", (x^(x^y) & -(x<y)))