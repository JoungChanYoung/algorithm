
month,day = map(int,input().split())

x = day

while month>1:
    month = month-1
    if month==1 or month==3 or month==5 or month==7 \
        or month==8 or month==10 or month==12:
        x = x+31
    elif month==4 or month==6 or month==9 or month==11:
        x = x+30
    elif month==2:
        x = x+28
    else:
        print("error")
        
y = x%7
if y == 1:
    print("MON")
elif y==2:
    print("TUE")
elif y==3:
    print("WED")
elif y==4:
    print("THU")
elif y==5:
    print("FRI")
elif y==6:
    print("SAT")
elif y==0:
    print("SUN")
    
