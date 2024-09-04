def robotSim(commands: list[int], obstacles: list[list[int]]) -> int:   
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # ['N', 'E', 'S', 'W']
    curr_dir = 0
    curr_pos = [0, 0]    
    furthest = 0
    obstacles_map = {}

    for o in obstacles:
        obstacles_map[(o[0], o[1])] = 1

    for command in commands:
        if command == -1:
            curr_dir = (curr_dir + 1) % 4
        elif command == -2:
            curr_dir = (curr_dir - 1) % 4
        else:
            for _ in range(command):
                cur_x, cur_y = curr_pos[0] + directions[curr_dir][0], curr_pos[1] + directions[curr_dir][1]
                if (cur_x, cur_y) in obstacles_map:
                    break
                curr_pos[0] = cur_x
                curr_pos[1] = cur_y

        furthest = max(furthest, curr_pos[0] ** 2 + curr_pos[1] ** 2)

    return furthest

def robotSim_Refactoring(commands: list[int], obstacles: list[list[int]]) -> int:   
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # ['N', 'E', 'S', 'W']
    cur_dir = 0
    x, y = 0, 0    
    furthest = 0
    obstacles_map = {}

    for obstacle in obstacles:
        x_obstacle, y_obstacle = obstacle[0], obstacle[1]
        obstacles_map[(x_obstacle, y_obstacle)] = 1

    for command in commands:
        if command == -1:
            cur_dir = (cur_dir + 1) % 4
        elif command == -2:
            cur_dir = (cur_dir - 1) % 4
        else:
            for _ in range(command):
                x_new, y_new = x + directions[cur_dir][0], y + directions[cur_dir][1]
                if (x_new, y_new) in obstacles_map:
                    break
                x, y = x_new, y_new

            furthest = max(furthest, x ** 2 + y ** 2)

    return furthest
print(robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))