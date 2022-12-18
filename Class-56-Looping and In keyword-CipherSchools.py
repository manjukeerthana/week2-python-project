user_info = {
    'name' : 'manju',
    'age' : 24,
    'fav_movies' : ['coco','kimi no na wa'],

}
if 'name' in user_info:
    print('present')
else:
    print('not present')
if 18 in user_info.values():
    print('present')
else:
    print('not presen')
for i in user_info.values():
    print(i)

user_info_keys =user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

for i in user_info:
    print(user_info[i])

# items method
user_items = user_info.items()
print(user_items)
print(type(user_items))

# [{'name', 'harika'),('age', 24),('fav_movies',['coco','kimi no na wa'])}]

for i,j in user_info.items():
    print(f"key is {i} and value is {j}")
    
