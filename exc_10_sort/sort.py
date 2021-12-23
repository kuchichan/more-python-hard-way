import argparse

def get_input():
    while True:
        try:
            yield input()
        except EOFError:
            break

def try_to_int(list_):
    ints = []
    non_ints = []
    for elem in list_:
        try:
            ints.append(int(elem))
        except ValueError:
            non_ints.append(elem)
    return ints, non_ints

if __name__ == "__main__":
    parser = argparse.ArgumentParser("sort")
    parser.add_argument("--reverse", "-r", action="store_true", default=False)
    parser.add_argument("--general-numeric-sort", "-g", action="store_true", default=False)
    parser.add_argument("--ignore-case", "-f", action="store_true", default=False)
    # parser.add_argument("file", type=str)

    args = parser.parse_args()

    comparison = lambda x: x.upper() if args.ignore_case else x
    lines = (x for x in get_input())


    if args.general_numeric_sort:
        ints, non_ints = try_to_int(lines)
        sorted_lines = sorted(non_ints, reverse=args.reverse, key=comparison)
        sorted_lines.extend(
            sorted(
                ints, reverse=args.reverse
            )
        )
    else:
        sorted_lines = sorted(lines, reverse=args.reverse, key=comparison)

    print("\n".join(sorted_lines))
    
    
