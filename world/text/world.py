import turtle
import robot
import world.obstacles



def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(robot.position_x)+','+str(robot.position_y)+').')

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return robot.min_x <= new_x <= robot.max_x and robot.min_y <= new_y <= robot.max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    new_x, x1 = robot.position_x, robot.position_x
    new_y, y1 = robot.position_y, robot.position_y

    if robot.directions[robot.current_direction_index] == 'forward':
        new_y = new_y + steps
    elif robot.directions[robot.current_direction_index] == 'right':
        new_x = new_x + steps
    elif robot.directions[robot.current_direction_index] == 'back':
        new_y = new_y - steps
    elif robot.directions[robot.current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        if world.obstacles.is_position_blocked(new_x,new_y):
            robot.count += 1
            return False
        elif world.obstacles.is_path_blocked(x1, y1, new_x, new_y):
            robot.count += 1
            return False
        else:
            robot.position_x = new_x
            robot.position_y = new_y
            return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif robot.count > 0:
        robot.count = 0
        return True, robot_name+' Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif robot.count > 0:
        robot.count = 0
        return True, robot_name+' Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """

    robot.current_direction_index += 1
    if robot.current_direction_index > 3:
        robot.current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """

    robot.current_direction_index -= 1
    if robot.current_direction_index < 0:
        robot.current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'

def do_replay(robot_name, arguments, history):
    """
    Replays historic commands
    :param robot_name:
    :param arguments a string containing arguments for the replay command
    :return: True, output string
    """

    silent = arguments.lower().find('silent') > -1
    reverse = arguments.lower().find('reversed') > -1
    range_args = arguments.lower().replace('silent', '').replace('reversed', '')

    range_start = None
    range_end = None

    if len(range_args.strip()) > 0:
        if robot.is_int(range_args):
            range_start = -int(range_args)
        else:
            range_args = range_args.split('-')
            range_start = -int(range_args[0])
            range_end = -int(range_args[1])

    commands_to_replay = robot.get_commands_history(reverse, range_start, range_end,history)

    for (command_name, command_arg) in commands_to_replay:
        (do_next, command_output) = robot.call_command(command_name, command_arg, robot_name)
        if not silent:
            print(command_output)
            show_position(robot_name)

    return True, ' > '+robot_name+' replayed ' + str(len(commands_to_replay)) + ' commands' + (' in reverse' if reverse else '') + (' silently.' if silent else '.')

def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)
