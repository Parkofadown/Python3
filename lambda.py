# lambda expressions are one time anyoumous functions

# lambda param: action(param)

my_list = [1, 2, 3]
print(list(map(lambda item: item*2, my_list)))
print(my_list)
