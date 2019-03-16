if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    for i in arr :
        for j in arr :
            print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
            if i == j:
                print()
                break
