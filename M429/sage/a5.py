





def q4():
    M = matroids.catalog.K4()

    print(M.circuits())

    print(M.cocircuits())



def q11():
    M = matroids.catalog.K33()
    D = matroids.catalog.K33dual()

    print(D.rank())

    for c in sorted([sorted(list(c)) for c in M.cocircuits()]):
        print(c)
q11()

