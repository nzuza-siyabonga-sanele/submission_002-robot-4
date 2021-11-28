import random

ls_obs = []

def is_position_blocked(x,y):
    for i in ls_obs:
        if x in range(i[0],i[0]+4) and y in range(i[1],i[1]+4):
            return True
        
def is_path_blocked(x1, y1, x2, y2):
    for i in ls_obs:
        if x2 < x1:
            x1,x2 = x2,x1
        elif y2 < y1:
            y1,y2 = y2,y1
        if x2 == x1 and x1 in range(i[0], i[0]+4) and i[1] in range(y1, y2):
            return True
        elif y2 == y1 and y1 in range(i[1], i[1]+4) and i[0] in range(x1, x2):
            return True
        else:
            return False


def get_obstacles():
    number = random.randint(0,10)
    if number != 0:
        for i in range(number):
            obsx, obsy= random.randint(-100, 100), random.randint(-200,200)
            positions = (obsx,obsy)
            ls_obs.append(positions)
        return ls_obs
    else:
        return []
    
    

def draw_obstacles():
    list_of_obstacles = get_obstacles()
    if len(list_of_obstacles) != 0:
        print('There are some obstacles:')
        for i in list_of_obstacles:
            print(f'- At position {i[0]},{i[1]} (to {i[0]+4},{i[1]+4})')
            
def draw_turtle_obstacles(t):
    list_of_obstacles = get_obstacles()
    if len(list_of_obstacles) != 0:
        if len(ls_obs) == 0:
            for i in list_of_obstacles:
                t.color('red')
                t.penup()
                t.goto(i[0],i[1])
                t.pendown()
                t.begin_fill()
                t.rt(90)
                t.goto(i[0]+4,i[1])
                t.rt(90)
                t.goto(i[0]+4,i[1]+4)
                t.rt(90)
                t.goto(i[0],i[1]+4)
                t.rt(90)
                t.goto(i[0],i[1])
                t.end_fill()
                t.penup()
                t.goto(0,0)
                t.pendown()
            
