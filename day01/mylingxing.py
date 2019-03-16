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

     for i in n :
         for x in n :
             print(" ",end=" ")
             if i == x :
                 break
         for y in n :
             if i <y :
                 print("*",end=" ")
             if i <y-1 :
                 print("*",end=" ")
         print()
