import time
import folium
from matplotlib.animation import FuncAnimation

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


def save_html_map(route):
    peru_map = folium.Map(location=[-9.497415, -75.142212], zoom_start=6)
    for i in range(len(route)):
        folium.Circle(
            route[i].location,
            radius=10000,
            popup=route[i].name,
            color="crimson",
            fill=True,
        ).add_to(peru_map)
        if i < len(route) - 1:
            folium.PolyLine(
                [route[i].location, route[i + 1].location],
                color="blue",
                weight=2.5,
                opacity=1
            ).add_to(peru_map)
        else:
            folium.PolyLine(
                [route[i].location, route[0].location],
                color="blue",
                weight=2.5,
                opacity=1
            ).add_to(peru_map)
    peru_map.save(r"peru_map.html")


if __name__ == '__main__':
    departments = get_departments_list()
    FuncAnimation()
    best_route = simulated_annealing(departments, 50)
    save_html_map(best_route)
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
    # plt.show()




