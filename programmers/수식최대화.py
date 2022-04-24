#level2 2020 카카오 인턴십
from itertools import permutations
def solution(expression):
    answer = []
    op = ['+', '-', '*']
    for p in permutations(op):
        li = []
        for e in expression.split(p[0]):
            tmp = ["({})".format(i) for i in e.split(p[1])]
            li.append("({})".format(p[1].join(tmp)))
        result = "({})".format(p[0].join(li))
        answer.append(abs(eval(("".join(result)))))
    return max(answer)

if __name__ == "__main__":
    print(solution("100-200*300-500+20"))