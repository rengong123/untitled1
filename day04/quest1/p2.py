import random
def chekedNum():
    slist = [random.randint(1,30) for i in range(0,10)]
    mlist = [random.randint(1,30) for i in range(0,15)]
    set1 = set(slist)
    print(set1)
    set2 = set(mlist)
    print(set2)
    nlist = set1 | set2
    print(nlist)
    pass
if __name__ == '__main__':
    pass
