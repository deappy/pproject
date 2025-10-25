import os
terminal_width = os.get_terminal_size().columns

print("=======================================================================================".center(terminal_width))

text = r'''
 _
| |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___| 
'''

print(text.center(terminal_width))
print('\n\n\n')

print("=======================================================================================".center(terminal_width))
print("Welcome to TREASURE ISLAND!".center(terminal_width))
print("=======================================================================================".center(terminal_width))

print('You are required to reach the island to acquire wealth from TREASURE!')
print("=======================================================================================".center(terminal_width))
choice1 = input("You are required to choose \"left\" or \"right\". Enter your choice!").lower()