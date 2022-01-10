from personn import Person

class Player(Person):
    def __str__(self) -> str:
        return f'Hello!, I\'m { self.name} and i\'m from { self.country }'

#print(help(Player))

pl = Player('harry Kane', 'm', 29)
print(pl)

other_player = Player.from_file('other_one.txt')
print(other_player)