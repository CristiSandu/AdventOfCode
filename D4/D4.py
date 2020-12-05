import re

def function_verify(dictionaryFunc):
    ok = 0
   
    if len(dictionaryFunc) == 7:
        if "cid" not in dictionaryFunc:
            ok = 1                 
    elif len(dictionaryFunc) == 8:
        ok = 1
    # print(ok)
    if ok == 1:
        for key,value in dictionaryFunc.items():
            # print(key,value)
            if key == "hcl":
                if pattern_hcl.match(value) == False:
                    ok = 0
            elif key == "byr":
                if int(value) < 1920 or int(value) > 2002 :
                    ok = 0
            elif key == "iyr":
                if int(value) < 2010 or int(value) > 2020 :
                    ok = 0
            elif key == "eyr" :
                if int(value) < 2020 or int(value) > 2030 :
                    ok = 0
            elif key == "hgt" :
                list1 = value.split("c")
                if len(list1) == 2:
                    if int(list1[0]) < 150 or int(list1[0]) > 193 :
                        ok = 0
                else:
                    list2 = value.split("i")
                    if len(list2) == 2:
                        if int(list2[0]) < 59 or int(list2[0]) > 76 :
                            ok = 0
                    else: 
                        ok = 0
                    
            elif key == "ecl":
                if value not in ecl_dic:
                    ok = 0
            elif key == "pid":
                if pattern_pid.match(value) == False:
                    ok = 0

    if (ok == 1):
        return True
    else:
        return False

        

f = open("inputd4.txt", "r")

l = list()
pattern_hcl = re.compile("#([a-f0-9]{6})$")
pattern_pid = re.compile("[0-9]{9}$")
ecl_dic = {
    "amb" : 1,
    "blu" : 1,
    "brn" : 1,
    "gry" : 1,
    "grn" : 1,
    "hzl" : 1,
    "oth" : 1
}

for x in f:
    l.append(x)

dictionary = dict()
nr = 0

for x in l:
    spit_elem = x.split()
    if x == "\n" :
        if function_verify(dictionary) == True:
            nr += 1
            print(dictionary)

        dictionary.clear()
    else:
        for y in spit_elem:
            next_split = y.split(":")
            if next_split[0] not in dictionary:
                dictionary[next_split[0]] = next_split[1]

if function_verify(dictionary) == True:
    nr += 1

print(nr)