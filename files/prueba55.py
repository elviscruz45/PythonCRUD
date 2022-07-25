def funcion(p1, p2, *ps, p3=None):
    print(f'p1 es {p1}')
    print(f'p2 es {p2}')
    print(f'p3 es {p3}')

# llamando a la función pasando p2 y p3 por posicion
funcion(1, 2, 3,6)

# llamando a la función pasando p3 por nombre
funcion(1, 2, p3=3)



