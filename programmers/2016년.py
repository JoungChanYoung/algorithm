#level1 연습문제

def solution(a, b): 
    #2016년 1월 1일은 금요일
    answer = ''

    li = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    tmp = (sum(days[:a-1]) + b) % 7
    answer = li[tmp-1]        
    return answer

if __name__ == "__main__":
    print(solution(5, 24))