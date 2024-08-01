import hashlib
import time


class Block:
    """
    Provides a blueprint for creating and managing blocks
    in a blockchain system.

    Attributes:
        timestamp (float): The time when the block was created.
        data (str): The data stored in the block.
        previous_hash (str): The hash of the previous block in the chain.
        hash (str): The hash of the current block.

    Time complexity: O(1) for initialisation.
    """
    def __init__(self, timestamp: float, data: str, previous_hash: str):
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

    def calc_hash(self) -> str:
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
    """
    Represents a blockchain using a linked list implementation.

    Provides methods to create and manage a blockchain,
    including adding new blocks and printing the entire chain.

    Attributes:
        chain (list): A list of Block objects representing the blockchain.

    Time complexity: O(1) for initialization.
    """
    def __init__(self):
        """
        Creates an intance of a block to add as first block.
        Uses prvious hash '0' by convention.

        Time complexity: O(1)
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Creates and returns the genesis block of the blockchain.

        The genesis block is the first block in the blockchain and has a
        previous hash of "0" by convention.

        Returns:
            Block: The genesis block.

        Time complexity: O(1)
        """
        return Block(time.time(), "Genesis Block", "0")

    def add_block(self, data: str):
        """
        Adds a new block to the blockchain.

        This method creates a new block with the given data and adds it to
        the end of the blockchain. The new block's previous_hash is set to
        the hash of the last block in the chain.

        Args:
            data (str): The data to be stored in the new block.

        Time complexity: O(1) for adding the block, O(n) for hash calculation
        where n is the length of the combined input data.
        """
        previous_block = self.chain[-1]
        new_block = Block(time.time(), data, previous_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        """
        Print the entire blockchain to the console.

        This method iterates through all blocks in the chain and prints
        their details, including index, timestamp, data, previous hash,
        and current hash.

        Time complexity: O(n) where n is the number of blocks in the chain.
        """
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
