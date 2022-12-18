# more about get, two same keys in dictionaries

user = {'name': 'manju', 'age': 18, 'age': 20}
print(user)
print(user.get('name'))
print(user.get('names'))
print(user.get('fav', 'not found ! '))