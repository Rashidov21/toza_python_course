# function - harakat, amal, ish 
# function - kod bo'lagi, uni kodni istalgan joyida istalgan marta ishlatish mumkin bo'ladi

# print("Hello world")
# print("Hello world")
# print("Hello world")

# for i in range(10):
#     print(i)

# def <funksiya nomi> (qiymat1 ,qiymat2):
#     funksiya tanasi 
#     return natija

# funksiya nomi - o'zgaruvchilarni nomlashdagi qonun qoidalar amal qiladi 
# funksiya nomi - nima qiladi ? savoliga javob bo'lishi kerak !
# x = 1
# y = 2
# plus = 1 
# print(plus) # 1
# def plus(number1,number2):
#     return number1 + number2

# print(plus(x,y)) # 3

# def main():
#     print("OK")
    
# main() # funksiyani e'lon qilish (chaqirish)

# positional argument 
# def main(status,message):
#     print(f"{status} - OK, {message}")
    
# main(200,"success") # 200 - OK, success

# # not positional argument 
# def main(status,message="no message"):
#     print(f"{status} - OK, {message}")
    
# main(200,) # 200 - OK, no message

# def main(a=0,b=0,c=0):
#     return a + b + c

# def check_letters(name,surname=""):
#     letter_count = 0
#     for i in name+surname:
#         if i in "aiuoe":
#             letter_count += 1
#     return letter_count
# print(check_letters("abdurahmon")) # 4
# print(check_letters("ali","vali")) # 4

# result = main(1,2,3)
# print(result) # 6
# result = main(1,2)
# print(result) # 3

# *args - istalgancha qiymatlarni berish

# def multiple(*numbers):
#     # *numbers > () # * bilan qiymatlarni qabul qilish (args) tuple qilib beradi 
#     # print(numbers) # (1, 2, 3, 4, 5)
#     summa = 1
#     for i in numbers:
#         summa *= i
#     return summa    
# print(multiple(1,2,3,4,5)) # 120

# **kwargs - keyword arguments - kalit qiymatlarni ko'rsatish
# def main(**kwargs):
#     print(kwargs) # {'a': 1, 'b': 2, 'c': 3}
    
# main(a=1,b=2,c=3) # {'a': 1, 'b': 2, 'c': 3}
# main(name="John",surname="Doe") # {'name': 'John', 'surname': 'Doe'}

# def super_func(*args,**kwargs):
#     print(args) # (1, 2, True, 'salom')
#     print(kwargs) # {'name': 'Ali', 'age': 23}
    
# super_func(1,2,True,"salom",name="Ali",age=23)

# lambda anonim funksiyalar , nomsiz funksiyalar, bir qatorda yoziladigan funksiyalar
# main = lambda num1: num1 * 2
# print(main(2)) # 4


# l = lambda x,y,z: x + y + z
# print(l(1,2,3)) # 6



# map - siz korsatgan funksiyani siz korsatgan ketma-ketlik elementlarini har birigi qo'llaydi 
# def main(x):
#     return x * 2

# print(map(main,[1,2,3,4,5])) # <map object at 0x000002AE019D7880>
# print(type(map(main,[1,2,3,4,5]))) # <class 'map'>
# print(dir(map(main,[1,2,3,4,5])))
# l = list(map(main,[1,2,3,4,5]))
# print(l) # [2, 4, 6, 8, 10]

# l = list(map(main,"python"))
# print(l) # ['pp', 'yy', 'tt', 'hh', 'oo', 'nn']

# print(list(map(lambda x:x*2,[1,2,3]))) # [2, 4, 6]

# result = list(
#     map(
#         lambda x:x*2,
#         [1,2,3]
#     )
# )
# print(result) # [2, 4, 6]

# zip - siz korsatgan ketma-ketliklardan bir hil miqdorda elementlarni olib tuple qilib qaytaradi

# text = "abc"
# nums = [1,2,3]

# print(zip(text,nums)) # <zip object at 0x000001A678F55080>
# print(list(zip(text,nums))) # [('a', 1), ('b', 2), ('c', 3)]

# d = dict(zip(text,nums))
# print(d) #{'a': 1, 'b': 2, 'c': 3}

# text = "abc"
# nums = [1,2,3,4,5]
# symobls = "@#$%^&*"

# print(list(zip(text,nums, symobls))) # [('a', 1, '@'), ('b', 2, '#'), ('c', 3, '$')]

# filter - siz korsatgan function shartlariga kora siz korsatgan ketma-ketlik filterlaydi 

# print(filter(lambda x:x.isdigit(),"abc123")) # <filter object at 0x000001711D6A7EB0>
# print(list(filter(lambda x:x.isdigit(),"abc123"))) # ['1', '2', '3']

# def digit_nums(elem):
#     if elem.isdigit():
#         return elem
# print(list(filter(digit_nums,"qwerty12345"))) # ['1', '2', '3', '4', '5']


# dekoratorlar - oddiy function ni ishlashiga ta'sir o'tqazadigan function
# Dekorator — bu funksiyani o‘zgartirmasdan turib, unga qo‘shimcha xatti-harakat qo‘shib beradigan funksiya. 



# def deco(func):
#     def wrapper():
#         print("Funksiya ishga tushdi")
#         func()
#         print("Funksiya tugadi")
#     return wrapper

# @deco
# def salom():
#     print("Salom, dunyo!")

# salom()

# def check_username(get_username):
#     def check():
#         username = get_username()
#         if username in ["qwery","messi","jamal"]:
#             print("username is already exist")
#         else:
#             print("username ok")
#     return check
            
# @check_username      
# def get_username():
#     username = input("username ? : ")
#     return username

# get_username()

# def factorial(n):
#     if n == 0 or n == 1: return 1
#     else:
#         return n * factorial(n - 1) 
# print(factorial(5)) # 120

# global x 
# x = 10
# name = "john"

# for i in range(10):
#     if i == 5:
#         def main(x):
#             surname = "doe"
#             print(surname)
#             return x 
#         main(i)
# print(surname)
        
# global o'zgaruvchi deb o'zgaruvchini o'zidan pastki qatorlarda barcha blocklarda mavjud ekanlgiini 
# lokal ozgaruvchi deb function tanasida elon qilingan ozgaruvchilar nazarda tutiladi va ular faqat mana shu function tanasidagina mavjud boladi , boshqa bloklarda emas 