from src.problem_2 import find_files


def test_empty_directory():
    no_match_files = "src/testdir/subdir2"
    result = find_files(".c", no_match_files)
    assert result == []
