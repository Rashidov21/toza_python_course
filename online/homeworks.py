n = int(input("Nechta baho kiritasiz"))
# arr = []
# for i in range(n):
#     baho = int(input(f"{i+1}-bahoni kiriting"))
#     arr.append(baho)
# normal = sum(arr) / len(arr)
# high = max(arr)
# low = min(arr)
# print("O'rtacha baho -", normal)
# print("Eng yuqori baho -", high)
# print("Eng past baho -", low)

# code = "python"
# trying = 0
# while trying < 3:
#     user = input("\n Parolni kiriting")
#     trying += 1
#     if user == code:
#         print("Siz to'g'ri parol kiritdingiz")
#         break
# else:
#     print("Kod hato yana urinib ko'ring")
# if trying == 3 and user != code:
#     print("Kirish bloklandi")


# n = int(input("Nechta talaba bor"))
# baholar = []
# ismlar = []
# for i in range(n):
#     data= input(f"{i +1 }- talabani ismi va nbahosini kiriting")
#     types = data.split()
# ism = types[0]
# baho = int(types[1])
# ismlar.append(ism)
# baholar.append(baho)
# medium = sum(baholar) / len(baholar)
# high = max(baholar)
# idex = baholar.index(high)
# student = ismlar[idex]
# print("Ortacha baho", medium)
# print('Eng yuqori baho', high)
# print('eng yahshi talaba', student)

balance = 0
while True:
    x = "Pul qo'yish 1 ni kiriting"
    y = 'Pul yechish'
    z = "Balansni ko'rish"
    o = "Chiqish"
    user = input("Hizmat turini tanlang")
    if user == "1":
        summa = int(input("Qo'yiladigon summani kiriting"))
        balance += summa
        print("Pul muvaffaqtiyatli qo'yildi va hozirgi balance", balance)
    elif user == y:
        summa = int(input("Yechmoqchi bo'lgan summani kiriting"))
        if summa <= balance:
            balance -= summa
        print("Pul muvaffaqiyatli yechildi va hozirgi balance", balance)
        

    elif user == z:
        print("Hozirgi balansingiz", balance)
    elif user == o:
        print("Hizmat yakulandi")
        break
    else:print("Noto'g'ri tanlov")