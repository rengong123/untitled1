import day04.quest1.p1 as p1
import day04.quest1.p2 as p2
import day04.quest1.p3 as p3
import day04.quest1.p4 as p4
if __name__ == '__main__':
    sdict = {1:"[1]输入用户姓名及性别，然后给出下列的提示",
             2:"[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
             3:"[3]注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
             4:"[4]从键盘输入一行字符串，判断是否是回文数（什么是回文数？例如，若n=1234321，则称n为回文数；若n=1234，则n不是回文数）"
             }
    mdict = {1:p1.checkedSex,
             2:p2.chekedNum,
             3:p3.checkedEmail,
             4:p4.checkedHnum
             }
    while True:
        for s in sdict:
            print(sdict[s])
        indexf = input("请选择服务")
        mdict[int(indexf)]()



