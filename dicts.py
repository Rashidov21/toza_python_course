# dict - elementlariga index orqali emas balki kalit (nom) orqali murojaat qilinadigan to'plam
# d = {
#     'one':1,
#     'two':2
# }

# d = dict(a=1,b=2)
# print(d) # 

# d = {"a":1,"b":2}

# user = {
#     "username":"master",
#     "password":"DRF%&(*U)()",
#     "age":23,
#     "skills":[1,2,3],
#     "props":{"a":1}
# }
# print(user["age"])
# # print(user["fullname"])
# print(user.get("skills"))
# print(user.get("fullname"))

# d = {"b":2}
# print(d.setdefault("a",1))
# print(d)

# keys,values,items 
# user = {
#     "username":"master",
#     "password":"DRF%&(*U)()",
#     "age":23,
#     "skills":[1,2,3],
#     "props":{"a":1}
# }
# for k in user.keys():
#     print(k)
# for k in user.values():
#     print(k)
# for k in user.items():
#     print(k)
# user = {
#     "username":"master",
#     "password":"DRF%&(*U)()",
#     "age":23,
#     "skills":[1,2,3],
#     "props":{"a":1}
# }
# print("username" in user)
# print("fullname" in user)
# print("fullname" not in user)

# user.pop("username")
# print(user)
# user.popitem()
# print(user)


# user = {
#     "username":"master",
#     "password":"DRF%&(*U)()",
#     "age":23,
#     "skills":[1,2,3],
#     "props":{"a":1}
# }
# user.clear()
# print(user)

user = {
    "username":"master",
    "password":"DRF%&(*U)()",
    "age":23,
    "skills":[1,2,3],
    "props":{"a":1}
}
user.update({"address":"Andijan", "zipcode":170100})
user["phone"] = "9399989563"
user["email"] = "email@email.com"
# print(user)

d = user.copy()
print(d)
print(user)