from bowling import BowlingGame

def tests() -> None:
    """
    Define separate tests to evaluate/verify BowlingGame
    """

    # Single frame
    game = BowlingGame()
    game.roll(2)
    game.roll(3)
    assert 5 == game.score()

    # Two frames
    game = BowlingGame()
    game.roll(1)
    game.roll(2)
    game.roll(3)
    game.roll(4)
    assert 10 == game.score()

    # Spare behaviour
    game = BowlingGame()
    game.roll(5)
    game.roll(5)
    game.roll(5)
    game.roll(1)
    assert 21 == game.score()

    # Strike behaviour
    game = BowlingGame()
    game.roll(10)
    game.roll(1)
    game.roll(1)
    assert 14 == game.score()

    # Perfect game
    game = BowlingGame()
    for _ in range(12):
        game.roll(10)
    assert 300 == game.score()

    return

if __name__ == '__main__':
    tests()
