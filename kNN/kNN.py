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
    # Notice: linalg.solve(matA, matB) for division operation
    norm_dataset = norm_dataset/tile(data_range, (m, 1))

    return norm_dataset, data_range, min_value


def dating_class_test():
    ratio = 0.10
    dating_data_matrix, dating_labels = file2matrix('datingTestSet2.txt')
    norm_matrix, ranges, min_value = auto_norm(dating_data_matrix)
    m = norm_matrix.shape[0]

    num_test_vectors = int(m*ratio)
    error_count = 0.0

    for i in range(num_test_vectors):
        classifier_result = classify0(norm_matrix[i, :], norm_matrix[num_test_vectors:m, :],
                                      dating_labels[num_test_vectors:m], 3)
        print "the classifier came back with: %s, the real answer is: %s" \
              % (classifier_result, dating_labels[i])

        if classifier_result != dating_labels[i]:
            error_count += 1.0

    print "the total error rate is: %f" % (error_count/float(num_test_vectors))


def classify_person():
    result_list = ['not at all', 'in small doses', 'in large doses']
    percent_time = float(raw_input("percentage of time spent playing video games?"))
    fly_miles = float(raw_input("frequent flier miles earned per year?"))
    ice_cream = float(raw_input("liters of ice cream consumed per year?"))
    dating_data_matrix, dating_label = file2matrix('datingTestSet.txt')
    norm_matrix, ranges, min_value = auto_norm(dating_data_matrix)
    in_array = array([fly_miles, percent_time, ice_cream])
    classifier_result = classify0((in_array - min_value)/ranges, norm_matrix,dating_label, 3)

    print "you will probably like this person: ", classifier_result