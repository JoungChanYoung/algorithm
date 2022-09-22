
exist = 0
for x in range(4):
    s = input().split()
    if exist < exist + (int(s[1]) - int(s[0])):
        exist = exist + int(s[1]) - int(s[0])
print(exist)

