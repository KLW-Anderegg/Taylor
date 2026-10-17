import math


def ableitung_an_einer_stelle(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def ableitung(f, h=1e-5):
    def ableitung_f(x):
        return ableitung_an_einer_stelle(f, x)

    return ableitung_f


def nte_ableitung(f, n, h=1e-5):
    def nte_ableitung_f(x):
        if n == 0:
            return f(x)
        else:
            return ableitung(nte_ableitung(f, n - 1, h), h)(x)

    return nte_ableitung_f


def taylor_approximation(f, x0, n, h=1e-5):
    def taylor_approximation_f(x):
        approximation = 0
        for k in range(n + 1):
            ableitung_k = nte_ableitung(f, k, h)
            print(f"{k}-te Ableitung an der Stelle {x0} ist ungefähr {ableitung_k(x0)}")
            approximation += (ableitung_k(x0) / math.factorial(k)) * ((x - x0) ** k)
        return approximation

    return taylor_approximation_f


# Beipiel
f = lambda x: math.sin(x)
print("Approx, ", taylor_approximation(f, 0, 6)(math.pi))
print("Built-in function", f(math.pi))
