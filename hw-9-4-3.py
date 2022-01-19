# MEE 1/18/22


def count_e(word):
    num = 0
    for x in word:
        if x == "e":
            num += 1
    
    return num

m = count_e("me")
o = count_e("tree")
h = count_e("heeeee")
print(m,o,h)