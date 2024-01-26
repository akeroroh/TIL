class Dog():
    def __init__(self, sound):
        self.sound = sound

class Cat():
    sound = '야옹'

class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()

    def __str___(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

dog = Pet('멍멍')
print(dog)
