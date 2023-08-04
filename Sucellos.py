from rgbprint import *
import os
import time


def menu():
    os.system('clear')
    os.system('cls')
    gradient_print(
    """                                                                                 
______                    __     __                   
\  ___)                   \ \    \ \                  
 \ \    _   _ __   __ ___  \ \    \ \    _   _   ____ 
  > >  | | | |\ \ / // __)  > \    > \  | | | | /  ._)
 / /__ | |_| | \ v / > _)  / ^ \  / ^ \ | |_| |( () ) 
/_____) \___/   > <  \___)/_/ \_\/_/ \_\ \___/  \__/  
               / ^ \                                  
              /_/ \_\                                 """,
              
    start_color=Color.blue, 
    end_color=Color.dark_magenta
)
    gradient_print("\n  Dev by pliplou \n  version: 0.0.1", start_color=Color.green, end_color=Color.white)
    rgbprint("\n\nThe dev is not responsible for damage caused by the tool. Warning, educational purpose \n\n", color='red')

    rgbprint("""
        |01|--------|06|--------
        |02|--------|07|--------
        |03|--------|08|--------
        |04|--------|09|--------
        |05|--------|10|--------

                                [99]quit

    """, color="red")
    value = int(input("enter a number --->"))

    if value == 1:
        rgbprint("[Error] number selected is not correct", color="dark_red")
        input()
        menu()

    if value == 99:
        os.system('cls')
        os.system('clear')

menu()



