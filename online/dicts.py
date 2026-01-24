# dict - elementlariga indeks emas balki kalit so'z orqali murojaat qilinadigan obyektlar to'plami

# ketma-ketlik 
# l = [1,2,3,4,5]
# print(l[0])
# print(l[1])
# print(l[3])

# dict - lug'at 
# d = dict(name="John",age=23)
# print(d) # {'name': 'John', 'age': 23}

# d = {"salary":1500,"point":30}
# print(d["salary"]) # 1500
# print(d["point"]) # 1500

# print(d["skills"]) # KeyError: 'skills'

# get - olish, agar kalit mavjud bolsa uni qiymatini oladi aks holda None qaytaradi

# print(d.get("point")) # 30
# print(d.get("skills")) # None

# user = {
#     "name":"John",
#     "age":30,
#     "point":25
# }
# user_copy = user.copy()
# print(user_copy) # {'name': 'John', 'age': 30, 'point': 25}

# print(len(user)) # 3
# for i in user: # name,age,point
#     print(i) 

# for i in user.keys(): # name,age,point
#     print(i)
# for i in user.items(): # ('name', 'John'),('age', 30),('point', 25)
#     print(i)
# for i in user.values(): # name,age,point
#     print(i)

# setdefault - agar siz ko'rsatgan kalit dict da mavjud bolsa uni qiymatini oladi, aks holda 2-parametr sifatida bergan qiymatizni kalit bilan birga biriktirib qoyadi

# book = {
#     "author":"diego"
# }
# print(book.setdefault("author", 30)) # diego
# print(book.setdefault("pages",30)) # 
# print(book) # {'author': 'diego', 'pages': 30}

# pop - siz korsatgan kalit ostida elementni o'chiradi
# book.pop("pages")
# print(book) # {'author': 'diego'}
# popitem - dict tasodiy elementni o'chiradi va o'chirilgan elementni tuple qilib qaytaradi

# book = {
#     "author":"diego",
#     "pages":250,
#     "price":5
# }
# print(book.popitem()) # ('price', 5)


# book.clear()
# print(book) # {}

# # update - dict ga element qo'shish uchun 
# book.update({"author":"O'tkir Hoshimov"})
# book.update(price=50000,star=5)
# print(book) # {'author': "O'tkir Hoshimov", 'price': 50000, 'star': 5}

# dict generator 
# d = {}
# for v,k in enumerate(["anor","olma","behi"]):
#     d.update({k:v})
# print(d) # {'anor': 0, 'olma': 1, 'behi': 2}


# task 1 
# user kiritgan matnni olib undagi 3 tadan ko'p unli harf ishtirok etgan so'zlarni alohida dict ga yozish kerak (kalitlar standart : word1,word2...)
# input : salom nima gaplar qalaysan
# output: {"word1":"qalaysan"}


# task 19  dict, for, if , split
# sometimes = [
#     {'date':'2022/10/11'},
#     {'date':'2023/02/05'},
#     {'date':'2005/05/15'},
#     {'date':'2004/03/25'},
#     {'date':'2006/11/22'},
#     {'date':'2009/10/30'},
#     {'date':'2012/06/10'},
# ]
# ushbu ma'lumotlardagi sanalarni tekshiring va 2007-yildan keyingi sanalarni barchasini ekranga chiqaring


# task 6 
# Berilgan massivdan sonlarni bir xillarini olib tashlab faqat sanoqdagi ketma-ket sonlarni qoldiring
# Masalan arr = [1,5,6,1,8,5,9]  Output/Javob arr = [1,5,6,8,9]
# Sizga berilgan Massiv bu >> arr = [2,6,6,4,7,8,2,9,7,1,9]

# task 7 

# Kinoteatrda 15 ta qator  bor har bir qatorda 20 tadan o'rin bor. O'rindiqlar seriya raqamlangan
# misol : A12 A bu yerda qator tartib harfi 12 esa  o’rindiq tartib raqami siz foydalanuvchi kiritgan seriya raqamiga qarab o’rindiq qaysi qatorda joylashganini topishingiz kerak. 

# Bundan tashqari random shaklda o’rindiqlar band qilinadi , Kinoteatr 50% ga to’ldiriladi siz foydalanuvchi kiritgan o’rindiq band yoki bosh ekanini chiqarishingiz kerak.

# task 8 
# 9 qavatli uyda 3-ta podyezd bor har bir qavatda 6 tadan kvartira bor. Foydalanuvchi kvartira raqamini kiritsa siz topishingiz kerak;
# (kvartiralar raqamlari 1-chi qavatdan 1-podyezdan boshlanadi : 1-kv , 1-podyezd 1-etaj)
# Kvartira qaysi qavatda ekanini
# Kvartira qaysi podyezdda ekanini

