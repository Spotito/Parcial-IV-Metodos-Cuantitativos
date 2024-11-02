# Importar la biblioteca de PuLP
from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, PULP_CBC_CMD

def main ():

    # Crear un problema de maximización
    prob = LpProblem("Ejemplo_Programacion_Entera", LpMaximize)

    # Definir variables (enteras)
    x = LpVariable('x', lowBound=0, cat='Integer')
    y = LpVariable('y', lowBound=0, cat='Integer')

    x1 = int(input("Valor de x1: "))
    x2 = int(input("Valor de x2: "))

    print("=== Restricciones ===")
    r1x1 = int(input("Valor de x1 de la restriccion 1: "))
    r1x2 = int(input("Valor de x2 de la restriccion 1: "))
    r1c = int(input("Valor de la constante de la restriccion 1: "))

    r2x1 = int(input("Valor de x1 de la restriccion 2: "))
    r2x2 = int(input("Valor de x2 de la restriccion 2: "))
    r2c = int(input("Valor de la constante de la restriccion 2: "))

    # Definir la función objetivo
    prob += x1 * x + x2 * y, "Función Objetivo"

    # Definir las restricciones
    prob += r1x1 * x + r1x2 * y <= r1c, "Restriccion_1"
    prob += r2x1 * x - r2x2 * y >= r2c, "Restriccion_2"

    # Resolver el problema utilizando el solucionador por defecto (CBC)
    prob.solve(PULP_CBC_CMD(msg=True))

    # Mostrar el estado de la solución
    print(f"Estado de la solución: {LpStatus[prob.status]}")

    # Mostrar los Valores óptimos de las variables
    print(f"x = {x.varValue}")
    print(f"y = {y.varValue}")

    # Mostrar el Valor óptimo de la función objetivo
    print(f"Valor óptimo de Z = {prob.objective.value()}")
