import time
import datetime
import calendar
import locale
from timeit import Timer
locale.setlocale(locale.LC_ALL,"UZ_uz") # lokal tilni o'zgartirish

# print(time.time()) # 1770702419.8074286
# print(type(time.time())) # <class 'float'>
# print(dir(time.time()))
# print(time.gmtime()) # time.struct_time(tm_year=2026, tm_mon=2, tm_mday=10, tm_hour=5, tm_min=48, tm_sec=42, tm_wday=1, tm_yday=41, tm_isdst=0)

# t = time.gmtime() # UTC bo'yicha vaqtni olish
# print(t.tm_year) # 2026
# print(t.tm_mon) # 2
# print(t.tm_mday) # 10
# print(t.tm_hour) # 5

# t = time.localtime() # lokal vaqtni olish
# print(t.tm_year) # 2026
# print(t.tm_mon) # 2
# print(t.tm_mday) # 10
# print(t.tm_hour) # 10
# print(t.tm_min) # 51


# time.strftime() # sana va vaqtni matn ko'rinishi 
# print(time.strftime("%y %Y")) # 26 2026
# print(time.strftime("%m")) # 02
# print(time.strftime("%m")) # 02
# print(time.strftime("%b")) # Feb
# print(time.strftime("%B")) # February
# print(time.strftime("%w")) # 2 
# print(time.strftime("%a")) # Tue
# print(time.strftime("%A")) # Tuesday
# print(time.strftime("%H")) # 10 (24)
# print(time.strftime("%I")) # 10 (12)
# print(time.strftime("%M")) # min
# print(time.strftime("%S")) # sec
# print(time.strftime("%x")) # 02/10/26
# print(time.strftime("%X")) # 10:56:16
# print(time.strftime("%x %X")) # 02/10/26 10:56:35



# n = datetime.datetime.now()
# print(n) # 2026-02-10 11:00:48.650682
# print(n.year)
# print(n.month)
# print(n.day)
# print(n.hour)
# print(n.minute)
# print(n.second)

# first_date = datetime.timedelta(days=10,hours=5)
# second_date = datetime.timedelta(days=4,hours=3)
# print(first_date - second_date) # 6 days, 2:00:00

# print(datetime.timedelta(weeks=2)) # 14 days, 0:00:00

# d1 = datetime.date(year=2026,month=2,day=10)
# d2 = datetime.date(year=1991,month=8,day=31)
# print(d1 - d2) # 12582 days, 0:00:00

# t1 = datetime.time(hour=2,minute=35)
# t2 = datetime.time(hour=1,minute=20)
# print(t1 > t2) # True
# print(t1 < t2) # False


# c = calendar.LocaleHTMLCalendar()
# c = calendar.LocaleTextCalendar(0)
# print(c.formatyear(2026))
# print(c.formatmonth(2026,2))

# for name in calendar.day_name: # hafta kunlari nomlarini olish
#     print(name)
    
# for name in calendar.day_abbr: # hafta kunlari nomlarini qisqa olish
#     print(name)
# for name in calendar.day_abbr: # hafta kunlari nomlarini qisqa olish
#     print(name)
# for name in calendar.month_name: # oy nomlarini olish
#     print(name)
# for name in calendar.month_abbr: # oy nomlarini qisqa olish
#     print(name)

# with open("calendar.html", "w+") as file:
#     file.write(c.formatyear(2026))


code1 = """\
i,j = 1, 0
while i < 10001:
    i += 1 
    j += 1
"""
code2 = """\
j = 0
for i in range(1, 10001):
    j += 1
"""
t1 = Timer(stmt=code1)

print("while : ", t1.timeit(10000))
t2 = Timer(stmt=code2)
print("for : ", t1.timeit(10000))

