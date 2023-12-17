import keyboard
from time import sleep
#this is first alpha of ATF cheats 0.1
print('Welcome to ATF cheats.\nversion: 0.1 alpha\nBasic delay is 4 seconds.\n\n')
text = str(input('Insert text to type here: '))
sleep(4)
for character in text:
    keyboard.press(character)
    sleep(0.15)
