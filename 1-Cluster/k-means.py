import numpy as np
from scipy.cluster.vq import kmeans,vq,whiten
# vq is mean of vector quantization
# data generation with three features

data=np.vstack((np.random.rand(100,3) + np.array([.5,.5,.5]),np.random.rand(100,3)))

# whitening of data
data = whiten(data)
# computing K-Means with clusters
centroids,_ = kmeans(data,3)
print(centroids)