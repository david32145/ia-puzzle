from models.puzzle import Puzzle

puzzle = Puzzle([
    [1, 3, 4],
    [2, None, 6],
    [5, 8, 7]
])

print(puzzle)
print("========================")

for action in puzzle.get_available_movements():
    p = puzzle.clone()
    p.move(action)
    print(p)