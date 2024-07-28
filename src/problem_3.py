import heapq
from collections import Counter


class Node:
    _node_count = 0

    def __init__(self, freq, char=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        # We need a tie braker for nodes with same frequencies, use class var
        self.creation_order = Node._node_count
        Node._node_count += 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        if self.char is not None and other.char is not None:
            return self.char < other.char
        if self.char is None and other.char is None:
            return self.creation_order < other.creation_order
        return self.char is not None  # Leaf nodes come before internal nodes


def huffman_encoding(data):
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

    return heap[0] if heap else None


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

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

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
