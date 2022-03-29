def solution(phone_book):
    answer = True
    phone_book=sorted(phone_book)
    
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            answer = False
   
    return answer

if __name__=="__main__":
    print (solution(["119", "97674223", "1195524421"]))
