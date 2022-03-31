#level1 2022 kakao blind recruitment

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]    
    report_flag = [[] for _ in range(len(id_list))]    

    for i in range(len(report)):
        person, target = report[i].split(" ")
        if id_list.index(target) not in report_flag[id_list.index(person)]:
            report_flag[id_list.index(person)].append(id_list.index(target))

    target_flag = [0 for _ in range(len(id_list))] 
    for i in range(len(report_flag)):
        tmp = report_flag[i]
        for j in tmp:
            target_flag[j] += 1
    for i in range(len(report_flag)):
        tmp = report_flag[i]
        for j in tmp:
            if target_flag[j] >= k:
                answer[i] += 1
    return answer

if __name__ == "__main__":
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 1))