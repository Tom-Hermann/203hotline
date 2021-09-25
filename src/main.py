#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-203hotline-tom.hermann
## File description:
## main
##

from sys import argv
from src.error import error_case
from src.proba import calcule_coef_b, binomialLaw, poissonLaw
from src.struct import Data
from src.create_graph import create_graph

error_case(len(argv))

if (len(argv) == 3):
    n = int(argv[1])
    k = int(argv[2])
    print("%d-combinations of a set of size %d:" %(k, n))
    print("%d\n" %(calcule_coef_b(n, k)))
else:
    binLaw = Data()
    poiLaw = Data()
    d = int(argv[1])
    binomialLaw(d, binLaw)
    poissonLaw(d, poiLaw)
    create_graph(binLaw, poiLaw)
exit(0)

