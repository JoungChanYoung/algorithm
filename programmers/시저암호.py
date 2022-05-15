#level1 
def solution(s, n):
    answer = ''
    for i in s:
        if i != " ":  
            if ord(i) <= ord('Z') and ord(i) + n > ord('Z'):
                i = chr(ord(i) + n - (ord('Z') - ord('A') + 1))
            elif ord(i) + n > ord('z'):
                i = chr(ord(i) + n - (ord('z') - ord('a') + 1))
            else:
                i = chr(ord(i)+n)
        answer += i
    return answer

if __name__ == "__main__":
    print(solution("a B zZaA", 2))