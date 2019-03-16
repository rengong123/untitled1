if __name__ == '__main__':
      str = input("请输入:")
      #strs用来存储重复过的字符串
      strs = ""
      #字符串长度遍历
      for i in range(0,len(str)):
          #判断字符串在strr中是否重复
          if (str.count(str[i])>1) :
              #判断是否有字符已经存入
              #下标=-1就是没有字符   将字符存入strs
              if (strs.find(str[i])== -1) :
                  strs += str[i]

      print("原字符串是"+str)

      for i in range(0,len(strs)) :
          print("重复字符串是",strs[i],"出现了",str.count(strs[i]))





