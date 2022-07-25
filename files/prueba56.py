def funcion(p1, p2, *, p3=None):
    print(f'p1 es {p1}')
    print(f'p2 es {p2}')
    print(f'p3 es {p3}')


# llamando a la función pasando p3 por nombre
funcion(15,3, p3=3)

