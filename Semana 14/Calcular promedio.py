print ("Ariana gasto en ropa 5000 en una sección del 30%.")
print ("y otra compra de 1000 en la sección de 50%.")
print ("¿Cuanto debe pagar en cada compra aplicando los descuentos por separado?")
def calcular_descuento(monto_total, porcentaje_decuento=30):
    descuento = monto_total * (porcentaje_decuento/100)
    return descuento

if __name__=="__main__":
    monto1 = 5000
    monto2 = 1000
#llamada de función
    descuento1 = calcular_descuento(monto1)
    print(f"***monto de la compra es {monto1}, el descuento es {descuento1}")

#llamada del segundo monto
    descuento2 = calcular_descuento(monto2, 50)
    print(f"***monto de la segunda compra es {monto2}, el descuento es {descuento2}")

