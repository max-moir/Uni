





def q9():
    M = matroids.catalog.P6()

    N = M / 'f'

    for c in N.circuits():
        print(c)

q9()

