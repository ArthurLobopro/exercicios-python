import math
angulo = float(input('Digite o ângulo desejado:\n'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("O ângulo de {}° têm:\nSeno de: {:.2f}\nCosseno de: {:.2f} e\nTangente de: {:.2f}.".format(angulo,sen,cos,tan))
