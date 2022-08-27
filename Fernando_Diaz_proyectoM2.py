

#Pedimos al usuario que inserte una palabra
palabra = input("Inserte una palabra: ")
longitud_palabra = len(palabra)  #Guardamos en una variable el tamaño de esa letra
tipo_palabra = palabra.isalpha  #Vemos que sea un caracter



#Vemos si el usuario dejó la casilla vacía o insertó otro valor que no haya sido string
while tipo_palabra is False or longitud_palabra == 0:  #Entramos en un bucle en el que le seguimos pidiendo al usuario que escriba una palabra o no deje vacio el campo
    print("No inserto un caracter o puso un elemento no válido.")
    print("Intente nuevamente.")
    palabra = input("Inserte una palabra: ")  #Nuevamente le pedimos al usuario la palabra
    longitud_palabra = len(palabra)
    tipo_palabra = palabra.isalpha
    if tipo_palabra is True or longitud_palabra > 0: #Si cumple con las instrucciones salimos del bucle con un break
        break
    else:
        continue


#Finalmente vemos que condiciones cumple la palbra escrita por el usuario.
if longitud_palabra >= 4 and longitud_palabra <= 8:  #Este if es por si cumple con la condicion de que el numero de caracteres sean mayores a 4 y menores a 8
    print("La palabra es correcta")


else :  # Por lo tanto lo unico que resta del if es que sea menor a 4 caracteres y mayor a 8 caracteres
    if longitud_palabra < 4: # Desplegamos un mensaje si es que la palabra contiene menos de 4 caracteres
        print("La palabra es incorrecta")
        print(f"La palabra solo tiene {longitud_palabra} caracteres.")
        print(f"Faltan letras")
        print("Recuerde poner una palabra de entre 4 y 8 caracteres")
    else:
        print("La palabra es incorrecta") # Desplegamos un mensaje en el que la palabra contiene mas de 8 caracteres
        print(f"La palabra tiene {longitud_palabra} caracteres.")
        print(f"Sobran letras.")
        print("Recuerde poner una palabra de entre 4 y 8 caracteres")

