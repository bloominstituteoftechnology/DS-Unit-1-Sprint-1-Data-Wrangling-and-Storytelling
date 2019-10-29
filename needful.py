import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# In Google Colab, upload from local.
# from google.colab import files
# uploaded = files.upload()

# Load data from a URL.
data_url = "PUT-A-URL-HERE"

# If needed, define column names.
column_headers = [ 'cats', 'dogs']
df = pd.read_csv(df, header=None, names=column_headers)

df.head()
df.tail()
df.isnull().sum()
df.describe

# map strings to integers.
# map_dict = {'cat': 0, 'dog' : 2}
# df.replace({'column1name': map_dict, 'column2name': map_dict}, inplace=True)

# Seaborn for visualization
sns.set(style="ticks", color_codes=True)

sns.pairplot(df)

# Vizualization - edit these.
# Histogram
# df['acceptability'].hist(bins=20);

# Plot density
# df['acceptability'].plot.density();

# Scatterplot
# df.plot.scatter('buying', 'acceptability');
