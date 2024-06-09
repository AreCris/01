#Realizar un programa que determine si un triángulo es equilátero, 
#isósceles o escaleno.

lado1 = 2
lado2 = 8
lado3 = 9

if lado1 == lado2 == lado3:
    print("El triangulo es equilatero")
elif lado1 != lado2 & lado2 != lado3:
    print("El triangulo es escaleno")
else:
    print("El triangulo es isosceles")