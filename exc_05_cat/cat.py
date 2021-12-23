import argparse
import os
def read_file(file_, number, empty, num=1):
    count = num
    if number:
        for  line in file_:
            print(count,  line, end='')
            count += 1
        return count
    elif empty:
        for line in file_:
            if line != "\n": 
                print(count, "", line, end='')
                count += 1
            else:
                print(line, end='')
        return count
    else:
        for line in file_:
            print(line, end='')
        return count

def cat(args):
    count = 1
    for file_ in args.files:
        lst_count = read_file(file_, args.number, args.empty, count)
        count += lst_count


if __name__ == "__main__":
    # print(os.path.realpath(os.path.dirname(__file__)))
    print(os.path.dirname(os.getcwd()))
    parser =argparse.ArgumentParser(prog="cat", description="Concatenates files")
    parser.add_argument('-number', '-n', action="store_true", help="number in list")
    parser.add_argument('-empty', '-b', action="store_true", help="number in list")
    parser.add_argument('files', type=argparse.FileType('r'), nargs='+')
    args = parser.parse_args()
    cat(args)

