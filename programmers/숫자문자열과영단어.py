#level1 2021 카카오 채용연계형 인턴십 
from collections import Counter
def solution(s):
    answer = 0
    li = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(len(li)):
        if li[i] in s:
            s = s.replace(li[i], str(i))
    answer = int(s)
    return answer

if __name__ == "__main__":
    print(solution("one4seveneight"))