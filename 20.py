dinero=int(input("ingrese el valor a desglozar:  "))
###
###
if dinero >= 100000:
    queda=dinero//100000
    print("hay",str(queda),"billetes de 100 mil pesos")
    dinero=dinero%100000
if dinero >= 50000:
    queda=dinero//50000
    print("hay",str(queda),"billetes de 50 mil pesos")
    dinero=dinero%50000
if dinero >= 20000:
    queda=dinero//20000
    print("hay",str(queda),"billetes de 20 mil pesos")
    dinero=dinero%20000
if dinero >= 10000:
    queda=dinero//10000
    print("hay",str(queda),"billetes de 10 mil pesos")
    dinero=dinero%10000
if dinero >= 5000:
    queda=dinero//5000
    print("hay",str(queda),"billetes de 5 mil pesos")
    dinero=dinero%5000
if dinero >= 2000:
    queda=dinero//2000
    print("hay",str(queda),"billetes de 2 mil pesos")
    dinero=dinero%2000
if dinero >= 1000:
    queda=dinero//1000
    print("hay",str(queda),"billetes de 1 mil pesos")
    dinero=dinero%1000