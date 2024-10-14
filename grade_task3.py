import numpy as np
from tasks import compute_dimensions, compute_output_size, convolute 


def test_convolute():
	input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	kernel_matrix = np.array([[1, 0], [0, 1]])
	expected_output = np.array([[6, 8], [12, 14]])
	assert np.array_equal(convolute(input_matrix, kernel_matrix), expected_output)

	input_matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
	kernel_matrix = np.array([[1, 0], [0, 1]])
	expected_output = np.array([[7, 9, 11], [15, 17, 19]])


	assert np.array_equal(convolute(input_matrix, kernel_matrix), expected_output)
