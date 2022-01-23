
#1) Imprimir números del 0-150 
for i in range( 0, 151 ):
    print( i )


#2) Imprimir múltiplos de 5 entre 5 y 1,000 
i = 10
while i > 5 and i < 1000:
    print( i )
    i += 5


#3) Contar, a la manera del Dojo
y = 1
while y > 0 and y <= 100:
    print(y)
    y = y + 1
    if y % 5 == 0:
        print("Coding")
    if y % 10 == 0:
        print("Coding Dojo")


#4) Whoa. Es un gran idiota
# Agrega los enteros impares del 0 al 500,000, e imprime la suma final.

suma=0

for x in range( 0, 500001 ):
    if x%2 !=0:
        suma = suma+x
    x+=1
print(suma)

#5) Cuenta regresiva de a 4
#Imprimir cuenta regresiva de a 4
y = 2018

while y > 0:
    print(y)
    y = y - 4



#6) Contador flexible

lowNum = 1
highNum = 20
mult = 4
z = 1

while z>=1 and z<=20:
    if z % 4 == 0:
        print(z)
    z += 1


