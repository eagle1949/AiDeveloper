print("Hello, World!")
x = 10
if x > 0:
    print("正数")      # 缩进4空格
else:
    print("非正数")
name = "Alice"
print (f"Hello, {name}!")  # 使用 f-string 格式化字符串
age = 30
print("年龄:", age)  # 打印年龄
pi = 3.14
print("圆周率:", pi)  # 打印圆周率
is_student = True
print("是否为学生:", is_student)  # 打印是否为学生
print(f"Hello, World! {name}!")  # 使用 f-string 格式化字符串



age = 30
print("年龄:", age)  # 打印年龄
age = age + 1
print("年龄:", age)  # 打印年龄

if age > 18:
    print("成年人")  # 如果年龄大于18岁
else:
    print("未成年人")

name = "Alice"
print(f"Hello, {name}!")  # 使用 f-string 格式化字符串

xiaoshu = 3.14
print("圆周率:", xiaoshu)  # 打印圆周率

is_student = True
print("是否为学生:", is_student)  # 打印是否为学生
is_student = False
print("是否为学生:", is_student)  # 打印是否为学生

if is_student:
    print("是学生") # 如果是学生
else:
    print("不是学生")