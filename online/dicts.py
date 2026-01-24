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