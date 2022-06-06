"""Cuantos multiplos de 7  y cuantos de 9 hay en los múmeros comprendidos entre 1000 y 5000"""
m= int(input("Ingrese el valor m: "))
n=int(input("Ingrese el valor de n: "))


m_7= 0
m_9= 0

for i in range(m, n+1, 1):
    if i%7 ==0:
        m_7 += 1
    if i%9 == 0:
        m_9 += 1

print("Entre",m, "y" ,n, "mil hay ")
print(m_7, "Multiplos de 7")
print(m_9, "Multiplos de 9")
