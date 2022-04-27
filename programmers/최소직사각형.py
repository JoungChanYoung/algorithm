#level1 위클리챌린지

def solution(sizes):

    max_w = max_h = 0
    
    for  i in range(len(sizes)):
        w, h = sorted(sizes[i], reverse=True)
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
    
    return max_w*max_h

if __name__ == "__main__":
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))