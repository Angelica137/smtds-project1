from src.problem_2 import find_files


def test_empty_directory():
    no_match_files = "src/testdir/subdir2"
    result = find_files(".c", no_match_files)
    assert result == []


def test_subdir5():
    subdir5 = "src/testdir/subdir5"
    result = find_files(".c", subdir5)
    assert result == ["src/testdir/subdir5/a.c"]
