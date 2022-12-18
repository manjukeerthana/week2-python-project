# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
mixed = (1, 2, 3, 4, 0)

nums = (1,)
words = ('word1',)
print(type(nums))
print(type(words))


guitars  = 'yamaha', 'taylor'
print(type(guitars))

guitarists = ('manju', 'orange', 'kiwi')
guitarist1, guitarist2, guitarsit3 = guitarists
print(guitarist1)

favorites = ('southern mangolia', 'landscape')
favorites[1].pop()
favorites[1].append("we made it")
print(favorites)

print(min(mixed))
print(max(mixed))
print(sum(mixed))
