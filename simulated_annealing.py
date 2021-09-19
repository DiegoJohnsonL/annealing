from department import Department, get_haversine_distance
import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Calcula la distancia total de la ruta
def get_energy(route):
    energy = 0
    for i in range(len(route) - 1):
        energy += Department.get_distance_between_departments(route[i], route[i + 1])
    energy += Department.get_distance_between_departments(route[len(route) - 1], route[0])
    return energy


def draw(route, temp, distance, i_best):
    plt.clf()
    for i in range(len(route) - 1):
        plt.plot(route[i].longitude, route[i].latitude, marker='o', color="red")
        x_values = [route[i].longitude, route[i + 1].longitude]
        y_values = [route[i].latitude, route[i + 1].latitude]
        plt.plot(x_values, y_values)
    plt.plot(route[len(route) - 1].longitude, route[len(route) - 1].latitude, marker='o', color="red")
    x_values = [route[len(route) - 1].longitude, route[0].longitude]
    y_values = [route[len(route) - 1].latitude, route[0].latitude]
    plt.plot(x_values, y_values)
    red_patch = mpatches.Patch(color="red", label=f'Temperatura: {round(temp, 6)}')
    blue_patch = mpatches.Patch(color="blue",label=f'Distancia: {round(distance, 6)} Km')
    green_patch = mpatches.Patch(color="green",label=f'Iteracion: {i_best}')
    plt.legend(handles=[red_patch,blue_patch, green_patch])
    plt.pause(.00000000000000000001)


def simulated_annealing(route, iterations):
    temp = 1000
    cooling_index = 0.003
    random.shuffle(route)
    actual_route = route.copy()
    best_route = route.copy()
    best_energy = get_energy(route)
    prob = 0
    # Variables para guardar resultados y poder sacar conclusiones
    best_temp = 0
    i_best = 0
    for i in range(iterations):
        new_route = actual_route.copy()
        # Selccion de dos randoms
        rand1, rand2 = random.sample(range(len(actual_route) - 1), 2)
        # Intercambiando dos ciudades en la nueva ruta
        new_route[rand1], new_route[rand2] = new_route[rand2], new_route[rand1]
        # Calculando energias(distancias)
        actual_energy = get_energy(actual_route)
        new_energy = get_energy(new_route)
        if new_energy < actual_energy:
            prob = 1
        else:
            prob = math.exp((actual_energy - new_energy) / temp)
        if prob > random.randint(0, 1):
            actual_route = new_route
            actual_energy = new_energy
        if actual_energy < best_energy:
            best_route = actual_route.copy()
            best_energy = get_energy(best_route)
            best_temp = temp
            i_best = i
            draw(actual_route, temp, best_energy, i_best)
        # Enfriamiento
        temp = (1 - cooling_index) * temp

    plt.close()
    print("La ruta es de: " + str(round(get_energy(best_route), 4)) + "km")
    return best_route, best_temp, best_energy, i_best, cooling_index
