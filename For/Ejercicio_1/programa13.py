

n=int(input("Ingrese el valor de n: "))

s= "Serie: "

#processing

for i in range(1,n+1):
    t= i**2+1
    if i < n:
        s= s + "1/"+ str(t)+ ", "
    else:
        s= s + "1/" + str(t)

# output
print(s)