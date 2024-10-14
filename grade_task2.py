import numpy as np
from tasks import compute_dimensions, compute_output_size


def test_compute_output_size():
    input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    kernel_matrix = np.array([[1, 0], [0, 1]])
    assert compute_output_size(input_matrix, kernel_matrix) == (2, 2)
    
    input_matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    kernel_matrix = np.array([[1, 0], [0, 1]])
    assert compute_output_size(input_matrix, kernel_matrix) == (2, 3)

