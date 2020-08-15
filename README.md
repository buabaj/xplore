# xplore
---
xplore is a python package built with Pandas for data scientist or analysts, AI/ML engineers or researchers for exploring features of a dataset in one line of code for quick analysis before data wrangling and feature extraction.
---
# Getting started

## Install the package
```bash
pip install xplore
```

### Import the package into your code
```python
import xplore
```

### Assign the read/open command to the file path or URL of your structured dataset to a variable name 
```python
data = < Open / Read in your dataset file here >
```

### Explore your dataset using the xplore() method
```python
xplore(data)
```

### Testing xplore
Navigate to the test.py file after installing the package and run the code in that file to see and understand how xplore works.

## Sample Output
```python
------------------------------------
The fist 5 entries of your dataset are:

   rank country_full country_abrv  total_points  ...  three_year_ago_avg  three_year_ago_weighted  confederation   rank_date
0     1      Germany          GER           0.0  ...                 0.0                      0.0           UEFA  1993-08-08
1     2        Italy          ITA           0.0  ...                 0.0                      0.0           UEFA  1993-08-08
2     3  Switzerland          SUI           0.0  ...                 0.0                      0.0           UEFA  1993-08-08
3     4       Sweden          SWE           0.0  ...                 0.0                      0.0           UEFA  1993-08-08
4     5    Argentina          ARG           0.0  ...                 0.0                      0.0       CONMEBOL  1993-08-08

[5 rows x 16 columns]

------------------------------------
The description of you dataset is:

<bound method NDFrame.describe of        rank country_full country_abrv  total_points  ...  three_year_ago_avg  three_year_ago_weighted  confederation   rank_date
0         1      Germany          GER           0.0  ...                 0.0                      0.0           UEFA  1993-08-08
1         2        Italy          ITA           0.0  ...                 0.0                      0.0           UEFA  1993-08-08
2         3  Switzerland          SUI           0.0  ...                 0.0                      0.0           UEFA  1993-08-08
3         4       Sweden          SWE           0.0  ...                 0.0                      0.0           UEFA  1993-08-08
4         5    Argentina          ARG           0.0  ...                 0.0                      0.0       CONMEBOL  1993-08-08
...     ...          ...          ...           ...  ...                 ...                      ...            ...         ...
57788   206     Anguilla          AIA           0.0  ...                 0.0                      0.0       CONCACAF  2018-06-07
57789   206      Bahamas          BAH           0.0  ...                 0.0                      0.0       CONCACAF  2018-06-07
57790   206      Eritrea          ERI           0.0  ...                 0.0                      0.0            CAF  2018-06-07
57791   206      Somalia          SOM           0.0  ...                 0.0                      0.0            CAF  2018-06-07
57792   206        Tonga          TGA           0.0  ...                 0.0                      0.0            OFC  2018-06-07

[57793 rows x 16 columns]>

------------------------------------
The total number of null values from individual columns of your data set are:

rank                       0
country_full               0
country_abrv               0
total_points               0
previous_points            0
rank_change                0
cur_year_avg               0
cur_year_avg_weighted      0
last_year_avg              0
last_year_avg_weighted     0
two_year_ago_avg           0
two_year_ago_weighted      0
three_year_ago_avg         0
three_year_ago_weighted    0
confederation              0
rank_date                  0
dtype: int64

------------------------------------
The shape of your dataset in the order of rows and columns is:

(57793, 16)

------------------------------------
The features of your dataset are:

Index(['rank', 'country_full', 'country_abrv', 'total_points',
       'previous_points', 'rank_change', 'cur_year_avg',
       'cur_year_avg_weighted', 'last_year_avg', 'last_year_avg_weighted',
       'two_year_ago_avg', 'two_year_ago_weighted', 'three_year_ago_avg',
       'three_year_ago_weighted', 'confederation', 'rank_date'],
      dtype='object')

------------------------------------
```
## Contributing to xplore
Fork and clone this repo if you have any contributions you want to make. 
Push your commits to a new branch and send a PR when done.
I'll review your code and merge your PR as soon as possible.

## Maintainer: [Jerry Buaba](https://www.linkedin.com/in/buabaj/)