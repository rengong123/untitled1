def checkedEmail():
    name = input("请输入你的用户名")
    if len(name) < 6 :
        print("姓名长度不能少于6位")
    else:
        email = input("请输入你的email")
        a = email.find("@")
        if a == -1 :
            print("邮件中不包含@")
        else:
            print("注册成功！用户名{name},邮箱为{email}".format(name=name,email=email))

if __name__ == '__main__':
    checkedEmail()