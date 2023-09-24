ages = { 'kevin': 59, 'alex': 29, 'bob': 40}
print (ages)
# key must be unique
print(ages['kevin'])
# dictionaries are mutable
ages['kayla'] = 21
print (ages)
ages['kevin'] = 60
print (ages)
del ages['kevin']
print (ages)
print('kevin' in ages)
print('alex' in ages)

# how to create dictionaries
weights = dict(kevin = 16, bob = 240, kayla = 134)
print(weights)

colors = dict([('kevin', 'blue'), ('bob','green'), ('kaykla','red') ])
print(colors)

# methods
ages = { 'kevin': 59,  'bob': 79}
print (list(ages.keys()))
print (list(ages.values()))
print(list(ages.items()))