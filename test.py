import random

colors = {
    'purple': '#7A4198',
    'turquoise':'#9ACBC9',
    'orange': '#EF5C35',
    'blue': '#19457D',
    'green': '#5AF9B5',
    'red': ' #E04160',
    'yellow': '#F9F985'
}


color = {}
# color=random.choice([color for color_value in colors.values()]
for i in range(3):
    color_random = (random.choice(list(colors.keys())))
    color[color_random] = colors[color_random]
    colors.pop(color_random)

# color = random.choice(list(colors.keys()))
print(f'The new color is: {color}')