from department import Department, get_haversine_distance
import random
import math
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def get_energy(route):
    energy = 0
    for i in range(len(route) - 1):
        energy += Department.get_distance_between_departments(route[i], route[i + 1])
    energy += Department.get_distance_between_departments(route[len(route) - 1], route[0])
    return energy


def draw(route, data):
    region_geojson = gpd.read_file(data)
    c_map = ListedColormap(['white' for _ in range(25)], name='test')
    region_geojson.plot(figsize=(20, 20), edgecolor='black', cmap=c_map)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    for i in range(len(route) - 1):
        plt.plot(route[i].longitude, route[i].latitude, marker='o', color="red")
        x_values = [route[i].longitude, route[i + 1].longitude]
        y_values = [route[i].latitude, route[i + 1].latitude]
        plt.plot(x_values, y_values)
    plt.show()


def simulated_annealing(route, iterations):
    url_data = "https://raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson"
    temp = 1000
    cooling_index = 0.003
    random.shuffle(route)
    t_actual = route.copy()
    t_best = route.copy()
    prob = 0
    for i in range(iterations):
        t_new = t_actual.copy()
        rand1, rand2 = random.sample(range(len(t_actual) - 1), 2)
        t_new[rand1], t_new[rand2] = t_new[rand2], t_new[rand1]
        e_actual = get_energy(t_actual)
        e_new = get_energy(t_new)
        if e_new < e_actual:
            prob = 1
        else:
            prob = math.exp((e_actual - e_new) / temp)
        if prob > random.randint(0, 1):
            t_actual = t_new
        e_best = get_energy(t_best)
        if e_actual < e_best:
            t_best = t_actual.copy()
        temp = (1 - cooling_index) * temp
        draw(t_actual, url_data)

    print(str(get_energy(t_best)) + "km")
    return t_best
