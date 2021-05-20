#!/usr/bin/env python
# coding: utf-8

# In[39]:


# importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize


# In[40]:


# reading the gene expression file as pandas dataframe

df = pd.read_csv("GDS2002 - Copy.csv") 
gene_names = df['ID_REF']
del df['ID_REF']


# In[41]:


# replacing the infinite, nan values

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(0, inplace=True)

# normalizing the data for faster and homogeneous calculations
data_scaled = normalize(df)
data_scaled = pd.DataFrame(data_scaled, columns=df.columns)


# In[42]:


# plotting the dendrogram using Hierarchical Clustering

import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10, 7))  
plt.title("Dendrograms")  
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))


# In[43]:


# looking at the dendorgram lets decide the thresold value as 16

plt.figure(figsize=(10, 7))  
plt.title("Dendrograms")  
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
plt.axhline(y=16, color='r', linestyle='--')
plt.show()


# In[44]:


# we got total 5 clusters, now lets get which gene belong to which cluster

from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')  
clusterNumber = cluster.fit_predict(data_scaled)
clusterNumber


# In[45]:


# segregating genes by their cluster numbers

cluster_array = [[], [], [], [], []]
for i in range(len(gene_names)):
    cluster_array[clusterNumber[i]].append(gene_names[i])
index = 0
for cluster in cluster_array:
    print("Genes belonging to Cluster " + str(index)+' :-->\n')
    for gene in cluster:
        print(gene, end=', ')
    print('\n\n\n')
    index+=1

