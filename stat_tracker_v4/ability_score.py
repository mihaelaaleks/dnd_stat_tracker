class AbilityScore():
    def __init__(self, score):
        self.score = score
        # self.label = f'{label.capwords():}'
        
    def get_modifier(self):
        # we want the modifier to be rounded down
        # the // operator is used to perform floor division
        modifier = (self.score - 10) // 2
        return modifier