"""
You will implement a simple 2 player racing game. Each player rolls a 6-sided die and moves forward in a lane based
on the value of the die. In order to win the game, a player must move their game piece exactly onto the last position.
If one player exceed the last position, it won't move for this round. If one player overlap with another,
player be overlapped will go back to beginning.
"""

import random


def roll_die():
    # Roll the die, given how many steps one play can jump.
    return random.randint(1, 6)


def display_state(state):
    # Show the state of two players.
    print('update: ' + ' '.join(state) + '\n************************************')


def update_position(state, num, user, rival):
    # Update the state based on the die's number.
    target = state.index(user)  # Find the position of the player right now.
    r_target = target + num  # Calculate the destiny of the player.

    #  Update the state while considering the two special conditions.
    if state.index(user) + num >= 8:
        print('The roll was too high, player ' + user + ' stays in this position')
    elif state[state.index(user) + num] != '-':
        state[r_target], state[target], state[0] = user, '-', rival
        print(user + ' kicked the rival!')
    else:
        state[target], state[r_target] = state[r_target], state[target]

    print('************************************')


def check_game_over(state):
    # Check whether the game is over, based one the final element in the list.
    if state[-1] == 'x':
        print('Player x has won!')
        return True
    elif state[-1] == 'o':
        print('Player o has won!')
        return True
    else:
        return False


def opponent(temp):
    # Update who is the player based on previous records.
    # temp.append('x')
    if temp[-1] == 'x':
        temp.append('o')
    else:
        temp.append('x')
    return temp[-1]


def main():
    state, temp, key, x = ['*', '-', '-', '-', '-', '-', '-', '-'], list(), True, roll_die()
    temp.append('x')
    print('Players begin in the starting position\n************************************')
    display_state(state)

    # The first round of x. It's a special situation so it don't involve in any user-defined functions.
    input('Player x press enter to roll!')
    print('Player x rolled a ' + str(x) + '\n************************************')
    state[0], state[x] = 'o', 'x'
    display_state(state)

    while key:
        num, user = roll_die(), opponent(temp)  # Update who the player is for this round.
        rival = 'o' if user == 'x' else 'x'  # Based on the player, check who is the rival.
        input('Player ' + user + ' press enter to roll!')  # Prompt user to press "enter" in order to process.
        print('Player ' + user + ' rolled a ' + str(num))
        update_position(state, num, user, rival)
        display_state(state)
        key = False if check_game_over(state) else True


main()
