##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-203hotline-tom.hermann
## File description:
## struct
##


from sys import stderr

class Data:

    def __init__(self):
        self.x_axe = []
        self.y_axe = []
        self.overload = 0.0
        self.compute_time = 0.0

    def get_x(self):
        return self.x_axe

    def get_y(self):
        return self.y_axe

    def get_overload(self):
        return self.overload

    def get_compute_time(self):
        return self.compute_time

    def add_to_x(self, new):
        self.x_axe.append(new)

    def add_to_y(self, new):
        self.y_axe.append(new)

    def set_compute_time(self, compute_time):
        self.compute_time = compute_time

    def set_overload(self, overload):
        self.overload = overload