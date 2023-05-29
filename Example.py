lista =[1,5,25,100,500]
#Inicial se refiere a la lista al inicio
print("Inicial: ",lista)

#Perimte agregar un obejto a la lista

lista.append(250)
print("append: ", lista)

#Extend toma una segunda lista y la agrega a la principal

lista2=[75,125]
lista.extend(lista2)
print("Extend: ", lista)

#insert sirve para agregar los datos que queremos, debo poner primero el lugar en el que queremos que esté y luego el valor que vamos añadir

lista.insert(2,400)
print("insert: ", lista)

#Remove busca el dato y elimina, debemos escoger el numero que queremos

lista.remove(400)
print("Remove: ", lista)

#Pop elimina el ultimo resgistro

lista.pop()
print("pop: ", lista)
lista.pop(2)
print("pop: ", lista)

#Reverse invierte el orden de la lista

lista.reverse()
print("Reverse: ", lista)

#Sor ordena la lista de menor a mayor

lista.sort()
print("Sort: ", lista)

#Sort(Reverse=true) ordena la lista de mayor a menor

lista.sort(reverse=True)
print("Sortreverse: ", lista)