import re
ecl_dic = {
        "amb" : 1,
        "blu" : 1,
        "brn" : 1,
        "gry" : 1,
        "grn" : 1,
        "hzl" : 1,
        "oth" : 1
    }

value2 = "brn"

if value2 not in ecl_dic:
    print("nu este")
else :
    print("este")
value = "z"
pattern_hcl = re.compile("^#([a-f0-9]{6})$")
if (pattern_hcl.match(value)):
    print("yes")
else :
    print("no")

value4 = "2022"
if (int(value4) < 2010 or int(value4) > 2020 ):
    print("No No")
else:
    print(value4)

