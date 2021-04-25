# OOP
class PlayerCharacter:
    membership = True # class object attribute
    def __init__(self, name,age):
            self.name = name # attributes
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1,num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter("Harry Potter", 35)
player2 = PlayerCharacter("Sloppy Toppy", 20)
player2.attack = 50

print(player2.attack)
print(player1.name)
print(player1.age)
print(player1.shout())
print(player2.shout())
print(player2.name)
print(player2.age)
print(player1.membership)
print(player2.membership)
print(player1.adding_things(2,3))
player3 = PlayerCharacter.adding_things(2,3)
player4 = PlayerCharacter.adding_things2(2,3)
# help(PlayerCharacter)

# print(help(PlayerCharacter))