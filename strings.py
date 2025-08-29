# s = ""
# s = ''
# s = """"""
# s = "python"
# print(len(s)) # 6

# print(s[0]) # p
# print(s[-1]) # n

# print(s[30]) # IndexError: string index out of range

# age = 63
# salary = 1500
# print(f"Yosh = {age}, oylik = {salary}") # Yosh = 63, oylik = 1500
# print("Yosh = {0}, oylik = {1}".format(age,salary))
# print("Yosh = %s, oylik = %s" % (age ,salary)) 


# n = 32
# print(str(n) + 30) # TypeError: can only concatenate str (not "int") to str

# print("Enter\nyour name")
# print("Enter\t\t\tyour name") # Enter                   your name
# print("Enter\'your name") # 
# print("Enter\"your name") # 
# print(repr("Enter\t\t\tyour name")) # 'Enter\t\t\tyour name'

# strip - str oldidagi va oxiridagi probellarni ochiradi 
# s = " Salom "
# print(len(s)) # 7
# print(len(s.strip())) # 5
# print(len(s.lstrip())) # 6
# print(len(s.rstrip())) # 6

# split - siz korsatgan belgi boyicha qatorni bo'lib massiv elementlariga aylantiradi 
# text = "python is better"
# print(text.split()) # ['python', 'is', 'better']
# text = "Mike,Sara,David"
# print(text.split(",")) # ['Mike', 'Sara', 'David']
# text = "Mike-Sara-David"
# print(text.split("-")) # ['Mike', 'Sara', 'David']
# text = """разделяет строку на подстроки по символу перевода строки (\п)
# и добавляет их в список. Символы новой строки включаются в результат, только если
# необязательный параметр имеет значение True. Если разд"""
# print(text.splitlines())

# join - massivni string qilib beradi 
# arr = ["javascript","python","ruby"]
# print(" ".join(arr))
# import calendar
# import locale
# locale.setlocale(locale.LC_ALL,"UZ_uz")

# cal = calendar.LocaleTextCalendar(0)
# print(cal.formatyear(2025))

# s = "Python"
# print(s.upper()) # PYTHON
# print(s.upper().lower()) # python
# print(s.swapcase())
# print(s.capitalize())

# word = "python programming language"
# print(word.find("lang")) # 19
# print(word.find("java")) # -1

# index - siz korsatgan belgilarni qatordagi indeksini qaytaradi 
# print(word.index("lang")) # 19
# print(word.index("java")) # ValueError: substring not found

# count  -qatorda siz korsatgan elementlarni sonini qaytari 
# word = "python programming language"
# print(word.count("o")) # 2
# print(word.count("a")) # 3

# startswith, endswith - siz korsatgan belgilar bilan qator tugayaptimi yoki yoqmi aniqlab beradi 

# print(word.startswith("p")) # True
# print(word.endswith("e")) # True
# print(word.endswith("a")) # False

# replace - siz korsatgan belgilarni siz korsatganlariga almashtirib beradi 
# word = "python programming language"
# print(word.replace("programming", "human")) # python human language


# s = "Enter\t\t\tyour name"
# print(s.replace("\t","")) # Enteryour name

# s = "abc123"
# print(s.isalpha()) # hamma belgilari alfavit harflarimi  ?
# s = "abc"
# print(s.isalpha()) # hamma belgilari alfavit harflarimi  ?

# s = "abc123"
# print(s.isalnum()) # hamma belgisi alfavit harflari va sonlardan iboratmi ? 

# s = "123"
# print(s.isdigit()) # butun sonmi ?
# s = "12.3"
# print(s.isdigit()) # butun sonmi ?
# print(s.isdecimal()) # onlik  sonmi ?
# s = "1"
# print(s.isnumeric()) # raqamlardan iboratmi ?

# s = "Abc"
# print(s.isupper()) # katta harfmi ?
# print(s.islower()) # kichik harfmi ?
# print(s.istitle()) # birinchi belgisi kattami ?

# print(" ".isspace()) # probel belgisini tekshirish
# print("..".isspace())

import hashlib
h = hashlib.sha1(b"python")
h2 = hashlib.sha1(b"javascript")

print(h.digest()) # b'B5"{QCj\xd8m\x07\xc7\xcf]i\xbd\xa2dI\x84\xde'
print(h.hexdigest()) # 4235227b51436ad86d07c7cf5d69bda2644984de


print(h.hexdigest() == h.hexdigest()) # True
print(h.hexdigest() == h2.hexdigest()) # True

