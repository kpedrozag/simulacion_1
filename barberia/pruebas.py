import numpy as np


def arrival_clients_hour(x):
    # x = true -> jornada de la mañana 7-11
    # x = false -> jornada de la tarde 2-5
    rt = np.random.poisson(3, 4) if x else np.random.poisson(3, 3)
    """
    if x:
        return np.random.poisson(3, 4)
    else:
        return np.random.poisson(3, 3)
    """

    return rt


print(arrival_clients_hour(True).size, "4")
print(arrival_clients_hour(False).size, "3")
