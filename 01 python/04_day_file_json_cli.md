# Python 入门 Day 4：文件读写 + JSON + 命令行项目

## 🎯 今日目标

- 学会使用 Python 进行文件操作（读/写/追加）
- 掌握 JSON 数据的读取与写入
- 了解如何处理命令行参数
- 实战一个简单的命令行小工具（如记账本或抽签器）

---

## 📁 1. 文件读写

### 写入文件（覆盖模式）

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
```

### 追加写入

```python
with open("data.txt", "a", encoding="utf-8") as f:
    f.write("再来一行。\n")
```

### 读取文件

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

### 逐行读取

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

## 🔄 2. JSON 数据处理

### Python → JSON 写入文件

```python
import json

data = {"name": "风中", "age": 32}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

### JSON 文件 → Python 读取

```python
with open("user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user["name"])
```

---

## 🧰 3. 命令行参数

### 使用 sys.argv

```python
import sys

print("命令行参数：", sys.argv)

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"你好，{name}！")
```

**执行方式示例：**

```bash
python greet.py 风中
# 输出：你好，风中！
```

---

## 🎯 4. 实战项目：简单记账工具（命令行）

### 功能说明

- 添加一笔记录
- 查看所有记录
- 存储在 records.json

### 代码示例：budget.py

```python
import sys, json, os

filename = "records.json"

def load():
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save(data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_record(amount, category):
    records = load()
    records.append({"amount": amount, "category": category})
    save(records)
    print("✅ 已添加")

def show_records():
    records = load()
    for i, r in enumerate(records):
        print(f"{i+1}. {r['category']} - {r['amount']} 元")
    print("共计：", sum(r['amount'] for r in records), "元")

# 命令行处理
if len(sys.argv) < 2:
    print("用法: python budget.py add <金额> <分类> | list")
    sys.exit()

command = sys.argv[1]

if command == "add" and len(sys.argv) == 4:
    amount = float(sys.argv[2])
    category = sys.argv[3]
    add_record(amount, category)
elif command == "list":
    show_records()
else:
    print("命令错误。示例: python budget.py add 50 早餐")
```

### 使用示例

```bash
python budget.py add 20 午餐
python budget.py add 35 交通
python budget.py list
```