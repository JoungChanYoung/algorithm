#평균점수보다 큰 학생 비율출력
'''for example
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''
test_case = input()

for i in range(int(test_case)):
    temp = input()
    student_num = temp.split(" ")[0]
    score_list = temp.split(" ")[1:]
    score_list = [int (i) for i in score_list] #2int
    avg = sum(score_list)/int(student_num)
    temp3 = 0
    for k in range(len(score_list)):
        if int(score_list[k])>avg:
            temp3 = temp3 + 1
    rate = temp3/len(score_list)
    print("{:.3%}".format(rate))
