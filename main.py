from models.puzzle import Puzzle
from models.bfs import BreadthFirstSearch

puzzle = Puzzle([
    [1, 3, 4],
    [2, None, 6],
    [5, 8, 7]
])

print("Initial state")
print(puzzle)
puzzleBFS = BreadthFirstSearch(puzzle)
movements = puzzleBFS.search()
print("Finish search")

final_puzzle = puzzle
for movement in movements:
    final_puzzle = puzzle.clone()
    final_puzzle.move(movement)

final_puzzle.pprint()