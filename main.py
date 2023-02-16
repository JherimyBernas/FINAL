from tkinter import *


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


final1 = Tk()
final1.title("Data Structures and Algorithms")
final1.geometry("425x325")
number_tree = []


def btn_click(number):
    global expression
    expression += str(number)
    main_str.set(expression)


def btn_d():
    global expression
    expression = expression[:-1]
    main_str.set(expression)


def btn_enter():
    try:
        new_num = int(expression)
        if new_num in number_tree:
            raise ValueError
        if new_num == 0:
            raise ValueError
        if len(number_tree) == 10:
            raise ValueError
    except ValueError:
        exp_clear()
    else:
        number_tree.append(new_num)
        inputs_str.set(number_tree)
        exp_clear()


def exp_clear():
    global expression
    expression = ""
    main_str.set("")


expression = ""
main_str = StringVar()
inputs_str = StringVar()
result_str = StringVar()

dollar_sign = Label(final1, text="Enter a number:").place(x=50, y=20)
main_box = Label(final1, width=32, textvariable=main_str, borderwidth=3, relief="sunken", anchor="center")\
    .place(x=149, y=20)

button1 = Button(final1, text="1", width=4, height=2,  borderwidth=3, command=lambda: btn_click(1)).place(x=50, y=50)
button2 = Button(final1, text="2", width=4, height=2, borderwidth=3, command=lambda: btn_click(2)).place(x=90, y=50)
button3 = Button(final1, text="3", width=4, height=2, borderwidth=3, command=lambda: btn_click(3)).place(x=130, y=50)
button4 = Button(final1, text="4", width=4, height=2, borderwidth=3, command=lambda: btn_click(4)).place(x=50, y=92)
button5 = Button(final1, text="5", width=4, height=2, borderwidth=3, command=lambda: btn_click(5)).place(x=90, y=92)
button6 = Button(final1, text="6", width=4, height=2, borderwidth=3, command=lambda: btn_click(6)).place(x=130, y=92)
button7 = Button(final1, text="7", width=4, height=2, borderwidth=3, command=lambda: btn_click(7)).place(x=50, y=134)
button8 = Button(final1, text="8", width=4, height=2, borderwidth=3, command=lambda: btn_click(8)).place(x=90, y=134)
button9 = Button(final1, text="9", width=4, height=2, borderwidth=3, command=lambda: btn_click(9)).place(x=130, y=134)
button0 = Button(final1, text="0", width=4, height=2, borderwidth=3, command=lambda: btn_click(0)).place(x=90, y=176)
button_d = Button(final1, text="D", width=4, height=2, borderwidth=3, command=btn_d).place(x=130, y=176)

button_enter = Button(final1, text="Enter", width=11, borderwidth=3, command=btn_enter).place(x=200, y=60)
button_submit = Button(final1, text="Submit", width=11, borderwidth=3).place(x=200, y=88)
button_sum = Button(final1, text="Sum", width=11, borderwidth=3).place(x=200, y=116)
button_delete = Button(final1, text="Delete", width=11, borderwidth=3).place(x=200, y=144)
button_clear = Button(final1, text="Clear", width=11, borderwidth=3).place(x=200, y=172)

inputs = Label(final1, textvariable=inputs_str, width=46, borderwidth=2, relief="sunken", anchor="center")\
    .place(x=50, y=230)
result = Label(final1, textvariable=result_str, width=46, borderwidth=2, relief="sunken", anchor="center")\
    .place(x=50, y=265)

button_in = Button(final1, text="In-Order", width=11, borderwidth=3).place(x=289, y=60)
button_pre = Button(final1, text="Pre-Order", width=11, borderwidth=3).place(x=289, y=88)
button_post = Button(final1, text="Post-Order", width=11, borderwidth=3).place(x=289, y=116)
button_min = Button(final1, text="Min", width=11, borderwidth=3).place(x=289, y=144)
button_max = Button(final1, text="Max", width=11, borderwidth=3).place(x=289, y=172)
final1.mainloop()
