class Person:
    name = '',
    gander = '',
    country = ''
    def __init__(self, name, gander, country):
        self.name = name
        self.gander = gander
        self.country = country
    def introduce(self):
        print(f' name={self.name}, gander={self.gander},country={self.country}')
    def walk(self):
        print('i\'m walking alone')


p = Person('Shango jos', 'm', 'Kenya')
p.introduce()
p.walk()
