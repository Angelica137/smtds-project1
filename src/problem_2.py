import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = []

    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith(suffix):
                    result.append(entry.path)
                elif entry.is_dir():
                    result.extend(find_files(suffix, entry.path))
    except PermissionError:
        print(f"Permission denied: {path}")
    return result

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3

# I am not sure that these test cases need to be implemented for this
# problem? We would not get null and I am not sure about setting up
# The tests that create a large number of files.
