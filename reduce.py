from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumlator(acc, item):
    return acc + item


print(reduce(accumlator, my_list, 0))
print(my_list)
