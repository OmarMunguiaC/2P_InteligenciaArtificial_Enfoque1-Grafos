from constraint import Problem, AllDifferentConstraint

csp = Problem()
csp.addVariables(['A', 'B', 'C'], [1, 2, 3])
csp.addConstraint(AllDifferentConstraint())

def arc_consistency(csp):
    queue = [(X, Y) for X, Y in csp.constraints]
    while queue:
        (X, Y) = queue.pop(0)
        if remove_inconsistent_values(X, Y, csp):
            for Z in csp.neighbors[X]:
                queue.append((Z, X))

def remove_inconsistent_values(X, Y, csp):
    removed = False
    for x in csp.domains[X]:
        if not any(satisfies_constraint(x, y, X, Y, csp) for y in csp.domains[Y]):
            csp.domains[X].remove(x)
            removed = True
    return removed

def satisfies_constraint(x, y, X, Y, csp):
    # Implementar lógica para verificar si la asignación x, y satisface la restricción entre X e Y
    return True

# Ejemplo de uso
# csp = define el problema de satisfacción de restricciones
arc_consistency(csp)
