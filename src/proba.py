##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-203hotline-tom.hermann
## File description:
## proba
##

import math
from src.constante import NB_PEOPLE, TIME_INTERVAL, SEC_PER_HOUR
import time
import datetime
from src.struct import Data
from sys import stderr

def calcule_coef_b(n, k):
    x = math.factorial(n)
    y = math.factorial(k) * math.factorial(n - k)
    return x // y

def binomialLaw(d, data):
    start = datetime.datetime.now()
    p = d / (SEC_PER_HOUR * TIME_INTERVAL)
    overload = 0
    for i in range(0, 51):
        proba = (calcule_coef_b(NB_PEOPLE, i)) * (p ** i) * ((1 - p) ** (NB_PEOPLE - i))
        if (i > 25):
            overload += proba
        data.add_to_x(i)
        data.add_to_y(round(proba * 100, 2))
    data.set_overload(overload * 100)
    data.set_compute_time((datetime.datetime.now() - start).microseconds / 100)


def poissonLaw(d, data):
    start = datetime.datetime.now()
    overload = 0
    λ = NB_PEOPLE * d / (SEC_PER_HOUR * TIME_INTERVAL)
    for i in range(0, 51):
        proba = (λ ** i) / math.factorial(i) * math.exp(-λ)
        if (i > 25):
            overload += proba
        data.add_to_x(i)
        data.add_to_y(round(proba * 100, 2))
    data.set_overload(overload * 100)
    data.set_compute_time((datetime.datetime.now() - start).microseconds / 100)
