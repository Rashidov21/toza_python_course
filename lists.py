# list - tartibli elementlar ro'yhati (list bu array larni dinamik ko'rinishi)

# arr = [1,2,3,4,5]
# print(arr) #c [1, 2, 3, 4, 5]
# arr = list("python") # ['p', 'y', 't', 'h', 'o', 'n']
# # arr = list(1,2,3,4,5) # TypeError: list expected at most 1 argument, got 5
# print(arr)

# task 1 
# 1 dan 10 gacha bo'lgan sonlar iborat list hosil qiling 
# l = [1,2,3,4,5,6,7,8,9,10]
# print(l)

# l = []
# for i in range(1,11):
#     l.append(i)
# print(l)

# print(list(range(1,11)))

# x,y,*z = [1,2,3,4,5]
# print(x) # 1
# print(y) # 2
# print(z) # [3, 4, 5]

# arr = [1,2,3,4,5]
# print(arr[0])
# print(arr[-1])
# copy_arr = arr[:] # list copy qilish
# print(copy_arr) # [1, 2, 3, 4, 5]

# print(arr[dan:gacha])
# print(arr[0:3]) # [1, 2, 3]
# print(arr[3:]) # [4, 5]
# print(arr[:3]) # [1, 2, 3]

# arr = [1,2,3,4,5]
# print(arr[::-1])  # [5, 4, 3, 2, 1]

# arr = [1,2,3,4,5]
# arr.reverse()
# print(arr) # [5, 4, 3, 2, 1]

# arr = [1,2,3,4,5]
# for n in arr:print(n)

# list generators 

# arr = [i for i in range(1,11,2)]
# print(arr) # [1, 3, 5, 7, 9]
# arr = [i for i in range(1,101) if i % 10 == 0]
# print(arr) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# task 2 
# user kiritgan matndan faqat unli harflarni ajratib alohida listga yozing 

# user = "javascript"
# data = []
# for l in user:
#     if l in "auieo":
#         data.append(l)
# print(data) # ['a', 'a', 'i']
 
# print([l for l in user if l in "aiueo"]) #['a', 'a', 'i']

# arr = [1,2,3]
# arr.append(4) # oxiriga element qoshish
# print(arr) # [1, 2, 3, 4]

# arr.clear() # listni tozalash 
# print(arr) # []

# arr = [1,2,3,1,1,1]
# arr2 = arr.copy() # nusxalash
# print(arr2) # [1, 2, 3]

# print(arr.count(1)) # list ichidagi siz korsatgan elementlar sonini sanash

# arr = [1, 2, 3, 4]
# ex_arr = [5,6,7,8,9]
# arr.extend(ex_arr) # list ni boshqa bir list bilan kengaytirish
# print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# arr = [1, 2, 3, 4]
# arr.insert(1,"salom") # siz korsatgan index ga siz korsatgan elementni joylaydi
# print(arr) # [1, 'salom', 2, 3, 4]

# arr = [1, 2, 3, 4]
# print(arr.index(4)) # 3 - siz korsatgan elementni index joylashuvini qayataradi 
# arr = [1, 2, 3, 4]
# arr.pop() # index berilmasa oxirgi elementi ochiradi 
# print(arr)
# arr = [1, 2, 3, 4]
# arr.pop(0) # index berilsa o'sha elementni ochiradi 
# print(arr)
# arr = [1, 2, 3, 4]
# arr.pop(23) # IndexError: pop index out of range
# print(arr)

# arr = ["salom","olma","nok"]
# arr.remove("olma") # siz korsatgan elementni o'chiradi 
# print(arr) # ['salom', 'nok']

# arr = [1,2,3]
# arr.reverse() # listni teskari qilish 
# print(arr) # [3, 2, 1]

# arr = [4,5,6,7,9,5,1,2,3]
# arr.sort()
# print(arr) # [1, 2, 3, 4, 5, 5, 6, 7, 9]

# arr = [4,5,6,7,9,5,1,2,3]
# arr.sort(reverse=True)
# print(arr) # [9, 7, 6, 5, 5, 4, 3, 2, 1]

# arr = ['b','c','a','f','j']
# arr.sort()
# print(arr) # ['a', 'b', 'c', 'f', 'j']

# arr = [1,2,3]
# print(arr[0])