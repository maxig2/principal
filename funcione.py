
def es_par(x: int) -> bool:
    if x == 0:
        return True
    elif x == 1:
        return False
    else:
        return es_par(x - 2)

resultado = es_par(1)

print(resultado)


