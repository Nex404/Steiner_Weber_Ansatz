#Steiner-Weber Standortermittlung
#by Dennys-Daniel Vogt

from math import sqrt

bi = []
xi = []
yi = []

def eukliedische_distanz(x, x1, y, y1):
    return sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))

def calc_x0():
    zaehler_x = 0
    nenner_x = 0
    for i in xrange(len(xi)):
        zaehler_x += bi[i] * xi[i]

    for i in xrange(len(bi)):
        nenner_x += bi[i]

    return zaehler_x / nenner_x

        

def calc_y0():
    zaehler_y = 0
    nenner_y = 0

    for i in xrange(len(yi)):
        zaehler_y += bi[i] * yi[i]

    for i in xrange(len(bi)):
        nenner_y += bi[i]

    return zaehler_y / nenner_y

def calc_x(x, y):
    x_zaehler = 0
    x_nenner = 0

    for i in xrange(len(xi)):
        x_zaehler += (bi[i] * xi[i]) / eukliedische_distanz(x, xi[i], y, yi[i])

    for i in xrange(len(bi)):
        x_nenner += bi[i] / eukliedische_distanz(x, xi[i], y, yi[i])

    return x_zaehler / x_nenner

def calc_y(x, y):
    y_zaehler = 0
    y_nenner = 0

    for i in xrange(len(xi)):
        y_zaehler += (bi[i] * yi[i]) / eukliedische_distanz(x, xi[i], y, yi[i])

    for i in xrange(len(bi)):
        y_nenner += bi[i] / eukliedische_distanz(x, xi[i], y, yi[i])

    return y_zaehler / y_nenner

if __name__ == "__main__":
    #taking input from user
    print("Welcome to the Steiner-Weber optimisation model \n")
    print("Following please insert the needed coordinates and the demand \n")

    used = True
    
    while used:
        xi.append(float(input("Enter the x-coord:")))
        #xi.append = float(input())
        yi.append(float(input("Enter the y-coord:")))
        bi.append(int(input("Enter the demand:")))
        print("Do you want to enter one more location?")
        
        #print("y for yes, n for no: ")
        onemore = int(input("1 for yes, 2 for no: "))
        if onemore == 2:
            used = False

     #startcoordinates input or calc  
           
    print("Do you have start coordinates? 1 for y / 2 for n: ")
    start = int(input())
    if start == 1:
        x, y = float(input("Please enter x and y coord in this order: ").split())

    else:
        x = calc_x0()
        y = calc_y0()

    alpha = float(input("What is your alpha? :"))

    used2 = True
    while used2:
        xplaceholder = calc_x(x, y)
        yplaceholder = calc_y(x, y)

        if abs(x-xplaceholder) < alpha:
            if abs(y-yplaceholder) < alpha:
                x = xplaceholder
                y = yplaceholder
                used2 = False
            
        else:
            x = xplaceholder
            y = yplaceholder

    print("The optimal coordinates are x: {}, y: {}" .format(x, y))

