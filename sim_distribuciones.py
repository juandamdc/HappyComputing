from random import random
import math

def sim_exponencial(lmbda):
    return -1 * math.log(random()) / lmbda

def sim_poisson(lmbda):
    sum = 0
    n = 0

    while True:
        sum += sim_exponencial(1)
        n += 1

        if sum > lmbda:
            break

    return n - 1

def sim_normal(media, varianza):
    while True:
        y_1 = sim_exponencial(1)
        y_2 = sim_exponencial(1)

        if y_2 - (y_1 - 1)**2 / 2 > 0:
            if random() <= 1/2:
                return y_1 * math.sqrt(varianza) + media
            return -1 * y_1 * math.sqrt(varianza) + media

def sim_serv_type():
    u = random()

    if u <= 0.45:
        return 1

    if  u <= 70:
        return 2

    if u <= 80:
        return 3

    return 4