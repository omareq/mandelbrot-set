#!/usr/bin/env python3

import cmath
import numpy as np
import matplotlib.pyplot as plt


def main():
    x_limits = (-2, 0.5)
    y_limits = (-1.15, 1.15)

    x_num_pts = 1000
    y_num_pts = 1000

    xx = np.linspace(x_limits[0], x_limits[1], x_num_pts)
    yy = np.linspace(y_limits[0], y_limits[1], y_num_pts)

    img = np.full((x_num_pts, y_num_pts), 255)

    max_steps = 100
    threshold = 4

    for i in range(len(xx)):
        for j in range(len(yy)):
            x = xx[i]
            y = yy[j]
            c = complex(x, y)
            itt = 1

            z = c
            while itt < max_steps and (z * z.conjugate()).real < threshold:
                z = z * z + c
                itt = itt + 1

            img[i][j] = 255 - itt

    plt.imshow(img, cmap="jet")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
