#  آموزش شرط‌ها در پایتون (if, elif, else)

# شرط یعنی بررسی کنیم آیا یک عبارت درست است یا نه، و بر اساس آن تصمیم بگیریم چه کاری انجام شود.

age = 18

if age >= 18:
    print("شما بزرگ‌سال هستید.")
else:
    print("شما هنوز زیر 18 سال هستید.")

# 🔹 استفاده از elif برای چند شرط

score = 85

if score >= 90:
    print("عالی!")
elif score >= 70:
    print("خوبه!")
else:
    print("نیاز به تلاش بیشتر داری!")

# 🔹 استفاده از شرط تو در تو (nested if)

is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("به پنل مدیریت خوش آمدید.")
    else:
        print("به سایت خوش آمدید.")
else:
    print("لطفاً وارد شوید.")

# 🔹 بررسی چند شرط با and / or

username = "moeen"
password = "1234"

if username == "moeen" and password == "1234":
    print("ورود موفقیت‌آمیز بود.")
else:
    print("نام کاربری یا رمز اشتباه است.")
