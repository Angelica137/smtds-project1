import hashlib
import time


class Block:
    """
    This class provides a blueprint for creating and managing blocks
    in a blockchain system.

    Attributes:
        timestamp (float): The time when the block was created.
        data (str): The data stored in the block.
        previous_hash (str): The hash of the previous block in the chain.
        hash (str): The hash of the current block.

    Time complexity: O(1) for initialisation.
    """
    def __init__(self, timestamp, data, previous_hash):
        """
        Initialises a new Block instance.

        Args:
            timestamp (float): The time when the block was created.
            data (str): The data to be stored in the block.
            previous_hash (str): The hash of the previous block in the chain.

        Time complexity: O(1) for attribute assignment, O(n) for hash calculation
        where n is the length of the input string.
        """
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        Calculates the hash of the block.
        Provides the hashing algorithm using SHA-256 from hashlib.

        Returns:
            str: The hexadecimal digest of the hash.

        Time complexity: O(n) where n is the length of the input string.
        """
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        encoded_hash_str = hash_str.encode('utf-8')  # unicode obj must be encoded before hashing
        sha.update(encoded_hash_str)
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(time.time(), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(time.time(), data, previous_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for i, block in enumerate(self.chain):
            print(f"Block {i}:")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Data: {block.data}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Hash: {block.hash}")
            print()


"""
Test casesin test file
"""

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
