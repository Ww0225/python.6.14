actions = ((1,0),(0,1),(2,0),(0,2),(1,1))
visited = set()

def apply_actions(state):
    state_lst = []
    for action in actions:
        if state[2] == 1:
            new_state = (state[0]-action[0], state[1]-action[1], 0, state[3]+action[0], state[4]+action[1], 1)
        else:
            new_state = (state[0]+action[0], state[1]+action[1], 1, state[3]-action[0], state[4]-action[1], 0)
        if is_valid_state(new_state):
            state_lst.append(new_state)
            visited.add(new_state)
    return state_lst

def is_valid_state(state):
    if (state[0] >= state[1] or state[0] == 0) and (state[3] >= state[4] or state[3] == 0):
        return True
    return False

def crossing_river():
    pathes_queue = [[(3, 3, 1, 0, 0, 0)]]
    visited.add((3, 3, 1, 0, 0, 0))
    while pathes_queue:
        path = pathes_queue.pop(0)
        frontier = path[-1]
        if is_goal_state(frontier):
            return path
        new_states_lst = apply_actions(frontier)
        for state in new_states_lst:
            new_path = path + [state]
            pathes_queue.append(new_path)
    return None

def is_goal_state(state):
    return state[0] == 0 and state[1] == 0 and state[2] == 0

lst = crossing_river()
if lst:
    print("Here are the actions to cross the river:")
    for element in lst:
        print(element)
else:
    print("Sorry, I cannot find a way to cross the river.")
