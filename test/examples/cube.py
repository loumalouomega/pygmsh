#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Creates a mesh on a cube.
'''

import pygmsh as pg

import numpy as np


def generate():

    geom = pg.Geometry()

    geom.add_box(0, 1, 0, 1, 0, 1, 0.05)

    points, cells = pg.generate_mesh(geom)

    return points, cells


if __name__ == '__main__':
    generate()
