


n=int(input("Ingrese el valor de n: "))

s= "Serie: "

#processing

for i in range(1,n+1):
    t= i**2+i
    if i < n:
        s= s + str(t)+ ", "
    else:
        s= s + str(t)

# output
print(s)