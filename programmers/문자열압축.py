#level2 2022 kakao blind recruitment
import math
def solution(s):
    answer = 0
    if len(s) == 1:
        return len(s)
    
    for k in range(1, math.floor(len(s)/2)+1):
        new_str = "" #압축된 string
        tmp_str = "" 
        tmp_num = 0 #중복 횟수 체크
        for i in range(len(s)):            
            tmp_str = s[i*k:k+i*k]
            if i*k > len(s)-1:
                break
            if tmp_str == s[(i+1)*k:k+(i+1)*k]:
                tmp_num += 1
            else:
                if not tmp_num:
                    new_str += tmp_str
                else:
                    new_str += str(tmp_num + 1) + tmp_str      
                    tmp_num = 0        
        if not answer:
            answer = len(new_str)
        else:
            answer = min(answer, len(new_str))
    return answer

if __name__ == "__main__":
    print(solution("aabbaccc")) #->2a2ba3c 처럼 가장 압축된 형태로 만들고, 그때의 길이 출력