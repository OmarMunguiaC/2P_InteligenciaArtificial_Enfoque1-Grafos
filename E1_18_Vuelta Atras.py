from constraint import Problem, AllDifferentConstraint

csp = Problem()
csp.addVariables(['A', 'B', 'C'], [1, 2, 3])
csp.addConstraint(AllDifferentConstraint())

def backtrack(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_unassigned_variable(assignment, csp)
    for value in csp.domains[var]:
        assignment[var] = value
        if is_consistent(assignment, csp):
            result = backtrack(assignment, csp)
            if result is not None:
                return result
        del assignment[var]
    return None

def select_unassigned_variable(assignment, csp):
    for var in csp.variables:
        if var not in assignment:
            return var

def is_consistent(assignment, csp):
    # Implementar lógica para verificar la consistencia de la asignación
    return True

# Ejemplo de uso
assignment = {}
# csp = define el problema de satisfacción de restricciones
result = backtrack(assignment, csp)
print("Solución encontrada:", result)
