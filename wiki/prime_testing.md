
## La prueba de Fermat 

### Teorema de Fermat

En el teorema de Fermat, menciona lo siguiente:

Dado cierto número primo `P` y cierto número entero `a`. Donde `a < P` sabemos que `P` divide `a^P - a`. 

El teorema se escribe de la siguiente forma

```
a^P Ξ a mod P
```

Debido a que `a` y `P` no comparten factores por que `P` es primo y el máximo comun divisor de `a` y `P` es uno podemos expresar el teorema de la siguiente forma.

```
a^(P-1) Ξ 1 mod P
```

### Descripción de la prueba

La prueba consistira en buscar un entero `a` que intente probar un número `x` sea primo. Para que el número se primo debe cumplir con la siguiente proposición.

```
a^(x-1) mod x = 1
```

Cuando el resultado no sea uno se entiende que el número `x` es compuesto.

Los pasos para encontrar si un número x es primo son los siguientes

1. Seleccionar un número `x` a verificar si es primo
2. Seleccionar un número aleatorio entero `a<x`
3. Realizamos la prueba
4. Verificamos el resultados, si el número no es uno se trata de un número compuesto y termina la prueba.
5. Verificamos el resultados, si el número es uno se trata de un número primo. Sin embargo existe una consideración en el teorema que se explica más adelante.

En algunos casos la prueba puede fallar y encontrar pseudoprimo. Estos números son llamados `números de Carmichael`. 
Esto sucede cuando un entero `a` genera un número 1 en la prueba para un número compuesto `x`.

Se ha comprobado que la muestra de números `a<x` que generan un pseudoprimo, a lo máximo se trata del 50% de los números de la muestra.

Por lo que se puede repetir la prueba, llamaremos `t` al número de itereaciones a realizar. La probabilidad de que no aparezcan pseudoprimos sera `P<=1/2^t`.

Ejemplo si realizamos 20 pruebas la probabilidad de encontrar un pseudoprimo en todas las iteraciones será de

```
t = 20
P = 1/2^t
P = 1/1048576
P = 0.00019073%
```

## Prueba de Miller-Rabin 

Funciona como una versión avanzada de la prueba de Fermat. Digamos que `P` es un número primo y considera la siguiente formula.

```
x² Ξ 1 (mod P)
x²-1 Ξ 0 (mod P)
Donde 
(x - 1)(x + 1) Ξ 0 (mod P)
Dado que P es primo y debe dividir (x - 1) o (x + 1)
x Ξ  1 (mod P)
x Ξ -1 (mod P)
```