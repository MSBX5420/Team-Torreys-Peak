#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import necessary libraries.
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


import os
os.chdir('data')
path = os.getcwd()
print(path)









# In[8]:


df = pd.read_csv("/news.csv", index_col=0)


# In[9]:


df.head()



# In[32]:


text = df.text[0]

# Create and generate
wordcloud = WordCloud().generate(text)

# Display
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[34]:



wordcloud = WordCloud(max_font_size=50, max_words=1000, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# In[37]:


text = " ".join(review for review in df.text)
print ("There are {} words in the combination of all descriptions.".format(len(text)))


# In[35]:


stopwords = set(STOPWORDS)
stopwords.update(["said", "one", "many", "covid", "say","will","COVID", "says", "Canada", "wednesday", "thursday", "province", "https"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[ ]:
