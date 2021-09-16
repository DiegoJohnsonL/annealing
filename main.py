import time

from department import Department
import pandas as pd
import geopandas as gpd
from simulated_annealing import simulated_annealing
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def get_departments_list():
    departments_data = pd.read_csv("data/departamentos.csv")
    departments_list = []
    for i in range(len(departments_data["Departamentos"])):
        name = departments_data["Departamentos"][i]
        location = tuple(map(float, departments_data["Location"][i].split(', ')))
        departments_list.append(Department(name, location))
    return departments_list


if __name__ == '__main__':
    departments = get_departments_list()
    best_route = simulated_annealing(departments, 50)

    # url_data = "https://raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson"
    # region_geojson = gpd.read_file(url_data)
    # c_map = ListedColormap(['white' for _ in range(25)], name='test')
    # region_geojson.plot(figsize=(20, 20), edgecolor='black', cmap=c_map)
    # plt.xlabel('longitude')
    # plt.ylabel('latitude')

    # for i in range(23):
    #     plt.plot(best_route[i].longitude, best_route[i].latitude, marker='o', color="red")
    #     x_values = [best_route[i].longitude, best_route[i+1].longitude]
    #     y_values = [best_route[i].latitude, best_route[i + 1].latitude]
    #     plt.plot(x_values, y_values)
    #
    # plt.show()

