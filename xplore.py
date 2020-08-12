import pandas as pd

def xplore(data):
    '''
    xplore is a python package for light-weight python projects in data science and analytics, AI and ML.\n
    The xplore() function takes the arg 'data', which is a variable assigned to the file path/url of a labelled dataset.\n
    xplore converts the labelled dataset to a DataFrame and performs some predefined exploratory data analysis on the dataset.
    '''
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


