# MEE 1/18/22


def products(lst, num):
    for i, v in enumerate(lst):
        lst[i] = v * num
    
    print(lst)

products([1,2,3,4,5,6,7],3)
