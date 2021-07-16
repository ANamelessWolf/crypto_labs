import math
import random


class primeTester:

    def __init__(self, number):
        self.Number = number

    def trial_division(self):
        n = self.square()
        test = True
        divisibleBy = None
        if n < 2:
            test = False
        for i in range(2, n+1):
            if self.Number % i == 0:
                test = False
                divisibleBy = i
        return (test, divisibleBy)

    def fermat_test(self, trials):
        a = None
        i = None
        for i in range(trials):
            # 1: Selección de un número aleatorio menor a la prueba y mayor a 2
            a = random.randrange(2, self.Number)
            # 2: Se genera la prueba a^(n-1) mod n
            fermatTest = pow(a, self.Number-1, self.Number)
            if fermatTest != 1:  # El número es compuesto
                test = False
                break
            else:
                test = True  # Posiblemente primo
        return (test, a, i+1)

    def miller_rabin_test(self, trials):
        test = None
        # 1: Se agilizan las pruebas para algunos elementos del conjunto
        if self.Number < 2:
            test = False
        if self.Number < 4:
            test = True
        if self.Number % 2 == 0:
            test = False
        # 2: El número a probar es mayor a 3
        s = 0
        d = self.Number-1
        while d % 2 == 0:
            s += 1
            d = math.floor(d / 2)
        # n = 2^s * d es impar

        for i in range(trials):
            a = random.randrange(2, self.Number-1)    # 2 <= a <= d
            x = pow(a, d, self.Number)
            if x == 1:
                continue
            for j in range(s):
                if x == self.Number-1:
                    break
                x = pow(x, 2, self.Number)
            else:
                test = False
        test = True
        return (test, a, i+1)

    def square(self):
        n = math.sqrt(self.Number)
        n = math.modf(n)
        n = int(n[1])
        return n
