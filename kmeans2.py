#!/usr/bin/env python
#-*-coding=utf-8-*-
import numpy as np
def get_test_data():
    """
    调试数据
    """
    data = [
       [ 1.658985, 4.285136],
       [-3.453687, 3.424321],
       [4.838138, -1.151539],
       [-5.379713, -3.362104],
    ]
    return np.mat(data)
def dist_eclud(vec_a, vec_b):
    """
    计算距离
    """
    return np.sqrt(np.sum(np.power(vec_a-vec_b, 2)))
def rand_cent(data_set, k):
    """
    随机选取质心
    """
    m = np.shape(data_set)[1]
    center = np.mat(np.zeros((k, m)))
    for col in range(m):
        min_col = min(data_set[:, col])
        max_col = max(data_set[:, col])
        center[:, col] = min_col + float((max_col-min_col)) * np.random.rand(k, 1)
    return center
def kmeans(data_set, k, dist_method=dist_eclud, cent_methon=rand_cent):
    sample_count = np.shape(data_set)[0]
    is_change = True
    keep_result = np.mat(np.zeros((sample_count, 2)))
    center_roids= cent_methon(data_set, k)
    while is_change:
        is_change = False
        for sample_index in range(sample_count):
            min_dist, min_index = np.Inf, -1
            for j in range(k):
                dist_j = dist_method(data_set[sample_index,:], center_roids[j,:])
                if dist_j< min_dist:
                    min_dist , min_index = dist_j , j
            if keep_result[sample_index, 0] != min_index:
                is_change = True
            keep_result[sample_index,:] = min_index, min_dist**2
        for cent_index in range(k):
            temp_cluster = data_set[np.nonzero(keep_result[:,0].A==cent_index)[0]]
            center_roids[cent_index,:] = np.mean(temp_cluster, axis=0)
    return  keep_result
if __name__ == '__main__':
    data_set = get_test_data()
    print data_set
    result = kmeans(data_set,2)
    print result