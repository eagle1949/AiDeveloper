class Person:
    def __init__(self, name, age): # 构造函数
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p = Person("Alice", 30)
print(p.greet())  # 输出: Hello, my name is Alice and I am 30 years old.



# 继承与方法重写
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def say_hello(self):
        return f"Hello, I am {self.name} from {self.school}."

s = Student("Bob", 20, "XYZ University")
print(s.greet())      # 输出: Hello, my name is Bob and I am 20 years old.
print(s.say_hello())  # 输出: Hello, I am Bob from XYZ University.
