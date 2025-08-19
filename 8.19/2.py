a,b,c = input().split()
max_num = a


for now_num in  [b, c]:
    if max_num < float(now_num):
        max_num = now_num
    # max_num = int(now_num) if int(now_num) > max_num else max_num


print(max_num)