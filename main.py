import numpy as np
import csv
from body import Body
from system import System


def string_to_vector(string):
    elements = string.strip('[]').split(',')
    vector = [float(element.strip()) for element in elements]
    return np.array(vector)


def read_csv_data(filename):
    system_data = {}
    bodies_data = []

    file = open(filename, 'r')
    bodies_reader = csv.DictReader((line for line in file if not line.startswith('#')))
    for body_data in bodies_reader:
        body = {"name": body_data["name"],
                "color": body_data["color"],
                "mass": float(body_data["mass"]),
                "position": string_to_vector(body_data["position"]),
                "velocity": string_to_vector(body_data["velocity"])}
        bodies_data.append(body)
    file.close()

    file = open(filename, 'r')
    system_reader = csv.reader((line for line in file if line.startswith('#')))
    for row in system_reader:
        elements = row[0].strip('#').strip().split(':')
        if elements[0] == "system_name":
            system_data["system_name"] = elements[1].strip()
        elif elements[0] == "system_dimension":
            system_data["system_dimension"] = int(elements[1].strip())
        elif elements[0] == "system_totaltime":
            system_data["system_totaltime"] = float(elements[1].strip())
        elif elements[0] == "system_timestep":
            system_data["system_timestep"] = float(elements[1].strip())
    file.close()

    return system_data, bodies_data


def simulate_system(system_info, bodies_info):
    system = System(system_info["system_name"], system_info["system_dimension"])
    for body_info in bodies_info:
        body = Body(body_info["name"], body_info["color"], body_info["mass"], body_info["position"], body_info["velocity"])
        system.add_body(body)

    system.run_simulation(system_info["system_totaltime"], system_info["system_timestep"])


system_dic, bodies_list = read_csv_data('arbitrary_system.csv')
simulate_system(system_dic, bodies_list)
