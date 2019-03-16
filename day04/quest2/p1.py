def checkedSex():
    # 输入用户姓名及性别，然后给出下列的提示：（20分）
    # XX先生你好 或 XX女士你好
    name = input("请输入用于姓名")
    sex = input("请输入性别")
    #定义空字典
    mdict = {}
    #判断是否枯涸条件
    if sex == "男" or sex == "man":
        #键值对赋值
        mdict[sex] = False
    else:
        mdict[sex] = True
        #通过键那到值
    if mdict[sex]:
        print("{name}:女士你好".format(name=name))
    else:
        print("{name}:男士你好".format(name=name))
if __name__ == '__main__':
    pass

