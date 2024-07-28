from src.problem_3 import *


def test_new_node():
    new_node = Node('a', 6)
    assert new_node.char == 'a'
    assert new_node.freq == 6
