#level2 2019카카오 개발자 겨울 인턴십
from collections import Counter
def solution(s):
    answer = []
    tmp = []
    li = []
    s = s[1:-1]
    tmp_s = ''
    for i in range(len(s)):
        if s[i] == '{':
            tmp = []
        elif s[i] == '}':
            tmp.append(int(tmp_s))
            li.extend(tmp)
        elif s[i] != ',':
            tmp_s += s[i]
        elif s[i] == ',':
            tmp.append(int(tmp_s))
            tmp_s = ''

    counter = Counter(li)
    counter_tmp = []
    for key,val in counter.items():
        counter_tmp.append((val, key))
    counter = sorted(counter_tmp,reverse=True)
    for val, key in counter:
        answer.append(key)
    return answer

if __name__ == "__main__":
    print(solution(	"{{4,2,3},{3},{2,3,4,1},{2,3}}"))