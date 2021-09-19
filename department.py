import numpy as np

#Distancia entre dos Geo Coordenadas
def get_haversine_distance(latitude1, longitude1, latitude2, longitude2):
    r = 6371
    phi1 = np.radians(latitude1)
    phi2 = np.radians(latitude2)
    delta_phi = np.radians(latitude2 - latitude1)
    delta_lambda = np.radians(longitude2 - longitude1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)


class Department:
    def __init__(self, name, location):
        self.name = name
        self.latitude = location[0]
        self.longitude = location[1]
        self.location = location
    
    @staticmethod
    def get_distance_between_departments(department_one, department_two):
        result = get_haversine_distance(department_one.latitude, department_one.longitude,
                                        department_two.latitude, department_two.longitude)
        return result
