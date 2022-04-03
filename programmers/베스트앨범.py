#level3 hash
def solution(genres, plays):
    answer = []

    genres_dic = {}
    for i in range(len(genres)):
        if genres[i] in genres_dic.keys():
            genres_dic[genres[i]].append((plays[i], i))
        else:
            genres_dic[genres[i]] = [(plays[i], i)]
    while genres_dic:
        curr_genre = ""
        max_num = 0
        for key in genres_dic.keys():       
            sum_val = 0
            for i in range(len(genres_dic[key])):
                val, _ = genres_dic[key][i]
                sum_val += val            
            if max_num < sum_val:
                curr_genre = key
                max_num = sum_val
        tmp = sorted(genres_dic.pop(curr_genre),reverse=True)
        play_list=[]

        val = 0
        for i in range(2):
            if tmp:
                val_tmp, song_id = tmp.pop(0)                
                if val_tmp == val:
                    play_list.insert(0, song_id)
                else:
                    play_list.append(song_id)
                val = val_tmp
        answer += play_list
    return answer

if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic3", "pop2"], [500, 600, 500, 800, 2500]))