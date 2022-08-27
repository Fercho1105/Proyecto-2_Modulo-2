#Le pedimos al usuario las coordenadas

x=(input("Coordenada en x: ")) # Le pedimos al usuario la coordenada "x" 
Caracteres_x=len(x) #Guardamos en una variable el tamaño de la variable
tipo_x=x.isdigit() #Vemos que sea un digito, ya que son coordenadas


#En este bucle, hacemos que el usuario no deje vacia la casilla, o digite algo que no sea un numero
while Caracteres_x ==0 or tipo_x == False:
    print("Error!!! No deje la coordenada vacia o inserte el valor correcto")
    x=(input("Coordenada en x: "))
    Caracteres_x=len(x)
    tipo_x=x.isdigit()
    if Caracteres_x > 0 and tipo_x == True :
        break


y=(input("Coordenada en y: ")) # Le pedimos al usuario la coordenada "y" 
Caracteres_y=len(y) #Guardamos en una variable el tamaño de la variable
tipo_y=y.isdigit() #Vemos que sea un digito, ya que son coordenadas

#En este bucle,de igual manera pero con la coordenada en y, hacemos que el usuario no deje vacia la casilla, o digite algo que no sea un numero
while Caracteres_y ==0 or tipo_y == False:
    print("Error!!! No deje la coordenada vacia o inserte el valor correcto")
    y=(input("Coordenada en y: "))
    Caracteres_y=len(y)
    tipo_y=y.isdigit()

    if Caracteres_y > 0 and tipo_y == True :
        break


# Hacemos un cast de ambas coordenadas y las convertimos a enteros
x = int(x) 
y = int(y)

#Definimos las condicionas que determinan en que parametro se encuentran las coordenadas.
if x==0 and y==0:  # En dado caso que este en el origen,las coordenadas se lo hacemos saber al usuario
    print ('Origen')
elif x>0 and y>0:
    print ('Cuadrante I') #Si el eje "X" y "Y" son mayores a cero,las coordenadas están en el cuadrante 1.
elif x==0 and y>0:
    print("Entre cuadrante I y II") # Si el eje "X" es igual a cero y el eje "Y" es mayor a cero, la coordenada esta entre el 1er  y 2do cuadrante.
elif x<0 and y>0:
    print ('Cuadrante II') # Si el eje "X" es menor a cero, y el eje "Y" es mayor a cero, las coordenadas están en el cuadrante 2.
elif x<0 and y==0:
    print("Entre cuadrante II y III") # Si el eje "X" es menor a cero y el eje "Y" es igual a cero, la coordenada esta entre el 2do  y 3er cuadrante.
elif x<0 and y<0:
    print ('Cuadrante III') #Si el eje "X" y "Y" son menores a cero,las coordenadas están en el cuadrante 3.
elif x==0 and y<0:
    print("Entre cuadrante III y IV") # Si el eje "X" es igual a cero y el eje "Y" es menor a cero, la coordenada esta entre el 3er  y 4to cuadrante.
elif x>0 and y<0 :
    print ('Cuadrante IV ') # Si el eje "X" es mayor a cero, y el eje "Y" es menor a cero, las coordenadas están en el cuadrante 4.
else :
    print("Entre cuadrante IV y I") # Si el eje "X" es mayor a cero y el eje "Y" es igual a cero, la coordenada esta entre el 4to  y 1er cuadrante.

print(f"La coordenada es: {(x,y)}") #Finalmente imprimimos la coordenada.