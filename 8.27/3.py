num_list = list(map(int, input("请输入数字：").split()))
bucket_list = list(0 for i in range(11))
for i in range(0, len(num_list), 1):
    bucket_list[num_list[i]] += 1

for i in range(len(bucket_list)):
    if bucket_list[i] != 0:
        print(f"{(str(i) + ' ') * bucket_list[i]}", end="")
