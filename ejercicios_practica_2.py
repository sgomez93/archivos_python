# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'

    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    cantornillos = 0
    csvfile = open(archivo) # Abro el archivo y no le digo que modo abrir porque por defecto es lectura

    # Leo el archivo lo guardo en la variable stock como una lista de diccionarios 
    stock = list(csv.DictReader(csvfile)) 

    # Cierro el archivo porque no lo nesecito mas ya que que todo quedo guardado en la variable stock y puedo trabajar con eso solo                                    
    csvfile.close()

    #Recorro la lista de diccionarios stock, productos es el elemeto de la lista
    # (osea para el primer caso seria el diccionario en la posicion 0, luego productos en el siguente caso seria
    # el diccionario en la posicion 1 o fila 1). Para entender la variable productos representaria las filas que en
    # este caso cada fila es un diccionario conformado por tornillos,tuercas, arandelas
    # Esto no lo coloco para que los demas lo entiendan, sino para que yo lo entienda y en un futuro si me 
    # olvido como se usaba repasar esto para recordarlo rapido.
    for productos in stock:          
        #coloco int porque el valor de la clave tornillos esta guardado como strig. Y yo nesecito enteros para sumar
        cantornillos += int(productos.get('tornillos')) 

    print('Cantidad de tornillos:', cantornillos)


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    dep2amb = 0
    dep3amb = 0

    with open(archivo) as csvfile:
        propiedades = list(csv.DictReader(csvfile))
        
        for departamento in propiedades:
            try:
                if int(departamento.get('ambientes')) == 2:
                    dep2amb += 1
                if int(departamento.get('ambientes')) == 3:   
                    dep3amb += 1
            except:
                    dep2amb += 0  # cuando no esta especificado los ambientes le sumo un cero 
                    dep3amb += 0

        print('Hay {} departamentos de 2 ambientes y {} departamentos de 3 ambientes'.format(dep2amb, dep3amb))

            
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
