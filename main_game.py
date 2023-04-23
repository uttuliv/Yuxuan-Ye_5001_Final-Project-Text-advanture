"""
Final Project - Text adventrue- main game
Student: Yuxuan Ye
Semester: 2023 Spring
Course: 5001
"""
import ast
import os
import sys
from text_game import Player, print_pause,read_zonemap, player_move,prompt,player_kind, help_menu

def first_selection():
    option = str.capitalize(input("Should I get into this house? \n['Yes', 'No']:"))
    if option == 'No':
        print_pause("Only brave items can live in this world! YOU DIE!")
        sys.exit()
    return None


def setup_game():
    os.system('clear')
    # choosing your kind ---human, cat or dog
    print_pause("You push this heavy wooden door open, creak and groan... ..., \n"
                "You look at your hand, which is putting on the door, it looks a little bit strange...,\n"
                "What kind of creature is me?\n ['human', 'cat', 'mouse']")
    player_hp = player_kind()
    # collecting player's name
    print_pause("No matter who you are, you are my dear visitor now. So, what's your name?\n")
    player_name = input("> ")
    #Player
    print_pause(f"\nWelcome! {player_name}! If you have any question, please tap ['help'] to get more information."
                                 "If you don't have any question, please type ['no']\n")
    command = str.casefold(input("> "))
    if command == 'help':
        help_menu()
    else:
        pass
    return player_name, player_hp


def main():
    os.system('clear')
    print_pause("You woke up in front of a huge dark house, a voice appears in your mind: \n"
                "'Hello my dear client, welcome to the Unknown House!'\n"
                "The sound seems really strange......")
    first_selection()
    player_name, player_hp = setup_game()
    myPlayer = Player(name = player_name, hp = player_hp)
    map = read_zonemap('zonemap.txt')
    print_pause(map[myPlayer.location]['DESCRIPTION'])
    while myPlayer.hp > 0:
        print('\n' + '=========')
        prompt(map, myPlayer)
        if myPlayer.location == 'Forest':
            myPlayer.sub_hp(3)
    print_pause(f"Sorry, {myPlayer.name}. You die. See you next time>")
    sys.exit()


main()

