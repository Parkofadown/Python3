# list , set ,dictionary comprehensions
# my_list = [param for param in iterable]


my_list = {char for char in 'hello'}
my_list2 = {number for number in range(0, 100)}
my_list3 = {num * 2 for num in range(0, 100)}
my_list4 = {num ** 2 for num in range(0, 100) if num % 2 == 0}

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
