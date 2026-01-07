# WHILE 1
# a = 25
# b = 7
# while a >= b:
#     a -= b
# print(a)

# WHILE 2
# a = 24
# b = 8
# maksimum = 0
# while a >= b:
#     a -= b
#     maksimum += 1
# print(maksimum)

# WHILE 3
# n = 12
# k = 5
# maksimum = 0
# while n >= k:
#     n -= k
#     maksimum += 1
# print( maksimum)
# print(n)

# WHILE 4
# n = 9
# while n == 9:
#     print(n," soni 3ning darajasi")
# else: 
#     print(n,"Soni 3 ning darajasi emas")

# WHILE 5
# n = 16
# temp = n
# if n % 2 == 0:
#     while temp < n:
#         temp = (n - 2)
#         print(n * (n - 2))
#         n = n - 2
# else:
#     while temp < n:
#         temp = (n - 1)
#         print(n * (n - 1))
#         n = n - 1
# print(temp)
    # task 3 
# n soni berilgan (30 > n > 0) 0 dan n gacha bo'lgan sonlarni orasida probellar bilan chiqaring agar son toq bo'lsa bitta probel bilan uni keyingi son orasini belgilaysiz agar juft bo'lsa 2 ta probel bilan. misol : 0  1 2  3 4  5

# 10 ta 2 xonalik butun son berilgan ulardan faqat 0 bilan tugaganlarini summasini hisoblang

# 1 usul 
import random 
arr = []
for i in range(10):
    arr.append(random.randint(10,100))
print(arr)
summa = 0
for k in arr:
    if k % 10 == 0:
        summa += k
print("Summa : ", summa)

# 2 - usul 
arr2 = random.sample(range(10,100),10)
print("Summa : ", arr2)
print(sum([k for k in arr2 if k % 10 == 0]))

# task 
# user hohlagan miqdorda harf kiritadi 
# agar "stop" deb yozsa dastur to'xtaydi 
# va kiritgan harflarini ichida nechta unli harf bor ekanini ekranga chiqaradi 
# input: a ,y ,h, t ,i 
# output: 2 ta unli harf 