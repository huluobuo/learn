import time

# 读取输入并分割成字符串列表
input_str = input().strip()
l_1 = input_str.split()

# 创建一个空列表来存储转换后的数值和对应的原始字符串（用于错误处理）
valid_numbers = []

for s in l_1:
    try:
        # 尝试将每个元素转换为浮点数，如果成功则保留原字符串
        num_val = float(s)
        valid_numbers.append((num_val, s))
    except ValueError:
        # 如果元素无法转换为数字，则打印警告并跳过该元素
        print(f"Warning: '{s}' is not a number and will be ignored.")
    except Exception as e:
        # 处理其他可能的异常，例如空输入或格式错误
        print("An error occurred:", e)

# 如果有有效数字，则找到最大数值对应的原始字符串（如果需要输出原格式）
if valid_numbers:
    max_num_val = max(valid_numbers, key=lambda x: x[0])[0]  # 最大浮点数值
    max_original_str = max(valid_numbers, key=lambda x: x[0])[1]  # 对应的原始字符串
    
    # 输出最大数值（作为浮点数）或其原始字符串形式，取决于需求
    print("Maximum value (as float):", max_num_val)
else:
    print("No valid numbers in the input.")


###################################################################
#     by:   deepseek-r1:8b
#     修改：huluobuo（某些小问题）
###################################################################