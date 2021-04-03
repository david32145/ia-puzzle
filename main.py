from models.puzzle import Puzzle

puzzle = Puzzle([
    [1, 3, 4],
    [2, None, 6],
    [5, 8, 8]
])

print(puzzle)
print("========================")

for movement in puzzle.get_available_movements():
    p = puzzle.clone()
    p.move(movement)
    p.pprint()

goal = Puzzle([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, None]
])

goal.pprint()
print(goal.is_goal)