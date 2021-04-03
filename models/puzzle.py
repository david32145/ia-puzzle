from typing import List, Tuple
from collections import deque

Matrix = List[List[int]]
Position = Tuple[int, int]

_GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, None]
]

class Puzzle:
    blank_position: Position
    state = Matrix

    def __init__(self, state: Matrix):
        valid = self._validate_state(state)
        if not valid:
            raise Exception("The state is invalid")
        self.state = state
        self.blank_position = self.find_blank_position()

    def find_blank_position(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] is None:
                    return (i, j)

    def clone(self):
        [l1, l2, l3] = self.state
        state = [l1.copy(), l2.copy(), l3.copy()]
        return Puzzle(state)

    def get_available_movements(self):
        blank_position = self.blank_position
        (line, column) = blank_position
        available_movements = []
        if line - 1 >=0:
            available_movements.append(((line - 1, column), "DOWN"))
        if column - 1 >=0:
            available_movements.append(((line, column - 1), "RIGHT"))
        if line + 1 <= 2:
            available_movements.append(((line + 1, column), "UP"))
        if column + 1 <= 2:
            available_movements.append(((line, column + 1), "LEFT"))
        return available_movements

    def move(self, movement):
        (position, _) = movement
        blank_position = self.blank_position
        (line, column) = blank_position
        (nLine, nColumn) = position
        self.state[line][column] = self.state[nLine][nColumn]
        self.state[nLine][nColumn] = None
        self.blank_position = position

    @property
    def is_goal(self):
        return self.state == _GOAL_STATE

    def pprint(self):
        print(self.__str__())
        
    # Criando uma 'chave' para indexar o estado do tabuleiro no conjunto de nós visitados:
    def key_set(self):
        return ''.join(str(ele) for sub in self.state for ele in sub)

    def __str__(self):
        str_x = ""
        for line in self.state:
            for value in line:
                str_x = str_x + str(value) + "  "
            str_x = str_x + "\n"
        return str_x

    @staticmethod
    def _validate_state(state: Matrix):
        if state == None:
            return False
        if Puzzle._is_not_list(state):
            return False
        if len(state) != 3:
            return False
        if Puzzle._is_not_list(state[0]) or Puzzle._is_not_list(state[1]) or Puzzle._is_not_list(state[2]):
            return False
        if len(state[0]) != 3 or len(state[1]) != 3 or len(state[2]) != 3:
            return False
        discovery_numbers = [False, False, False, False, False, False, False, False, False]
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] is None:
                    if discovery_numbers[8]:
                        return False
                    discovery_numbers[8] = True
                    continue
                if not isinstance(state[i][j], int) or state[i][j] <=0 or state[i][j] >= 9:
                    return False
                if discovery_numbers[state[i][j] - 1]:
                    return False
                discovery_numbers[state[i][j] - 1]
        return True
                

    @staticmethod
    def _is_not_list(obj):
        return not isinstance(obj, list)
    
class BreadthFirstSearch:
    def __init__(self, puzzle):        
        self.start_state = puzzle
        
    def search(self): 
        # Para armazenar um tipo de 'chave' dos nós visitados:
        visitedNodes = set()
        
        queue = deque([self.start_state])
        
        while queue:
            currentNode = queue.popleft()
            visitedNodes.add(currentNode.key_set())

            if currentNode.is_goal:
                print("ACHIEVED GOAL STATE:")
                print(currentNode)
                
                return True
            
            expandingNodes = []
            
            # Gerando os nós filhos com as possibilidades de movimento:
            for moviment in currentNode.get_available_movements():
                newNode = currentNode.clone()
                newNode.move(moviment)
                expandingNodes.append(newNode)
            
            # Processo de geração dos nós, para a gente mostrar no dia da apresentação:
            for node in expandingNodes:
                print(node)
            
            # Verificando se os nós expandidos já foram acessados:
            for expandedNode in expandingNodes:
                if expandedNode.key_set() not in visitedNodes:
                    queue.append(expandedNode)
                    visitedNodes.add(expandedNode.key_set())