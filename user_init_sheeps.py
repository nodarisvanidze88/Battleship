from sheeps import letters, numbers, directions, sheeps_more_then_one, sheep_one
from crud import writer, clear_boards,printer
from file_names import template_file, user_file
def get_user_sheeps():
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
            writer(user_file, sheep_cordinates, "O")
            printer()
        else:
            print("Impossible to create the sheep")
    while sheeps_one > 0:
        get_init_cordinate = get_users_cordinate()
        new_sheep_one = sheep_one(sheep_cordinates, get_init_cordinate)
        if new_sheep_one:
            sheep_cordinates.append(new_sheep_one)
            sheeps_one -= 1
            writer(user_file, sheep_cordinates, "O")
            printer()
        else:
            print("Impossible to create the sheep")

    clear_boards(template_file, user_file)
    writer(user_file, sheep_cordinates, "O")
    return sheep_cordinates
        
def get_users_cordinate():
    while True:
        user  = input("Add sheep init cordinate (eg. A1 or C2 and so on): ")
        if len(user)==2:
            col, row = list(user)
            if col.upper() in letters and row in numbers:
                return user.upper()
            else:
                print("Incorrect cordinate format")
        else:
            print("Wrong Cordinates")

def get_user_direction():
    while True:
        user = input("Give the direction of the sheep (eg. v or h): ").lower()
        if user in directions:
            return user
        else:
            print("Incorrect directions")
