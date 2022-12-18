# some more methods to add data in our List
# insert method
# how to join(concatenate) two List
# expand method
# difference between append and extend method

fruits1 = ['mango', 'orange']
fruits1.insert(2, "grapes")
print(fruits1)
fruits2 = ['grapes','apple']
fruits = fruits1 + fruits2
print(fruits)
fruits1.extend(fruits2)
fruits.append(fruits2)
print(fruits1)
print(fruits2)