import csv                                                              # იმპორტი csv ბიბლიოთეკა
from sheeps import letters                                              # იმპორტი ასოები
from file_names import enemy_file, user_file                            # იმპორტი ფაილების სახელები
import tabulate                                                         # იმპორტი ტაბულეიტი

def opener(file_name):                                                  # ფუნქციის ინიცირება რომელიც ფაილს წაიკითხავს
    board = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for i in reader:
            board.append(i)
    return board


def writer(file_name, coordinates, symbol):
    board = opener(file_name)
    for cord in coordinates:
        col = cord[0]
        row = cord[1]
        ind = letters.index(col)
        for i in board:
            if i[0] == row:
                i[ind+1] = symbol
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        for i in board:
            writer.writerow(i)

def clear_boards(template, file_name):
    clear_data = opener(template)
    with open(file_name,"w", newline="") as file:
        writer = csv.writer(file)
        for i in clear_data:
            writer.writerow(i)

def printer():
    enemy = opener(enemy_file)
    user_board = opener(user_file)

    table1 = tabulate.tabulate(enemy, tablefmt="mixed_grid")
    table2 = tabulate.tabulate(user_board, tablefmt="mixed_grid")

    lines1 = table1.split('\n')
    lines2 = table2.split('\n')

    combined_lines = [line1 + '  ' + line2 for line1, line2 in zip(lines1, lines2)]

    print('\n'.join(combined_lines))