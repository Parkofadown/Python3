# dict
# dictionary = {
#   'a': [1, 2, 3],
#  'b': 'hello',
# 'x': True
# }
my_list = [
    {
        'a': 1,
        'b': 2,
        'x': 3
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'c': True
    }
]
print(my_list[0]['a'])

dictionary = {
    123: [1, 2, 3],
    '123': 'hello'
}
print(dictionary['123'])

user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

user2 = dict(name='JohnJohn')
print(user.get('age', 55))
print(user2)

user3 = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print(user3.items())
# print(user3.clear())
user4 = user3.copy()
print(user3)
print(user4)
print(user3.pop('age'))
print(user3.popitem())
all_tech = ['Power Lost', 'Failure', 'no Supply']
all_limit = ['High Temp', 'Low Humid']
current_list = ['High Temp', 'Low Humid', 'Power Lost', 'no Supply']


for item in current_list:
    if item in all_limit:
        current_list.remove('High Temp')
        current_list.remove('Low Humid')
        current_list.insert(0, 'Limit')
        current_list.insert(1, 'Limit')
    if item in all_tech:
        current_list.remove('Power Lost')
        current_list.remove('no Supply')
        current_list.insert(0, 'Tech')
        current_list.insert(2, 'Tech')
print(current_list)
print(current_list.count('Tech'))
print(current_list.count('Limit'))