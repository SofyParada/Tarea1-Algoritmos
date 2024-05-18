
"""
        GAPS_OPTIMOS
- Parametros:
            L: longitud de la Pared
            n: Cantidad de ladrillos
            ladrillos: lista de las longitudes de los n ladrillos
            i: índice del ladrillo actual 
            fila_actual: lista de ladrillos actuales
            suma_actual: suma de las longitudes de los ladrillos de la fila actual
            pared: lista de listas de la pared
            min_suma: la suma mínima de los gaps al cuadrado
            mejor_pared: lista con la mejor combinació de ladrillos que minimiza la suma de los gaps al cuadrado
- La función gaps_optimos busca todas las posibles combinaciones de ladrillos en la pared.
- Calcula la suma de los gap^2 y compara que suma de gaps^2 es menor y la devuelve como min_suma y la mejor combinacion de ladrillos correspondiende como mejor_pared
"""
def gaps_optimos(L, n, ladrillos, i, fila_actual, suma_actual, pared, min_suma, mejor_pared):    
    if i == n:
        if fila_actual:
            pared.append(fila_actual[:])

        gaps_cuadrados = sum((L - sum(fila)) ** 2 for fila in pared)
        
        if gaps_cuadrados < min_suma:
            min_suma = gaps_cuadrados
            mejor_pared = [fila[:] for fila in pared]
        return min_suma, mejor_pared
    
    if suma_actual + int(ladrillos[i]) <= L:
        fila_actual.append(int(ladrillos[i]))
        min_suma, mejor_pared = gaps_optimos(L, n, ladrillos, i + 1, fila_actual, suma_actual + int(ladrillos[i]), pared, min_suma, mejor_pared)
        fila_actual.pop() 
    
    new_fila = [int(ladrillos[i])]
    min_suma, mejor_pared = gaps_optimos(L, n, ladrillos, i + 1, new_fila, int(ladrillos[i]), pared + [fila_actual[:]], min_suma, mejor_pared)
    
    return min_suma, mejor_pared


while True: 
    try: 
        x = input()
        L, n = map(int, x.strip().split(" "))
        i = input() 
        ladrillos = [int(i) for i in i.strip().split(" ")]

        fila_actual = []
        suma_actual = 0
        pared = []
        min_suma = float('inf')
        mejor_pared = []

        resultado,pared = gaps_optimos(L, n, ladrillos, 0, fila_actual, suma_actual, pared, min_suma, mejor_pared)
        print(resultado)
 
    except EOFError:
        break

