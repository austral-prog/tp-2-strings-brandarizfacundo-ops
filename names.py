def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    n=input()
    a=input()
    print(f"{n} {a}".lower())
    print(f"{n} {a}".title())
    print(f"{n} {a}".upper())
    print (f"\t{n} {a}".lower())
