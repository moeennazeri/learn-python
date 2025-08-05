# 🧠 آموزش کلاس‌ها و آبجکت‌ها در پایتون

# برنامه‌نویسی شی‌گرا (OOP) یعنی ما برنامه‌مون رو با استفاده از "کلاس" و "شیء" می‌سازیم.

# ----------------------------------------
# 🔸 تعریف کلاس

class Person:
    # متد __init__ سازنده‌ست، موقع ساخت شیء اجرا میشه
    def __init__(self, name, age):
        self.name = name      # ویژگی name
        self.age = age        # ویژگی age

    # متد یا تابع داخل کلاس
    def say_hello(self):
        print("سلام! من", self.name, "هستم و", self.age, "سالمه.")

# ----------------------------------------
# 🔸 ساخت شیء (Object) از روی کلاس

person1 = Person("مبین", 23)
person2 = Person("زهرا", 19)

# صدا زدن متد برای هر شیء
person1.say_hello()
person2.say_hello()

# دسترسی مستقیم به ویژگی‌ها
print(person1.name)   # مبین
print(person2.age)    # 19

# ----------------------------------------
# 🔸 کلاس با متد محاسباتی

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# ساخت مستطیل
rect1 = Rectangle(4, 6)

print("مساحت:", rect1.area())         # 24
print("محیط:", rect1.perimeter())     # 20

# ----------------------------------------
# 🔸 تغییر مقدار ویژگی

rect1.width = 10
print("مساحت جدید:", rect1.area())    # 60
