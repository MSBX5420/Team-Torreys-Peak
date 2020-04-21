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

type(news)

news['text'][1]
type(news['text'][1])

news['url'][1]

news.text.replace("\xa0", "", regex= True, inplace=True)
news.text.replace("\\'s", "", regex= True, inplace=True)

news['text'][1]

type(news['text'])

news.text.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0)


newstest = news.iloc[:3]
newstest
newstest.text.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).sort_values(ascending=False).head(10)
