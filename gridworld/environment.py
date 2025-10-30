class Environment:
    def __init__(self, size=10):
        # define grid's size
        self.size = 10

        # Agent and Target position
        self.agent_pos = None
        self.target_pos = None

        self.reset()

    def reset(self):
        # get the position where is able in the grid
        all_grids = list(range(self.size*self.size))

        # decide the agent's pos randomly
        agent_index = random.choice(all_positions)
        self.agent_pos = self._index_to_coord(agent_index)

        remaining_position = [p for p in all_grids if p != agent_index]
        target_index = random.choice(remaining_position)
        self.target_pos = self._index_to_coord(target_index)

        return self.agetn_pos
    
    def step(self, action):
        """
        Agent will do action and then return 'next state', 'reward', 'end frag'

        Args:
            action (int): 1:up, -1:down, 2:left, -2:right
        
        Return:
            tuple: (next_state, reward, done)
        """

    def _index_to_coord(self, index):
        """
        change index to (x, y) coordinate
        origin = (0, 0) is up left, x is horizontal, y is vertical
        """

        x = index % self.size
        y = index // self.size

        return (x, y)

    def _coord_to_index(self, coord):
        x, y = coord
        
        return y * self.size + x