import math

#koef noteiksana taisnes vienadojuma funkcijai, tiri emocijam

def l_koef(x1, y1, x2, y2):
    k=(y1-y2)/(x1-x2)
    b=y1-k*x1
    koef=[]
    koef.append(k)
    koef.append(b)
    return koef

def p_koordinates(x1, y1, x2, y2):
    dx=x2-x1
    dy=y2-y1
    x3=x1+2*dx
    y3=y1+2*dy
    p=[]
    p.append(x3)
    p.append(y3)
    return p

xa=float(input("Ievadi xa: "))
ya=float(input("ievadi ya: "))
xb=float(input("Ievadi xb: "))
yb=float(input("Ievadi yb: "))
xc=float(input("Ievadi xc: "))
yc=float(input("Ievadi yc: "))

#Pārbaude

#Šeitvajag

xo=float(input("Ievadi xo: "))

yo=float(input("Ievadi yo: "))

# A _ O xa ya xo yo

# y=k*x+b

a1=[]

b1=[]

c1=[]

print(p_koordinates(xa, ya, xo,yo)) #a1 punkta koordinates

print(p_koordinates(xb, yb, xo, yo)) #b1 punkta koordinates

print(p_koordinates(xc, yc, xo, yo)) #c1 punkta koordinates