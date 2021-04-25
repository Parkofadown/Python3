#parameters
def say_hello(name='Darth Vader', emoji=':3'):
    print(f'hello {name} {emoji}')

# positional arguments
say_hello('Richard',':)')

# keyword arguments
say_hello(emoji=';)', name='Bibi')

#Default Parameters
say_hello()

def sum(num1, num2):
    return num1 + num2

print(sum(4,5))

total = sum(10,5)
print(sum(5, total))