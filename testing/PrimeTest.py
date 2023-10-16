import sys
sys.path.insert(1, 'Y:\\bin\\')
from ns_crypto.primeTester import primeTester

# 1: Pruebas generales
# number = 98402937  # Compuesto
number = 67391 # Primo
print("\nVerificar si el número {0} es primo".format(number))
pTest = primeTester(number)
pResult = pTest.trial_division()
pResult = pTest.fermat_test(20)
pResult = pTest.miller_rabin_test(20)
test = 'es primo' if pResult[0] else 'no es primo'
print(
    "Existen un número de {0} primos para el rango especificado".format(number))

# 2: Rangos de primos
start = 100
end = 1000
print("\n¿Cuantos números primos hay entre {0} y {1}".format(start, end))
primesList = []
pTest = primeTester(start)
for n in range(start, end, 1):
    if n % 2 != 0:  # Nos saltamos pares
        pTest.Number = n
        test = pTest.trial_division()
        if test[0]:
            primesList.append(n)
print("El número de los primos generados son: {0}".format(len(primesList)))


# 3: Si un número impar n>1 cumple que 2^(n−1) ≡ 1 (mod n). Entonces n puede ser primo.
# ¿Cúal es el número más pequeño que no cumple la regla anterior?
# Nota la condición a evaluar será un número que no es primo y que 2^(n−1) % n = 1
print("\nSi un número impar n>1 cumple que 2^(n−1) ≡ 1 (mod n). Entonces n puede ser primo.\n¿Cúal es el número más pequeño que no cumple la regla anterior?")
n = 1
test = None
for i in range(1000):
    n = n+2
    test = pow(2, n-1, n)
    pTest.Number = n
    isPrime = pTest.fermat_test(20)[0]
    if not isPrime and test == 1:
        break
print("El número más pequeño es: {0}".format(n))

# 4: Cuando n=3, 2^n - 3 = 5 Este es el primer valor de n por el cual  2^n - 3 es primo.
#  ¿Cúal es el valor 24 de n donde  2^n - 3 es un número primo?
member = 24
print("\nCuando n=3, 2^n - 3 = 5 Este es el primer valor de n por el cual  2^n - 3 es primo. ¿Cúal es el valor {0} de n donde  2^n - 3 es un número primo?".format(member))
n = 2
primesList = []
while len(primesList) < 24:
    n += 1
    value = pow(2, n) - 3
    pTest.Number = value
    isPrime = pTest.miller_rabin_test(20)[0]
    if isPrime:
        primesList.append("({0}) {1}".format(n, value))

print("El número más pequeño es: {0}".format(n))
