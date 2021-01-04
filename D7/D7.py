import re
f = open("inputd7.txt", "r")

l = list()
for x in f:
    l.append(x)
    # print(x)

lista_bagaje = list()
lista_bagaje_verify = list()

lista_bagaje.append("shiny gold")
lista_bagaje_verify.append("shiny gold")


nr = 0
while len(lista_bagaje) != 0:
    element_din_list = lista_bagaje.pop(0)
    element = element_din_list.split()
    print(element_din_list)
    for y in l:
        words = y.split()

        for x in words:
            if x == element[0] :
                if words.index(x) != 0 :
                    if words.index(x) + 1 <= len(words):
                        if words[words.index(x) + 1] == element[1]:
                            if lista_bagaje_verify.count(words[0] +" "+ words[1]) <= 1:
                                lista_bagaje.append(words[0] +" "+ words[1])
                                lista_bagaje_verify.append(words[0] +" "+ words[1])
                                print(lista_bagaje)
                                nr += 1

print(lista_bagaje)
print(nr)