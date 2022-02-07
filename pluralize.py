class Pluralize:
    def pluralize(self, word) -> str :
        plural = word + 's'
        return plural

    def get_plural(self, quantity, word) -> str:
        if quantity < 0:
            return 'The quatity should\'t be under 0'

        return word if quantity <= 1 else word + 's'