#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from pol_function import feval

def simple_trapezoidal(a, b, f):
    # a = the minimum value of the interval
    # b = the maximum value of the interval
    # f = the polynomial function coefficients (ex : 3*X^2 + 4*X + 5)

    h = (b - a) / 2
    
    # I = the approximated value of the interval
    I = h * (feval(f, a) + feval(f, b)) / 2
    return I

def composed_trapezoidal(a, b, n, f):
    # a = the minimum value of the interval
    # b = the maximum value of the interval
    # n = the chosen number of equidistant point
    # f = the polynomial function coefficients (ex : 3*X^2 + 4*X + 5)
    
    h = (b - a) / n
    s = 0.0

    for i in range(0, n):
        s = s + feval(f, a + i * h)

    # I = the approximated value of the interval
    I = h * (feval(f, a) + feval(f, b) + 2 * s) / 2
    return I

def trapezoidal_plot(a, b, n, f):
    # a = the minimum value of the interval
    # b = the maximum value of the interval
    # n = the chosen number of equidistant point
    # f = the polynomial function coefficients (ex : 3*X^2 + 4*X + 5)
    

    x_values = np.linspace(a, b, 100)

    # Calculate y values for the polynomial function at each point
    y_values = np.polyval(f, x_values)

    # Plot the polynomial function in blue
    plt.plot(x_values, y_values, color='blue')

    # Plot n - 1 trapezoidal lines in red
    for i in range(n - 1):
        x_segment = [x_values[i], x_values[i + 1]]
        y_segment = [y_values[i], y_values[i + 1]]
        plt.plot(x_segment, y_segment, color='red')

    plt.title("Polynomial Function and Trapezoidal Approximation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    f = [1, 1, 3, 4, 5]
    print(f"simple trapezoidal =  {simple_trapezoidal(1, 10, f) :.3f}")
    print(f"composed trapezoidal =  {composed_trapezoidal(1, 10, 5, f) :.3f}")

    trapezoidal_plot(1, 10, 5, f)

if __name__ == "__main__":
    main()
