height = []
for x in range(9):
    height.append(int(input()))

flag = False
height_tmp = []
for x in range(len(height)):    
    for y in range(len(height)):
        if y == x:
            continue
        height_tmp = height[:]
        if x>y:
            height_tmp.pop(x)
            height_tmp.pop(y)
        else:
            height_tmp.pop(y)
            height_tmp.pop(x)
        if sum(height_tmp) == 100:
            flag = True
            break
    if flag == True:
        break


height_tmp.sort()
for x in range(len(height_tmp)):
    print(height_tmp[x])
