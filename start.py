

def get_user_input():
    direction = input('Enter N, S, E, or W: ').upper()
    return direction

    # if direction in ['N', 'S', 'E', 'W']:
    # print("Sorry, not a direction.")
    # return False

def move_player(player, direction):
    if direction == 'N':
        player['y'] += 1
    elif direction == 'E':
        player['x'] += 1
    elif direction == 'S':
        player['y'] -= 1
    elif direction == 'W':
        player['x'] -= 1
    else:
        print('Not a valid direction.')
        return False

player = {
    'x': 0,
    'y': 0,
}

valid_moves = ['N', 'S', 'E', 'W']

while True:
    direction = get_user_input()
    # print(direction)
    if direction in valid_moves:
        move_player(player, direction)

    elif direction == 'EXIT':
        print('Exiting. Thanks for playing!')
        break

    print(player)
