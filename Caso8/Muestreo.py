def crearMuestreo():
    listaFinal = []
    aumento = 1
    cont1 = 1
    cont2 = 256
    for i in range(0, 4):
        nuevaLista = []
        for j in range(0, 4):
            lista = []
            cont2 *= aumento;
            for x in range(cont1, cont2):
                for y in range(cont1, cont2):
                    lista += [[x, y]]
            cont1 = cont2
            aumento += 1
        nuevaLista += [lista]
        listaFinal += [[nuevaLista]]

    return listaFinal