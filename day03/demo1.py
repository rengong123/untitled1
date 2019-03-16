import day03.demo2
if __name__ == '__main__':
    mdict = {"name":"good","age":"18"}
    ndict = dict()
    print(type(mdict))
    print(type(ndict))

    mdict = {"name": "good", "age": "18",("addr"):"gun"}
    print(mdict)
    mdict = {"one" :1,"two":2,"three":3}
    print("create not null way1->type=",mdict)

    mdict = dict({"one":1,"two":2,"three":3})
    print("create not null way2->type=", mdict)

    mdict = {"name": "good", "age": "18"}
    mdict["addr"] = "beijing"
    print(mdict)

    mdict = {"name": "good", "age": "18", "addr": "beijing"}
    strdict = str(mdict)
    print(type(strdict))
    print("strdict = ",strdict)

    mdict = {"name": "good", "age": "18", "addr": "beijin"}
    strdict = len(mdict)
    print(strdict)

    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]

    qlist = []
    for k in klist :
         a =k.strip()
         qlist.append(a)

    qset = set(qlist)
    zd = {}

    for q in qset :
        zd[q] = qlist.count(q)
    print(zd)

    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]




    qlist = []
    for k in klist:
        a = k.strip()
        qlist.append(a)

    qset = set(qlist)
    zd = {}

    for q in qset:
        zd[q] = q
    print(zd)

if __name__ == '__main__':
    di = ndict.items()
    print("type of items = ",type(di))
    print(di)

    nk = ndict.keys()
    print("type of keys = ",type(nk))
    print(nk)

    nk = ndict.values()
    print("type of values = ",type(nk))
    print(nk)

    mdict = {"name": "good", "age": "18"}
    mdict["addr"] = "beijing"
    print(mdict)
    del mdict["addr"]
    print(mdict)

    ng = ndict.get("two")
    print("type of get = ",type(ng))
    print(ng)

    ndict.clear()
    print("after clear of dict = ",ndict)

    mlanguage = {"j":"java","c":"c","p":"python"}
    for l in sorted(mlanguage.keys()) :
        print(l)
        print(mlanguage[l])

    for v in sorted(mlanguage.values()) :
        print(v)

    mlist = list(range(1,11))
    print("mlist = {mlistkey}".format(mlistkey=mlist))

    mlist = list()
    for i in range(1,11) :
        mlist.append(i**2)
    print(mlist)


    mlist = [i**2 for i in range(1,11)]
    print("mlist = {mlistkey}".format(mlistkey=mlist))

    mlist = list()
    for i in range(1, 11):
        if i % 2 ==0 :
            mlist.append(i ** 2)
    print(mlist)

    mlist = [i ** 2 for i in range(1, 11) if i % 2 == 0]
    print("mlist = {mlistkey}".format(mlistkey=mlist))

    mdict = {"name": "good", "age": "18"}
    ndict = dict()
    print(type(mdict))
    print(type(ndict))
    mdict = {"name": "good", "age": "18", ("addr"): "gun"}
    print(mdict)
    mdict = {"one": 1, "two": 2, "three": 3}
    print("create not null way1->type=", mdict)
    mdict = dict({"one": 1, "two": 2, "three": 3})
    print("create not null way2->type=", mdict)

    mlist = list()
    print(type(mlist))

    mstr = "good good study , day day up"
    mindex = mstr.find("good")
    print(mindex)

    mcount = mstr.count("good")
    print(mcount)

    nstr = mstr.replace("good", "gud")
    print(nstr)

    mlist = mstr.split(" ")
    print(mlist)

    mlist = mstr.split(" ", 1)
    print(mlist)

    nstr = mstr.capitalize()
    print(nstr)

    mstr = "10"
    nstr = mstr.ljust(10, "-")
    print(nstr)

    # mstr = "10"
    # nstr = mstr.Rjust(10, "-")
    # print(nstr)

    mlist = list()
    print(type(mlist))

    mlist.append("班长")
    print(mlist)

    mlist.insert(0, "学委")
    print(mlist)

    mlist.pop()
    print(mlist)

    # 导入随机数生成器用到的包
    import random

    if __name__ == '__main__':
        # 随机从给定范围取一个整数
        val = random.randint(1, 2)
        print(val)

        # 从给定序列中随机选择一个数
        val = random.choice(range(3))
        print("val = {val}".format(val=val))

        # 数据源
        mstr = "abcdefghijklmnopqrstuvwxyz"

        # 临时存储变量
        tstr = ""

        # 循环三次，相当于控制循环次数，从数据源中取出三个字符
        for i in range(3):
            # 随机从数据源中取出一个字符
            v = random.choice(mstr)

            # 追加到临时变量
            tstr += v

        print(tstr)

    # 导入随机数生成器用到的包
    import random

    if __name__ == '__main__':
        # 从0到9随机生成一个整数
        rval = random.randrange(0, 10, 1)

        print("val = {rval}".format(rval=rval))

    # 导入随机数生成器用到的包
    import random

    if __name__ == '__main__':
        # 数据源
        mstrs = ["hehe", "hoho", "heihei"]

        # 打印打乱顺序前的数据源
        print("before {0}".format(mstrs))

        # 对数据源执行顺序打乱
        random.shuffle(mstrs)

        # 打印打乱顺序后的数据源
        print("after {0}".format(mstrs))

        print(random.uniform(3, 4))

        # random.randrange()

if __name__ == '__main__':
            myarr = [1, 2, 3, 4, 5]

            for m in myarr:
                if m == 3:
                    continue
                print(m)

if __name__ == '__main__':

            myarr = [[1, 2, 3], [1, 2, 3]]
            for i in myarr:
                for j in i:
                    print(j)

if __name__ == '__main__':
            mage = input("your age")
            print(type(mage))
            nage = int(mage)
            print(type(nage))

if __name__ == '__main__':
            myarr = [1, 2, 3, 4, 5]

def regUser (name,pwd) :
        print("name = {0}".format(name))
        print("pwd = {0}".format(pwd))
regUser(pwd="1234",name="hehe")

def rsgUser (name,pwd="000") :
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))
rsgUser(name="hehe")

def regUser (name,pwd,nakeName = "") :
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))
regUser(pwd="123",name="hehe")
regUser(pwd="123",name="hehe",nakeName="sha")
#按照关键词传参的方式调用函数
def regUser (name,pwd,nakeName = "") :
    if nakeName :
        user = {"name":name,"pwd":pwd,"nakeName":nakeName}
    else:
        user={"name":name,"pwd":pwd}
    return user
u = regUser("good","4321",nakeName="gg")
print(u)
#该函数接受一个列表数据
def getUser(names) :
    for n in names :
        print(n)
names =["good","luck","to","me"]
getUser(names)

def getUser(names) :
    names.append("gun")
if __name__ == '__main__':
    names=["good","luck","to","me"]
    getUser(names)
    print(names)

#定义一个函数，该函数能接受一个列表数据
#注意在函数中对该列表参数进行了修改
def getUser(names) :
    names.append("gun")

if __name__ == '__main__':
    names=["good","luck","to","me"]
    getUser(names[:])
    print(names)



print(day03.demo2.qwe())
print(day03.demo2.oo())
print(day03.demo2.pp())





