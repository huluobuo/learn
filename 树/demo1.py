import tkinter as tk
from tkinter import ttk
# 创建一个简单的二叉树节点实例
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# GUI 窗口类
class TreeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("二叉树可视化")
        self.geometry("700x500")
        self.resizable(False, False)

        # 左侧控制面板
        control_frame = ttk.Frame(self, padding=10)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)

        # 手动输入树结构
        ttk.Label(control_frame, text="输入节点值（空格分隔）:").pack(anchor=tk.W)
        self.entry_nodes = ttk.Entry(control_frame, width=20)
        self.entry_nodes.pack(pady=5)

        ttk.Button(control_frame, text="生成二叉树", command=self.build_tree).pack(pady=5)

        ttk.Separator(control_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)

        ttk.Button(control_frame, text="打印树结构", command=self.print_tree_gui).pack(pady=5)
        ttk.Button(control_frame, text="前序遍历", command=self.preorder_gui).pack(pady=5)
        ttk.Button(control_frame, text="节点总数", command=self.count_nodes_gui).pack(pady=5)
        ttk.Button(control_frame, text="最大深度", command=self.max_depth_gui).pack(pady=5)

        # 右侧结果显示
        self.result_text = tk.Text(self, width=50, height=25)
        self.result_text.pack(side=tk.RIGHT, padx=10, pady=10)

        # 默认树
        self.root = None
        self.build_default_tree()

    def build_default_tree(self):
        # 默认示例树
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.left = TreeNode(6)
        self.root.right.right = TreeNode(7)

    def build_tree(self):
        # 从输入框读取节点值，按层序构建二叉树
        values = self.entry_nodes.get().strip().split()
        if not values:
            self.clear_result()
            self.insert_result("请输入节点值！")
            return
        nodes = [TreeNode(int(v)) if v != "None" else None for v in values]
        if not nodes:
            self.root = None
            return
        self.root = nodes[0]
        queue = [self.root]
        i = 1
        while queue and i < len(nodes):
            current = queue.pop(0)
            if current:
                if i < len(nodes):
                    current.left = nodes[i]
                    queue.append(nodes[i])
                    i += 1
                if i < len(nodes):
                    current.right = nodes[i]
                    queue.append(nodes[i])
                    i += 1
        self.clear_result()
        self.insert_result("二叉树已生成！")

    def clear_result(self):
        self.result_text.delete(1.0, tk.END)

    def insert_result(self, text):
        self.result_text.insert(tk.END, text + "\n")

    # 可视化二叉树结构
    def print_tree(self, node, prefix="", is_left=True):
        if node is not None:
            line = prefix + ("|-- " if is_left else "`-- ") + str(node.val)
            self.insert_result(line)
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, prefix + ("|   " if is_left else "    "), True)
                if node.right:
                    self.print_tree(node.right, prefix + ("|   " if is_left else "    "), False)

    def print_tree_gui(self):
        self.clear_result()
        if self.root:
            self.insert_result("二叉树结构如下：")
            self.print_tree(self.root)
        else:
            self.insert_result("树为空！")

    # 前序遍历打印节点值
    def preorder(self, node):
        if node:
            self.insert_result(str(node.val) + " ")
            self.preorder(node.left)
            self.preorder(node.right)

    def preorder_gui(self):
        self.clear_result()
        if self.root:
            self.insert_result("前序遍历结果：")
            self.preorder(self.root)
        else:
            self.insert_result("树为空！")

    # 计算树的节点总数
    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def count_nodes_gui(self):
        self.clear_result()
        if self.root:
            self.insert_result("节点总数： " + str(self.count_nodes(self.root)))
        else:
            self.insert_result("树为空！")

    # 计算树的最大深度
    def max_depth(self, node):
        if not node:
            return 0
        return 1 + max(self.max_depth(node.left), self.max_depth(node.right))

    def max_depth_gui(self):
        self.clear_result()
        if self.root:
            self.insert_result("树的最大深度： " + str(self.max_depth(self.root)))
        else:
            self.insert_result("树为空！")

# 启动 GUI
if __name__ == "__main__":
    app = TreeApp()
    app.mainloop()
