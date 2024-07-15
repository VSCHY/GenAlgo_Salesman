import json
import numpy as np
import os

dir = os.path.dirname(os.path.dirname(__file__))


def load_data_TSP1():
    with open(os.path.join(dir,"inputs",'TSP1','StadiumsFull.json'), 'r') as file:
        data = json.load(file)

    toursize = data["TourSize"]
    distance_matrix = data["DistanceMatrix"]
    coordinates = data["Coordinates"]
    teams = data["Teams"]
    stadiums = data["Stadiums"]

    matrix = np.array(distance_matrix)
    if np.allclose(matrix, matrix.T, rtol=1e-05, atol=1e-08):
        out = "Validated"
    else:
        out = "Error"
    print(f"Outcome test symmetry: {out}.")
    return matrix