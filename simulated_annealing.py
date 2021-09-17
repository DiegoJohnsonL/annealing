from department import Department, get_haversine_distance
import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def get_energy(route):
    energy = 0
    for i in range(len(route) - 1):
        energy += Department.get_distance_between_departments(route[i], route[i + 1])
    energy += Department.get_distance_between_departments(route[len(route) - 1], route[0])
    return energy


def draw(route, temp, distance):
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
    plt.legend(handles=[red_patch,blue_patch])
    plt.pause(.00000000000000000001)


def simulated_annealing(route, iterations):
    temp = 1000
    cooling_index = 0.003
    random.shuffle(route)
    t_actual = route.copy()
    t_best = route.copy()
    e_best = get_energy(route)
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
        if e_actual < e_best:
            t_best = t_actual.copy()
            e_best = get_energy(t_best)
            draw(t_actual, temp, e_best)

        temp = (1 - cooling_index) * temp
        print(f'Iteracion: {i}')

    plt.close()
    print("La ruta es de: " + str(round(get_energy(t_best), 4)) + "km")
    return t_best
