#!/usr/bin/env python
# coding: utf-8

# # New York City Leading Causes of Death
# ## Importing libraries and modules to be used

# In[2]:


import itertools
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib.colors as colors
import seaborn as sns
import scipy.optimize as opt
import pylab as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.cluster import KMeans
from sklearn.externals.six import StringIO
get_ipython().system('pip install pydotplus')
import pydotplus
import matplotlib.image as mpimp
from sklearn import tree
import matplotlib.patches as mpatches
mpl.style.use
get_ipython().system('pip install beautifulsoup4')
print("Libraries imported")


# In[51]:


df = pd.read_csv(r"C:\Users\c3273214\Desktop\NYCity.csv")


# In[52]:


df.head()


# In[ ]:




