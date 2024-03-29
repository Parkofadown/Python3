class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_of_arrows}')


class Ogre(User):
    pass


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100)
# polymorphism
for char in [wizard1, archer1]:
    char.attack()

wizard1.attack()
archer1.attack()
print(wizard1.sign_in())
print(wizard1.email)

print(isinstance(wizard1, Wizard))

# introspection
print(dir(wizard1))