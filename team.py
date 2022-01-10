#my class
class Team:
    wins = 0
    loss = 0
    draws = 0

    def __init__(self, name, city, nickname, bio, players):
        self.name = name
        self.city = city
        self.nickname = nickname
        self.bio = bio
        self.players = players

    def __str__(self) -> str:
        return 'We are {} and we are from {}'.format(self.name, self.city)

    def introduce(self) -> str:
        print(f'{self.name} : {self.bio}')

    def get_wins(self):
        print(f'{self.name} : { self.wins }')

#Practice
man_city = Team('Manchester city', 'Manchester', 'Blues', 'One of the bigs teams of the decade 2010 - 2020', None)
liecester = Team('Liecester city', 'Liecester', 'Foxes', 'We\'re foxes and we\'re fearless', None)

print('------ Welcome to the premier league -------')
print(man_city)
print(liecester)

#class attributes
print(man_city.name)
print(liecester.city)

#instance attribute [ added dynamicly ] 
man_city.manager = 'Pep Guardiola'
print(man_city.manager)

#other way to call a method
Team.introduce(liecester)
man_city.introduce()

#adding players
city_player = ['Ilkay gindoghan', 'Bernardo silva', 'Ryad Mahrez', 'Kevin de Bruyne', 'Ruben Dias', 'Kyle Walker', 'Joao Cancelo', 'Reheem sterling']
man_city.players = city_player
print(man_city.players)

liecester_players = ['Jamie vardy', 'Youri tielmans', 'James madisson', 'Ayoze perez', 'Kelechi iheanacho', 'Caster Schmeichel', 'Wilfried ndidi', 'Patson daka']
liecester.players = liecester_players
print(liecester.players)

#more info about teams 
man_city.get_wins()