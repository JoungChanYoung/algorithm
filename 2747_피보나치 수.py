n = int(input()) #n>=2

fibonacci = []

fibonacci.append(0) #0,1은 항상 포함
fibonacci.append(1)

tmp1 = 0
tmp2 = 1

for x in range(n):
    tmp_now = tmp1 + tmp2 #Fn = Fn-1 + Fn-2
    fibonacci.append(tmp_now)
    tmp1 = tmp2
    tmp2 = tmp_now
print(fibonacci[n])
