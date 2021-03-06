class Action:
    NOOP = 0        # NOOP
    ACCELERATE = 1  # FIRE
    BRAKE = 5       # DOWN
    RIGHT = 11      # RIGHT_FIRE
    LEFT = 12       # LEFT_FIRE

    @staticmethod
    def toString(a):
        return {
            0: 'NOOP',
            1: 'ACCELERATE',
            5: 'BRAKE',
            11: 'RIGHT',
            12: 'LEFT'}[a]
