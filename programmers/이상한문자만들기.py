#level1
def solution(s):
    answer = ''
    li = []
    flag = 0
    for i in range(len(s)):
        if s[i] == " ":
            li.append(s[i])
            flag = 0
        elif not flag:
            li.append(s[i].upper())
            flag = 1
        elif flag:
            li.append(s[i].lower())
            flag = 0
    
    answer = "".join(li)
    return answer

if __name__ == "__main__":
    print(solution("    try  HEllo world"))