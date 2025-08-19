import time

# ��ȡ���벢�ָ���ַ����б�
input_str = input().strip()
l_1 = input_str.split()

# ����һ�����б����洢ת�������ֵ�Ͷ�Ӧ��ԭʼ�ַ��������ڴ�����
valid_numbers = []

for s in l_1:
    try:
        # ���Խ�ÿ��Ԫ��ת��Ϊ������������ɹ�����ԭ�ַ���
        num_val = float(s)
        valid_numbers.append((num_val, s))
    except ValueError:
        # ���Ԫ���޷�ת��Ϊ���֣����ӡ���沢������Ԫ��
        print(f"Warning: '{s}' is not a number and will be ignored.")
except Exception as e:
    # �����������ܵ��쳣�������������ʽ����
    print("An error occurred:", e)

# �������Ч���֣����ҵ������ֵ��Ӧ��ԭʼ�ַ����������Ҫ���ԭ��ʽ��
if valid_numbers:
    max_num_val = max(valid_numbers, key=lambda x: x[0])[0]  # ��󸡵���ֵ
    max_original_str = max(valid_numbers, key=lambda x: x[0])[1]  # ��Ӧ��ԭʼ�ַ���
    
    # ��������ֵ����Ϊ������������ԭʼ�ַ�����ʽ��ȡ��������
    print("Maximum value (as float):", max_num_val)
else:
    print("No valid numbers in the input.")


###################################################################
#     by:   deepseek-r1:8b
###################################################################