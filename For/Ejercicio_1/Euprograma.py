


# programa para saber cuantas vocales tiene mi nombre

nombre= input("Escriba su nombre: ")
a= "a"
e= "e"
i= "i"
o= "o"
u= "u"

contador = 0

for letra in nombre:
    if nombre == 'a':
        contador= contador + 1
        print(letra)
        print(contador)
    if nombre == 'e':
        contador = contador + 1
        print(contador)
    if nombre == 'i':
        contador = contador + 1
        print(contador)
    if nombre == 'o':
        contador = contador + 1
        print(contador) 
    if nombre == 'u':
        contador = contador + 1
        print(contador)
