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
print('偶数-方法1（for循环）：')
start_time = time.time()
num = 0
for i in range(0, n + 1, 1):
    if i % 2 == 0:
        num += i
        print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法2  ->  获取最小的偶数并逐步加2，最后到n
print('\n偶数-方法2（for循环）：')
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
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法3  ->  使用列表推导式
print('\n偶数-方法3（列表推导式）：')
start_time = time.time()
even_numbers = [i for i in range(0, n + 1) if i % 2 == 0]
num = sum(even_numbers)
for i in even_numbers:
    print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法4  ->  使用数学公式：等差数列求和
print('\n偶数-方法4（数学公式）：')
start_time = time.time()
# 偶数序列：0, 2, 4, 6, ..., n (如果n是偶数) 或 n-1 (如果n是奇数)
if n % 2 == 0:
    max_even = n
else:
    max_even = n - 1
count = (max_even // 2) + 1
num = count * (0 + max_even) // 2  # 等差数列求和公式：n*(a1+an)/2
for i in range(0, max_even + 1, 2):
    print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


###########################################################################################
# 获取 0 - n（包括0和n）所有奇数，并输出和


# 方法1  ->  获取所有数字并检查
print('\n奇数-方法1（for循环）：')
start_time = time.time()
num = 0
for i in range(0, n + 1, 1):
    if i % 2 != 0:
        num += i
        print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法2  ->  获取最小的偶数并逐步加2，最后到n
print('\n奇数-方法2（for循环）：')
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
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法3  ->  使用列表推导式
print('\n奇数-方法3（列表推导式）：')
start_time = time.time()
odd_numbers = [i for i in range(0, n + 1) if i % 2 != 0]
num = sum(odd_numbers)
for i in odd_numbers:
    print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法4  ->  使用数学公式：等差数列求和
print('\n奇数-方法4（数学公式）：')
start_time = time.time()
# 奇数序列：1, 3, 5, 7, ..., n (如果n是奇数) 或 n-1 (如果n是偶数)
if n % 2 != 0:
    max_odd = n
else:
    max_odd = n - 1
count = (max_odd + 1) // 2
num = count * (1 + max_odd) // 2  # 等差数列求和公式：n*(a1+an)/2
for i in range(1, max_odd + 1, 2):
    print(i, end=' ')
print(f'\n 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


###########################################################################################
# 获取 1 - n 所有数字的和


# 方法1  ->  获取所有数字并检查
print('\n所有数字和-方法1（for循环）：')
start_time = time.time()
num = 0
for i in range(0, n + 1, 1):
    num += i
print(f' 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法2  ->  使用sum()函数
print('\n所有数字和-方法2（sum函数）：')
start_time = time.time()
num = sum(range(0, n + 1))
print(f' 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法3  ->  使用数学公式：等差数列求和
print('\n所有数字和-方法3（数学公式）：')
start_time = time.time()
num = n * (n + 1) // 2  # 等差数列求和公式：n*(a1+an)/2
print(f' 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")


# 方法4  ->  使用列表推导式
print('\n所有数字和-方法4（列表推导式）：')
start_time = time.time()
numbers = [i for i in range(0, n + 1)]
num = sum(numbers)
print(f' 和为：{num}')
end_time = time.time()
print(f"本次运行使用了 {(end_time - start_time) * 1000:.2f} 毫秒")