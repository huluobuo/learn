n, m = map(int, input("请输入两个数字：").split())
input_num_list = list(map(int, input(f"请输入{n}个数字：").split()))


i = 0
res = 0
while i < n:
    if input_num_list[i] == m:
        res += 1
    i += 1

print(res)

print(input_num_list.count(m))