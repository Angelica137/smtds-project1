import sys
import heapq
from collections import Counter


class Node:
    _node_count = 0

    def __init__(self, freq: int, char=None):
        """
        Initialise a Node object for use in a Huffman tree.

        This class is used to create objects that store frequency-character pairs.
        Each node keeps track of its order of creation to help prioritize nodes
        with the same frequency.

        Args:
            freq (int): The frequency of the character.
            char (str, optional): The character represented by this node. Defaults to None.

        Attributes:
            char (str): The character represented by this node.
            freq (int): The frequency of the character.
            left (Node): The left child node in the Huffman tree.
            right (Node): The right child node in the Huffman tree.
            creation_order (int): The order in which this node was created.

        Class Attributes:
            _node_count (int): A class-level counter to keep track of node creation order.
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        # We need a tie braker for nodes with same frequencies, use class var
        self.creation_order = Node._node_count
        Node._node_count += 1

    def __lt__(self, other: object) -> bool:
        """
        Compares this node with another node for ordering.

        This method defines a custom ordering for Node objects to be used in the priority queue.

        The comparison is based on:
        1. Frequency (lower frequency comes first)
        2. Character value (if both nodes have characters)
        3. Creation order (for internal nodes without characters)
        4. Node type (leaf nodes come before internal nodes)

        Args:
            other (object): The other node to compare with.

        Returns:
            bool: True if this node should be considered 'less than' the other node,
            False otherwise.

        Raises:
            TypeError: If 'other' is not a Node object.

        Time complexity: O(1)
        """
        if self.freq != other.freq:
            return self.freq < other.freq
        if self.char is not None and other.char is not None:  # if same freq check chars
            return self.char < other.char
        if (
            self.char is None and other.char is None
        ):  # if same freq and chars check creation order
            return self.creation_order < other.creation_order
        return self.char is not None  # Leaf nodes come before internal nodes


def huffman_encoding(data: str) -> tuple[str, Node]:
    """ "
    Create a Huffman tree and encode the input data.

    This method implements the Huffman coding algorithm to compress the input string.

    Args:
        data (str): The input string to be encoded.

    Returns:
        tuple[str, Node]: A tuple containing the encoded data as a string and
                          the root node of the Huffman tree.
                          Returns (None, None) if the input data is empty.

    Process:
    1. Check if input data exists.
    2. Reset the Node count.
    3. Count character frequencies using Counter().
    4. Create a min heap of Nodes based on character frequencies.
    5. Build the Huffman tree by repeatedly merging the two least frequent nodes.
    6. Generate Huffman codes for each character.
    7. Encode the input data using the generated codes.

    Time Complexity:
        O(n log k), where n is the length of the input string and k is the number of unique characters.
        - Counting frequencies: O(n)
        - Creating initial heap: O(k log k)
        - Building Huffman tree: O(k log k)
        - Generating codes: O(k)
        - Encoding data: O(n)
    """
    if not data:
        return None

    Node._node_count = 0  # Reset node count for each encoding
    frequency = Counter(data)
    heap = [Node(freq, char) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = generate_codes(root)
    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, root


# Helper function to generate codes
def generate_codes(root: Node) -> dict:
    """
    Generate Huffman codes for each character in the Huffman tree.

    This function uses recursion to traverses the Huffman to generate binary codes
    for each character. It assigns '0' for left branches and '1' for right branches.

    Args:
        root (Node): The root node of the Huffman tree.

    Returns:
        dict: A dictionary where keys are characters and values are their
              corresponding Huffman codes as strings of '0's and '1's.

    Time Complexity:
        O(k), where k is the number of nodes in the Huffman tree.
        Each node is visited exactly once.

    Note:
        This function uses a nested helper function for the recursive traversal.
    """
    codes = {}

    def _generate_codes(node, current_code):
        # if we have gone past a leaf node, we completed traversal, so return
        if node is None:
            return
        # if we reached a leaf (coz it has a char) add the char and its code to the dict and return
        if node.char is not None:
            codes[node.char] = current_code
            return
        # else, traverse the tree building the code
        _generate_codes(node.left, current_code + "0")
        _generate_codes(node.right, current_code + "1")

    # start recursion
    _generate_codes(root, "")
    return codes


def huffman_decoding(data: str, tree: Node) -> str:
    """
    Decodes a Huffman-encoded string using the provided Huffman tree.

    Traverses the Huffman tree based on the input binary string,
    reconstructing the original text.

    Args:
        data (str): The Huffman-encoded string consisting of '0's and '1's.
        tree (Node): The root node of the Huffman tree used for decoding.

    Returns:
        str: The decoded string.

    Time Complexity:
        O(n), where n is the length of the encoded data string.
        Each bit in the encoded data is processed once.

    Note:
        - This function assumes that the provided Huffman tree corresponds to the encoded data.
        - The function resets to the root of the tree each time a character is decoded.
    """
    decoded_data = []
    current_node = tree

    for bit in data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree  # Go back to the root for the next character

    return "".join(decoded_data)


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    print("TEST")
    print(huffman_encoding(a_great_sentence))
    print("END TEST")

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(
        "The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))
        )
    )
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


"""
Test cases are in test file
"""
## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
