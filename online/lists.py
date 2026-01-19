# list - ro'yhat , ketma-ketlik
# list - tartibli elementlar ro'yhati 

# arr = [1,2,3,4,5]
# print(arr)
# arr = list("python")
# print(arr)
# print(arr[0])
# print(arr[-1])
# print(arr[6]) # IndexError: list index out of rang
# arr = [1,2,3,4,5]

# x,y,z = [1,2,3]
# print(x + y + z) # 6

# a,*b = [1,2,3,4,5]
# print(a , b) # 1 [2, 3, 4, 5]

# arr = [1,2,3,4,5]
# print(arr[0:3]) # [1, 2, 3]
# print(arr[-3:]) # [3, 4, 5]

# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# print(arr) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in arr:
#     # print(i)
#     for k in i:
#         print(k)

# enumerate - ketma-ketlik elementlarini indexi bilan olish 

# arr = [1,2,3]
# arr[0] = 0
# arr[2] = 5
# print(arr) # [0, 2, 5]

# list generator 
# for i in range(10):print(i)
# arr = [i for i in range(10)]
# print(arr) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print([i for i in range(10) if i % 2 == 0]) # [0, 2, 4, 6, 8]
# print([i for i in range(10) if i % 2 == 1]) # [1, 3, 5, 7, 9]
# print([i**2 for i in range(10) if i % 2 == 1]) # [1, 9, 25, 49, 81]
arr = []
# append - list oxiriga element qo'shish 
arr.append(1)
arr.append(2)
print(arr) # [1, 2]
# extend - listni boshqa list bilan kengaytirish 
arr2 = [3,4]
arr.extend(arr2)
print(arr) # [1, 2, 3, 4]
# insert - listni istalgan joyiga index orqali element qo'shish 
arr.insert(2,0)
print(arr) # [1, 2, 0, 3, 4]
# pop - list ichidan element o'chirish (oxirgisi)
arr.pop(0)
print(arr) # [2, 0, 3, 4]
# remove - ko'rsatilgan elementni o'chirish
arr.remove(3)
print(arr) # [2, 0, 4]
# clear - list ni tozalash 
print(arr2)
arr2.clear()
print(arr2) # [2, 0, 4]

# index - elementni indexini olish 
print(arr.index(4)) # 2
# count - elementni sonini bilish 
print(arr.count(0)) # 1
# all - barcha elementlarni True 
print(all(arr)) # False
# any - ayrim elementlar True 
print(any(arr)) # True

result = arr.copy()
print(result) # [2, 0, 4]

print(2 in arr) # True
print(9 in arr) # False