listaFrutas = ['manzanas', 'naranjas', 'peras']
listaCuidadoP = ['Shampoo','Loción corporal', 'Jabón para la cara']
listaBebidas = ['Coca Cola', 'Pilsener', 'Sprite']

tuplaFrutas = ('manzanas', 'naranjas', 'peras')
tuplaCuidadoP = ('Shampoo','Loción corporal', 'Jabón para la cara')
tuplaBebidas = ('Coca Cola', 'Pilsener', 'Sprite')

diccionarioTienda = {"Bebidas": listaBebidas,
                    "Frutas": listaFrutas,
                    "Cuidado Personal": listaCuidadoP
                    }

tuplaTienda = (tuplaBebidas, tuplaFrutas, tuplaCuidadoP)
listaTienda = [listaBebidas, listaFrutas, listaCuidadoP]

"""Actualiza un value de una key específica: """
diccionarioTienda['Bebidas'][2] = 'Gallo'

"""Actualiza los valores específicos dentro de una matriz: """
listaTienda[0][0] = 'Pepsi'
listaTienda[2][1] = 'Loción a base de agua'


print('Esta colección es una:')
print(type(listaTienda))
print('Esta colección es una:')
print(type(tuplaTienda))
print('Esta colección es una:')
print(type(diccionarioTienda))
print('---------------------------------------------------------------------')
print(listaTienda)
print(tuplaTienda)
print(diccionarioTienda)

"""Imprime todos los value de la key -> Bebidas"""
for x in diccionarioTienda['Bebidas']:
    print(x)

copiaDatosTienda = diccionarioTienda.copy()
""" Otra manera de poder hacerlo es con la función dict(): """
copia2DatosTienda = dict(diccionarioTienda)