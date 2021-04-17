notas = (2, 4, 6, 8)

#primero se ha de resolver el error que da al contar lista, cuando no hay mas numeros. Realizando una excepción con una función.

def contenido(lista,indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    
    return resultado