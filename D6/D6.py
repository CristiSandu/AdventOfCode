f = open("inputd6.txt", "r")

l = list()
for x in f:
    l.append(x)

suma = 0
suma2 = 0
nr = 0
dictionary = dict()

for x in l:
    if (x != "\n"):
        for y in x:
            if y not in dictionary:
                dictionary[y] = 1
            else:
                dictionary[y] +=1
        nr += 1
    else:
        suma += len(dictionary.keys()) - 1
        for z in dictionary:
            if (dictionary[z] == nr and z != "\n" ):
                suma2 += 1
        dictionary.clear()
        nr = 0

print("Prima parte: ",suma)
print("A doua parte: ",suma2)
