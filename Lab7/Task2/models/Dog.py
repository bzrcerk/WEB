from Task2.models.Animal import Animal


class Dog(Animal):
    color : str

    def __init__(self, name, age, weight, color):
        super().__init__(name, age, weight)
        self.color = color

    def makeSound(self) -> str:
        return f'gafgaf!'

    def move(self) -> str:
        return f'Dog runs!'

    def __str__(self):
        return f'Dog: {self.name}, {self.age}, {self.weight}, {self.color}'