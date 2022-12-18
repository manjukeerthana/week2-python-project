# fromkeys
d = {'name' : 'unknown', 'age' : 'unknown'}

d = dict.fromkeys(range(1,11),'unknown')
print(d)

d = {'name' : 'unknown', 'age' : 'unknown'}
print(d['name'])

print(d.get('name'))

if 'name' in d:
    print('present')
else:
    print('not present')

if d.get('name'):
    print('present')
else:
    print('not present')
d.clear()
print(d)

d1 = d.copy()
d1 = d
print(d1)
print(d1.popitem())
print(d)

print(d1 is d)

