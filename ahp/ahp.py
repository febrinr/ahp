import numpy as np


def get_number_of_criteria(comparison_matrix):
    matrix_shape = comparison_matrix.shape
    count_matrix_rows = matrix_shape[0]

    return count_matrix_rows


def get_normalized_matrix(comparison_matrix):
    sum_matrix_columns = np.sum(comparison_matrix, axis=0)
    normalized_matrix = comparison_matrix / sum_matrix_columns

    return normalized_matrix


def calculate_priority_vector(normalized_matrix):
    average_normalized_matrix_rows = np.mean(normalized_matrix, axis=1)

    return average_normalized_matrix_rows


def calculate_consistency_index(priority_vector, comparison_matrix, number_of_criteria):
    w = priority_vector
    max_eigenvalue = np.dot(w, np.dot(comparison_matrix, w))
    consistency_index = (max_eigenvalue - number_of_criteria) / (number_of_criteria - 1)

    return consistency_index


def calculate_consistency_ratio(number_of_criteria, consistency_index):
    # (Table of random index values can be found in AHP literature)
    random_index = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.89, 5: 1.12, 6: 1.24, 7: 1.35, 8: 1.47, 9: 1.59}

    if number_of_criteria not in random_index:
        print("WARNING: Random index (RI) not available for matrix size", number_of_criteria)
        consistency_ratio = np.nan  # Not a number
    else:
        consistency_ratio = consistency_index / random_index[number_of_criteria]

    return consistency_ratio


def ahp(comparison_matrix):
    number_of_criteria = get_number_of_criteria(comparison_matrix)
    normalized_matrix = get_normalized_matrix(comparison_matrix)
    priority_vector = calculate_priority_vector(normalized_matrix)
    consistency_index = calculate_consistency_index(priority_vector, comparison_matrix, number_of_criteria)
    consistency_ratio = calculate_consistency_ratio(number_of_criteria, consistency_index)

    return priority_vector, consistency_ratio


# Example usage with error handling
comparison_matrix = np.array(
    [[1, 3, 5],
    [1/3, 1, 4],
    [1/5, 1/4, 1]]
)

priority_vector, consistency_ratio = ahp(comparison_matrix)

print("Priority vector:", priority_vector)
print("Consistency ratio:", consistency_ratio)
