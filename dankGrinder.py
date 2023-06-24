import pyautogui #pip install pyautogui
from colorama import Fore
import random
import time

random_time = random.randint(3,6)
commands = ['beg', 'fish', 'dig', 'hunt', 'balance', 'shop sell all']

def command(command):
    pyautogui.write("/")
    time.sleep(0.9)
    pyautogui.write(command)
    time.sleep(1.4)
    pyautogui.press('enter')
    time.sleep(1.4)
    pyautogui.press('enter')
    time.sleep(1.5)


user_input = input(Fore.BLUE + "Welcome to DankGrinder Program.\nThis program will grind dank money for you while you are AFK.\nSay 's' and switch to discord the script will start in 5 seconds automatically\nYou can also add your own commands by saying 'new'\n")

if user_input == "s":

    time.sleep(5)

    for i in range(100):
        
        for j in range(6):
        
            command(random.choice(commands))
            time.sleep(random_time)

        time.sleep(25)

elif user_input == "new":

    user_input = input(Fore.WHITE + "Enter the command you want to add.\n It will run automatically like our built in commands!\n")

    commands.append(user_input)

    print("The command is added successfully! The script will start in 5 seconds so switch to discord quickly!\n")

    time.sleep(5)

    for i in range(100):
        
        for j in range(6):
        
            command(random.choice(commands))
            time.sleep(random_time)

        time.sleep(25)
