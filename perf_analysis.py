import random

from shared.utils import time_attack
from exc_21_binary_search.binary_search import binary_search, binary_search_on_list
from exc_13_double_linked_list.double_linked_list.dl_list import DoubleLinkedList

POPULATION_RANGE = 500
LIST_RANGE = 10000

targets = random.choices([i for i in range(LIST_RANGE)], k=POPULATION_RANGE)


def measure_python_list():
    list_ = [i for i in range(LIST_RANGE)]

    print("Measurement of time for regular python list =>\n")

    with time_attack():
        for target in targets:
            binary_search(list_, target)


def measure_double_linked_list():
    double_linked_list = DoubleLinkedList()

    for i in range(LIST_RANGE):
        double_linked_list.push(i)

    print("Measurement of time for double linked list =>\n")

    with time_attack():
        for target in targets:
            binary_search_on_list(double_linked_list, target)


if __name__ == "__main__":
    print("Time comparison for binary search across different data structures:")
    print("=" * 30)
    measure_python_list()
    measure_double_linked_list()

