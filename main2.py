import random
from crud import clear_boards, printer, opener, writer
from file_names import enemy_file, user_file, template_file, ai_board
from ai_init_sheeps import get_ai_sheeps
from user_init_sheeps import get_user_sheeps
from sheeps import letters, numbers
from user_init_sheeps import get_users_cordinate

def main():
    prepare_init_tables()
    print("\nWelcome to Buttlesheep Game\n")
    print("Your enemy is ready\n")
    get_ai_sheeps()
    print("Now is your time to generate sheeps\n")
    user_cordinates = get_user_sheeps()
    printer()
    print("Ok!!! lets start")
    enemy_cordinates = get_enemy_and_user_cordinates(ai_board)
    while len(enemy_cordinates)>0 or len(user_cordinates) > 0:
        user_shoots, test = user_shoot(enemy_cordinates)
        if test:
            enemy_cordinates.remove(user_shoots)
            writer(enemy_file, [user_shoots], "X")
            printer()
        else:
            writer(enemy_file, [user_shoots], "-")
            printer()
        # en_shoot, en_test = enemy_shoot(user_cordinates)
        # if en_test:
        #     user_cordinates.remove(en_shoot)
        #     writer(enemy_file, [user_shoot], "X")
        #     printer()
        # else:
        #     writer(enemy_file, [user_shoot], "-")
        #     printer()


def get_enemy_and_user_cordinates(board):
    data = opener(board)
    cordinates_tuple = []
    final_cordinates = []
    for rows in range(len(data)):
        for cols in range(len(data[rows])):
            if data[rows][cols] == "O":
                cordinates_tuple.append((cols, rows))
    for x,y in cordinates_tuple:
        temp = ""
        temp+= letters[x-1]
        temp+=str(y)
        final_cordinates.append(temp)
    return final_cordinates


def prepare_init_tables():
    clear_boards(template_file, enemy_file)
    clear_boards(template_file, ai_board)
    clear_boards(template_file, user_file)

def user_shoot(enemy_cordinates):
    shoot = get_users_cordinate()
    if shoot in enemy_cordinates:
        return shoot, True
    else:
        return shoot, False
    
def enemy_shoot(user_cordinat):
    shoot_col = random.choice(letters)
    shoot_row = random.choice(numbers)
    enemy_shoot = shoot_col+shoot_row
    if enemy_shoot in user_cordinat:
        return enemy_shoot, True
    else:
        return enemy_shoot, False

if __name__=="__main__":
    main()


