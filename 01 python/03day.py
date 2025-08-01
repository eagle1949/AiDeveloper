def sayName(name):
    print("Hello, " + name + "!")

sayName("Alice")


def add(x, y):
    return x + y

x = 5
y = 10  

result = add(x, y)
print(result)

# 默认参数
def greet(name="World"):
    print("Hello, " + name + "!")

greet()
greet("Alice")


# 标准库
import math
print(math.sqrt(16))  # 输出 4.0
print(math.pi)  # 输出 3.141592653589793


from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 格式化输出


from dayexport import max_of_two;

print(max_of_two(5, 10))
print(max_of_two(20, 15))

try:
    print(max_of_two("apple", "banana"))
except TypeError as e:
    print("Error:", e)
finally:
    print("Execution completed.")