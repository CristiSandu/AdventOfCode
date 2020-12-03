f = open("inputd3.txt", "r")

l = list()
matrix = list()
for x in f:
    l.append(x)
    matrix.append(l)
  #  print(l)
    l.clear()

for i in range(1,33,1):
    print(matrix[i])
    l.append(x)
    matrix[i] = l
    l.clear()

#for i in matrix:
#    print(i,"\n")