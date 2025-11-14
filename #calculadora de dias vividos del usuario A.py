#calculadora de dias vividos del usuario

#ingresar edad
edad_ingresada=input("ingrese su edad: ")
edad= int(edad_ingresada)
total_edad= edad*365
if edad_ingresada >="1":
    print(f"su total de dias vividos es de: {total_edad} ")
else:
    print("edad no valida")
 
 #esto lo hizo jose estanga, el tester del grupo es Victor Gonzalez