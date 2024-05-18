
def min_suma_gaps_cuadrado(L, n, ladrillos):
    # dp para almacenar la suma mínima de espacios al cuadrado
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  #si no hay ladrillos no hay gaps
    
    for i in range(1, n + 1):
        sum_actual = 0
        for j in range(i, n + 1):
            sum_actual += int(ladrillos[j - 1])
            if sum_actual > L:
                break
            gap = L - sum_actual
            dp[j] = min(dp[j], dp[i - 1] + gap * gap)
    
    return dp[n]


while True: 
    try: 
        # Lectura por entrada estandar desde el archivo input-1.dat
        x = input()
        L, n = map(int, x.strip().split(" "))
        i = input() 
        ladrillos = [int(i) for i in i.strip().split(" ")]

        resultado = min_suma_gaps_cuadrado(L, n, ladrillos)
        #print(pared)
        print(resultado)
 
    except EOFError:
        break
