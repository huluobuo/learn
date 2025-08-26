year = int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Yes")
else:
    print("No")

# 简化版
# print("Yes") if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else print("No")