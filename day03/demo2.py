if __name__ == '__main__':
     n = [1, 2, 3, 4, 5]
     for i in n :
         for j in n :

             if i < j :
                 print("  ",end = "")

         for x in n[0:i-1] :
             print("*",end = " ")

         for j in n :
             print("*",end = " ")
             if j == i :
                 print()
                 break
if __name__ == '__main__':

    arr = [1,2,3,4,5,6,7,8,9]
    for i in arr :
        for j in arr :
            a = str(i * j)

            print(str(i)+"*"+str(j)+"="+a.rjust(2),end=" ")
            if i  == j :
                print()
                break

if __name__ == '__main__':
    arr = range(1,101)
    for i in arr :
        print(str(i).rjust(4),end=" ")
        if i % 10 == 0 :
            print()



def oo ():

    arrt = [1,2,3,4]
    for i in arrt :
        for j in arrt :
            if i < j :
                print(" ",end=" ")
        for x in arrt[0:i-1]:
            print("*",end=" ")
        for j in arrt :
            print("*",end=" ")
            if i == j :
                print()
                break
    for i in arrt:
        for l in arrt:
            print(" ", end=" ")
            if i == l:
                break
        for k in arrt:
            if i < k:
                print("*", end=" ")
            if i < k - 1:
                print("*", end=" ")

        print()
print(oo())


def qwe ():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in arr:
        for j in arr:
            a = str(i * j)

            print(str(i) + "*" + str(j) + "=" + a.rjust(2), end=" ")
            if i == j:
                print()
                break
print(qwe())

def pp():
    x = int(input("请输入"))
    for i in range(x):
        print(" " * (x - 1), end="")
        print(" *" * i, sep=" ")
print(pp())


