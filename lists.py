list
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

# Data Structure
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
    ]
print(amazon_cart[0])
print(amazon_cart[1])
print(amazon_cart[2])
# List Slicing
print(amazon_cart[0:2])
print(amazon_cart[0::2])
amazon_cart[0] = 'laptop'
print(amazon_cart)
print(amazon_cart[0:3])
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

matrix = [
[1,0,1],
[0,1,0],
[1,0,1]
]
print(matrix)

print(matrix[0][1])

basket = [1,2,3,4,5,2]
new_list = basket.append(100)
print(basket)
print(new_list)

# adding
new_list = basket.extend([100,101])
print(basket)
print(new_list)

#removing
basket.pop()
print(basket)
new_list = basket.remove(4)
print(new_list)
new_list = basket.pop(5)
print(new_list)

print(basket.index(2)) # looks for 2 in the basket index
print(2 in basket)
print(basket.count(2))
print(sorted(basket))
print(basket)
basket.reverse()
print(basket)


print(list(range(101)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is','JOJO'])
print(sentence)
print(new_sentence)

#list unpacking
a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)