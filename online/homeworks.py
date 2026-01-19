# Homeworks
# task1
# n = 9
# arr = []
# for i in range(n):
#     arr.append(2 * i +1)
# print(arr)
# 
# task2
# n = 5
# arr = [] 
# for i in range(n+1):
#     arr.append(i **2)
# print(arr)

# task3
# n = 5
# a = 2
# d = 8
# arr =[]
# for i in range(n):
#     arr.append(a + i *d)
# print(arr)

# task 4 n soni beriladi. Dastlabki n ta toq sondan iborat ro‘yxat tuzing va chiqaring.
# n = 10
# arr = []
# for i in range(n):
#     arr.append(2 *i + 1)
# print(arr)

# Task 5 Juft va toqni ajratish
# arr = [1,2,3,4,5,6,7,8,9,10]
# juft_son = []
# toq_son =  []
# for i in arr:
#     if i % 2 == 0:
#         juft_son.append(i)
#     else:
#         toq_son.append(i)
# print(f"Juft sonlar ro'yhati{juft_son}")
# print(f"Toq sonlar ro'yhati {toq_son}")

# task6 3️ Eng katta va eng kichik son
# arr = [1,2,3,4,5,6,7,8,9]
# print("Eng kichik son", min(arr))
# print("Enk katta son", max(arr))

# task7 Ro‘yxatdagi barcha sonlar yig‘indisini hisoblang.
# arr = [1,2,3,4,5,6,7,8,9]
# print(sum(arr))

# task 8 Elementlarni teskari tartibda chiqarish
# arr = [1,2,3,4,5,6,7,8]
# print(arr[::-1])

# Task Takrorlanuvchi elementlarni topish
# arr = [1,2,3,4,5,6,6,6,7,8,8]
# print(arr.count(6))

#Task 10.Ro‘yxatni o‘sish va kamayish tartibida saralang.
# arr = [1,3,2,5,4,6,7,8]
# print(arr.sort())

# n = int(input("Nechta baho kiritasiz"))
# arr = []
# for i in range(n):
#     baho = int(input(f"{i + 1}-bahoni kiriting:"))
#     arr.append(baho)
# ortacha = sum(arr) / len(arr)
# high = max(arr)
# low = min(arr)
# past = []
# for baho in arr:
#     if baho < 60:
#         past.append(baho)
# print("O'rtacha baholar", ortacha)
# print("Baland baholar", high )
# print("Past baholar", low)
# print("60dan past baholar", past)

n = int(input("sonlarni kiriting"))
arr = []
for i in range(n):
    baho = int(input(f"{i + 1}-bahoni kiriting"))
    arr.append(baho)
juft_sonlar = []
for baho in arr:
    if baho % 2 == 0:
        juft_sonlar.append(baho)
toq_sonlar = []
if baho  % 2 == 1:
    toq_sonlar.append(baho)
musbat = []
manfiy = []
if baho > 0:
    musbat.append(baho)
if baho < 0:
    manfiy.append(baho)


print("Juft sonlar", juft_sonlar)
print("Toq sonlar", toq_sonlar)
print("Musbat sonlar", musbat)
print("Manfiy sonlar", manfiy)