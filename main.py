# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import pandas as pd
# import plotly.graph_objs as go
# import numpy as np
# import matplotlib.pyplot as plt
#
# data_url = 'https://raw.githubusercontent.com/youraunt/public/master/ENVS.csv'
# df = pd.read_csv(data_url, index_col='Miles')
# print(df.head())
# colors = (0,0,0)
# area = np.pi*3
#
#
# x_values = [10, 1.2, 15, 2.9, 9.1, 20, 20, 1, 10, 1, 22, 2, 3.7, 1, 6.6, 5.7]
# y_values = [25, 6, 36, 8, 27, 36, 40, 5, 16, 10, 41, 5, 11, 6, 30, 15]
# plt.scatter(x_values, y_values)
# correlation_matrix = np.corrcoef(x_values, y_values)
# correlation_xy = correlation_matrix[0, 1]
# r_squared = correlation_xy ** 2
# plt.show()
# print(r_squared)
# import numpy
#
# print("5 x 7 array of ints between 6 and 35 inclusive")
# newArray = numpy.random.random_integers(6, 36, size=(5, 7))
# print(newArray)

import secrets as s
import random as r


def random_a():
    return s.randbelow(6)


def random_b():
    return s.randbelow(9)


def a_from_b():
    return random_b() % 6


def b_from_a():
    # return (random_a() % 2)*3 + (random_a())
    return (random_a() & 3) + (random_a())


if __name__ == "__main__":
    print(random_a(), random_b())
    print(a_from_b())
    temp_int_storage = []
    for x in range(0, 10000):
        temp = a_from_b()
        temp_int_storage.append(temp)
        print(temp)
for x in range(0, 15):
    print(x, temp_int_storage.count(x))
