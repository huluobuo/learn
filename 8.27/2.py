num_list = list(map(int, input("请输入数字：").split()))
fin_num_list = [num_list[0]]
for i in range(1 , len(num_list), 1):
    isok = False
    for j in range(0, len(fin_num_list), 1):
        """num_list[i]"""
        if num_list[i] >= fin_num_list[j]:
            fin_num_list.insert(j, num_list[i])
            isok = True
            break
    if not isok:
        fin_num_list.append(num_list[i])

print("  ".join(map(str, fin_num_list)))
