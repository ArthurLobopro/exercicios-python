from math import hypot,sqrt
cateto1 = float(input("Digite o cateto oposto: \n"))
cateto2 = float(input("Digite o cateto adjacente: \n"))
hip = sqrt(cateto1**2+cateto2**2) #Ou hip = hip = hypot(cateto1,cateto2)
print("Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {}".format(cateto1,cateto2,hip))
