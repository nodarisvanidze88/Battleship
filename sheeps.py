letters = ["A","B","C","D","E","F","G","H",]
numbers = ["1","2","3","4","5","6","7","8",]
directions = ['v','h']

def sheeps_more_then_one(cordinates, init, direction, cell_num):
    if init in cordinates:
        return False
    call, row = list(init)
    sheep_cordinates = []
    call_index = letters.index(call)
    row_index = numbers.index(row)
    direction_v, direction_h = directions
    try:
        if direction == direction_v:
            for i in range(cell_num):
                new_cordinate = ""
                new_cordinate+=call
                new_cordinate+=numbers[row_index+i]
                if new_cordinate in cordinates:
                    return False
                else:
                    sheep_cordinates.append(new_cordinate)
        elif direction == direction_h:
            for i in range(cell_num):
                new_cordinate = ""
                new_cordinate+=letters[call_index+i]
                new_cordinate+=row
                if new_cordinate in cordinates:
                    return False
                else:
                    sheep_cordinates.append(new_cordinate)
        return sheep_cordinates
    except:
        return False
    

def sheep_one(cordinates, init):
    if init in cordinates:
        return False
    else:
        return init


