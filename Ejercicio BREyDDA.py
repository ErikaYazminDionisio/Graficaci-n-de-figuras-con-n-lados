from matplotlib import pyplot as plt
import turtle as vic
import matplotlib.pylab as pl

def poligono():
   
    lados = int(input("Ingrese la medida de la circunferencia, \n ejemplo--> 100: "))
    n = int(input("Ingrese el número de lados de la figura: \n"))
    for i in range(n):
        vic.forward(lados)
        vic.right(360/n)
def Algorithm_Bresenham(x1, y1, x2, y2):
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = (2 * dy - dx)

    while x <= x2:
        pl.plot(x, y, 'm.')
        x = x + 1
        if (p < 0):
            p = p + 2 * dy
        else:
            p = p + (2 * dy)-(2 * dx)
            y = y + 1

        print('(', x, ',', y, ')')

    pl.title('Tarea')
    pl.xlabel('X')
    pl.ylabel('Y')
    pl.grid(color='k', linestyle='dotted', linewidth=1)
    pl.show()

    print("Valor dx: ", dx)
    print("Valor dy: ", dy)


def main():
    x1 = int(input("Ingrese el valor de  x1: "))
    y1 = int(input("Ingrese el valor de  y1: "))
    x2 = int(input("Ingrese el valor de  x2: "))
    y2 = int(input("Ingrese el valor de  y2: "))

    Algorithm_Bresenham(x1, y1, x2, y2)


if __name__ == "__main__":
    #main()
    poligono()
    

