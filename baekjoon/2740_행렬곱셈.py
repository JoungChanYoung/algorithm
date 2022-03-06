a = input().split()

A = []
for t in range(int(a[0])):
    tmp = input().split()
    A.append(tmp)

b = input().split()

B = []
for t in range(int(b[0])):
    tmp = input().split()
    B.append(tmp)    

for xx in range(len(A)):
    for y in range(len(B[0])):
        tmp = 0
        for x in range(len(A[0])):
            tmp += int(A[xx][x]) * int(B[x][y])
        print(tmp,end=" ")
    print("")
