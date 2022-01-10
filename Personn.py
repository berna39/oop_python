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
        
    def __str__(self) -> str:
        return f'I\'m { self.name} and i\'m from { self.country }'

    @classmethod
    def from_string(cls, person_as_string):
        data = person_as_string.split('-')
        return cls(data[0], data[1], data[2])


#p = Person('Shango jos', 'm', 'Kenya')
#p.introduce()
#p.walk()

person_fr_str = Person.from_string('Robinson-m-Kneya')
print(person_fr_str)
