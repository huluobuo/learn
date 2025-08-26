# 使用for循环

input_num = int(input("请输入数字："))
res_list = []
for i in range(1, input_num + 1):
    if i % 3 == 0:
        res_list.append(i)

if res_list:
    for i in res_list:
        print(i, end=" ")
else:
    print(0)

####### ------------- ########

# 使用while循环
input_num = int(input("请输入数字："))
res_list = []
i = 1
while i <= input_num:
    if i % 3 == 0:
        res_list.append(i)
    i += 1
if res_list:
    for i in res_list:
        print(i, end=" ")
else:
    print(0)