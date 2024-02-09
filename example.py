#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
print('hello world')


count = int(input("Enter a number: "))

print(count)


x = np.arange(count)

y = 2*x + np.random.randn(len(x))


plt.plot(x,y)

plt.savefig('example_nontext.png')
