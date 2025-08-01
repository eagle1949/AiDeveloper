
# 判断正负零
x = 10
if x > 0:
    print("正数")
elif x == 0:
    print("零")
else:
    print("非正数")


# 循环
for i in range(5):
    print(i)

arr = [1, 2, 3, 4, 5, 5, 5]

arr[0] = 10  # 修改数组第一个元素
print(arr[0])  # 访问数组第一个元素

arr.append(6)  # 添加元素到数组末尾
arr.append(7)  # 另一种添加元素的方法
arr.remove(3)  # 删除元素3
for i in arr:
    print(i)


# 元组
t = (1, 2, 3)
print(t[0])  # 访问元组元素

# 字典
d = {"name": "Alice", "age": 30}
print(d["name"])  # 访问字典元素
print(d["age"])   # 访问字典元素


for key in d:
    print(key, d[key])  # 遍历字典


# 集合
s = {1, 2, 3}
s.add(4)  # 添加元素
s.remove(2)  # 删除元素
for i in s:
    print(i)

# 去重
unique_list = list(set(arr))  # 将列表转换为集合再转换回列表
print(unique_list)  # 打印去重后的列表