import calendar


def p(m1,m2,y1,y2):
    c=0
    times=[0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    for i in range(y1, y2+1):
        
        y=i
        y-=1
        day = (y+int(y/4)-int(y/100)+int(y/400)+times[1]+1)%7
        if (day == 0 and not ((i%4==0 and i%100 != 0) or i%400==0) or day == 6):
                c+=1
        print(c)
      
                
for _ in range(int(input())):
    m,y = map(int, input().split(' '))
    m2,y2 = map(int, input().split(' '))
    x=0
    if m>2:
        y+=1
    if m2<2:
        y2-=1

    if y2-y>=400:
        years_left = (y2-y)%400
        x = ((y2-y)//400)*101
        # print(years_left)


        if y%400+years_left == 400:
            y2=y+years_left
        else:
            y= y2-years_left
   

    p = (m,m2,y,y1)
    

    


