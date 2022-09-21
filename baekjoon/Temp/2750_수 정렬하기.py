#bubble sorting

num = int(input())
li=[]

for x in range(num):
    li.append(int(input()))
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if(li[j]>li[j+1]):
            tmp = li[j]
            li[j] = li[j+1]
            li[j+1] = tmp
for k in range(len(li)):
    print(li[k])

    
