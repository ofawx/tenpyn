# tenpyn 🎳 
Bowling Scoring in Python

## Interface
```python
from bowling import BowlingGame
game = BowlingGame()
game.roll(10)
game.roll(1)
game.roll(1)
game.score() # == 14
```
## Demo/Tests
```bash
# Use python3 if python is Python 2
$ python test_bowling.py
```

## TODOs
* Proper tests using PyTest
* Better validation of all inputs
