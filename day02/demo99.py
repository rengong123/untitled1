if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    for i in arr :
        for j in arr :
            a = str(i*j)
            print(str(i)+"*"+str(j)+"="+a.rjust(2),end=" ")

            if i == j:
                print()
                break

