# importiere die math-Bibliothek für die Fakultätszahlen und für pi
import math

# Stelle, an welcher der Sinus approximiert werden soll
x = 0.25 * math.pi

# startwert
approx = 0
for i in range(10):
    # der nächste Summand wird zur Approximation addiert
    approx += ((-1) ** i / math.factorial(2 * i + 1)) * x ** (2 * i + 1)

print(f"sin({x}) ist ungefähr {approx}")
print(f"Zum Vergleich: sin({x})= {math.sin(x)}")