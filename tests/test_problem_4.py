from src.problem_4 import *


def test_is_user_in_empty_group():
    empty = Group("empty")
    user1 = 'user1'
    assert is_user_in_group(user1, empty) is False


def test_is_user_in_parent_group():
    parent = Group("parent")
    user1 = 'user1'
    parent.add_user(user1)
    assert is_user_in_group(user1, parent) is True
