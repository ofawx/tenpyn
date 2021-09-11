class Frame:
    """
    A single frame in a game of bowling.
    Earns points from rolls within this frame,
        plus points from subsequent frames if
        all pins downed.
    """
    def __init__(self):
        self.rolls = []
        self.bonuses = []

    def roll(self, pins: int) -> None:
        self.rolls.append(pins)

    def bonus(self, pins: int) -> None:
        """
        Add bonus pins from subsequent frames, if applicable
        """
        if self.__apply_bonus():
            self.bonuses.append(pins)

    def score(self) -> int:
        return sum(self.rolls) + sum(self.bonuses)

    def rolls_complete(self) -> bool:
        return len(self.rolls) == 2 or sum(self.rolls) == 10

    def __apply_bonus(self) -> bool:
        """
        Private boolean method to determine whether bonus
        should be added (whether N/A or quota filled)
        """
        # No strike/spare or frame incomplete
        if self.score() < 10 or not self.rolls_complete():
            return False
        # Strike
        elif len(self.rolls) == 1:
            return True if len(self.bonuses) < 2 else False
        # Spare
        elif len(self.rolls) == 2:
            return True if len(self.bonuses) < 1 else False
        # Undefined
        else:
            raise NotImplementedError('Check logic')


class BowlingGame:
    """
    A complete game of bowling.
    Consists of 10 frames.
    """
    def __init__(self):
        self.frames = [Frame()]

    def score(self) -> int:
        return sum(f.score() for f in self.frames)

    def roll(self, pins: int):
        # If start of new frame, instantiate new current frame
        if self.frames[-1].rolls_complete():
            self.frames.append(Frame())

        # Apply score to current frame
        self.frames[-1].roll(pins)

        # Apply bonus score to previous two frames only
        for f in self.frames[-3:-1]:
            f.bonus(pins)
