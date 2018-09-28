#s1에 대해 이분탐색
#s2는 탐색해야하는 값 벡터
n = int(input())
s1 = input().split()
m = int(input())
s2 = input().split()

s1 = sorted(s1)
for i in range(len(s2)):
    left = 0
    right = len(s1) - 1
    flag = 0
    while(left <= right):
        mid = int((left + right) / 2)
        if s1[mid] > s2[i] :
            right = mid - 1
        elif s1[mid] < s2[i] :
            left = mid + 1
        else :
            flag = 1
            break
    if flag :
        print(1)
    else :
        print(0)
