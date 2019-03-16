if __name__ == '__main__':
    import random

if __name__ == '__main__':
        mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        # 通过id来证明该列表和新列表是否相同
        olist = [o for o in mlist if o % 2 == 0]
        print("olist =", olist)
        plist = [1, 2, 3, 4]
        ilist = [100, 200, 300, 400]
        jlist = [m + n for m in plist for n in ilist]
        print("no if ->", jlist)
        jlist = [m + n for m in plist if m % 2 == 0 for n in ilist]
        print("with if ->", jlist)
        olist = [m for m in mlist if m % 2 == 0]
        print("olist=", olist)
        jlist = [m + n for m in plist for n in ilist]
        print("jlist == ", jlist)
        jlist = [m + n for m in plist if m % 2 == 0 for n in ilist]
        print("plist == ", jlist)
        mlist = [['a', 'b'], ['e', 'f'], ['g', 'h']]
        nlist = [[m, n] for m, n in mlist]
        print(mlist)
        nlist = [[m, n] for m, n in mlist]
        print(mlist)
        nlist = [[m, n] for m, n in mlist]
        print(mlist)
        # 随机生成整数 1-100  10个随机数
        mlist = [random.randint(0, 100) for i in range(0, 10)]
        print(mlist)
        mlist = [random.randint(0, 100) for i in range(0, 30)]
        print(mlist)
        mlist = [random.randint(0, 200) for i in range(0, 20)]
        print(mlist)

if __name__ == '__main__':
        print("输入两个数字，计算除法")
        print("树入Q退出")
        while True:
            print("\t")
            fnum = input("first number")
            if fnum == "q":
                break

                snum = input("second number:")
                if snum == "q":
                    break
        try:
            f = open("good.text", "r")

            f.close()
        except Exception as e:
            print(e)
        else:
            print("excetion else")
        finally:
            print("finally")
        # 定义一个函数 如果参数是0 则手动抛出异常
        def mfun(v):
            if v == 0:
                raise Exception("good")
        try:
            mfun(0)
        except Exception as e:
            print("excetp->{0}".format(e))
            pass
        print("good")

        class myException(ValueError):
            pass

        try:
            print("brfor raise exception")
            raise myException
            print("after raise exception")
        except MyException as me:
            print("catch myException")
        except ValueError as ve:
            print("catch ValueError")
        except Exception as e:
            print("exception")
            print(e)
        class MyExcept(Exception):
            pass

            def show(self):
                print("hehe")
if __name__ == '__main__':
    mlist = ["gun","dan","u can u up"]
    mfile = open()
    mbool = mfile.writable()
    mwr = mfile.write("gundan")
    print("mwr = {mwrkey}".format(mwrkey =mwr))
    mfile.writelines(mlist)
    mfile.close()
    f = open(r"./test.txt","w")
    len = f.write("good good study , day day up")
    print(len)
    f.close()

if __name__ == '__main__':
    mfile = open(r"./test.txt")
    mbool = mfile.readable()
    print(mbool)
    val = mfile.read()
    mline = mfile.readline()
    mlist = mfile.readlines()
    mfile.close()

    f = open(r"./test.txt","r")
while True:
    fbuf = f.readline()
    if fbuf.__len__() == 0 :
        break
        print("line = {0}".format(fbuf))
        fpos = f.tell()
        print("fpos = {0}".format(fpos))
f.close()

with open(r"./test.txt","r")as f :
    while True:
        mlist = f.readline()
        if mlist == "" :
            break
        print(mline,end="")

with open(r"./test.txt","r")as f :
    pass
    fli = list(f)
    for l in fli :
        print(l,end="")

with open(r"./test.txt","r")as f :
    pass
    c = f.read()
    print(c)

with open(r"./test.txt",mode="r")as f :
    pass
    while True:
        c = f.read(1)
        if c == "":
            break
        print(c,end="")
import  time
with open(r"./test.txt",mode="r")as f :
    pass
    while True:
        c = f.read(1)
        if c == "":
            break
        print(c,end="")
        time.sleep(1)
