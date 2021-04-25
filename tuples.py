# tuples are immutable, can't be changed.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(5 in my_tuple)
user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print(user[(1, 2)])

new_tuple = my_tuple[1:4]
print(new_tuple)
x, y, z, *other = (1, 2, 3, 4, 5)
print(other)

my_tuple2 = (1, 2, 3, 4, 5, 5)
print(my_tuple2.count(5))  # how many times 5 appears
print(my_tuple2.index(5))  # where 5 appears in the index
print(len(my_tuple2))
