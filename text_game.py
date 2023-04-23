"""
Final Project - Text adventrue
Student: Yuxuan Ye
Semester: 2023 Spring
Course: 5001
"""
import cmd
import textwrap
import sys
import os
import time
import ast

screen_width = 100


### player setup
class Player:
    def __init__(self, name = '', hp = 2):
        self.name = name
        self.hp = hp
        self.location = 'Entrance'

    def sub_hp(self, num):
        self.hp -= num


def player_kind():
    player_kind = str.casefold(input("> "))
    if player_kind == 'human':
        print("You are an arrogant human. You should pay for your arrogance. hp = 1\n")
        hp = 1
    elif player_kind == 'cat':
        print("You are cute and clever. hp = 2\n")
        hp = 2
    elif player_kind == 'mouse':
        print("Mouse life matters! hp = 3\n")
        hp = 3
    else:
        print("Please type a valid choice.\n")
        player_kind()
    return hp
    

def print_pause(text, width=70):
    """
    make the strings more RPG style.
    """
    wrapper = textwrap.TextWrapper(width=width)
    lines = wrapper.wrap(text=text)
    for line in lines:
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        sys.stdout.write('\n')
        sys.stdout.flush()
    return None

def help_menu():
    print_pause("- Use ['left','right','up'] to move \n Use['Leave'] to back to regret")
    print_pause('- Type the commands to do them')
    print_pause('- Here are some other movements, please follow the hints.')

#adventure
def read_zonemap(filename) -> dict[str, str]:
    """
    Open the zonemap file, returns the current location.
    use dictionary to return every steps

    """
    with open('zonemap.txt', 'r') as file:
        whole_map = file.read()
        map = ast.literal_eval(whole_map)
    return map

def prompt(map, myPlayer):
    action = str.capitalize(input('>What would you like to do?\n>'))
    acceptable_actions = ['Left', 'Right', 'Up', 'Leave', 'Open', 'Sleep', 'Quit']
    while action not in acceptable_actions:
        print('Unknown action, try again. \n')
        action = str.capitalize(input('What would you like to do?'))
    if action == 'Quit':
        sys.exit()
    elif action in ['Left', 'Right', 'Up', 'Leave']:
        try:
            player_move(map, myPlayer,action)
            print_pause(map[myPlayer.location]['DESCRIPTION'])
        except KeyError:
            print("You can't go this way now.")
    elif action in ['Open', 'Sleep']:
        player_damage(myPlayer, map, action)
        print(f"Your hp is: {myPlayer.hp} now.")


def player_move(map, myPlayer, action):
    if action == 'Left':
        des = map[myPlayer.location]['Left']
    elif action == 'Right':
        des = map[myPlayer.location]['Right']
    elif action == 'Up':
        des = map[myPlayer.location]['Up']
    elif action == 'Leave':
        des = map[myPlayer.location]['Leave']
    print_pause(f"You have moved to the {des} .")
    myPlayer.location = des

def player_damage(myPlayer, map, action):
    if action in ['Open','Sleep']:
        myPlayer.sub_hp(1)
        print_pause(map[myPlayer.location][action])
