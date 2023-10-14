from funciones1 import multi_param_keys, Suma #con * importa todo las funciones

#multi_param_keys(nombre='Juan', edad=19, ciudad='Milagro')

print(Suma(2, 7))

#definir una funcion que reciba area y altura de un triangulo

def area_triangulo(base, altura):
    area = (base * altura)/2
    return area
print(area_triangulo(2,5))

#una funcion que al enviarle una lista me sume los numeros pares

def suma_pares(lista):
    suma = 0
    for numero in lista: #recorre la lista
        if numero % 2 == 0:
            suma += numero
    return suma
#Lista= [1,2,3,4,5,6,7,8,9,10]
#print(suma_pares(Lista))

#crea una funcion que el usuario que cuente la cantidad de letras que define el usuario ejemplo: 'a' en una cadena dada
print("ejercicio cantidad de letras:")
def contar_letras_ejercicio(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador
print(contar_letras_ejercicio('soy juan aviles', 'a'))

def contar_letras2(letra, frase):
    x = frase.count(letra)
    return x
letter = input("ingrese la letra a contar: ")
phrase = input("ingrese la frase: ")
print(contar_letras2(letter, phrase))
#print(contar_letras2('a', 'soy juan aviles')) #esto si no pide un print
