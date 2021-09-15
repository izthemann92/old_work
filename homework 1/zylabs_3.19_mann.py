# Name: Blake Mann
# PSID: 1832387
height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))
area = height*width
paint = area/350
print('Wall area:', int(area), 'square feet')
print("Paint needed: %.2f gallons"%paint)
round_paint = round(paint)
print('Cans needed:', round_paint, 'can(s)')
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23,
}
color = input("\nChoose a color to paint the wall:\n")  # type: object
print("Cost of purchasing", color, "paint:", "${}".format(paint_colors[color]*round_paint))
