# Taller de Estructuras de Datos: Punto 5

**Curso:** Análisis y Diseño de Algoritmos
**Universidad:** Universidad del Valle
**Profesor:** John Alexander Vargas

## Integrantes

- Alejandro Valencia Sandoval
- Maria Alejandra Pizarro Sarria


## Descripción

Solución en **Python 3** de dos problemas de HackerRank, con el código tal como fue aprobado en la plataforma y su evidencia.

| # | Problema | Archivo | Técnica | Tiempo | Espacio |
|---|----------|---------|---------|--------|---------|
| 1 | [Detect Whether a Linked List Contains a Cycle](https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem) | `ciclo.py` | Tortuga y liebre (Floyd) | O(n) | O(1) |
| 2 | [Largest Rectangle](https://www.hackerrank.com/challenges/largest-rectangle/problem) | `rectangulo.py` | Pila monótona | O(n) | O(n) |

## Problema 1: Detectar un ciclo en una lista enlazada

**Idea:** se usan dos punteros, uno lento que avanza de 1 en 1 y uno rápido que avanza de 2 en 2.

- Si **no hay ciclo**, el puntero rápido llega a `None` y se devuelve `0`.
- Si **hay ciclo**, ambos quedan atrapados dentro de él y el rápido gana una posición de ventaja en cada iteración, por lo que tarde o temprano coinciden en el mismo nodo y se devuelve `1`.
- Se compara con `is` (mismo nodo en memoria) y no con `==` (mismo valor).

**Ventaja:** usa memoria constante, a diferencia de guardar los nodos visitados en un conjunto, que cuesta O(n).

## Problema 2: Rectángulo más grande en un histograma

**Idea:** el mejor rectángulo que usa una barra como la más baja se extiende hasta la primera barra menor a la izquierda y la primera barra menor a la derecha.

- Se recorre el arreglo guardando en una **pila los índices** de barras con alturas crecientes.
- Cuando aparece una barra menor que la cima, esa barra encontró su límite derecho (`i`) y su límite izquierdo es la nueva cima de la pila. Con eso se calcula `altura * ancho`.
- Se agrega una altura 0 al final (centinela) para vaciar la pila.

**Ventaja:** cada índice entra y sale de la pila una sola vez, por lo que es O(n), frente a O(n²) de la fuerza bruta, que daría *timeout* con hasta 10^6 barras.

## Evidencia

Ambos problemas fueron enviados con **Submit Code** y aprobaron todos los casos de prueba.

**Problema 1: Cycle Detection**

![Evidencia problema 1](evidencia_ciclo.png)

**Problema 2: Largest Rectangle**

![Evidencia problema 2](evidencia_rectangulo.png)

## Estructura del repositorio

- `README.md`
- `ciclo.py`
- `rectangulo.py`
- `evidencia_ciclo.png`
- `evidencia_rectangulo.png`