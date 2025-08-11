import numpy as np
import pandas as pd
import os

from Methods import get_matrix_with_wieght, get_completion_matrix, complection_time, Matrix_info, new_matrix_step, transpose_neighbourhood, exchange_neighbourhood, insert_neighbourhood, WTC


def test_get_matrix_with_weight_and_w():
    # Build a small dataframe-like numpy array as Methods.getDataframe returns .values
    data = np.array([
        [3, 4, 2],
        [1, 5, 3],
    ])
    # Last column is weight
    M, w = get_matrix_with_wieght(data)
    assert M.tolist() == [[3, 4], [1, 5]]
    assert w == [2, 3]


def test_get_completion_matrix_basic():
    A = np.array([[3, 4], [1, 5]])
    D = get_completion_matrix(A)
    # Expected completion times for flow shop
    # Row 0: [3, 7]
    # Row 1: [4, 12]
    assert D.tolist() == [[3, 7], [4, 12]]


def test_complection_time():
    D = np.array([[3, 7], [4, 12]])
    last_col = complection_time(D)
    assert last_col == [7, 12]


def test_Matrix_info():
    last_col = [7, 12]
    w = [2, 3]
    W, Max, Sum1, Sum2 = Matrix_info(last_col, w)
    assert W == [14, 36]
    assert Max == 12
    assert Sum1 == 19
    assert Sum2 == 50


def test_new_matrix_step_and_WTC():
    # Matrix with 2 jobs, 2 machines + last col ignored by WTC pipeline
    data = np.array([
        [3, 4, 2],
        [1, 5, 3],
    ])
    # Permutation [1, 0]
    perm = [1, 0]
    m2 = new_matrix_step(data, perm)
    assert m2.tolist() == [[1, 5, 3], [3, 4, 2]]

    Sum1, Sum2 = WTC(m2)
    # Build expected directly
    M, w = get_matrix_with_wieght(m2)
    D = get_completion_matrix(M)
    last = complection_time(D)
    W, Max, Sum1_expected, Sum2_expected = Matrix_info(last, w)
    assert Sum1 == Sum1_expected
    assert Sum2 == Sum2_expected


def test_neighbourhood_generators():
    seq = [0, 1, 2]

    trans = transpose_neighbourhood(seq)
    # Must contain original and one adjacent swap at least
    assert seq in trans
    assert [1, 0, 2] in trans or [0, 2, 1] in trans

    exch = exchange_neighbourhood(seq)
    assert seq in exch
    assert [2, 1, 0] in exch or [1, 0, 2] in exch or [0, 2, 1] in exch

    ins = insert_neighbourhood(seq)
    assert seq in ins
    assert [1, 0, 2] in ins or [0, 2, 1] in ins