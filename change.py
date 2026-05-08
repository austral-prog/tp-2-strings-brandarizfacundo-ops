def change():
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)
    print("Dinero recibido")
    dinero = int(input())
    print(dinero)

    vuelto = dinero - gasto

    decimal = int(round(vuelto * 100))
    pesos = decimal // 100
    centavos = decimal % 100


    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(int(centavos))
