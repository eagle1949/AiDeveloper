class Person:
    def __init__(self, name, age): # 构造函数
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p = Person("Alice", 30)
print(p.greet())  # 输出: Hello, my name is Alice and I am