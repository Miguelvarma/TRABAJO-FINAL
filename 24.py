n=int(input("ingrese el numero para determinar si es positivo o negativo y par o impar : "))
if n < 0 and n % 2 == 0:
    print('El número', n, 'es negativo y par')
elif n >0 and n % 2 == 0:
    print('El número', n, 'es positivo y par.')
elif n >0 and n % 2 != 0:
    print('El número', n, 'es positivo y impar.')
else:
    print ("el numero",n,"esnegativo e impar")