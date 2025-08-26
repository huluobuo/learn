user = '123'
password = '456'
user_input = input("请输入用户名及密码（格式：用户名 密码）：").split()
if user_input[0] == user and user_input[1] == password:
    print("登录成功")
elif user_input[0] == user and user_input[1] != password:
    print("密码错误")
elif user_input[0] != user and user_input[1] == password:
    print("用户名错误")
else:
    print("用户名和密码错误")