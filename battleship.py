import random
from collections import OrderedDict, deque


COLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ROWS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def read_field(f):
    """
    (str) -> (data)
    """
    grid = OrderedDict()
    d = deque()
    with open(f,"r") as fl:
        lines = fl.readlines()
        for line in lines:
            line = line.rstrip("\n")
            d.extend(line)
    for row in ROWS:
        for col in COLS:
            v = d.popleft()
            if v == " ":
                v = '_'
            grid[(col, row)] = v


    return grid


#print(read_field("field.txt"))
def has_ship(grid,pos):
    """
    :param grid: dictionary  containing battleship grid
    :param pos:tuple(col,row) position on grid
    :return:boolean if ship is located in this pos

    """
    if grid[pos] == '*':
        return True
    else:
        return False


def get_right(pos):
    col, row = pos
    index = COLS.index(col)
    if index == 9:
        return None
    else:
        return (COLS[index + 1], row)


def get_left(pos):
    col, row = pos
    index = COLS.index(col)
    if index == 0:
        return None
    else:
        return (COLS[index - 1], row)


def get_down(pos):
    col, row = pos
    index = ROWS.index(row)
    if index == 9:
        return None
    else:
        return (col,ROWS[index + 1])


def get_up(pos):
    col, row = pos
    index = ROWS.index(row)
    if index == 0:
        return None
    else:
        return (col,ROWS[index - 1])


def ship_size(grid,pos):
    """
    (data, tuple) -> (tuple)
    """
    if has_ship(grid,pos):
        size = 1
    else:
        return 0
    cur_pos = pos

    direction = 'n'
    if get_left(cur_pos):
        if has_ship(grid,get_left(cur_pos)):
            direction = 'h'
    if get_right(cur_pos):
        if has_ship(grid,get_right(cur_pos)):
            direction = 'h'
    if get_up(cur_pos):
        if has_ship(grid,get_up(cur_pos)):
            direction = 'v'
    if get_down(cur_pos):
        if has_ship(grid,get_down(cur_pos)):
            direction = 'v'
    if direction == 'n':
        return size

    col, row = pos
    if direction == 'h':
        while get_left((col, row)) and has_ship(grid,get_left((col, row))):
            col, row = get_left((col, row))
        while get_right((col, row)) and has_ship(grid,get_right((col, row))):
            col, row = get_right((col, row))
            size += 1
    else:
        while get_up((col, row)) and has_ship(grid,get_up((col, row))):
            col, row = get_up((col, row))
        while get_down((col, row)) and has_ship(grid,get_down((col, row))):
            col, row = get_down((col, row))
            size += 1
    return size

grid = read_field("field.txt")
# for k in grid:
#     print(k, grid[k])
#print(get_right(("I", 2)))
#print(get_right(("J", 2)))
#print(get_left(("B", 2)))
#print(get_left(("A", 2)))
#print(get_down(("I", 9)))
#print(get_down(("I", 10)))
#print(get_up(("I", 2)))
#print(get_up(("I", 1)))

#print(has_ship(grid,("C",4)))
#print(has_ship(grid,("D",4)))

# print(grid[("C",1)])
# print(grid[("D",4)])

#print(ship_size(grid, ('E',3)))
# print(has_ship(grid,("I",5)))
# print(has_ship(grid,("I",6)))
# print(has_ship(grid,("I",7)))
# print(has_ship(grid,("I",8)))

 


def field_to_str(grid):
    """
    (data) -> (str)
    """
    with open("ship_field.txt", "w") as fl:
            out = ''
            for row in ROWS:
                for col in COLS:
                    out += grid[(col, row)]
                out += "\n"
            
            fl.write(out)

print(field_to_str(read_field(("field.txt"))))
