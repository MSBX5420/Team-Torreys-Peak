print("hello world!")

import os
path = os.getcwd()
print(path)

# change working directory to where the data file stores
# os.chdir('data')
# print(path)

import pandas as pd
from pandas import  *
news = pd.read_csv('news.csv')
news
news.columns
news = news.drop(columns=['Unnamed: 0'])
news
