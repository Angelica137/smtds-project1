import pytest
from src.problem_4 import *


def test_is_user_in_empty_group():
    empty = Group("empty")
    user1 = "user1"
    assert is_user_in_group(user1, empty) is False


def test_is_user_in_parent_group():
    parent = Group("parent")
    user1 = "user1"
    parent.add_user(user1)
    assert is_user_in_group(user1, parent) is True


def test_is_user_in_subgroup():
    parent = Group("parent")
    sub_group = Group("sub_group")
    parent.add_group(sub_group)
    user1 = "user1"
    sub_group.add_user(user1)
    assert is_user_in_group(user1, parent) is True


def test_is_user_not_in_group():
    parent = Group("parent")
    sub_group = Group("sub_group")
    parent.add_group(sub_group)
    user1 = "user1"
    assert is_user_in_group(user1, parent) is False


def test_is_user_in_null_group():
    # null group is = None
    with pytest.raises(AttributeError):
        is_user_in_group("user123", None)


def test_empty_user_id():
    group = Group("group")
    group.add_user("")
    assert is_user_in_group("", group) is True
    assert is_user_in_group("", Group("empty")) is False


def test_is_user_in_very_large_group():
    large_group = Group("large")
    for i in range(1000000):  # Add a million users
        large_group.add_user(f"user{i}")
    assert is_user_in_group("user999999", large_group) is True
    assert is_user_in_group("nonexistent", large_group) is False
