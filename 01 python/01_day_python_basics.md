# Python 基础语法速查

## 1. ✅ 缩进

代码块靠缩进决定，而不是大括号 `{}`。

```python
x = 10

if x > 0:
    print("正数")      # 缩进4空格
else:
    print("非正数")
```
> 注意：缩进必须保持一致（推荐每层用 4 个空格）

---

## 2. ✅ 变量声明

无需 `let`、`const`，直接写：

```python
name = "风中"
age = 28
pi = 3.14
is_dev = True
```
不用声明类型，自动推断类型。变量名推荐使用蛇形命名（如 `user_name`）。

---

## 3. ✅ print()：打印到控制台（相当于 console.log）

```python
print("Hello, Python")
```

也可以打印变量或表达式：

```python
x = 10
print("x =", x)
print("x 的平方是", x * x)
```

---

## 4. ✅ 基本数据类型

| 类型   | 示例         | 说明               |
| ------ | ------------ | ------------------ |
| str    | "hello"      | 字符串             |
| int    | 123          | 整数               |
| float  | 3.14         | 浮点数             |
| bool   | True/False   | 布尔值（首字母大写）|

```python
name = "风中"
score = 99.5
is_ok = True
```

---

## 5. ✅ 输入输出（input / print）

```python
name = input("请输入你的名字：")
print("你好,", name)
```

> `input()` 会返回一个字符串类型，要转换成数字用 `int()` 或 `float()`：

```python
age = int(input("你几岁了？"))
print("你明年就", age + 1, "岁了")
```

---

## 6. ✅ 注释

和 JS 一样，`#` 是单行注释：

```python
# 这是一个注释
print("Hello")  # 也可以写在后面
```

多行注释可以用三引号（不是官方推荐方式，但常用）：

```python
"""
这是一段
多行注释
"""
```

---

## 7. ✅ 字符串格式化（推荐 f-string）

```python
name = "风中"
age = 28

print(f"你好，{name}，你今年 {age} 岁了")
```
这是最现代、可读性最强的方式（Python 3.6+ 推荐）。

还可以嵌入表达式：

```python
print(f"明年你就 {age + 1} 岁了")
```