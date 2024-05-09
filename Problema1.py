def superposicion(A, n):
    #n = len(A)
    if n == 1:
        return 0
    else:
        # Dividir el conjunto A en dos mitades
        A1 = A[:n//2]  # A1 mitad izquierda de A
        A2 = A[n//2:]  # A2 mitad derecha de A
        
        # Resolver recursivamente el problema para las dos mitades
        maxA = superposicion(A1, len(A1))
        maxB = superposicion(A2, len(A2))    

        i = 0 
        j = 0 
        max_final = 0

        #Hay que comparar los intervalos y ver el valor de la intersección

        while i < len(A1) and j < len(A2):  #Recorre largo de mitades

            if A1[i][1] >= A2[j][0]: #Si el final de A1 es mayor o igual al inicio de A2, hay intersección
                inters = min(A1[i][1], A2[j][1]) - A2[j][0] + 1  #Elige el menor de los dos finales y le resta el inicio del otro, mas 1
                if inters > max_final:
                    max_final = inters
                j += 1  
                if j == len(A2) and i < len(A1):
                    j = 0
                    i += 1
            else:
                i += 1
        
        # Se toman maximos de las recursividades y el procedimiento actual
        return max(maxA, maxB, max_final)




   

x = input()

while x != "": 
    i = input()
    linea = i.split(" ")
    conjunto = []
    y = 0
    while y < 2*int(x) :   
            conjunto.append((int(linea[y]), int(linea[y + 1])))
            y += 2
            
    conjunto = sorted(conjunto, key=lambda x: x[0])
    #print(conjunto)
    print(superposicion(conjunto , int(x)))
    try:
        x= input()
    except EOFError as er:
        x = ""

