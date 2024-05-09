
def min_suma_gaps_cuadrado(L, n, ladrillos): #en construcción 
    suma = 0
    pared = []
    i = 0
    while i <= n:
        if suma > L:
            pared.append(suma - int(ladrillos[i-1]))#se le elimina el ultimo que se le sumo ya que no puede ser mayor a L
            suma = 0
            suma += int(ladrillos[i-1])

        
        elif suma == L and i < n:
            pared.append(suma)
            suma = 0
            suma += int(ladrillos[i])
            i += 1

        elif i == n:
            pared.append(int(ladrillos[i-1]))
            i+= 1

        else:
            suma += int(ladrillos[i])
            i += 1

 
    return  pared



x = input() #"6 9"
L, n= map(int, x.strip().split(" "))

print(L, n)


while x != "": 
    i = input() 
    ladrillos = i.strip().split(" ")

    resultado = min_suma_gaps_cuadrado(L, n, ladrillos)
    print(resultado)
    
    try:
        x= input()
        L, n = map(int, x.strip().split(" "))
        print(L,n)
    except EOFError as er:
        x = ""

