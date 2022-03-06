#이항 쇼다운
#n개의 원소중에서 k개를 순서없이 선택하는 방법의 수


while 1:
    a = input()
    n,k = map(int,a.split())
    
    if n + k == 0:
        break
    k = min(k,n-k)
    tmp = 1
    for x in range(k):
        tmp = tmp * (n - x) / (x + 1)
    if tmp < pow(2,31):
        print("{:}".format(int(tmp)))
