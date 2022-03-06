def not_self_num(a): #self_num이 아닌수 저장
    global mat
    b = a
    for i in str(a): #자리수 더하기(a를 string으로 바꿔서 int로 한자리씩 받음)
        b = b + int(i)
    mat.append(b)
    
def is_self_num(a):
    if a in mat:
        return 0
    else:
        return 1
    
mat = [] #self_num이 아닌 수 matrix

for a in range(10000):
    a = a + 1    
    not_self_num(a)
    if is_self_num(a)==0: #self_num이 아닐때 skip
        continue
    else: #self_num일때 출력
        print(a)
   
