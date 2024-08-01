# Show Me the Data Structures

This project is my submission for the data structures module in the Data Structures and Algorithms Udacity Nanodegree


## Setup and Installation
Follow these steps to set up the project and run the tests:

### Prerequisites

Python 3.7 or higher
pip (Python package installer)

### Setup Instructions

1. Clone the repository:

```
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On macOS and Linux:
```
source venv/bin/activate
```

4. Install the required packages:
Copypip install -r requirements.txt


## Running Tests
After setting up the virtual environment and installing the requirements, you can run the tests using:
```
pytest
```


## Problem 1: LRU Cache
Design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

## Problem 2: File Recursion
Write code for finding all files under a directory (and all directories beneath it) that end with ".c"

## Problem 3: Huffman Coding
Implement the Huffman coding algorithm.

## Problem 4:  Active Directory
Find if a user is in a group by searching the tree

## Problem 5: Blockchain
A simple implementation of a blockchain


## Problem 5: Union and Intersection
Given 2 linked lists, write two function that return a new linked list that made up their union and intersection nodes respectively.