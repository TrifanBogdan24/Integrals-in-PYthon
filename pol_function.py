#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def feval(coeff, x):

    N = len(coeff)
    f = 0.0

    for i in range(0, N):
        f = f + coeff[i] * pow(x, N - i - 1)

    return f


def integrate(f):
    # f = cofficients of the polynomial function f
    # ex.: f=[1, 2, 3] => f = X^3 + 2*X^2 + 3

    integrate = []
    N = len(f)

    for i in range(0, N):
        integrate.append(float(f[i]) / float(N - i))

    integrate.append(0.0)
    return integrate


def disp_func(coeff):

    N = len(coeff)

    print("Y = f(X) = ", end = '')
    
    for i in range(0, N):

        if coeff[i] == 0.0:
            continue
        
        if coeff[i] > 0:
            if coeff[i] != 1.0:
                print(f"+ {coeff[i]}*", end = '')
            else:
                print(f"+ ", end = '')
        
        else:
            if coeff[i] != -1.0:
                print(f"- {-coeff[i]}*", end = '')
            else:
                printf(f"- ", end = '')

        if i == N - 2:
            print(f"X ", end = '')
        elif i != (N - 1):
            print(f"X^{N - i - 1} ", end = '')
    
    print()

def disp_integrate(coeff):

    N = len(coeff)

    print("∫ f(X) dx = ", end = '')
    
    for i in range(0, N):
        
        if coeff[i] > 0:
                print(f"+ {coeff[i]}/{N - i}*", end = '')
        
        else:
            print(f"- {-coeff[i]}/{N - i}*", end = '')

        if N - i != 1:
            print(f"X^{N - i} ", end = '')
        else:
            print(f"X", end = '')
    
    print()


def plot_function(a, b, f):
    # a = the minimum value of the interval
    # b = the maximum value of the interval
    # f = the polynomial function coefficients (ex : 3*X^2 + 4*X + 5)
    
    # the actual points that will be displayed of the plot
    x_values = np.linspace(a, b, 100)
    y_values = np.polyval(f, x_values)
    
    # Plot the function
    plt.plot(x_values, y_values)
    plt.title("Polynomial Function Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    coeff = [1, 1, 3, 4, 5]
    fintegral = integrate(coeff)
    
    disp_func(coeff)

    disp_integrate(coeff)
    disp_func(fintegral)

    print(feval(coeff, 10))
    
    plot_function(1, 10, coeff)

if __name__ == "__main__":
    main()
