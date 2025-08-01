# 写入数据
with open('data.txt', 'w') as f:
    f.write('Hello, World!')

with open('data.txt', 'a') as f:
    f.write('\nThis is a new line.')


# 读取数据
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)

# 逐行读取
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())


# json 写入数据
import json
data = {    "name": "Alice",
    "age": 30,
}

with open('data.json', 'w') as f:
    json.dump(data, f)

# json 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data.get('name'))  # 输出: Alice
    print(data.get('age'))   # 输出: 30

# 命令行参数
import sys
if len(sys.argv) > 1:
    print("命令行参数:", sys.argv[1])   
    print("Hello,", sys.argv[1])
