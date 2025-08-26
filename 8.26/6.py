#  斐波那契数列
# 方法1
input_num = int(input("请输入数字："))
fbnq_list = []
for i in range(1, input_num + 1):
    if i == 1:
        fbnq_list.append(1)
    elif i == 2:
        fbnq_list.append(1)
    else:
        fbnq_list.append(fbnq_list[i - 2] + fbnq_list[i - 3])

print(fbnq_list[-1])

# 方法2
a = 1
b = 1
c = 0
for i in range(1, input_num + 1):
    if i == 1:
        c = a
    elif i == 2:
        c = b
    else:
        c = a + b
        a = b
        b = c
print(c)
