import numpy as np
import pandas as pd

def xplore(data):
    data = pd.DataFrame(data)
    print('------------------------------------')
    print('The fist 5 entries of your dataset are:\n')
    print(data.head())
    print('')

    print('------------------------------------')
    print('The description of you dataset is:\n')
    print(data.describe)
    print('')

    print('------------------------------------')
    print('The total number of missing values from individual columns of your data set are:\n')
    print(data.isnull().sum())
    print('')

    print('------------------------------------')
    print('The shape of your dataset in the order of rows and columns is:\n')
    print(data.shape)
    print('')

    print('------------------------------------')
    print('The features of your dataset are:\n')
    print(data.columns)
    print('')

    print('------------------------------------')


