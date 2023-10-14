def my_first_function():
    print("hola mundo")
#my_first_function()

def my_second_function(name):
    print(f"hola, soy {name}")
#my_second_function("Juan")

#x=0
#def my_third_function():
    #return 20
#number = my_third_function()
#print(number)

def Suma(a,b):
    suma = a+ b
    return suma
    print(Suma(2,7))
#Suma(2,7)

def Suma_2(a,b=1):
    suma = a+ b
    return suma
    print(Suma_2(2))

def Suma_3(a,b):
    #print(f'a' {a}, 'b' {b})
    suma = a+ b
    return suma

Suma(b=7,a=5)
print(Suma_3(b=7,a=5))

def multi_parametros(*args): #para manejar datos solos
    print(args)

#multi_parametros(5, 7, 8, 9, 10, 'Juan', ['a', 2, True])

def multi_param_keys(kwargs): #para mandar un diccionario
    print(kwargs)
#multi_param_keys(nombre='Juan', edad=19, ciudad='Milagro')
