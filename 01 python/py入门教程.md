# Python 零基础到实战 6 天全攻略

---

## 第一天：基础语法速查

### 1. 缩进与代码块

```python
x = 10
if x > 0:
    print("正数")
else:
    print("非正数")
```
> 推荐每层用 4 个空格

### 2. 变量声明与类型

```python
name = "风中"
age = 28
pi = 3.14
is_dev = True
```

### 3. print 输出

```python
print("Hello, Python")
print(f"你好，{name}，你今年 {age} 岁了")
```

### 4. 输入 input

```python
name = input("请输入你的名字：")
age = int(input("你几岁了？"))
```

### 5. 注释

```python
# 单行注释
"""
多行注释
"""
```

---

## 第二天：数据类型与流程控制

### 1. 条件判断

```python
if x > 0:
    print("正数")
elif x == 0:
    print("零")
else:
    print("负数")
```

### 2. 循环

```python
for i in range(5):
    print(i)
while x < 5:
    print(x)
    x += 1
```

### 3. 列表、元组、字典、集合

```python
nums = [1, 2, 3]
point = (3, 5)
user = {"name": "风中", "age": 28}
s = {1, 2, 3}
```

### 4. 遍历与去重

```python
for fruit in fruits:
    print(fruit)
unique = set([1,2,2,3])
print(list(unique))
```

---

## 第三天：函数、模块、异常处理

### 1. 函数定义与调用

```python
def say_hello(name):
    print(f"你好，{name}")
say_hello("风中")
```

### 2. 标准库

```python
import math, random, datetime
print(math.sqrt(16))
print(random.randint(1, 10))
print(datetime.datetime.now())
```

### 3. 自定义模块

```python
# mymath.py
def square(x):
    return x * x
# main.py
import mymath
print(mymath.square(5))
```

### 4. 异常处理

```python
try:
    x = int(input("输入一个数字："))
    print(100 / x)
except ZeroDivisionError:
    print("不能除以 0")
except Exception as e:
    print("发生错误：", e)
```

---

## 第四天：文件读写、JSON、命令行

### 1. 文件操作

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

### 2. JSON 读写

```python
import json
data = {"name": "风中", "age": 28}
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
with open("user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
```

### 3. 命令行参数

```python
import sys
if len(sys.argv) > 1:
    print("命令行参数：", sys.argv[1])
```

### 4. 实战项目：记账工具

```python
# budget.py
import sys, json, os
filename = "records.json"
def load(): ...
def save(data): ...
def add_record(amount, category): ...
def show_records(): ...
```

---

## 第五天：面向对象、项目结构、实战项目

### 1. 类与对象

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"你好，我是 {self.name}，今年 {self.age} 岁")
```

### 2. 继承与方法重写

```python
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    def say_hello(self):
        print(f"我是学生 {self.name}，来自 {self.school}")
```

### 3. 项目结构设计

```
my_project/
├── main.py
├── modules/
│   └── user.py
├── utils/
│   └── file_ops.py
├── data/
│   └── users.json
└── README.md
```

### 4. CLI 用户管理工具

```python
# user_tool.py
class User: ...
def load_users(): ...
def save_users(users): ...
def add_user(name, age): ...
def list_users(): ...
```

### 5. 简单 API 服务（Flask）

```python
from flask import Flask, request, jsonify
app = Flask(__name__)
users = []
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"msg": "用户添加成功"})
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)
if __name__ == "__main__":
    app.run(port=5000)
```

---

## 第六天：第三方库、打包、GPT 应用

### 1. requests —— 网络请求

```python
import requests
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
```

### 2. pillow —— 图像处理

```python
from PIL import Image
img = Image.open('example.jpg')
img = img.resize((100, 100))
img.save('resized.jpg')
```

### 3. rich —— 命令行美化

```python
from rich.console import Console
console = Console()
console.print("Hello [bold magenta]World[/bold magenta]!", style="bold green")
```

### 4. Python 打包为可执行脚本

```bash
pip install pyinstaller
pyinstaller your_script.py --onefile
```
- 加 logo 图标：`--icon=icon.ico`
- 隐藏控制台窗口：`--windowed`

### 5. GPT API 应用

```python
import openai
openai.api_key = "你的API Key"
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "写一个关于AI的故事"}
    ]
)
print(response['choices'][0]['message']['content'])
```
- 推荐搭配 requests、异常处理、GUI

---

## 每日任务建议

| 模块      | 目标                         | 推荐时长 |
| --------- | ---------------------------- | -------- |
| requests  | 熟练调用 API，如 GitHub 或天气接口 | 30min    |
| pillow    | 把一张图片批量处理并保存           | 30min    |
| rich      | 美化终端输出结果                   | 15min    |
| 打包      | 学会使用 pyinstaller              | 20min    |
| GPT API   | 成功调用并获取结果                 | 30min    |

---

> 本文档适合零基础到实战，建议每天按模块练习，配合项目实践，快速掌握 Python 开发技