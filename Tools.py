
def search(lista, elemento):
    for i in range(len(lista)):
        if lista[i].__eq__(elemento):
            return i
