#!/usr/bin/env python
#-*-coding=utf-8-*-
import numpy as np
from sklearn.cluster import KMeans
data = np.random.rand(100, 2) #生成一个随机数据，样本大小为100, 特征数为3
print data
#假如我要构造一个聚类数为3的聚类器
estimator = KMeans(n_clusters=3)#构造聚类器
estimator.fit(data)#聚类
label_pred = estimator.labels_ #获取聚类标签
print label_pred
centroids = estimator.cluster_centers_ #获取聚类中心
print centroids
inertia = estimator.inertia_ # 获取聚类准则的总和
print inertia