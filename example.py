import math
lst = []
while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x.split(' '))
length = 0
width = 0
for item in lst:
        if item[0] == 'UP':
            length += int(item[1])
        if item[0] == 'DOWN':
            length -= int(item[1])
        if item[0] == 'LEFT':
            width -= int(item[1])
        if item[0] == 'RIGHT':
            width += int(item[1])
distance = int(math.sqrt(length**2 + width**2))
print(distance)
