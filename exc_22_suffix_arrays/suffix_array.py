from typing import List, Optional


class SuffixArray:
    def __init__(self, string_: str) -> None:
        self._array: List[str] = []

        for i in range(0, len(string_)):
            self._array.append(string_[i:])

        self._array.sort()

    @property
    def array(self) -> List[str]:
        return self._array

    def find_shortest(self, string_: str) -> Optional[str]:
        found = None
        left = 0
        right = len(self.array) - 1
        mid = len(self.array) // 2

        while left <= right:
            mid_suffix = self.array[mid]
            if string_ < mid_suffix:
                right = mid - 1
                mid = (right - left) // 2
                if (not found or mid_suffix < found) and mid_suffix.startswith(string_):
                    found = mid_suffix
            elif string_ > mid_suffix:
                left = mid + 1
                mid = (right + left) // 2
                if (not found or mid_suffix < found) and mid_suffix.startswith(string_):
                    found = mid_suffix
            else:
                return string_

        return found
