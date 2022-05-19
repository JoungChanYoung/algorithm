#level1 

def solution(s):
    answer = True
    s = s.lower()
    print(s)
    cnt_p = cnt_y = 0
    for i in s:
        if i == 'p':
            cnt_p += 1
        elif i == 'y':
            cnt_y += 1
    if cnt_p == cnt_y:
        return True
    else:
        return False


if __name__ == "__main__":
    print(solution("pPoooy"))