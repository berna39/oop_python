from pluralize import Pluralize

p = Pluralize()

print(p.pluralize('phone'))

print(p.get_plural(-3, 'song'))