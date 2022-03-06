# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    #T==10 J==11 Q==12 K==13 A==14
    
    A = list(A)
    B = list(B)
    for i in range(len(A)):
        if A[i] == 'T':
            A[i] = '10'
        elif A[i] == 'J':
            A[i] = '11'
        elif A[i] == 'Q':
            A[i] = '12'
        elif A[i] == 'K':
            A[i] = '13'
        elif A[i] == 'A':
            A[i] = '14'

        if B[i] == 'T':
            B[i] = '10'
        elif B[i] == 'J':
            B[i] = '11'
        elif B[i] == 'Q':
            B[i] = '12'
        elif B[i] == 'K':
            B[i] = '13'
        elif B[i] == 'A':
            B[i] = '14'
    print(A)
    print(B)
    tmp = 0 #이긴횟수
    for i in range(len(A)):
        if int(A[i])>int(B[i]):
            tmp = tmp+1
    print(tmp)
    pass

solution("23A84Q","K2Q25J")
