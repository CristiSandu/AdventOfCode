f = open("inputd3.txt", "r")

l = list()
nr = 0
matrix = list()
for x in f:
    matrix.append(x)
    nr = nr + 1
size = len(matrix[0])
#print(nr,size)
nr = nr - 1

input_check = [(1,1),(3,1),(5,1),(7,1),(1,2)]
list_to_multiply = list()
for t1,t2 in input_check:
  y = 0
  x = 0
  nr_pomi = 0 

  while (x < nr):
      y +=t1
      x +=t2
      if (y > 30):
        y = (y - 30) - 1
      if (matrix[x][y] == "#"):
        nr_pomi += 1

  list_to_multiply.append(nr_pomi) 

rez = 1
for x in list_to_multiply:
  rez *= x
  print(x)

print(rez)
