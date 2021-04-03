from models.puzzle import Puzzle, BreadthFirstSearch

puzzle = Puzzle([
    [1, 3, 4],
    [2, None, 6],
    [5, 8, 7]
])

print(puzzle)
print("========================")

puzzleBFS = BreadthFirstSearch(puzzle)
puzzleBFS.search()