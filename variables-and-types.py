#  آموزش متغیرها و انواع داده‌ها در پایتون

# در پایتون برای ساخت متغیر نیازی به تعریف نوع (مثل int یا string) نداریم.
# فقط اسم متغیر را می‌نویسیم و مقدار می‌دهیم.

# 🔸 نوع رشته‌ای (String)
name = "مبین"
print("نام:", name)  # خروجی: نام: مبین

# 🔸 نوع عدد صحیح (Integer)
age = 22
print("سن:", age)  # خروجی: سن: 22

# 🔸 نوع اعشاری (Float)
height = 1.75
print("قد:", height)  # خروجی: قد: 1.75

# 🔸 نوع بولی (Boolean): فقط True یا False
is_student = True
print("دانشجو هست؟", is_student)  # خروجی: دانشجو هست؟ True

# 🔸 لیست (List): مجموعه‌ای از مقادیر
colors = ["قرمز", "آبی", "سبز"]
print("رنگ‌ها:", colors)  # خروجی: ['قرمز', 'آبی', 'سبز']

# 🔸 دیکشنری (Dictionary): نگه‌داری داده‌ها با کلید و مقدار
person = {
    "name": "مبین",
    "age": 22,
    "city": "تهران"
}
print("اطلاعات فرد:", person)
# خروجی: {'name': 'مبین', 'age': 22, 'city': 'تهران'}

# 🔸 مقداردهی چند متغیر در یک خط
x, y, z = 1, 2, 3
print("x =", x, "y =", y, "z =", z)

# 🔸 بررسی نوع متغیر با تابع type
print("نوع name:", type(name))      # <class 'str'>
print("نوع age:", type(age))        # <class 'int'>
print("نوع is_student:", type(is_student))  # <class 'bool'>
