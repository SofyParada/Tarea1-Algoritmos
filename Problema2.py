
def min_suma_gaps_cuadrado(L, n, ladrillos):
    # dp array to store the minimum sum of gaps squared
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # No gaps when there are no bricks
    
    for i in range(1, n + 1):
        current_sum = 0
        for j in range(i, n + 1):
            current_sum += int(ladrillos[j - 1])
            if current_sum > L:
                break
            gap = L - current_sum
            dp[j] = min(dp[j], dp[i - 1] + gap * gap)
    
    return dp[n]

# Lectura de la entrada desde el archivo input-1.dat
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
