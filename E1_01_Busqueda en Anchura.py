
import os
#Se importa un grafo
grafo = {
	'a': [('p',4), ('j',15), ('b',1)],
    'b': [('a',1), ('d',2), ('e',2), ('c',3)],
	'j': [('a',15)],
	'p': [('a', 4)],
	'd': [('b',2), ('g',3)],
	'e': [('b',2), ('g',4), ('f',5), ('c',2)],
	'c': [('b',3), ('e',2), ('f',5), ('i',20)],
	'g': [('d',3), ('e',4), ('f',10), ('h',1)],
	'f': [('g',10), ('e',5), ('c',5)],
	'i': [('c',20)],
	'h': [('g',1)] 
}

#Imprime el grafo 
print("Muestra el grafo antes del recorrido: \n")
for key, lista in grafo.items():
	print(key)
	print(lista)
print()
		
visitados = [] #Lista de objetos ya revisados
cola = [] #Lista de objetos por revisar

origen = input("Ingresa el nodo origen: ") #Se coloca el vertice con el que se desea iniciar
print("\nLista de recorrido en anchura\n")

cola.append(origen) 
while cola: #Mientras haya vertices sin revisar, entonces;
	actual = cola.pop(0) #Cambia el vertice por el actual

	if actual not in visitados: #Si no se ha visitado el vertice, entonces: 
		print("Vertice actual -> ", actual) #Se imprime el vertice actual
		visitados.append(actual) #Se guarda el vertice en la lista de visitados

	for key, lista in grafo[actual]: #Añade todo vertice que no se ha visitado a la cola
		if key not in visitados:
			cola.append(key)

print()
os.system("pause")
