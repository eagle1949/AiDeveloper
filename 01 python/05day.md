# Python 入门 Day 5：面向对象 + 项目结构 + 实战项目

## 🎯 今日目标

- 理解类和对象，掌握 Python 的面向对象语法
- 理解继承、方法重写
- 学会组织 Python 项目的基本结构
- 实战构建一个 CLI 工具或 API 服务

---

## 🧱 1. 面向对象基础（OOP）

### 类的定义与使用

```python
class Person:
    def __init__(self, name, age):  # 构造函数
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"你好，我是 {self.name}，今年 {self.age} 岁")

p = Person("风中", 32)
p.say_hello()
```

### 继承与方法重写

```python
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def say_hello(self):
        print(f"我是学生 {self.name}，来自 {self.school}")

s = Student("小明", 18, "Python大学")
s.say_hello()
```

---

## 🗂️ 2. 项目结构设计

### 标准结构

```
my_project/
├── main.py            # 程序入口
├── modules/
│   ├── __init__.py
│   └── user.py        # 自定义类和函数
├── utils/
│   └── file_ops.py    # 工具模块
├── data/
│   └── users.json     # 数据存储
└── README.md
```

### 模块使用

```python
# modules/user.py
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"你好，{self.name}！")
```

```python
# main.py
from modules.user import User

u = User("风中")
u.greet()
```

---

## 🔧 3. 实战项目：CLI 用户管理工具

### 功能需求

- 添加用户（姓名、年龄）
- 列出用户
- 数据保存到 JSON

### 代码实现

```python
# user_tool.py
import sys, json, os

DB_FILE = "users.json"

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}

def load_users():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def add_user(name, age):
    users = load_users()
    user = User(name, age)
    users.append(user.to_dict())
    save_users(users)
    print("✅ 添加成功")

def list_users():
    users = load_users()
    for i, u in enumerate(users):
        print(f"{i+1}. {u['name']} - {u['age']}岁")

if len(sys.argv) < 2:
    print("用法: python user_tool.py add <姓名> <年龄> | list")
    sys.exit()

cmd = sys.argv[1]

if cmd == "add" and len(sys.argv) == 4:
    add_user(sys.argv[2], int(sys.argv[3]))
elif cmd == "list":
    list_users()
else:
    print("命令错误")
```

---

## 🌐 4. （进阶）构建一个简单 API 服务（基于 Flask）

### 安装 Flask

```bash
pip install flask
```

### 示例代码：app.py

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

### 测试方式（用 Postman 或 curl）：

```bash
curl -X POST http://localhost:5000/add_user -H "Content-Type: application/json" -d '{"name":"风中", "age":32}'
curl http://localhost:5000/users
```