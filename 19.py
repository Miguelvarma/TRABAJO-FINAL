t=int(input("ingrese el tiempo en sugundos trascurrido:      "))
minutos=t//60
hora=minutos//60
segundosR=t%60
minutosR=minutos%60
print("el tiempo trascurrido es",hora,":",minutosR,":",segundosR)