user_info = {
    'name' : 'manju',
    'age' : 18,
    'course' : 'btech',
}

user_info['course'] = ['AI','CyberSecurity']
print(user_info)

popped_item = user_info.pop('course')
print(f"popped item is {popped_item}")
print(user_info)

popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))