import pytest
from src.problem_6 import *


@pytest.fixture
def linked_lists():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    return linked_list_1, linked_list_2


def test_union_returns_set():
    new_union = union(linked_list_1, linked_list_2)
    sorted_union = sorted(list(new_union))
    assert sorted_union == [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]


def test_intersection_returns():
    new_intersection = intersection(linked_list_1, linked_list_2)
    sorted_intersection = sorted(list(new_intersection))
    assert sorted_intersection == [4, 6, 21]