with open(r"./test.txt",mode="r")as f :
    pass
    while True:
        c = f.read(1)
        if c == "":
            break
        print(c,end="")

with open(r"./test.txt",mode="r")as f :
    frstr = f.read(3)
    print(frstr)
    print("position = ",f.tell())

with open(r"./test.txt",mode="r")as f :
    while True:
        c = f.read(1)
        if c == "":
            break
        print("char = ",c)
        print("position = ",f.tell())
        print("*"*30)
with open(r"./test.txt",mode="r")as f :
    f.write("finally")
with open(r"./test.txt",mode="r")as f :
    mlist = ["u","can","u","up"]
    f.writelines(mlist)
import  pickle
with open(r"./test.txt",mode="r")as f :
    pass
    name = "simple"
    pickle.dump(name , f)
with open(r"./test.txt",mode="r")as f :
    pass
    name = pickle.load(f)
    print("name = ",name)
if __name__ == '__main__':
        print("输入两个数字，计算除法")
        print("树入Q退出")
        while True:
            print("\t")
            fnum = input("first number")
            if fnum == "q":
                break

                snum = input("second number:")
                if snum == "q":
                    break
        try:
            f = open("good.text", "r")

            f.close()
        except Exception as e:
            print(e)
        else:
            print("excetion else")
        finally:
            print("finally")
        # 定义一个函数 如果参数是0 则手动抛出异常
        def mfun(v):
            if v == 0:
                raise Exception("good")
        try:
            mfun(0)
        except Exception as e:
            print("excetp->{0}".format(e))
            pass
        print("good")

        class myException(ValueError):
            pass

        try:
            print("brfor raise exception")
            raise myException
            print("after raise exception")
        except MyException as me:
            print("catch myException")
        except ValueError as ve:
            print("catch ValueError")
        except Exception as e:
            print("exception")
            print(e)
        class MyExcept(Exception):
            pass

            def show(self):
                print("hehe")
if __name__ == '__main__':
    mlist = ["gun","dan","u can u up"]
    mfile = open()
    mbool = mfile.writable()
    mwr = mfile.write("gundan")
    print("mwr = {mwrkey}".format(mwrkey =mwr))
    mfile.writelines(mlist)
    mfile.close()
    f = open(r"./test.txt","w")
    len = f.write("good good study , day day up")
    print(len)
    f.close()

if __name__ == '__main__':
    mfile = open(r"./test.txt")
    mbool = mfile.readable()
    print(mbool)
    val = mfile.read()
    mline = mfile.readline()
    mlist = mfile.readlines()
    mfile.close()

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
    ndict=dict([('one',1),('tow',2),('three',3),('four',4),('five',5),('six',6)])
    for k,v in ndict.items():
        print('way4->ndict[{1}]={0}'.format(v,k))
    pass
    odict={k:v for k,v in mdict.items()}
    print('odict = ',odict)
    odict = {k: v for k, v in mdict.items()}
    print('odict = ', odict)
    pass
    pdict = {k:v for k,v in ldict.items() if v % 2 == 0 }
    print('pdict with option = ', pdict)
    pass
    print(ldict.__len__())
    mlen=len(ldict)
    print('len of dict = ',mlen)
    pass
    maxdict=max(ldict)
    print('max of  dict = ',maxdict)
    mindict =min(ldict)
    print('min of dict = ',mindict)
    pass
    di=ldict.items()
    print('type of items = ',type(di))
    print(di)
    pass
    nk=ldict.keys()
    print('type of keys = ',type(nk))
    print(nk)
    pass
    nk =ndict.values()
    print('type of values = ',type(nk))
    print(nk)
    pass
    abdict={'name':'lucky','age':'20'}
    abdict['addr']='beijing haidain'
    print(abdict)
    del abdict['addr']
    print(abdict)
    pass
    acdict={'name':'good',"age":"20"}
    del acdict
    #print(acdict)
    pass
    ng=ldict.get('tow')
    print('type of get = ',type(ng))
    print(ng)
    pass
    ldict.clear()
    print('after clear of dict = ',ldict)
    pass
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


