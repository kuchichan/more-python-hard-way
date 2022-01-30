from typing import List, Tuple


class SuffixArray:
    def __init__(self, string_: str) -> None:
        self._sentence = string_
        self._array: List[Tuple[str, int]] = []

        for i in range(0, len(string_)):
            self._array.append((string_[i:], i))

        self._array.sort()

    @property
    def array(self) -> List[Tuple[str, int]]:
        return self._array

    def search(self, P: str) -> Tuple[int, int]:
        """
        Return indices (s, r) such that the interval A[s:r] (including the end
        index) represents all suffixes of S that start with the pattern P.
        """
        # Find starting position of interval
        l = 0  # in Python, arrays are indexed starting at 0
        r = len(self._sentence)
        while l < r:
            mid = (l + r) // 2  # division rounding down to nearest integer
            # suffixAt(A[i]) is the ith smallest suffix
            if P > self.array[mid][0]:
                l = mid + 1
            else:
                r = mid
        s = l

        # Find ending position of interval
        r = len(self._sentence)
        while l < r:
            mid = (l + r) // 2
            if self.array[mid][0].startswith(P):
                l = mid + 1
            else:
                r = mid
        return (s, r)

    # I really do not understand what's going on ->
    # This will found only the shortest, if its already in array
    # Compared with Zed Shaw solution
    def binary_search(self, string_: str) -> Tuple[int, int]:
        left = 0
        right = len(self.array)
        mid = len(self.array) // 2

        while left < right:
            mid = (right - left) // 2 + left
            mid_val, starts_at = self.array[mid]
            if mid_val == string_:
                return mid, starts_at
            if mid_val > string_:
                right = mid
            if mid_val < string_:
                left = mid + 1

        return -1, -1

    def find_shortest(self, _string) -> Tuple[int, int]:
        mid, starts_at = self.binary_search(_string)
        if mid < 0:
            return -1, -1
        return mid, starts_at

    def get_shortest_suffix(self, _string) -> Tuple[str, int]:
        (
            array_index,
            _,
        ) = self.find_shortest(_string)

        if not array_index:
            return "", -1

        return self._array[array_index][0], array_index

    def get_longest_suffix(self, string_: str) -> Tuple[str, int]:
        suffix, array_index = self.get_shortest_suffix(string_)

        if not suffix:
            "", -1

        for temp_suffix, _ in self.array[array_index:]:
            if not temp_suffix.startswith(string_):
                break
            suffix = temp_suffix
            array_index += 1

        return suffix, array_index
