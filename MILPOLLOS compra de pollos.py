#MILPOLLOS

#precio y iva (el vaso en la variable del iva fue por que me daba error y lo puse asi por que si, lo importante es que sirva)
pre_pollos = 12
vaso_iva = 0.16

def calcular_descuento( nombre, edad, can_pollos):

    #funcion principal que define y almacena los descuentos (tarde 5 horas en hacer esta basura)

    if edad >= 65:
        #adultos mayores si compran entre 5 y 10 pollos
        if 5 <= can_pollos <= 10:
            return 12
        else:
            return 0
    elif edad >= 18:
        #adultos en caso de comprar mas de 10 pollos
        if can_pollos > 10:
            return 5
        #adultos en caso de comprar mas de 20 pollos
        elif can_pollos > 20:
            return 10
        else:
            return 0
    #menores de edad sin importar la cantidad de compra
    else:
        return 2

#esto de aca es la funcion para interfaz de compra (me quedo bonita esta cosa)
def main():
    
 #funcion principal que ejecuta el sistema de ventas
    print("=== BIENVENIDO A MILPOLLOS ===")
    print("Sistema de descuentos especiales\n")

    #1 solicitud de datos de el cliente
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    can_pollos = int(input("Ingrese la cantidad de pollos: "))

    #2 calculos de costo pre descuento
    subtotal = can_pollos * pre_pollos

    #3 calculo de descuento
    Porcen_descuento = calcular_descuento(nombre, edad, can_pollos)
    monto_descuento = subtotal * (Porcen_descuento / 100)

    #4 calculo de costo post descuento
    monto_descuento_aplicado = subtotal - monto_descuento

    #5 calculo del iva sobre el monto post descuento (seria tonto hacerlo antes del descuento)
    IVA = monto_descuento_aplicado * vaso_iva

    # calculo final de compra (se suma todo lo anterior y ya)
    total_pagar = monto_descuento_aplicado + IVA

    #7 RECIVO DE COMPRA

    print("\n" + "=" * 50)
    print("           FACTURA MILPOLLOS")
    print("=" * 50)
    print(f"Cliente: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Cantidad de pollos: {can_pollos}")
    print(F"Precio unitario: {pre_pollos}$")
    print(F"Subtotal: {subtotal:.2f}")
    print(f"Descuento aplicado: {Porcen_descuento}%")
    print(f"Monto de descuento: {monto_descuento:.2f}$")
    print(F"IVA base: {vaso_iva}$")
    print(f"IVA aplicado: {IVA:.2f}$")
    print(f"TOTTAL A PAGAR: {total_pagar:.2f}$")
    print(F"=" * 50)
    print("Gracias por su compra")


# esto ejecuta la interfaz, si no esta, ni arranca esta vaina
if __name__ == "__main__":
    main()

    #esta la hice yo, victor gonzalez, no confio en esos 2 como para dejarles la mas dificil
    #tarde 6 horas y 2 tazas de cafe en hacer que funciones
    #att:Victor gonzalez