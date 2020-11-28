import os
import pytest
import random
import string

from sort_rev import __version__
from sort_rev.sort import check, g_numeric_sort


@pytest.fixture
def random_int_list(request):
    return random.choices(range(100), k=request.param)


@pytest.fixture
def random_str_list(request):
    def generate_random_word():
        return "".join(letter for letter in random.choices(string.ascii_letters, k=random.randint(1,8)))
    return [generate_random_word() for _ in range(request.param)]


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "list_1, list_2",
    [
        ([1, 2, 3], [1, 2, 3]),
        (["aaa", "bbb", "ccc"], ["aaa", "bbb", "ccc"]),
        ([], []),
    ],
)
def test_check_calls_os_ex_when_lists_are_equal(list_1, list_2, mocker):
    patch = mocker.patch("sort_rev.sort.sys.exit")
    check(list_1, list_2)
    patch.assert_called_once_with(os.EX_OK)


@pytest.mark.parametrize(
    "list_1, list_2",
    [
        ([1, 2, 3], [1, 3, 2]),
        (["aaa", "bbb"], ["aaa", "bbb", "ccc"]),
        ([], [100, 1000]),
    ],
)
def test_check_calls_os_ex_when_lists_are_not_equal(list_1, list_2, mocker):
    patch = mocker.patch("sort_rev.sort.sys.exit")
    check(list_1, list_2)
    patch.assert_called_once_with(os.EX_SOFTWARE)


@pytest.mark.parametrize(
    "random_int_list, random_str_list", [
        (3, 3),
        (5, 2),
        (10, 10),
    ], indirect=True
)
def test_check_g_numeric_sort(random_int_list, random_str_list):
    given = random_str_list + random_int_list
    expected = sorted(random_str_list) + sorted(random_int_list)

    assert g_numeric_sort(given) == expected
    
