from src.problem_3 import *


def test_new_node():
    new_node = Node("a", 6)
    assert new_node.char == "a"
    assert new_node.freq == 6
    assert new_node.left is None
    assert new_node.right is None


def test_node_compares_itself():
    """
    GIVEN another node
    WHEN there is another node
    THEN check current node is less thatn other node
    """
    node_1 = Node("a", 5)
    node_2 = Node("c", 3)
    node_3 = Node("d", 5)
    assert node_2 < node_1
    assert not (node_1 < node_2)
    assert not (node_1 < node_3)


def test_huffman_encoding_no_data():
    data = ""
    assert huffman_encoding(data) == ""


def test_huffman_encoding_returns_heap():
    data = "aaabbbddd"
    expected_nodes = [Node("a", 3), Node("b", 3), Node("d", 3)]
    result = huffman_encoding(data)

    assert len(result) == len(expected_nodes)
    for node in result:
        assert any(
            node.char == expected.char and node.freq == expected.freq
            for expected in expected_nodes
        )
