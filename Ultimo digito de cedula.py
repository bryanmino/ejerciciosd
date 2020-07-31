cedula = [1,2,3,4,5,6,7,8,9]
cedula[0] = int(input("Ingrese el dígito 1 "))
cedula[1] = int(input("Ingrese el dígito 2 "))
cedula[2] = int(input("Ingrese el dígito 3 "))
cedula[3] = int(input("Ingrese el dígito 4 "))
cedula[4] = int(input("Ingrese el dígito 5 "))
cedula[5] = int(input("Ingrese el dígito 6 "))
cedula[6] = int(input("Ingrese el dígito 7 "))
cedula[7] = int(input("Ingrese el dígito 8 "))
cedula[8] = int(input("Ingrese el dígito 9 "))
posicion_1 = cedula[0] * 2
if posicion_1 > 9:
    posicion_1 = posicion_1 - 9
cedula[0] = posicion_1
posicion_3 = cedula[2] * 2
if posicion_3 > 9:
    posicion_3 = posicion_3 - 9
cedula[2] = posicion_3
posicion_5 = cedula[4] * 2
if posicion_5 > 9:
  posicion_5 = posicion_5 - 9
cedula[4] = posicion_5
posicion_7 = cedula[6] * 2
if posicion_7 > 9:
  posicion_7 = posicion_7 - 9
cedula[6] = posicion_7
posicion_9 = cedula[8] * 2
if posicion_9 > 9:
  posicion_9 = posicion_9 - 9
cedula[8] = posicion_9
suma_pares = cedula[1] + cedula[3] + cedula[5] + cedula[7]
suma_impares= cedula[0] + cedula[2] + cedula[4] + cedula[6] + cedula[8]
suma_total = suma_pares + suma_impares
if suma_total % 10 == 0:
    print("El último dígito de cédula es: 0")
else:
    udc = suma_total % 10
    print("El último dígito de cédula es:", udc-10)