# Name Blake Mann
# PSID: 1832387
# 12.9

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':

    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))

    except ValueError:
        age = 0
        print('{} {}'.format(name, age))

    parts = input().split()
    name = parts[0]

    # Get next line
