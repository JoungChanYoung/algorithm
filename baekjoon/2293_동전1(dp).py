n, obj = map(int,input().split())

a = [0 for x in range(obj+1)]
a[0] = 1
for i in range(n):
    k = int(input())
    for j in range(len(a)):
        if j < k:
            continue
        a[j] = a[j] + a[j-k]
print(a[-1])
