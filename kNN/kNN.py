__author__ = 'Liruo_000'
from numpy import *
import operator


def classify0(inX, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(inX, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5
    sorted_dist_indicies = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.iteritems(),
            key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B' ]
    return group, labels


def file2matrix(filename):
    fr = open(filename)
    n = len(fr.readlines())
    return_matrix = zeros((n, 3))
    class_label_vector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        words = line.split('\t')
        return_matrix[index, :] = words[0:3]
        class_label_vector.append((words[-1]))
        index += 1

    return return_matrix, class_label_vector


def auto_norm(dataset):
    min_value = dataset.min()
    max_value = dataset.max()

    data_range = max_value - min_value

    norm_dataset = zeros(shape(dataset))

    m = dataset.shape[0]
    norm_dataset = dataset - tile(min_value, (m, 1))
    norm_dataset = norm_dataset/tile(data_range, (m, 1))

    return norm_dataset, data_range, min_value







