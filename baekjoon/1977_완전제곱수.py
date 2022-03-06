#M<=N, M,N사이완전제곱수 찾기

M = int(input()) 
N = int(input())

li = []

M_first = M
N_first = N
x = 1
while M<=N:
    tmp = int(pow(x,2))    
    if (tmp>=M_first) & (tmp<=N_first):     
        li.append(tmp)
    x += 1
    M += 1

if not li:
    print(-1)
else:
    print(sum(li))
    print(min(li))
