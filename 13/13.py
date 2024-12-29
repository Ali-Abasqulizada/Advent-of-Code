testcase = open('13/13.txt', 'r').read().split('\n')

inputs = []

index = 0

while index + 3 <= len(testcase):
    buttons = []
    for i in range(2):
        button = testcase[index + i].split('+')
        buttonx = int(button[1].split(',')[0])
        buttony = int(button[2])
        buttons.append(buttonx)
        buttons.append(buttony)
    index += 2
    prize = testcase[index].split('=')
    prizex = int(prize[1].split(',')[0])
    prizey = int(prize[2])
    buttons.append(prizex)
    buttons.append(prizey)
    inputs.append(tuple(buttons))
    index += 2

print(inputs)