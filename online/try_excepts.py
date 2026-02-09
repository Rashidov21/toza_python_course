# Interpretator - xatoliklarga tekshiruvchi dastur 
# Kompilyator - kodni mashina kodiga (0,1) o'girib beradigan dastur

# x = 0
# print(x / 0) # ZeroDivisionError: division by zero
# print("hello")

# Xatolik turlari :
#     1-Synax, sintaksiz xatoliklar
#     2-mantiqiy xatoliklar
#     3-kod ishlashi vaqtida vujudga kelishi mumkin bolgan xatoliklar

# name = "John"
# print(nmae) # NameError: name 'nmae' is not defined

# try , except, else ,finally 
# try: # xatolik bo'lishi mumkin bolgan kod yoziladi
#     x = 4
#     result = x / 2
#     print(result)
# except: # xatolik chiqsa ishlaydigan kod
#     print("0 ga bolib bo'lmaydi")
# else:# agar xatolik chiqmasa ishlaydigan kod
#     print("Xatolik yo'q kod ishlaydi")
# finally: # xatolik chiqsa-chiqmasa ishlaydigan kod
#     print("tekshirish yakunlandi")
    
    
# try: 
#     x = 4
#     result = x / 0
#     print(result)
# except Exception as er:
#     print(f"Xatolik yuz berdi : {er}") # Xatolik yuz berdi : division by zero

# try: 
#     x = open("test.pdf","r")
# except Exception as er:
#     print(f"Xatolik yuz berdi : {er}") # Xatolik yuz berdi : [Errno 2] No such file or directory: 'test.pdf'
    
    
# raise - xatolikni qo'zg'atish, ko'tarish operatori 
# x = open("test.pdf","r") # FileNotFoundError
# try: 
#     x = open("test.pdf","r")
# except Exception as e:
#     # print(e)
#     raise ValueError("Fayl yo'q, fayl yoki papka notogri korsatildi")

# try,except,else,finally,raise