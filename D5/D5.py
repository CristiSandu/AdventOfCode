f = open("inputd5.txt", "r")
l = list()
id_list = list()
for x in f:
    l.append((x,0))

maxim = -1
for elem in l:   
    row = 0
    column =0

    for i in range(0,7):
        offset = 6 - i
        bit = -1
        if elem[0][i] == "F":
            bit = 0
        elif elem[0][i] == "B":
            bit = 1
        row += (bit << offset)    
    for j in range(7,10):
        offset = 2 - (j % 7)
        bit = 0
        if elem[0][j] == "R":
            bit = 0
        elif elem[0][j] == "L":
            bit = 1
        column += (bit << offset)

    mutiple = row * 8 + column
    id_list.append(mutiple)
    if (mutiple > maxim):
        maxim = mutiple 
print(maxim)

id_list.sort()
low_id = id_list[0]
print(low_id)
for x in range(low_id,mutiple):
    if not x in id_list:
        print(x)
        input()

