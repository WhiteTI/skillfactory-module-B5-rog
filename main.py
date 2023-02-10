def create_field():
    field = [['-'] * 3 for i in range(3)]
    return field


def show_field(field):
    coord = '  0 1 2'
    print(coord)
    for i, row in enumerate(field):
        print(i, end=' ')
        for elem in row:
            print(elem, end=' ')
        print()


def players_input(field, player):
    player_move = input(f'Ходит игрок {player}, введите координаты в формате строка столбец: ').split()
    
    if len(player_move) != 2:
        print('Введите две координаты')
        return None

    if not (player_move[0].isdigit() and player_move[1].isdigit()):
        print('Введите числа')
        return None
    
    player_move = list(map(int, player_move))
    x, y = player_move[0], player_move[1]
    
    if not((0 <= x <= 2) and (0 <= y <= 2)):
        print('Введите правильные координаты')
        return None

    if field[x][y] != '-':
        print('Клетка занята')
        return None

    return x, y


def victory_condition(field, player):
    condition = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    field_list=[]
    
    for row in field:
        field_list += row

    indices = set([i for i, x in enumerate(field_list) if x == player])
    
    for i in condition:
        if len(indices.intersection(set(i))) == 3:
            return True

    return False


def game_progress(field, players, progress = 1):
    while True:
        player_one_coord = players_input(field, players[0])
        if player_one_coord is not None:
            progress += 1
            break
    field[player_one_coord[0]][player_one_coord[1]] = 'x'
    show_field(field)
    
    if victory_condition(field, players[0]):
        return print(f'Выйграл {players[0]}')
    
    print()
    
    if progress == 10:
        return print('Ничья')
    
    while True:
        player_two_coord = players_input(field, players[1])
        if player_two_coord is not None:
            progress += 1
            break
    field[player_two_coord[0]][player_two_coord[1]] = 'o'
    show_field(field)
    
    if victory_condition(field, players[1]):
        return print(f'Выйграл {players[1]}')
    
    print()
    
    return game_progress(field, players, progress) 


def start_game():
    player_one = 'x'
    player_two = 'o'
    
    field = create_field()
    show_field(field)
    
    game_progress(field, (player_one, player_two))

start_game()