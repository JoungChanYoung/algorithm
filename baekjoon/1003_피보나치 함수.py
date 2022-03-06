test_case = int(input())

t = []
for i in range(test_case):
    t.append(int(input()))

cnt = [0] * 40

num = 0
def fibonacci(n):
    global cnt
    if n>=2 and (cnt[n-1] is not 0) and (cnt[n-2] is not 0):
        cnt[n] = cnt[n-1] + cnt[n-2]
        return cnt[n]
    
    if n ==0 :
        return 0
    elif n==1:
        return 1
    else:
        cnt[n] = fibonacci(n-1) + fibonacci(n-2)
        return cnt[n]    

for i in range(len(t)):
    if t[i] == 0:
        print("1 0")
    else:
        tmp1 = fibonacci(t[i])
        tmp2 = fibonacci(t[i]-1)
        print(str(tmp2) + " " + str(tmp1))
    
