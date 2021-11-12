import os
import colorama
from colorama import init
from colorama import Fore

init()

x = 6
y = 6
def draw(a):
    global x
    global y
    height = 11
    length = 11
    if a=="1" and y > 0:
        y-=1
    elif a=="2" and y < height-1:
        y+=1
    elif a=="3" and x > 0:
        x-=1
    elif a=="4" and x < length:
        x+=1
    elif a=="5":
        quit()
    else:
        print("Incorrect input...")
    changedX = x-1
    changedLength = length-x
    os.system('cls')
    for i in range(height):
        if i != y:
            print('\u001b[47m' + "O"*length)
        else:
            print('\u001b[47m' + "O"*changedX + ('\u001b[41m' + 'X') + '\u001b[0m' + '\u001b[47m' + "O"*changedLength)
    print('\u001b[0m')


draw("2")
while 1==1:
    print("="*11)
    print("Made by github.com/skill3472")
    print("="*11)
    print("\n(1) UP (2) DOWN (3) LEFT (4) RIGHT (5) QUIT: \n")
    draw(input())
