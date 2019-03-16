def checkedHnum():
    a = input("请输入数字")
    if len(a) % 2 == 0:
        print("该数字不是回文")
    else:
        print("长度",len(a))
        b = len(a) // 2
        mlist = a.split(a[b])

        klist = [a for a in mlist[1]]
        print(klist)
        klist.reverse()
        v = ""
        for a in klist:
            v+=a
        if mlist[0] == v:
            print("是回文数")
        else:
            print("不是回文数")
    pass
if __name__ == '__main__':
     checkedHnum()
