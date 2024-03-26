import tabulate
import csv
import random
import sys

def main():
    print("Welcome to battleship game <3")
    cleaner("user_board.csv")
    ship_setter()
    ship_setter_for_ai()
def opener(file_name):
    board = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for i in reader:
            board.append(i)
    return board

def printer():
    ai_board = opener("ai_board.csv")
    user_board = opener("user_board.csv")

    table1 = tabulate.tabulate(ai_board, tablefmt="mixed_grid")
    table2 = tabulate.tabulate(user_board, tablefmt="mixed_grid")

    lines1 = table1.split('\n')
    lines2 = table2.split('\n')

    combined_lines = [line1 + '  ' + line2 for line1, line2 in zip(lines1, lines2)]

    print('\n'.join(combined_lines))

def writer(file_name, coordinate):
    board = opener(file_name)
    new_board = []

    coordinate = list(coordinate)
    row = coordinate[0]
    col = coordinate[1]

    with open(file_name, "w") as file:
        writer = csv.writer(file)
        for i in board:
            if i[0] == row:
                i[int(col)] = "o"
                new_board.append(i)
            else:
                new_board.append(i)
        for i in new_board:
            writer.writerow(i)

def cleaner(file_name):
    board = opener(file_name)
    new_board = []
    with open("clear_board.csv", "r") as clearer:
        reader = csv.reader(clearer)
        for i in reader:
            new_board.append(reader)

def input_for_ship(argument):
    letters = ["a","b","c","d","e","f","g","h",]
    numbers = ["1","2","3","4","5","6","7","8",]

    print(f"Now we are creating {argument} point ship.")

    start = input("Enter the coordinate where starts your ship: ")
    direction = input("Enter the direction. horizontaly or verticaly (ex. H/V): ")

    if len(start) == 2 \
        and any(start.lower().startswith(letter) for letter in letters) \
        and any(start.lower().endswith(number) for number in numbers) \
        and (direction == "h" or direction == "v"):
        return start, direction

def clone_of_input_for_ship(argument, start, direction):
    letters = ["a","b","c","d","e","f","g","h",]
    numbers = ["1","2","3","4","5","6","7","8",]

    if len(start) == 2 \
        and any(start.lower().startswith(letter) for letter in letters) \
        and any(start.lower().endswith(number) for number in numbers) \
        and (direction == "h" or direction == "v"):
        return start, direction

def ship_validator(coordinate, direction, lenght):
    coordinate = list(coordinate)
    if direction == "h":
        if (8 - int(coordinate[1]) + 1) < lenght:
            return False
        else:
            return True
    elif direction == "v":
        if (72 - ord(coordinate[0]) + 1) < lenght:
            return False
        else:
            return True

def ship_list_generator(coordinate, direction, lenght):
    coordinate = list(coordinate)
    coordinates = []
    if direction == "v":
        for i in range(ord(coordinate[0]), ord(coordinate[0]) + lenght):
            coordinates.append(f"{chr(i)}{coordinate[1]}")
    elif direction == "h":
        for i in range(int(coordinate[1]), int(coordinate[1]) + lenght):
            coordinates.append(f"{coordinate[0]}{i}")
    return coordinates

def ship_setter_for_ai():
    ship_list = []
    new_ship_list_2 = set()

    letters = ["A","B","C","D","E","F","G","H",]
    numbers = ["1","2","3","4","5","6","7","8",]
    directions = ["h", "v"]

    for i in range(4,0, -1):
        letter = random.choice(letters)
        number = random.choice(numbers)
        coordinate = f"{letter}{number}"

        direction = random.choice(directions)

        coordinate, direction = clone_of_input_for_ship(i, coordinate, direction)
        ship_avaliablety = ship_validator(coordinate, direction, i)

        if ship_avaliablety:
            if coordinate not in new_ship_list_2:
                ship_list.append(ship_list_generator(coordinate, direction, i))
                for a in ship_list:
                    for b in a:
                        new_ship_list_2.add(b)
            else:
                sys.exit()
        else:
            sys.exit()

    coordinate, direction = input_for_ship(1)
    ship_avaliablety = ship_validator(coordinate, direction, 1)

    if ship_avaliablety:
        ship_list.append(ship_list_generator(coordinate, direction, 1))
        for a in ship_list:
            for b in a:
                new_ship_list_2.add(b)
    else:
        print("Ivalid input!")

    for i in new_ship_list_2:
        writer("ai_board.csv", i)

    return ship_list, new_ship_list_2

def ship_setter():
    ship_list = []
    new_ship_list = set()

    for i in range(4,0, -1):
        coordinate, direction = input_for_ship(i)
        ship_avaliablety = ship_validator(coordinate, direction, i)

        if ship_avaliablety:
            if coordinate not in new_ship_list:
                ship_list.append(ship_list_generator(coordinate, direction, i))
                for a in ship_list:
                    for b in a:
                        new_ship_list.add(b)
            else:
                sys.exit("the coordinate what you entered is occupied.")
        else:
            sys.exit("Ivalid input!")


    coordinate, direction = input_for_ship(1)
    ship_avaliablety = ship_validator(coordinate, direction, 1)

    if ship_avaliablety:
        ship_list.append(ship_list_generator(coordinate, direction, 1))
        for a in ship_list:
            for b in a:
                new_ship_list.add(b)
    else:
        print("Ivalid input!")

    for i in new_ship_list:
        writer("user_board.csv", i)

    return ship_list, new_ship_list

if __name__ == "__main__":
    main()