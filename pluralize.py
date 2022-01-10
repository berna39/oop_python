class Pluralize:
    def pluralize(self, word) -> str :
        plural = word + 's'
        return plural

    def  get_plural(self, quantity, word) -> str:
        return word if quantity <= 1 else word + 's'