A=int(input("ingrese un numero de 4 cifras para reordenarlo:  "))
n4=A%10
n3=(A%100)//10
n2=(A%1000)//100
n1=(A - (A%1000))//1000

print("el numero al reves es",(str(n4)+str(n3)+str(n2)+str(n1)))