import pytest
from src.main import kmp_search


def test_kmp_search_basic_case():
    haystack = "ABABDABACDABABCABAB"
    needle = "ABABCABAB"
    expected_indexes = [10]
    assert kmp_search(haystack, needle) == expected_indexes


def test_kmp_search_multiple_occurrences():
    haystack = "AAAAA"
    needle = "AA"
    expected_indexes = [0, 1, 2, 3]
    assert kmp_search(haystack, needle) == expected_indexes


def test_kmp_search_no_occurrences():
    haystack = "ABCDEF"
    needle = "XYZ"
    expected_indexes = []
    assert kmp_search(haystack, needle) == expected_indexes


if __name__ == "__main__":
    pytest.main()
