import time
import os


###########################################################################################
# 初始化界面和数据
os.system('cls' if os.name == 'nt' else 'clear')
n = 100          # 这个数值可以改
num = 0
i = 0
min_num = 0
start_time = 0
end_time = 0


###########################################################################################
# 获取0 - n（包括0 和 n）所有偶数，并输出和。


# 方法1  ->  获取所有数字并检查
print('偶数-方法1：')
start_time = time.time()
num = 0
for i in range(0, n + 1, 1):
    if i % 2 == 0:
        num += i
        print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {end_time - start_time} 秒")


# 方法2  ->  获取最小的偶数并逐步加2，最后到n
print('\n偶数-方法2：')
start_time = time.time()
num = 0
for i in range(0, n + 1, 1):
    if i % 2 == 0:
        min_num = i
        break
for i in range(min_num, n + 1, 2):
    num += i
    print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {end_time - start_time} 秒")


###########################################################################################
# 获取 0 - n（包括0和n）所有奇数，并输出和


# 方法1  ->  获取所有数字并检查
print('\n奇数-方法1：')
start_time = time.time()
num = 0
for i in range(0, n + 1, 1):
    if i % 2 != 0:
        num += i
        print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {end_time - start_time} 秒")


# 方法2  ->  获取最小的偶数并逐步加2，最后到n
print('\n奇数-方法2：')
start_time = time.time()
num = 0
for i in range(0, n + 1, 1):
    if i % 2 != 0:
        min_num = i
        break
for i in range(min_num, n + 1, 2):
    num += i
    print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {end_time - start_time} 秒")


###########################################################################################
# 获取 1 - n 所有数字的和


# 方法1  ->  获取所有数字并检查
print('\n所有数字和-方法1：')
start_time = time.time()
num = 0
for i in range(0, n + 1, 1):
    num += i
print(f' 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {end_time - start_time} 秒")