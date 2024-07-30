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


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def single_element_list():
    llist = LinkedList()
    llist.append(1)
    return llist


@pytest.fixture
def large_value_list():
    llist = LinkedList()
    llist.append(10**9)  # 1 billion
    return llist


def test_union_returns_set():
    new_union = union(linked_list_1, linked_list_2)
    sorted_union = sorted(list(new_union))
    assert sorted_union == [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]


def test_intersection_returns():
    new_intersection = intersection(linked_list_1, linked_list_2)
    sorted_intersection = sorted(list(new_intersection))
    assert sorted_intersection == [4, 6, 21]


# other test cases
def test_union_with_empty_lists(empty_list):
    assert list(union(empty_list, empty_list)) == []


def test_union_with_one_empty_list(empty_list, single_element_list):
    assert list(union(empty_list, single_element_list)) == [1]
    assert list(union(single_element_list, empty_list)) == [1]


def test_union_with_large_values(large_value_list, single_element_list):
    result = union(large_value_list, single_element_list)
    assert sorted(list(result)) == [1, 10**9]


def test_intersection_with_empty_lists(empty_list):
    assert list(intersection(empty_list, empty_list)) == []


def test_intersection_with_one_empty_list(empty_list, single_element_list):
    assert list(intersection(empty_list, single_element_list)) == []
    assert list(intersection(single_element_list, empty_list)) == []


def test_intersection_with_no_common_elements(single_element_list, large_value_list):
    assert list(intersection(single_element_list, large_value_list)) == []


def test_intersection_with_large_values(large_value_list):
    llist = LinkedList()
    llist.append(10**9)
    assert list(intersection(large_value_list, llist)) == [10**9]


def test_union_with_null_values():
    llist1 = LinkedList()
    llist1.append(None)
    llist2 = LinkedList()
    llist2.append(1)
    result = union(llist1, llist2)
    assert sorted(list(result), key=lambda x: (x is not None, x)) == [None, 1]


def test_intersection_with_null_values():
    llist1 = LinkedList()
    llist1.append(None)
    llist2 = LinkedList()
    llist2.append(None)
    llist2.append(1)
    assert list(intersection(llist1, llist2)) == [None]
