import numpy as np
import pandas as pd


class Calculator:
    def __init__(self):
        self.inp_list = list(int(x) for x in input())

    def calculate(self):
        np_array = np.asarray(self.inp_list)
        matrix = np_array.reshape((3, 3))

        # compute mean
        axis1_mean = list(matrix.mean(axis=0, dtype='float32'))
        axis2_mean = list(matrix.mean(axis=1, dtype='float32'))
        flattened_mean = matrix.mean()

        # compute variance
        axis1_var = list(matrix.var(axis=0, dtype='float64'))
        axis2_var = list(matrix.var(axis=1, dtype='float64'))
        flattened_var = matrix.var()

        # compute standard deviation
        axis1_std = list(matrix.std(axis=0, dtype='float64'))
        axis2_std = list(matrix.std(axis=1, dtype='float64'))
        flattened_std = matrix.std()

        # compute max
        axis1_max = list(matrix.max(axis=0))
        axis2_max = list(matrix.max(axis=1))
        flattened_max = matrix.max()

        # compute min
        axis1_min = list(matrix.min(axis=0))
        axis2_min = list(matrix.min(axis=1))
        flattened_min = matrix.min()

        # compute sum
        axis1_sum = list(matrix.sum(axis=0))
        axis2_sum = list(matrix.sum(axis=1))
        flattened_sum = matrix.sum()

        result_dict = {
            'mean': [axis1_mean, axis2_mean, flattened_mean],
            'variance': [axis1_var, axis2_var, flattened_var],
            'standard deviation': [axis1_std, axis2_std, flattened_std],
            'max': [axis1_max, axis2_max, flattened_max],
            'mim': [axis1_min, axis2_min, flattened_min],
            'sum': [axis1_sum, axis2_sum, flattened_sum]
        }

        return result_dict


if __name__ == "__main__":
    # initiate a calculator class
    calculator = Calculator()

    if len(calculator.inp_list) >= 9:
        print(calculator.calculate())
    else:
        raise ValueError('List must contain nine numbers.')
