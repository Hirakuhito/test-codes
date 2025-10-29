class State():
    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column
    
    def __repr__(self):
        return "<State: [{}, {}]".format(self.row, self.column)
    
    def clone(self):
        return State(self.row, self.column)

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

class Action(Enum):
    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2

class Environment():
    def __init__(self, grid, move_prob=0.8):
        self.grid = grid
        self.agent_state = State()

        self.default_reward = -0.04

        self.move_prob = move_prob
        self.reset()

@property
def row_length(self):
    return len(self.grid)

@property
def column_length(self):
    return len(self.grid[0])

@property
def action(self):
    return [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]

@property
def states(self):
    states = []
    for row in range(self.row_length):
        for column in range(self.column_length):
            if self.grid[row][column] != 9:
                states.append(State(row, column))

    return states

def transit_func(self, state, action):
    transition_probs = {}

    if not self.can_action_at(state):
        return transision_probs

    opposite_direction = Action(aciton.value * -1)
    
    for a in self.actions:
        prob = 0
        if a == action:
            prob = self.move_prob
        elif a != opposite_direction:
            prob = (1 - self.move_prob) / 2

        next_state = self._move(state, a)
        if next_state not in transition_probs:
            transition_probs[next_state] = prob
        else:
            transition_prob[next_state] += prob
    
    return transition_probs

def can_action_at(self.state):
    if self.grid[state.row][state.column] == 0:
        return True
    else:
        return False