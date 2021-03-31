# Readme

First let's create a class called Puzzle to represent the state of game such as:

```python
class Puzzle {
    blank_position: Tuple[int, int]
    state: List[List[int]]

    def __init__(self, state: List[List[int]]):

    def find_blank_position() -> Tuple[int, int]:

    def clone() -> Puzzle:

    def move(position: Tuple[int, int], direction: str)

    def moveLeft()
}
```