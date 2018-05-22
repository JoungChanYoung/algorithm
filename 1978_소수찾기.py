a = int(input())

b = []
b = input().split(" ")


tmp = []

for x in range(len(b)):
    y = 1
    cnt = 0 #약수의 개수
    while y <= int(b[x]):
        if int(b[x]) % y == 0:
            cnt = cnt + 1
        if cnt == 3:
            break
        y =  y+1
    if cnt >= 3:
        continue
    elif cnt>1:
        tmp.append(int(b[x]))
print(len(tmp))
    
