input_num = int(input("请输入数字："))
# 反转数字
a = str(input_num)
for i in range(len(a), 0, -1):
    print(a[i - 1], end="")
