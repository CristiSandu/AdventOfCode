f = open("input.txt", "r")

l = list()
for x in f:
    l.append(int(x))

pair = list()
for x in l:
    for y in l:
        if x + y == 2020 :
            pair.append(tuple((x,y,0)))


out = pair[0][0]*pair[0][1]
print(out)


pair2 = list()
for x in l:
    for y in l:
        for z in l:
            if x + y + z == 2020 :
                pair2.append(tuple((x,y,z)))


out2 = pair2[0][0]*pair2[0][1]*pair2[0][2]
print(out2)
