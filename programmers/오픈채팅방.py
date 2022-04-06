#level2 2019 kakao blind recruitment

def solution(record):
    answer = []
    di = {}

    for i in range(len(record)):
        tmp = record[i].split(" ")
        command = tmp[0]
        uid = tmp[1]
        if command == "Enter":            
            di[uid] = tmp[2]
            answer.append(uid + "님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(uid + "님이 나갔습니다.")
        elif command == "Change":
            di[uid] = tmp[2]
    
    for i in range(len(answer)):
        answer[i] = answer[i].replace(answer[i].split(" ")[0], di[answer[i].split("님이")[0]] + "님이")
        
    return answer

if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))