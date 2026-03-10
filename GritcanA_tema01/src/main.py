from util.calcule import manhattan_distance

# Ex1:Vectori diferiti
X = [1, 2, 3]
Y = [4, 5, 6]
distanta = manhattan_distance(X, Y)
print(f"Distanta Manhattan intre {X} si {Y} este: {distanta}")

# Ex:2: Vectori identici
X2 = [5, 10]
Y2 = [5, 10]
distanta2 = manhattan_distance(X2, Y2)
print(f"Distanta Manhattan intre {X2} si {Y2} este: {distanta2}")

# Ex 3: Vectori cu nr negative
X3 = [-1, 2]
Y3 = [1, 3]
distanta3 = manhattan_distance(X3, Y3)
print(f"Distanta Manhattan intre {X3} si {Y3} este: {distanta3}")