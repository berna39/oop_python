import pluralize

p = pluralize.Pluralize()

print(p.pluralize('phone'))

print(p.get_plural(3, 'song'))