# 自行车 --->  开锁上车 27s  -->  行程  ?s （3m/s）  -->  停车锁车 23s
# 步行   --->  ?s （1.2m/s）
# 输入一个整数（路程），判断是自行车快还是步行快

road = int(input("请输入路程："))
bick_time = 27 + road / 3 + 23
foot_time = road / 1.2
if bick_time < foot_time:
    print("自行车快")
elif bick_time > foot_time:
    print("步行快")
else:
    print("一样快")