#level3 dfs
from collections import deque
import sys
def solution(begin, target, words):
    answer = sys.maxsize
    q = deque()
    q.append(-1)

    visited = []
    cnt = -1
    while q:                
        n = q.pop()            
        cnt += 1
        visited.append(n)
        if n != -1:
            begin = words[n]

        if begin == target and cnt < answer:
            answer = cnt
            cnt = 0
        
        for k in range(len(words)):
            if k in visited:
                continue
            flag = 0
            for a,b in zip(begin, words[k]):
                if a != b:
                    flag += 1
            if flag == 1:
                q.append(words.index(words[k]))

    if answer == sys.maxsize:
        return 0
    return answer

if __name__ == "__main__":
    print(solution("hit",	"cog",	["hog", "hot", "dot", "dog", "lot","log", "cog"]	))