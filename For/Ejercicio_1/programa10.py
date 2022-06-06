

"""Generar la siguiente serie: 1,4,9,16,25,36,.......n"""

n=int(input("Ingrese el valor de n: "))

s= "Serie: "

#processing

for i in range(1,n+1):
    t= i*i
    if i < n:
        s= s + str(t)+ ", "
    else:
        s= s + str(t)

# output
print(s)

