class Dog:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    def bark(self):
        return print('Woof!')
    def pet(self):
        return print('Woof Woof!')


shiba_inu = Dog('Sapporo', 6, 'Orange')
print(shiba_inu._name)
print(shiba_inu._age)
print(shiba_inu._color)
print(shiba_inu.pet())