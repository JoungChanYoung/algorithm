#level1 2021 kakao blind recruitment
from string import ascii_lowercase
def solution(new_id):
    li = list(ascii_lowercase)
    num = [str(i) for i in range(10)]
    answer = ''
    new_id = new_id.lower()
    flag = 1
    for i in range(len(new_id)):
        if new_id[i] and new_id[i] not in li + num + ['.','-','_']:
            new_id = new_id.replace(new_id[i]," ")
    
    new_id = new_id.replace(" ", "")
    flag = 1
    while flag:
        if ".." in new_id:
            new_id = new_id.replace("..",".")
        else:
            flag = 0
    flag = 1
    while flag:
        if new_id[0] == '.':
            if len(new_id) == 1:
                flag = 0
                new_id = ""
                continue
            new_id = new_id[1:]
        elif new_id[-1] == '.':
            new_id = new_id[:-1]
        else:
            flag = 0

    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]

    flag = 1
    while flag:
        if new_id[-1] == '.':
            if len(new_id) == 1:
                flag = 0
                new_id = ""
                continue
            new_id = new_id[:-1]
        else:
            flag = 0
    if len(new_id) <= 2:
        flag = 1
        while flag:
            new_id += new_id[-1]
            if len(new_id) == 3:
                flag = 0

    return new_id

if __name__ == "__main__":
    print (solution("a...a"))