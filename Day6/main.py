def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
def walk_until():
    while front_is_clear():
        move()
    if not front_is_clear():
        if right_is_clear():
            turn_right()
            return
        turn_left()
    
def solve_maze():
    if not right_is_clear() or front_is_clear():
        walk_until()
    else:
        turn_right()
    

while not at_goal():
    solve_maze()
