class Mammal:
    def walk(self):
        print("walking.....")

class Dog(Mammal):
    def bark(self):
        print("barking....")

class Cat(Mammal):
    pass                    #pass used to inheirt properties of parent class

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()

