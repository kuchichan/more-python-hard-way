import argparse
import sys
import os

MODIFIERS = ("ignore_case", "ignore_leading_lines")

def get_input():
    while True:
        try:
            yield input()
        except EOFError:
            break

def print_elements(list_):
    for elem in list_:
        print(elem)

def check(list_, sorted_list):
    if list_ == sorted_list:
        sys.exit(os.EX_OK)
    sys.exit(os.EX_SOFTWARE)

def g_numeric_sort(list_, reverse=False, key=None):
    ints = []
    strs = []
    for elem in list_:
        try:
            ints.append(int(elem))
        except ValueError:
            strs.append(elem)

    strs.sort(reverse=False, key=None)
    ints.sort(reverse=False)
    strs.extend(ints)
    return strs
        
def ignore_case(elem):
    return elem.upper()

def ignore_leading_lines(elem):
    return elem.strip()


def apply_(args):
    if args.ignore_leading_lines and args.ignore_case:
        return lambda x: ignore_case(ignore_leading_lines(x))
    elif args.ignore_leading_lines:
        return lambda x : ignore_leading_lines(x)
    elif args.ignore_case:
        return lambda x : ignore_case(x)
    else:
        return lambda x: x
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser("sort")
    parser.add_argument("--reverse", "-r", action="store_true", default=False)
    parser.add_argument("--general-numeric-sort", "-g", action="store_true", default=False)
    parser.add_argument("--ignore-case", "-f", action="store_true", default=False)
    parser.add_argument("--ignore-leading-lines", "-b", action="store_true", default=False)
    parser.add_argument("--check", "-c", action="store_true", default=False)
    

    args = parser.parse_args()
    
    elements_to_sort = [x for x in get_input()]
    key = apply_(args)
    
    if args.general_numeric_sort:
        sorted_elements = g_numeric_sort(elements_to_sort, key=key)
    else:
        sorted_elements = sorted(elements_to_sort, reverse=args.reverse, key=key)

    if args.check:
        check(elements_to_sort, sorted_elements)

    print_elements(sorted_elements)
