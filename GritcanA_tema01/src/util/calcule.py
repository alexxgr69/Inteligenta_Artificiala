def manhattan_distance(X, Y):
    distance = sum(abs(X[i] - Y[i]) for i in range(len(X)))
    return distance
