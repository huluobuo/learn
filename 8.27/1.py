def bubble_sort(num_list) -> list:
    for i in range(len(num_list) - 1):
        swapped = False
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swapped = True
        if not swapped:
            break
    return num_list


def main():
    num_list = list(map(int, input("请输入数字：").split()))
    print(" ".join(map(str, bubble_sort(num_list))))


if __name__ == "__main__":
    main()
