from src.problem_3 import *


def test_new_node():
    new_node = Node(a, 6)
    new_node.char == 'a'
    new_node.freq == 6
