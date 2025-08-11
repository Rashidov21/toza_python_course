# Operators 

# Arithmetic operators 
print(7 * 3) # 21
print(2 + 2) # 4
print(2 - 2) # 0
print(7 / 3) # 2.3333333333333335
print(7 // 3) # 2
print(7 % 3) # 1
print(2 ** 10) # 1024

# konkatenatsiya - boglash , ulash 
print("aa" + "aa") # aaaa
print([1,2,3] + [4,5,6]) # [1, 2, 3, 4, 5, 6]

print("a" * 5) # aaaaa
# in - mavjudlikka tekshirish (ketma-ketlik ichida siz korsatgan narsa bor yoki yoq ekanligini tekshirish)



print("t" in "salom") # False
print("s" in "salom") # True

# not in - mavjud emaslikga tekshirish

users = ["johndoe","miketyson","davidchopper"]
print("harrypotter" not in users) # True
print("johndoe" not in users) # False

x = 1
x += 1
print(x) # 2

x *= 2
print(x) # 4

# x /= 2
x //= 2
print(x) # 2

x -= 1
print(x) # 1

n = 2
n **= 10
print(n) # 1024





# print(2 == 2) # True
# print(2 != 2) # False
# print(2 != 5) # True
# print(2 > 0) # True
# print(2 < 0) # False
# print(2 <= 2) # True
# print(2 >= 0) # True

x = 10
y = 10
z = 10
print(x == y) # True
# is - bir xil qiymatga yol korsatadigan ozgaruvchilar uchun True qaytaradi aks holda False
print(x is y) # True
print(x is z) # True

a = 12
print(x is a) # False

# is not - is ni aksi 
print(x is not y) # False
print(x is not a) # True


# and - mantiqiy VA 
print(10 > 5 and 5 > 0) # True
print(10 > 5 and -10 > 0) # False

# or - mantiqiy YOKI 
print(1 > 0 or 0 > -10) # True
print(2 > 5 or 0 > -10) # True
print(2 > 5 or 0 > 5) # False

print(not True) # False
print(not False) # True

print(not 1 > 0) # False