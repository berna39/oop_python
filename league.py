class League:
    matchs = 0
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
    def __str__(self):
        return f'league name = {self.name}'

    @classmethod #cls argument name is by convention
    def set_macths(cls, matchs):
        cls.matchs = matchs



l = League('Spor Toto Super Lig', ['Galatasaray', 'Fenerbace', 'Besiktas', 'Trabonzspor', 'kayiseri sport', 'trabzonspor'])
print(l)
print(l.teams)
print(l.matchs)
League.set_macths(12)
print(l.matchs)