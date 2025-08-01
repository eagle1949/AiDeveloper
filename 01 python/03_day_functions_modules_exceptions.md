# Python 入门 Day 3：函数 · 模块 · 异常处理

## 🎯 今日目标

- 掌握函数定义、参数、返回值
- 学会使用常见的 Python 标准库（`math`、`random`、`datetime`）
- 学会创建和导入模块
- 掌握 `try-except` 异常处理结构

---

## 1. 函数定义与使用

### 定义函数

```python
def say_hello(name):
    print(f"你好，{name}")
```

### 调用函数

```python
say_hello("风中")
```

### 带返回值的函数

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 输出 8
```

### 默认参数 & 命名参数

```python
def greet(name="朋友"):
    print(f"你好，{name}")

greet()           # 你好，朋友
greet("风中")     # 你好，风中
```

---

## 2. 常用标准库

### math 数学库

```python
import math

print(math.sqrt(16))     # 平方根
print(math.pow(2, 3))    # 幂
print(math.pi)           # π
```

### random 随机数

```python
import random

print(random.randint(1, 10))        # 随机整数
print(random.choice(["a", "b"]))    # 随机选择
print(random.random())              # 0~1 浮点数
```

### datetime 日期时间

```python
from datetime import datetime

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

---

## 3. 自定义模块导入

### 创建模块：mymath.py

```python
# 文件：mymath.py
def square(x):
    return x * x
```

### 使用模块

```python
# 文件：main.py
import mymath

print(mymath.square(5))  # 输出 25
```

也可以只导入部分内容：

```python
from mymath import square

print(square(6))  # 36
```

---

## 4. 错误处理 try-except

### 基本结构

```python
try:
    x = int(input("输入一个数字："))
    print(100 / x)
except ZeroDivisionError:
    print("不能除以 0")
except ValueError:
    print("请输入有效数字")
except Exception as e:
    print("发生错误：", e)
```

### 可选 finally

```python
try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("文件不存在")
finally:
    print("无论如何都会执行")
```