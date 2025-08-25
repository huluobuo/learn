# 接受一个字符串串并输出其长度（使用for循环）
input_str = input("请输入以逗号分隔的列表元素，例如 1,2,3: ")
l_1 = [x for x in input_str.split(',')]
res = 0
for i in l_1:
    res += 1
print(res)