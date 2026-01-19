# t = (1,"harf",-1,True) # tuple - o'zgarmas elementlar ketma-ketligi
# print(t)
# t = tuple("python")
# print(t)

# user_data = ("rashidov_21","Abdurahmon","Rashidov")
# print("username : ",user_data[0])
# print("first name:", user_data[1])
# t = tuple("python")
# print(t[-1]) # n

# print(len(t)) # 6
# print(t.index("n")) # 5
# print(t.count("o")) # 1

# set - unikal tartibsiz elementlar to'plami 
# s = set()
# s = {}

# s = set("python")
# print(s) # {'t', 'p', 'o', 'y', 'n', 'h'}
# s = {1,2,2,3,1,2,3}
# print(s) # {1, 2, 3}
# for i in s:print(i)

# union - birlashtirish
# s1 = set("python")
# s2 = {1,2,2,3,1,2,3}
# print(s1.union(s2)) # {1, 'y', 2, 3, 'p', 'n', 'h', 't', 'o'}

# update - setga yangi element qo'shish va yangilash 
# s1 = {1,2}
# s2 = {1,2,3}
# s2.update(s1)
# print(s2) # {1, 2, 3, 4}

# print(s2.difference(s1)) # {3}

# print(s2.intersection(s1)) # {1, 2}

# print(1 in s1) # True
# print(1 not in s1) # False
 
# print(s1 == s2) # False

# print(s1.copy()) #  {1, 2} - nuxsa olish

# s1.add(3)
# print(s1) # {1, 2, 3}
# s1.remove(3)
# print(s1) # {1, 2}

# discard - siz ko'rsatgan element agar setda mavjud bo'lsa o'chiradi 
# s1.discard(0)
# print(s1) # {2}
# pop - tasodify element  o'chiradi 
# s1.pop()
# print(s1) # {2}

# print({x for x in "set"}) # {'s', 'e', 't'}
# print(type({x for x in "set"})) # <class 'set'>

# print(tuple((i for i in range(10)))) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# frozenset - set bilan bir hil faqat o'zgarmas 
# print(frozenset("frozen")) # frozenset({'o', 'e', 'r', 'n', 'f', 'z'})
