def quick_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    else:
        pivot = num_list[0]
        lesser_nums = quick_sort([x for x in num_list[1:] if x <= pivot])
        greater_nums = quick_sort([x for x in num_list[1:] if x > pivot])
        return lesser_nums + [pivot] + greater_nums

def main():
    num_list = list(map(int, input("请输入数字：").split()))
    sorted_list = quick_sort(num_list)
    print("排序后的数字：", sorted_list)

if __name__ == "__main__":
    main()