"""
comentario
de
varias
líneas
"""
while True:
    nombre=input("¿Cómo te llamas? ")
    if nombre == "":
        print("No has \n escrito nada",end="\n")
    else:
        print(f"Hola {nombre} encantado",end=" ---")
        print("Adiós")
        break;