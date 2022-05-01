#level1

def solution(arr):
    arr.remove(min(arr))
    
    if not arr:
        return [-1]
    return arr

if __name__ == "__main__":
    solution([4,3,2,1])