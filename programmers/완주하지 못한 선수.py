import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution(participant, completion):
    answer = ''
    dic_participant = {}
    dic_completion = {}

    for name in participant:
        if name in dic_participant.keys():
            dic_participant[name] = dic_participant[name] + 1
        else:
            dic_participant[name] = 0
        
    for name in completion:
        if name in dic_completion.keys():
            dic_completion[name] = dic_completion[name] + 1
        else:
            dic_completion[name] = 0

    for name in dic_participant.keys():
        if name in dic_completion.keys():
            if dic_completion[name] == dic_participant[name]:
                pass
            else:
                answer = name
    return answer


if __name__=="__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["mislav", "stanko", "ana"]
    solution(participant, completion)
