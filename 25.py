precio=int(input("ingrese el valor del producto:"))
descuento = precio*0.5
precio_final = (precio*1.19)-descuento
if precio < 150000:
    print(precio*1.19)
else:
    print(precio_final)