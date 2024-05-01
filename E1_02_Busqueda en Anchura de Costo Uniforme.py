import heapq

def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start)]  # Cola de prioridad para el UCS
    while queue:
        cost, node = heapq.heappop(queue)
        if node not in visited:
            print(node)
            visited.add(node)
            if node == goal:
                return
            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + neighbor_cost, neighbor))

# Ejemplo de uso
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 3)],
    'C': [('F', 7)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
print("Búsqueda en Anchura de Costo Uniforme:")
ucs(graph, 'A', 'F')

#En este caso, la lista se detiene hasta que llega al punto deseado
#Empieza en A, y cuando llega a F termina de buscar dejando la D afuera
