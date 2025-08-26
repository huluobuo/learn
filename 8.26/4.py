weight = float(input("请输入包裹的重量（单位：千克）："))
if weight <= 15:
    money = round(weight * 6)
else:
    money = 15 * 6 + round((weight - 15) * 9)
print(f"包裹的费用为： {money}  元")
