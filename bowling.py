class Frame:
    """
    A single frame in a game of bowling.
    Earns points from rolls within this frame,
        plus points from subsequent frames if
        all pins downed.
    """
    def __init__(self):
        self.rolls = []

    def roll(self, pins: int) -> None:
        self.rolls.append(pins)

    def score(self) -> int:
        return sum(self.rolls)

    def rolls_complete(self) -> bool:
        return len(self.rolls) == 2 or sum(self.rolls) == 10


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
