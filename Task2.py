bushes = [10, 6, 3, 4, 5, 5, 7]

max_blueberries = 0
count_3_el = bushes[0] + bushes[1] + bushes[2]

for i in range(3, len(bushes) + 2):
    count_3_el -= bushes[i - 3]
    if i == (len(bushes)):
        i = 0
    if i == (len(bushes) + 1):
        i = 1
    count_3_el += bushes[i]
    if max_blueberries < count_3_el:
        max_blueberries = count_3_el

print(max_blueberries)