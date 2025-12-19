

# Arifmetik operatorlar :
# +, -, *, /, %, //, **
# print(2+2) # 4
# print(2-2) # 0
# print(4/2) # 2.0
# print(4*2) # 8
# print(5%2) # 1
# print(5//2) # 2
# print(2**10) # 1024
# print(2**2) # 4

# print("salom" + "salom") # salomsalom
# print("salom" * 3) # salomsalomsalom
# print("salom" / 3) # TypeError: unsupported operand type(s) for /: 'str' and 'int'

# in - mavjudlikka tekshirish operatori 
# print("salom" in "salom nima gap") # True
# print("xayr" in "salom nima gap") # False

# # not in - mavjud emaslikka tekshirish operatori
# print("xayr" not in "salom nima gap") # True

# arr = [1,2,3,4,5]
# print(3 in arr) # True

# Qiymatni biriktirish operatorlari :
# += - qo'shib tenglash
# -= - ayrib tenglash
# /= - bo'lib tenglash
# *= - ko'paytirib tenglash
# x = 10
# y = 20
# x += y # x = x + y
# print(x) # 30
# x = 5
# x -= 2
# print(x) # 3
# x /= 2
# print(x) # 1.5
# x *= 2
# print(x) # 3

# x = 5
# x **= 2
# print(x) # 25
# x //= 2
# print(x) # 12
# x %= 5
# print(x) # 2

# Taqqoslash operatorlari :  > True,False
# print(2 == 2) # True
# print(2 != 2) # False
# print("salom" == "salom") # True
# print("salom" == "Salom") # False
# print("salom" != "Salom") # True

# print(2 > 1) # True
# print(2 < 1) # False
# print(2 >= 1) # True
# print(2 <= 1) # False
# print(2 <= 2) # True

# x = 10
# y = 10 
# z = 5
# print(x is y) # True
# print(x is z) # False
# print(x is not z) # True

# Mantiqiy operatorlar 
# mantiqiy VA (and) , Mantiqiy Yoki (or)
# print(1 > 0 and 2 > 1) # True
# print(1 > 0 and 0 > 1) # False

# print(1 > 0 or 0 > 1) # True
# print(0 > 1 or 0 > 1) # False 

# print(not 1 > 0) # False
# print(not 1 < 0) # True

# task 1 
a = int(input("a = "))
print("Perimetr = ", 4*a)