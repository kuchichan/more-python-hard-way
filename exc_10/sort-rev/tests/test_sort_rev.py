import os
import pytest
from sort_rev import __version__
from sort_rev.sort import check


def test_version():
    assert __version__ == "0.1.0"

@pytest.mark.parametrize("list_1, list_2", [
    ([1,2,3], [1,2,3]),
    (["aaa", "bbb", "ccc"], ["aaa", "bbb", "ccc"]),
    ([], []),
])
def test_check_calls_os_ex_when_lists_are_equal(list_1, list_2, mocker):
    patch = mocker.patch("sort_rev.sort.sys.exit")
    check(list_1, list_2)
    patch.assert_called_once_with(os.EX_OK)    
