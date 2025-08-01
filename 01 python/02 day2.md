# Python 基础语法进阶

## 1. 条件判断（if / elif / else）

Python 的条件判断没有小括号 ()，没有花括号 {}，靠冒号 + 缩进：

```python
x = 10

if x > 0:
    print("正数")
elif x == 0:
    print("是零")
else:
    print("负数")
```
- `elif` 相当于 JS 的 `else if`（JS 里没有直接的等价写法）

---

## 2. 循环结构

### 2.1 for 循环（最常用）

```python
for i in range(5):
    print(i)
```
- `range(n)` 生成 0~n-1 的整数序列

#### 遍历列表

```python
fruits = ["苹果", "香蕉", "葡萄"]
for fruit in fruits:
    print(fruit)
```

### 2.2 while 循环

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

---

## 3. 列表（list）：有序、可变，支持索引和切片

```python
nums = [1, 2, 3, 4]

print(nums[0])       # 第一个元素
print(nums[-1])      # 最后一个元素
print(nums[1:3])     # 切片：索引1到2

nums.append(5)       # 添加元素
nums.remove(2)       # 删除元素
```

---

## 4. 元组（tuple）：有序、不可变（适合常量数据）

```python
point = (3, 5)
print(point[0])

# 元组可用于函数返回多个值
def get_position():
    return (10, 20)

x, y = get_position()
```

---

## 5. 字典（dict）：键值对，相当于 JS 的 object

```python
user = {
    "name": "风中",
    "age": 32
}

print(user["name"])
user["city"] = "深圳"

# 遍历字典
for key, value in user.items():
    print(f"{key} -> {value}")
```

---

## 6. 集合（set）：无序、无重复的元素集合

```python
s = {1, 2, 3}
s.add(4)
s.add(2)  # 自动去重

print(s)
```
可用于去重：

```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(list(unique))  # 转回列表
```