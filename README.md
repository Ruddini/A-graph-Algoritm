# A*-graph-Algoritm

Projekt na studia, polegający na przeszukiwaniu grafu i znalezieniu najszybszej drogi z punktu startowego do punktu końcowego. Algorytm zwraca numery węzłów w grafie, przez które należy przejść, aby dotrzeć do punktu końcowego najszybszą trasą. 

Aby włączyć algorytm należy wpisać:
```
python Maciej_Dabrowski.py NUMBER.txt
```
Numery plików to przedział 1-16 Znajdują się w nich grafy w postaci macierzy sąsiedztwa. 

Macierz sąsiedztwa to macierz kwadratowa, w której element aij wynosi 1, jeśli
istnieje krawędź z i do j, a 0 w przeciwnym wypadku (dla
grafów nieskierowanych ta macierz jest symetryczna)

Plikami wejściowymi grafów są pliki txt i znajdują się tam grafy zarówno skierowane jak i nieskierowane. Program pobiera nazwę pliku, w którym będzie jeden
wiersz zawierający współrzędne kolejnych wierzchołków grafu
(przyjmujemy, że numerujemy wierzchołki od liczby 1), w drugim
co jest startem, a co metą, a w kolejnych macierz sąsiedztwa
(przy czym zero oznacza brak krawędzi, a liczba oznacza, że
jest krawędź o takiej wadze [kropka to separator dzięsiętny])
Jako heurystyka algorytmu grafu jest używana odległość Euklidesowa danego wierzchołka od początku grafu



Przykładowy opis zadania pokazany jest na poniższej ilustracji:
![image](https://user-images.githubusercontent.com/58587279/153858064-dbfdba15-4735-43ae-a98c-983c30d6daed.png)
