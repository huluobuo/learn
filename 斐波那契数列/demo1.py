import matplotlib.pyplot as plt

class Demo():
    def __init__(self, long):
        self.a = 0
        self.b = 1
        self.c = 1
        self.round = 0
        self.long = long
        self.res_list = [self.a, self.b]
    
    def demo(self) -> list:
        self.round += 1
        self.c = self.a + self.b
        self.res_list.append(self.c)
        print(f'第{self.round}轮：上上个数：{self.a}，上个数：{self.b}，当前数：{self.c}')
        self.a, self.b = self.b, self.c
        if self.round >= self.long:
            return self.res_list
        else:
            return self.demo()

demo = Demo(30)
result = demo.demo()
print(f'最终结果：{result}')

# 使用plt绘制图表
plt.figure(figsize=(8, 4))
plt.plot(result, marker='o')
plt.title('斐波那契数列')
plt.xlabel('索引')
plt.ylabel('数值')
plt.grid(True)
plt.show()
