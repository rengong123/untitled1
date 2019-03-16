import random
if __name__ == '__main__':
    mstr = "good good study , day day up"
    mindex = mstr.find("good")
    print(mindex)

    mcount = mstr.count("good")
    print(mcount)

    nstr = mstr.replace("good","gud")
    print(nstr)

    mlist = mstr.split(" ")
    print(mlist)

    mlist = mstr.split(" ",1)
    print(mlist)

    nstr = mstr.capitalize()
    print(nstr)

    mstr = "10"
    nstr = mstr.ljust(10,"-")
    print(nstr)

    mstr = "10"
    nstr = mstr.Rjust(10, "-")
    print(nstr)


    mlist = list()
    print(type(mlist))

    mlist.append("班长")
    print(mlist)

    mlist.insert(0,"学委")
    print(mlist)

    mlist.pop()
    print(mlist)

    del mlist
    print(mlist)

    mynum = [3,7,4,2]
    random.shuffle(mynum)
    print(mynum)

    mynum.sort(reverse=True)
    print(mynum)

    mynum.reverse()
    print(mynum)

    mlist = [1,2,3,4,"hehe",3.3]

    mlen = len(mlist)

    print(mlen)

    mlist = [1,2,3,4]
    for i in mlist :
        print(i)

    mlist[0] = 10
    for i in mlist :
        pass
        #print(i)

    mlist = [1, 2, 3, 4]
    nlist = mlist
    print("mlist id is {mlistid}".format(mlistid = id(mlist)))
    print("mlist id is {nlistid}".format(nlistid=id(nlist)))

    mlist = [1,2,3,4,5,6,7,8,9,0]
    print(id(mlist))
    del mlist[0]
    print(mlist)

    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    t=2
    print("in -> ",t in mlist)
    print("not in ->", t not in mlist)







