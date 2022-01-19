# MEE 1/18/22

def smash(lst):
    sentence = ""
    for i, v in enumerate(lst):
        if i == 0:
            sentence = sentence + v
        else:
            sentence = sentence + " " + v

    return sentence

x = smash(["school", "is", "very", "cool"])
print(x)