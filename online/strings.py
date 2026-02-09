# Python - string 
# s = 'salom'
# print(type(s)) # <class 'str'>

# \n - new line 
# \t - tab 
# \a - sound
# s = "Python \n \t\tprogramming \a language"
# print(s)

# word = "don't \"worry\""
# word = 'don't'
# print(word)

# index - joylashuv 
# word = "python"
# print(word[0])
# print(word[1])
# print(word[-1])
# print(word[56]) # IndexError: string index out of range
# word = "python"
# print(word[-1])
# print(word[-2])

# word = "python"
# new_word = word[4:]
# print(new_word) # on
 
# print(word[2:4]) # th

# print(word[::-1]) # nohtyp

# age = 30
# salary = 1500
# name = "Ali"
# print(f"Your age : {age}, your salary : {salary}")
# # Your age : 30, your salary : 1500

# word = "Your name {0} Your salary {1}".format(name,salary)
# print(word)
# # Your name Ali

# print("Your age %s" %age) #Your age 30

# print(f""" Your name {name}
#       Your age {age}
#       Your salary {salary} """)

# word = "python" 
# print(len(word)) # 6
# print(len(word) + 6) # 12

# strip - qatordan ortiqcha probellarni ochirish uchun 
# word = " python " 
# print(len(word)) # 8
# print(len(word.strip())) # 6

# lstrip - qatordan ortiqcha probellarni ochirish uchun (chap tomondan)
# print(len(word.lstrip())) # 7
# rstrip - qatordan ortiqcha probellarni ochirish uchun (o'ng tomondan)
# print(len(word.rstrip())) # 7

# # split - qatorni siz korsatgan belgilari bo'yicha bo'lib ro'yhat qiladi 
# word = "pytho'n i's bet'ter" 
# print(word.split("'")) # ['pytho', 'n i', 's bet', 'ter']

# print(word.rsplit(" ")) # ["pytho'n", "i's", "bet'ter"]

# # splitlines - ko'p qatorli matnlarni \n bo'yicha bo'lib royhat qiladi \
# # join - royhat elementlarini string qiladi 
# arr = ["salom", "qale", "123"]
# print("".join(arr)) # salomqale123
# print(" ".join(arr)) # salom qale 123
# print("-".join(arr)) # salom-qale-123


# s = "Python is programming language"
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())

    # print(chr(65)) # A
    # print(ord("A")) # 65
    
# find - berilgan belgilarni qator ichidan qidiradi va indexini qaytaradi 
# print("salom".find("o")) # 3
# print("salom".find("t")) # -1
# rfind - o'ngdan chapga qarab 

# index - berilgan belgilarni qator ichidan qidiradi va indexini qaytaradi
# rindex -  o'ngdan chapga qarab 

# print("salom".index("o")) # 3
# print("salom".index("t")) # ValueError

# count - siz korsatgan belgini qator ichidan sanab nechtaligini qaytaradi (int)
# print("banana".count("a")) # 3
# print("banana".count("b")) # 1

# startswith - agar matn siz korsatgan belgilar bilan boshlansa > True
# print("salom".startswith('sa')) # True
# print("salom".startswith('lo')) # False
# endswith - agar matn siz korsatgan belgilar bilan tugasa > True
# print("salom".endswith('sa')) # False
# print("salom".endswith('lom')) # True

# replace  - siz korsatgan belgilarni siz korsatgan belgilarga almashtirish  

# print("salom".replace("m","n")) # salon
text = "lorem ipsum"

print("abc123".isalnum()) # true
print("abc123#".isalnum()) # false
print('abc'.isalpha()) # True
print('abc123'.isalpha()) # False
print("12".isdigit()) # True
print("12.5".isdigit()) # False

print("12.5".isdecimal()) # False
print("12".isdecimal()) # True

print("abc123".isnumeric()) # False
print("123".isnumeric()) # True

print("salom".islower()) # True
print("Salom".islower()) # False
print("SALOM".isupper()) # True
print("Salom".istitle()) # True

print(" ".isspace()) # True
print("#".isspace()) # False