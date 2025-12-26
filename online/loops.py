# loop - takrorlanish 
# for  - sanoqli takrorlanish 
# while - cheksiz 

# i , k , j , x
# i - iteration > takrorlanish 
# for i in "python":
#     print("Hello")


# range , enumerate 

# range - sonlar diapozoni (oraliq) 1,10
# start = 1
# stop = 11
# step = 2
# numbers = range(start,stop,step)
# for i in numbers:
#     print(i)

# for k in range(5):
#     print(k)
#     x  = int(input("Son ? :"))
#     print(x ** 2)

# for i in range(1,21):
#     print(i)

# enumerate - berilgan ketma ketlikdan elementlarni indeksini va elementni o'zini qaytaradi 
# arr = ["apple","banana","cherry"]
# for i,e in enumerate(arr):
#     print(f"Index = {i}")
#     print(f"Element = {e}")



# while - cheksiz takrorlanish 
# while True:
#     print(10)

# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         break # siklni to'xtatish
#         # continue # keyingi sikl o'tish va davom etish
#     print(i)

# for i in range(10):
#     # if i % 2 == 0:
#     #     continue
#     # if i == 5:
#     #     break
#     print(i)
# else:
#     print("sikl tugadi")
price = 15000
for i in range(1,11):
    print(float(f"0.{i}") * price)