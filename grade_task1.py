import numpy as np
from tasks import compute_dimensions

# Test for Task 1: compute_dimensions
def test_compute_dimensions():
    matrix = np.array([[1, 2], [3, 4]])
    assert compute_dimensions(matrix) == (2, 2)
    
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    assert compute_dimensions(matrix) == (2, 3)
    
    matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    assert compute_dimensions(matrix) == (3, 4)
