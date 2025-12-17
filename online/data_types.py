# bool , int, str, None, list, dict, range, tuple, set, frozenset
# Ma'lumot turi , Ma'lumot tuzilmasi 

# Python - dinamik tipizatsiya ega dasturlash tili
# Ma'lumot turi:
#     bool , int,float,complex, str, None,
# x = 10

# Ma'lumot tuzilmasi :
#     list, dict, range, tuple, set, frozenset
# arr = [1,2,3,4,5]

# ketma-ketlik - elementlar xotiradi ketma ket joylashadi
# to'plam - bir biriga boglangan elementlar turli xotira kataklarida saqlanadi


# bool - True, False
# int - 1,2,-1,-2
# float - 1.1,2.2,-1.1,-2.2
# complex - 1+2j, 2+3j, -1+2j, -2+3j
# str - "salom", 'salom', """salom"""
# None - None - mavjud emas

# list - [] - ro'yhatlar ketma ketlik
# dict - {} - lug'at - elementlariga kalit orqali murojaat qilinadi to'plam
# range - () - sonlar diapazoni, ketma-ketlik   
# tuple - () - o'zgarmas ro'yhatlar ketma ketlik
# set - {} - elementlari unikal to'plam
# frozenset - {} - o'zgarmas elementlari unikal to'plam


# a = 10
# print(type(a)) # <class 'int'>
# b = 1.3
# print(type(b)) # <class 'float'>

# print(), dir(), type() 

# number = "12"
# print(type(number))
# print(number + 10) # TypeError: can only concatenate str (not "int") to str
# print(number * 10) # TypeError: can only concatenate str (not "int") to str
# print(number / 10) # TypeError: can only concatenate str (not "int") to str
# number = "12"
# n = int(number)
# print(n + 10) # 22
# print(bool(56)) # True
# print(bool(-256)) # True
# print(bool(0)) # False
# print(bool("")) # False
# print(bool("sasasasa")) # True

# print(str(10) + "salom") # 10salom

# str(), float(),int(), bool()
# l = list("salom")
# print(l) # ['s', 'a', 'l', 'o', 'm']
# t = tuple("xayr")
# print(t) # ('x', 'a', 'y', 'r')

# range > start,stop,step 
# print(list(range(1,11,3))) # [1, 4, 7, 10]
# print(list(range(20)))


# binar sonlar > 0,1 > bit
# 1bayt = 8bit

# name = input()
# print(name)

# age = int(input("yoshni kiriting:"))
# print(age + 5)
# print(f"Siz 5 yildan keyin {age + 5} yosh bo'lasiz !")