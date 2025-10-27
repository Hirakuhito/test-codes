class State():
    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column
    
    def __repr__(self):
        return "<State: [{}, {}]".format(self.row, self.column)
    