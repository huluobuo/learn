l_1 = input().split()
max_num = float(l_1[0])


for now_num in  l_1[1:]:
    if max_num < float(now_num):
        max_num = now_num
    # max_num = int(now_num) if int(now_num) > max_num else max_num


print(max_num)