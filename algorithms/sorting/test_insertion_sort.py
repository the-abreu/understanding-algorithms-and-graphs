from insertion_sort import insertion_sort


def test_insertion_sort():
    assert insertion_sort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]


def test_empty_array():
    assert insertion_sort([]) == []


def test_single_element():
    assert insertion_sort([10]) == [10]


def test_already_sorted():
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_order():
    assert insertion_sort([4, 3, 2, 1]) == [1, 2, 3, 4]