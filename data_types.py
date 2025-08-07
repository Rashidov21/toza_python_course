# Python data types
# Python - dinamik tipizatsiya ega dasturlash tili 

# str - string > matn > unicode 
# s = "salom"
# constant - o'zgarmas 
# s[3] = "t"

# index - joylashuv 
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[15])

s1 = ''
s2 = ""
s3 = """"""

# print('don't')
# print("salom "dunyo"")
print('salom "dunyo"') # salom "dunyo"
print("""salom "dunyo" don't""") # salom "dunyo" don't

print(len("salom")) # 5
print(len("salom") + 5) # 10

s = "hello world"
print(len(s)) # 11
# type() > berilgan ozgaruvchi qiymatini qaysi ma'lumot turida ekanligini qaytaradi 
print(type(s)) # <class 'str'>

# int  - butun sonlar > integer 
# 10,1,-56
# float -qoldiqli sonlar 
# 1.12, -56.23
# complex - murakkab sonlar 
# 2n

# n = 10
# f = 10.2
# print(type(n)) # <class 'int'>
# print(type(f)) # <class 'float'>


# bool - True, False 

# t = True 
# f = False
# print(type(t)) # <class 'bool'>
# print(type(f)) # <class 'bool'>

# str,int,float,complex,dict,list,tuple,range,set,frozenset,bool,

# list - ro'yhatlar > tartibli elementlar ketma-ketligi 
# list - massiv ,array larni dinamik ko'rinishi

# l = [1,2,3,5]
# print(l[0]) # 1
# print(l[3]) # 5

# l[3] = 4
# print(l) # [1, 2, 3, 4]

# dict - lug'at > elementlariga index emas balki kalit nom orqali murojaat qilinadigan to'plam

# ketma-ketlik
# to'plam 

d = {
    "name":"John",
    "age":23
}
print(d) # {'name': 'John', 'age': 23}

# tuple - kortejlar > tartibli o'zgarmas elementlar ketma-ketligi
t = (1,2,3)
print(t[1]) #2
# t[1] = 25 

# range - diapazon > sonlar diapazon > o'ralig'i 
r = range(1,11,2)
print(r)
print(list(r)) # [1, 3, 5, 7, 9]

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,5))) # [1, 2, 3, 4]

# set - unikal elementlar to'plami
s = {1,2,3,1,4,3} 
print(s) # {1, 2, 3, 4}
# frozenset - unikal o'zgarmas elementlar to'plami 
fs = frozenset(s)
print(fs) # frozenset({1, 2, 3, 4})