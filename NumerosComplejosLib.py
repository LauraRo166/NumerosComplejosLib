import math

def sumaC(m, d):
    return (m[0] + d[0], m[1] + d[1])

def productoC(m ,d):
    posicionX = (m[0]*d[0])-(m[1]*d[1])
    posicionY = (m[0]*d[1])+(d[0]*m[1])
    return (posicionX, posicionY)

def restaC(m, d):
    return (m[0]-d[0], m[1]-d[1])

def divisionC(m, d):
    denominador = (d[0]**2) + (d[1]**2)
    pReal = ((m[0]*d[0]) + (m[1]*d[1]))/denominador
    pImg = ((d[0]*m[1])-(m[0]*d[1]))/denominador
    return (pReal, pImg)

def moduloC(num):
    a = num[0]**2
    b = num[1]**2
    return math.sqrt(a+b)

def conjugadoC(num):
    return (num[0], num[1]*-1)

def faseC(num):
    fase = math.atan2(num[1],num[0])
    return fase

def representacionPolarC(num):
    return moduloC(num),faseC(num)

def representacionCartesianaC(num):
    a = num[0]*math.cos(num[1])
    b = num[0]*math.sin(num[1])
    return a, b
    

