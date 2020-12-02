f = open("inputd2.txt", "r")

l = list()

for x in f:
    l.append(x)

min_nr = 0
max_nr = 0
char_to_search = 'a'
string_to_search = ""
nr = 0
nr2 = 0
dictionary = dict()

for x in l: 
    y = x.split()
    z= y[0].split("-")
    min_nr = int(z[0])
    max_nr = int(z[1])
    char_to_search = y[1][0]
    string_to_search = y[2]
    if string_to_search[min_nr - 1] == char_to_search:
        if string_to_search[max_nr - 1] != char_to_search:
            nr2 += 1
    else:
        if string_to_search[max_nr - 1] == char_to_search:
            nr2 += 1 
    for t in string_to_search:
        if t not in dictionary:
            dictionary[t] = 1
        else:    
            dictionary[t] += 1
    if char_to_search not in dictionary:
       nr = nr + 0;
    else:
        if dictionary[char_to_search] >= min_nr and dictionary[char_to_search] <= max_nr :
            nr = nr + 1     
    dictionary.clear()

print(nr)
print(nr2)



