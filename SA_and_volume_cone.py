#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 10.4.22
# Calculated the Surface Are and volume of a cone with user input.


import math

# These 2 variables are global functions are they are used in multiple functions.
cone_radius = float(input("What is the radius of your cone?(cm): "))
cone_height = float(input("What is the height of your cone?(cm): "))


def surface_area():
    surface_area = (
        math.pi
        * cone_radius
        * (cone_radius + math.sqrt((cone_height**2) + (cone_radius**2)))
    )
    # rounded the answer to 2 decimal places because it looks better.
    print("The surface area of your cone is {0:.2f} cm^2".format(surface_area))


def cone_volume():
    cone_volume = math.pi * cone_radius**2 * (cone_height / 3)
    # rounded the answer to 2 decimal places because it looks better.
    print("The volume of your cone is {0:.2f} cm^3".format(cone_volume))


if __name__ == "__main__":
    surface_area()
    cone_volume()
