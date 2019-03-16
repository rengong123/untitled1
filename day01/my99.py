if __name__ == '__main__':
    asd = [1,2,3,4,5,6,7,8,9]
    for i in asd :
        for j in asd :
            print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
            if i == j :
                print()
                break

if __name__ == '__main__':
    attr = [1,2,3]
    for i in attr :
        """左上空白三角形"""
        for j in attr :
            if i < j :
                print(" ",end=" ")
        """左上三角形"""
        for x in attr[0:i-1] :
            print("*",end=" ")
            """右上三角形"""
        for j in attr :
            print("*",end=" ")
            if i == j :
                print()
                break
    for i in attr :
        for l in attr :
            print(" ",end=" ")
            if i == l :
                break
        for k in attr :
            if i < k :
                print("*",end=" ")
            if i < k-1 :
                print("*",end=" ")

        print()



if __name__ == '__main__':
    arrt = [1,2,3,4,5]
    for i in arrt :
        for j in arrt :
            if i < j :
                print(" " ,end=" ")
        for l in arrt[0:i-1] :
            print("*",end=" ")
        for j in arrt :
            print("*" ,end=" ")
            if j == i :
                print()
                break
    for i in arrt:
        for x in arrt:
            print(" ", end=" ")
            if i == x:
                break
        for y in arrt:
            if i < y:
                print("*", end=" ")
            if i < y - 1:
                print("*", end=" ")
        print()