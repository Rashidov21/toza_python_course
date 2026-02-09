

# open() - fayllarni ochish

# f = open(file="test.txt", mode="r")
# print(f) # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1251'>
# print(type(f)) # <class '_io.TextIOWrapper'>
# print(dir(f)) # 
# f = open(file="test.txt", mode="r")
# f = open(file="test.txt", mode="r+") # o'qish hamda yozish rejimida faylni ochish
# f.write("Hello python")
# f.close() # fayl yopish


# f = open("test.txt")
# print(f.read()) # faylni o'qish, ochish
# f.close() # fayl yopish

# f = open("test.txt", "w")
# f.write("hello world")
# f.close()

# print(open("test.txt").read())

# f = open("test.txt", "a")
# f.write("\nhello backend")
# f.close()
# print(open("test.txt").read())

# try:
#     f = open("test.txt", "x")
# except Exception as e:
#     print(e)
#     f = open("test.txt", "r")
#     print(f.read())
#     f.close()
# finally:
#     print("Fayl ochish yakunlandi!")

# with as 

# with open("test.txt", "r+", encoding="UTF-8") as file:
    # print(file.readline()) # 1-qatorni o'qish
    # print(file.readlines()) # /n ya'ni keyingi qatorga otishlar bo'yicha qatorlarni royhat qilib beradi 



# import os 
# os.rename("rename_test.txt","test.txt") # qayta nomlash
# os.remove("text.txt") # faylni ochirish
# print(os.path.exists("test.txt")) # True
# print(os.path.exists("text.txt")) # False
# print(os.path.getsize("test.txt")) # fayl hajmni baytlarda qaytaradi
# print(os.path.getmtime("test.txt")) # faylni oxirgi ozgargan vaqtini
# print(os.path.getatime("test.txt")) # faylga oxirgi kirilgan vaqtni
# os.mkdir('./test') # papka ochish

