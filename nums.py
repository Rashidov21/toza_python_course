import math
import random 


# int, float,

# int(), float()
# s = "10"
# print(type(float(s))) # <class 'float'>
# print(int(s)) # 
# print(type(int(s))) # <class 'int'>

# round() - yaxlidlash 

# n = 12.51200000000
# print(round(n)) # 13
# print(round(n,2)) # 12.51
# print(round(n,4)) # 12.512

# r = range(1,11)
# print(max(r)) # 10
# print(min(r)) # 1
# print(sum(r)) # 55

# print(math.pi) # 3.141592653589793
# n = 2 
# ex = 10
# print(math.pow(n,ex)) # 1024.0
# print(math.pow(2,2)) # 4
# print(math.pow(5,5)) # 3125.0
 
# print(round(12.12)) # 12
# print(math.ceil(12.12)) # 13
# print(math.floor(12.95)) # 12

# print(math.sqrt(16)) # 4

# print(dir(random))

# r = range(1,6)
# randint - berilgan 2 ta sob orasida tasodify bitta sonni qayataradi 
# print(random.randint(1,60))
# print(random.randrange(1,100))
# choice - berilgan ketma-ketik elementlaridan tasodify bittasini qaytaradi 
# print(random.choice(r))
# print(random.choice("salom qale ishlar"))

# shuffle - beerilgan ketma-ketlik elementlarini ornlarini almashtiradi 
# l = [1,2,3,4,5]
# random.shuffle(l)
# print(l)
# sample - berilgan ketma-ketlik ichidan siz korsatgan miqdordan tasodify elementlarni olib alohida massiv qilib qaytaradi 
# s = "hello world"
# random_letter = random.sample(s,5)
# print(random_letter[0])
# print(random_letter[-1])

# password generator 
letters = "qwertyuiopasdfghjklzxcvbnm"
uppers = letters.upper()
nums = "0123456789"
symbols = "!@#$%^&*()_+"

data = letters + uppers + nums + symbols

password_length = int(input("password length ? :"))
password = ""
if password_length >= 8:
    for i in range(password_length):
        password += random.choice(data)
    print("Your password = ", password)
else:
    print("Password to short !")
    
# task 1 
# random modulidan foydalanib fake email hosil qilib bering 