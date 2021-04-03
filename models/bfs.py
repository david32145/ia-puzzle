from collections import deque
    
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