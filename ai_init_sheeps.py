from sheeps import letters, numbers, directions, sheeps_more_then_one, sheep_one
from crud import writer, clear_boards
from file_names import ai_board, template_file
import random

def get_ai_sheeps():
    sheeps_more_one = 4
    sheeps_one = 2
    sheep_cordinates = []
    while sheeps_more_one > 1:
        get_init_cordinate = get_users_cordinate()
        get_direction = get_user_direction()
        new_sheep = sheeps_more_then_one(sheep_cordinates, get_init_cordinate, get_direction, sheeps_more_one)
        if new_sheep:
            sheep_cordinates.extend(new_sheep)
            sheeps_more_one -= 1
    while sheeps_one > 0:
        get_init_cordinate = get_users_cordinate()
        new_sheep_one = sheep_one(sheep_cordinates, get_init_cordinate)
        if new_sheep_one:
            sheep_cordinates.append(new_sheep_one)
            sheeps_one -= 1
    clear_boards(template_file, ai_board)
    writer(ai_board, sheep_cordinates,"O")
    return sheep_cordinates
        
def get_users_cordinate():
    cordinates = ""
    col = random.choice(letters)
    row = random.choice(numbers)
    return cordinates + col + row

def get_user_direction():
    return random.choice(directions)

