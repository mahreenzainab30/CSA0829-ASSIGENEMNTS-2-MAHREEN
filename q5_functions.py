
# Problem: Default list argument

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


a = add_item_buggy("Tea")
b = add_item_buggy("Vada")

print("Buggy output:")
print(a, b)


# Correct solution

def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


a = add_item("Tea")
b = add_item("Vada")

print("Correct output:")
print(a, b)


# Positional and keyword arguments

def student(name, age=19):
    print(name, age)


student("Arun")
student(name="Ravi", age=20)


# Returning multiple values

def bill(price):
    gst = price * 0.05
    total = price + gst
    return gst, total


gst, total = bill(100)
print("GST:", gst)
print("Total:", total)


# Local and global variables

x = 10

def show():
    global x
    x = 20
    print("Inside function:", x)


show()
print("Outside function:", x)
