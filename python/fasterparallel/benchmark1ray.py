#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import numpy as np
import psutil
import ray
import scipy.signal

num_cpus = psutil.cpu_count(logical=False)

ray.init(num_cpus=num_cpus)


@ray.remote
def f(image, random_filter):
    # Do some image processing.
    return scipy.signal.convolve2d(image, random_filter)[::5, ::5]


filters = [np.random.normal(size=(4, 4)) for _ in range(num_cpus)]


def main():
    # Time the code below.

    for _ in range(10):
        image = np.zeros((3000, 3000))
        image_id = ray.put(image)
        ray.get([f.remote(image_id, filters[i]) for i in range(num_cpus)])


if __name__ == '__main__':
    main()
