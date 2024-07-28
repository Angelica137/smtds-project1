from src.problem_3 import *


def test_new_node():
    new_node = Node(6, "a")
    assert new_node.char == "a"
    assert new_node.freq == 6
    assert new_node.left is None
    assert new_node.right is None


def test_node_comparison():
    # Test case 1: Different frequencies
    node1 = Node(5, "a")
    node2 = Node(10, "b")
    assert node1 < node2
    assert not node2 < node1

    # Test case 2: Same frequency, different characters
    node3 = Node(5, "b")
    assert node1 < node3
    assert not node3 < node1

    # Test case 3: Same frequency, both internal nodes (no character)
    node4 = Node(5, None)
    node5 = Node(5, None)
    node4.creation_order = 1
    node5.creation_order = 2
    assert node4 < node5
    assert not (node5 < node4)

    # Test case 4: Same frequency, one leaf node and one internal node
    assert node1 < node4
    assert not node4 < node1

    # Test case 5: Equal nodes
    node6 = Node(5, "a")
    assert not node1 < node6
    assert not node6 < node1


def test_huffman_encoding_no_data():
    data = ""
    assert huffman_encoding(data) is None


def verify_tree_structure(node, expected, path="root"):
    if expected is None:
        assert node is None, f"Expected None at {path}, but got a node"
        return
    if node is None:
        assert False, f"Expected a node at {path}, but got None"

    print(
        f"Checking node at {path}: Expected {expected['char']}:{expected['freq']}, Got {node.char}:{node.freq}"
    )

    assert (
        node.char == expected["char"]
    ), f"At {path}: Expected char {expected['char']}, got {node.char}"
    assert (
        node.freq == expected["freq"]
    ), f"At {path}: Expected freq {expected['freq']}, got {node.freq}"

    verify_tree_structure(node.left, expected.get("left"), f"{path}.left")
    verify_tree_structure(node.right, expected.get("right"), f"{path}.right")


def print_tree_structure(node, prefix="", is_left=True):
    if node is not None:
        print(prefix + ("└── " if is_left else "┌── ") + f"{node.char}:{node.freq}")
        print_tree_structure(node.left, prefix + ("    " if is_left else "│   "), True)
        print_tree_structure(
            node.right, prefix + ("    " if is_left else "│   "), False
        )


def test_huffman_tree_structure_complex():
    data = "abcdefghabcdefgh"
    encoded_data, root = huffman_encoding(data)  # Unpack the tuple

    print("Actual tree structure:")
    print_tree_structure(root)  # Pass only the root to print_tree_structure

    expected_tree = {
        "freq": 16,
        "char": None,
        "left": {
            "freq": 8,
            "char": None,
            "left": {
                "freq": 4,
                "char": None,
                "left": {"freq": 2, "char": "a"},
                "right": {"freq": 2, "char": "b"},
            },
            "right": {
                "freq": 4,
                "char": None,
                "left": {"freq": 2, "char": "c"},
                "right": {"freq": 2, "char": "d"},
            },
        },
        "right": {
            "freq": 8,
            "char": None,
            "left": {
                "freq": 4,
                "char": None,
                "left": {"freq": 2, "char": "e"},
                "right": {"freq": 2, "char": "f"},
            },
            "right": {
                "freq": 4,
                "char": None,
                "left": {"freq": 2, "char": "g"},
                "right": {"freq": 2, "char": "h"},
            },
        },
    }

    verify_tree_structure(root, expected_tree)

    # Test the encoded data
    print(f"Encoded data: {encoded_data}")
    assert (
        len(encoded_data) == 48
    ), f"Expected encoded data length of 48, got {len(encoded_data)}"

    # Optionally, you can add more specific tests for the encoded data
    # For example, check if each character is encoded with 3 bits
    unique_codes = set(encoded_data[i : i + 3] for i in range(0, len(encoded_data), 3))
    assert (
        len(unique_codes) == 8
    ), f"Expected 8 unique 3-bit codes, got {len(unique_codes)}"


def test_generate_codes():
    # Create a simple Huffman tree
    leaf_a = Node(3, "a")
    leaf_b = Node(2, "b")
    leaf_c = Node(1, "c")
    internal_node = Node(3, None)
    internal_node.left = leaf_b
    internal_node.right = leaf_c
    root = Node(6, None)
    root.left = leaf_a
    root.right = internal_node

    # Generate codes
    codes = generate_codes(root)

    # Expected Huffman codes
    expected_codes = {"a": "0", "b": "10", "c": "11"}

    # Test if generated codes match expected codes
    assert codes == expected_codes, f"Expected {expected_codes}, but got {codes}"

    print("generate_codes test passed successfully!")


def test_huffman_decoding():
    test = "The bird is the word"
    encoded_data, tree = huffman_encoding(test)
    result = huffman_decoding(encoded_data, tree)
    assert result == "The bird is the word"
