import random as ran

import numpy as np

import matplotlib.pyplot as mpl

import math as ma

n = int(input())

b = int(ma.sqrt(n))

Throw_output_1 = []

Throw_output_2 = []

for i in range(0,n) :
    Throw_output_1.append(ran.randint(1,6))
    Throw_output_2.append(ran.randint(1,6))
    
die_1 = np.array(Throw_output_1)
    
die_2 = np.array(Throw_output_2)

output = die_1 + die_2

#print(output)

mpl.hist(output, bins = b)

mpl.show()