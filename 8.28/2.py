def quick_sort(num_list: list) -> list:
    if len(num_list) <= 1:
        return num_list
    else:
        pivot = num_list[0]
        lesser_nums = quick_sort([x for x in num_list[1:] if x <= pivot])
        greater_nums = quick_sort([x for x in num_list[1:] if x > pivot])
        return lesser_nums + [pivot] + greater_nums


def two_point_search(num_list: list, num: int) -> bool:
    left, right = 0, len(num_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == num:
            return True
        if num_list[mid] < num:
            left = mid + 1
        elif num_list[mid] > num:
            right = mid - 1
        else:
            return True
    return False


def main():
    num_list = list(map(int, input("请输入数字：").split()))
    sorted_list = quick_sort(num_list)
    print("排序后的数字：", sorted_list)
    num = int(input("请输入要查找的数字："))
    found = two_point_search(sorted_list, num)
    if found:
        print("存在")
    else:
        print("不存在")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("程序出错：", e)
    # main()
