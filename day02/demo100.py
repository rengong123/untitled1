if __name__ == '__main__':
    arr = range(1,101)
    for i in arr :

        print(str(i).rjust(4),end=" ")

        if i % 10 ==0 :
            print()

