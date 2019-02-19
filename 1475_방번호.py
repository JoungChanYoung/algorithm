import sys
import math

num = sys.stdin.readline().rstrip()
if int(num) == 0:
    digits = 1
else:
    digits = int(math.log10(int(num))) + 1

li = []
for i in range(digits):
    li.append(int(num[i]))

result = 0
tmp_sixornine = 0
for i in range(10):
    tmp = li.count(i)
    if i == 6 or i == 9: # 6,9는 호환가능
        tmp_sixornine += tmp
        continue
    result = max(tmp,result)
tmp_sixornine = int(tmp_sixornine / 2 + 0.5) #반올림
result = max(tmp_sixornine, result)
print(result)
