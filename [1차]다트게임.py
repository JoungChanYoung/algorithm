import re
def solution(dartResult):
    s1 = []
    s2 = []
    tmp = re.split('\D',dartResult)
    tmp2 = re.split('\d',dartResult)
    for i in tmp:
        try:
            s1.append(int(i))
        except:
            continue
    for i in tmp2:
        if i:
            s2.append(i)

    for i in range(len(s2)):
        t1 = s2[i]
        t2 = None
        if len(t1) > 1:
            t2 = t1[-1]
            t1 = t1[0]
        if t1 is 'S':
            pass
        elif t1 is 'D':
            s1[i] = pow(s1[i],2)
        elif t1 is 'T':
            s1[i] = pow(s1[i],3)
        if t2 is '#':
            s1[i] = s1[i] * -1
        elif t2 is '*':
            s1[i] = s1[i] * 2
            if i >= 1:
                s1[i-1] = s1[i-1] * 2
            else:
                continue
    answer = sum(s1)
    return answer

s = '1D2S3T*'
print(solution(s))
