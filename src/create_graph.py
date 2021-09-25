##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-203hotline-tom.hermann
## File description:
## create_graph
##


import matplotlib.pyplot as plt
from src.struct import Data
from matplotlib.patches import Polygon



def create_graph(binLaw, poiLaw):

    fig, (ax1, ax2) = plt.subplots(2, 1)
    plt.tight_layout(3.3)

    ax1.plot(binLaw.get_x(), binLaw.get_y(), label = "Binomial Law")
    ax1.set_ylabel('Probalities (%)')
    ax1.set_xlabel('Simultaneous call')
    ax1.set_title("Binomial Law (Exectution time: {:.2f}ms)".format(binLaw.get_compute_time()))
    ax1.legend()
    ax1.set_ylim(bottom=0)

    intergral = [(25, 0), *zip(binLaw.get_x()[25:-1], binLaw.get_y()[25:-1]), (50, 0)]
    poly = Polygon(intergral, facecolor='0.9', edgecolor='0.5')
    ax1.add_patch(poly)
    ax1.text(26, 0.1, "Overload: {:.2f}%".format(binLaw.get_overload()))


    ax2.plot(poiLaw.get_x(), poiLaw.get_y(), label = "Poisson Law")
    ax2.set_xlabel('Simultaneous call')
    ax2.set_ylabel('Probalities (%)')
    ax2.set_title("Poisson Law (Exectution time: {:.2f}ms)".format(poiLaw.get_compute_time()))
    ax2.legend()
    ax2.set_ylim(bottom=0)

    intergral = [(25, 0), *zip(poiLaw.get_x()[25:-1], poiLaw.get_y()[25:-1]), (50, 0)]
    poly = Polygon(intergral, facecolor='0.9', edgecolor='0.5')
    ax2.add_patch(poly)
    ax2.text(26, 0.1, "Overload: {:.2f}%".format(poiLaw.get_overload()))

    plt.show()