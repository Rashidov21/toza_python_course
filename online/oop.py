# object - atribut, metodlari bor narsa 
# atribut - sifat 
# metodlari - harakatlari 
# class - chizma 

# class Person:
#     age = 10 # atribut
#     def __init__(self, name): # metod
#         self.name = name

#     def say_hi(self): # metod
#         print("Salom, men", self.name)

# o = Person("Ali")
# o.say_hi() # Salom, men Ali

# o2 = Person("vali")
# o2.say_hi() # Salom, men vali


class MyClass:
    
    def __init__(self): # konstruktor
        self.x = 10
        
    def print_x(self):
        print(self.x)
    
    @staticmethod
    def plus(x,y):
        return x + y
        
c = MyClass()
# c.print_x()
# print(c.x)


# getattr() - olish
# hasattr() - tekshirish
# delattr() - o'chirish
# setattr() - biriktirish

# print(getattr(c ,"x")) # 10
# # print(getattr(c ,"y")) #  AttributeError: 'MyClass' object has no attribute 'y'
# print(hasattr(c , "x")) # True
# setattr(c, "y",20) # yangi atribut biriktirilyapti
# print(getattr(c,"y")) # 20
# delattr(c,"y") # ochirish
# print(getattr(c,"y")) # AttributeError: 'MyClass' object has no attribute 'y'



# Inkapsulyatsiya 
# Meros olish 
# Polimorfizm 
db_usernames = ["mike","david"]

class User:
    date_joined = None
    last_sign = None
    is_staff = False 
    is_active = True
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def check_username(self):
        if self.username not in db_usernames:
            return True
        else:
            return False

        
u = User("admin","admin123")
u = User("simpleuser","simple123")
