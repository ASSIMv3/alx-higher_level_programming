#!/usr/bin/python3
"""multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    # Validate m_a and m_b as lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Validate m_a and m_b as lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Validate m_a and m_b as non-empty lists of lists
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a) or len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Validate m_a and m_b elements as integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Validate m_a and m_b as rectangles
    num_cols_a = len(m_a[0])
    num_cols_b = len(m_b[0])
    if any(len(row) != num_cols_a for row in m_a) or any(len(row) != num_cols_b for row in m_b):
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if num_cols_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            val = 0
            for k in range(len(m_a[i])):
                val += m_a[i][k] * m_b[k][j]
            row.append(val)
        result.append(row)

    return result

