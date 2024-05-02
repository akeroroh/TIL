# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

class Cat(Animal):
    def __init__(self, sound):
        super().__init__()
        Cat.sound = sound

    def meow(self):
        print(f'{Cat.sound}!')



cat1 = Cat("야옹")
cat1.meow()
