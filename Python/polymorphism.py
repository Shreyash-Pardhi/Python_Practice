class Animal:
    def __init__(self, name):
        self.name = name
        
    def movement(self):
        print(self.name, "can walk.")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def movement(self):
        print(self.name, "can fly.")

if __name__ == '__main__':
    animal = Animal('Dog')
    bird = Bird('sparrow')
    animal.movement()
    bird.movement()