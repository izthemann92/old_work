# Name: Blake Mann
# PSID: 1832387
roster = {}

for i in range(5):
    jn = int(input("Enter player %d's jersey number:\n" %(i+1)))

    roster[jn] = int(input("Enter player %d's rating:\n" % (i + 1)))
    print('')

jers = list(roster.keys())

jers.sort()

print("ROSTER")

for jers in jers:
    print("Jersey number: %d, Rating: %d" %(jers,roster[jers]))

def menu():
    print('a - Add player\n')
    print('d - Remove player\n')
    print('u - Update player rating\n')
    print('r - Output players above a rating\n')
    print('o - Output roser\n')
    print('q - Quit\n')

print(menu)



