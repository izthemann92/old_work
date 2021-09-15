# Name: Blake Mann
# PSID: 1832387
lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print('\nLemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar\n')
num_servings = float(input('How many servings would you like to make?\n'))
cups_lemon = lemon/servings*num_servings
cups_water = water/servings*num_servings
cups_agave = agave/servings*num_servings

print('\nLemonade ingredients - yields', '{:.2f}'.format(num_servings), 'servings')
print('{:.2f}'.format(cups_lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(cups_water), 'cup(s) water')
print('{:.2f}'.format(cups_agave), 'cup(s) agave nectar\n')
print('Lemonade ingredients - yields', '{:.2f}'.format(num_servings), 'servings')
gal_lemons = cups_lemon/16
gal_water = cups_water/16
gal_agave = cups_agave/16
print('{:.2f}'.format(gal_lemons), 'gallon(s) lemon juice')
print('{:.2f}'.format(gal_water), 'gallon(s) water')
print('{:.2f}'.format(gal_agave), 'gallon(s) agave nectar')
