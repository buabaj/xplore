import pandas as pd
from xplore.data import xplore

df = pd.read_csv('tests/fifa_ranking.csv')
xplore(df)

