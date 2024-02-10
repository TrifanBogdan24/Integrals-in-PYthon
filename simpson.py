#!/usr/bin/env python3

from pol_function import feval

def simple_simpson(a, b, f):
    # a = the minimum value of the interval
    # b = the maximum value of the interval
    # f = the polynomial function coefficients (ex : 3*X^2 + 4*X + 5)

    # I = the approximated value of the integral
    I = (b - a) * (feval(f, a) + feval(f, b) + 4 * feval(f, (a + b) / 2)) / 6
    return I

def composed_simpson(a, b, n, f):
    # a = the minimum value of the interval
    # b = the maximum value of the interval
    # n = the chosen number of equidistant point
    # f = the polynomial function coefficients (ex : 3*X^2 + 4*X + 5)
    
    h = (b - a) / (2 * n)
    s1 = 0.0
    s2 = 0.0

    for i in range(1, n + 1):
        s1 = s1 + feval(f, a + (2 * i - 1) * h)

    for i in range(1, n):
        s2 = s2 + feval(f, a + 2 * i * h)

    # I  = the approximated value of the interval
    I = h * (feval(f, a) + feval(f,b) + 4*s1 + 2*s2) / 3
    return I

def main():
    f = [1, 2, 3, 4, 5]
    print(f"simple simpson integral value   = {simple_simpson(1, 10, f) :.3f}")
    print(f"composed simpson integral value = {composed_simpson(1, 10, 1000, f) :.3f}")

if __name__ == "__main__":
    main()
