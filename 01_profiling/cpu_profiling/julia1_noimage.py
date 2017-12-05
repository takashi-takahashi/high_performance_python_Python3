# coding=utf-8
import time
import functools

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# area of complex space to explored
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def timefn(func):
    @functools.wraps(func)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("@timefn:", func.__name__, "took", t2 - t1, "secnods")
        return result

    return measure_time


def calculate_z_serial_purepython(max_iterations, zs, cs):
    """Calculate output list using Julia update rule

    Args:
        max_iterations:
        zs: complex coordinate list
        cs: complex parameter list

    Returns:
        iteration number list
    """
    output = [0] * len(zs)
    for i in list(range(len(zs))):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < max_iterations:
            z = z * z + c
            n += 1
        output[i] = n

    return output


@timefn
def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex co-ordinates (zs) and complex parameters (cs), build Julia set and display

    Args:
        desired_width: desired grid width size
        max_iterations: max iterations

    Returns:

    """
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step

    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("length of x:{0}".format(len(x)))
    print("total elements:{0}".format(len(zs)))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__, "took", secs, "seconds")


if __name__ == '__main__':
    calc_pure_python(desired_width=1000, max_iterations=300)
