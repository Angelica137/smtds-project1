from src.problem_5 import *


def test_create_first_block_in_chain():
    blockchain = Blockchain()
    assert blockchain.chain[0].data == "Genesis Block"


def test_add_block():
    blockchain = Blockchain()
    blockchain.add_block("Test Block")
    assert len(blockchain.chain) == 2
    assert blockchain.chain[1].data == "Test Block"


def test_previous_hash():
    blockchain = Blockchain()
    blockchain.add_block("Block 1")
    blockchain.add_block("Block 2")
    assert blockchain.chain[2].previous_hash == blockchain.chain[1].hash


def test_add_empty_data_block():
    blockchain = Blockchain()
    blockchain.add_block("")
    assert blockchain.chain[-1].data == ""


def test_add_large_data_block():
    blockchain = Blockchain()
    large_data = "A" * 1000000  # 1 million characters
    blockchain.add_block(large_data)
    assert blockchain.chain[-1].data == large_data


def test_multiple_blocks():
    blockchain = Blockchain()
    for i in range(100):
        blockchain.add_block(f"Block {i}")
    assert len(blockchain.chain) == 101  # 100 + genesis block
