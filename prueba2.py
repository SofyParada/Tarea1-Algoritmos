def min_suma_cuadrados_brechas(L, n, ladrillos, indice=0, fila_actual=[], suma_actual=0, pared=[], min_suma=float('inf'), pared_minima=[]):
    # Caso base: todos los ladrillos han sido considerados
    
    if indice == n:
        # Agrega la fila actual a la pared si no está vacía
        if fila_actual:
            pared.append(fila_actual[:])

        # Calcula la suma de cuadrados de las brechas para la pared actual
        suma_cuadrados_brechas = sum((L - sum(fila)) ** 2 for fila in pared)
        
        # Actualiza la mínima suma de cuadrados de brechas si es necesario
        if suma_cuadrados_brechas < min_suma:
            min_suma = suma_cuadrados_brechas
            pared_minima = [fila[:] for fila in pared]
        
        # Retorna la mínima suma de cuadrados de brechas y la pared asociada
        return min_suma, pared_minima
    
    # Intenta agregar el ladrillo actual a la fila actual si cabe
    if suma_actual + int(ladrillos[indice]) <= L:
        fila_actual.append(int(ladrillos[indice]))
        min_suma, pared_minima = min_suma_cuadrados_brechas(L, n, ladrillos, indice + 1, fila_actual, suma_actual + int(ladrillos[indice]), pared, min_suma, pared_minima)
        fila_actual.pop()  # Deshace el último ladrillo agregado a la fila actual
    
    # Si no cabe el ladrillo actual en la fila actual, crea una nueva fila
    nueva_fila = [int(ladrillos[indice])]
    min_suma, pared_minima = min_suma_cuadrados_brechas(L, n, ladrillos, indice + 1, nueva_fila, int(ladrillos[indice]), pared + [fila_actual[:]], min_suma, pared_minima)
    
    # Retorna la mínima suma de cuadrados de brechas y la pared asociada
    return min_suma, pared_minima




x = input() #"6 9"
L, n= map(int, x.strip().split(" "))

print(L, n)


while x != "": 
    i = input() 
    #ladrillos = i.strip().split(" ")
    ladrillos = [int(i) for i in i.strip().split(" ")]

    resultado,pared = min_suma_cuadrados_brechas(L, n, ladrillos)
    print(pared)
    print(resultado)
    

    try:
        x= input()
        L, n = map(int, x.strip().split(" "))
        print(L,n)
    except EOFError as er:
        x = ""