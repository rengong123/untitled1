if __name__ == '__main__':
    mstr = "good good study , day day up"
    mindex =mstr.find("good",1)
    print(mindex)

    maindex = mstr.find("good",11,20)
    print(maindex)

    mstr = "good good study , day day up"
    mindex = mstr.index("good")
    print(mindex)
    mindex = mstr.index("good",1)
    print(mindex)
    mindex = mstr.index("good", 1,10)
    print(mindex)
    mstr = "good good study , day day up"
    mcount = mstr.count("good")
    print(mcount)
    mcount = mstr.count("good",1)
    print(mcount)
    mcount = mstr.count("good",1,10)
    print(mcount)
    mstr = "good good study , day day up"
    nstr = mstr.replace("good","gup")
    print(nstr)
    print(mstr)
    mstr = "good good study , day day up"
    mlist = mstr.split(" ")
    print(mlist)
    mlist = mstr.split(" ",1)
    print(mlist)
    mstr = "that was girl"
    nstr = mstr.capitalize()
    print(nstr)
    print(type(nstr))
    mstr = "u can u up , no zuo no die"
    mbool = mstr.startswith("u")
    print(mbool)
    mbool = mstr.startswith("c",2,4)
    print(mbool)



