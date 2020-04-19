print("hello world!")

import os
os.chdir('data')
path = os.getcwd()
print(path)

# change working directory to where the data file stores

import pandas as pd
from pandas import  *
news = pd.read_csv('news.csv')
news
news.columns
news = news.drop(columns=['Unnamed: 0'])
news
