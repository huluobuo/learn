input_num_list = list(map(int, input("请输入数字：").split()))

# 交换第一位和最后一位
a = input_num_list[0]
input_num_list[0] = input_num_list[-1]
input_num_list[-1] = a

# 输出结果
for i in input_num_list:
    print(i, end="")