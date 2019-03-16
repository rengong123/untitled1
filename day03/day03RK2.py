if __name__ == '__main__':

    str = input("请输入一串字符")
    sstr = ""
    #一输入字符串长度开始遍历
    for i in range(0,len(str)) :
        #判断字符串中每个数据是否大于1 大于1则为重复
        if (str.count(str[i]))>1 :
            #如果新字符串中没有数据，就返回-1
            #则将数据存入新字符串中
            if (sstr.find(str[i]))==-1 :
                sstr +=str[i]

    print("原字符串是",str)
    for i in range(0,len(sstr)) :
        print("重复的字符串是", sstr[i],"重复了",str.count(sstr[i]),"次")

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
    #创建新列表
    qlist = []
    for k in klist :
        #去掉所有空格
        a = k.strip()
        #把所有去完空格的数据放在新列表中
        qlist.append(a)
    #把新列表存到集合中，去重
    qset = set(qlist)
    #创建字典
    zd ={}
    #遍历集合
    for q in qset :
     # 字典的键     每一个在列表中出现的次数
        zd[q] = qlist.count(q)
    print(zd)


if __name__ == '__main__':
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

    # 创建空列表
    qlist = []
    #循环去除空格
    for k in klist :
        a = k.strip()
        #将去完的数据放在空列表中
        qlist.append(a)
    #创建集合并把列表放入  去重
    qtest = set(qlist)
    #创建字典
    zd = {}
    #遍历集合
    for q in qtest :
     # 字典的键     等于每次取出来的值
     zd[q]=q

    print(zd)

