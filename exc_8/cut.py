import argparse
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

def get_input():
    while True:
        try:
            yield input()
        except EOFError:
            break

def read_from_stdin(begin, end, delimiter):
    a = get_input()

    for line in a:
        print(" ".join(line.split(delimiter)[begin-1:end]))

def read_from_file(begin, end, delimiter, file_):
    with open(file_, 'r') as f:
        for line in f:
            print(" ".join(line.split(delimiter)[begin-1:end]))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser("cut")
    parser.add_argument("-d", type=str, default="\t")
    parser.add_argument("-f", type=str, default="")
    parser.add_argument("file", type=str, nargs="?", default="")

    args = parser.parse_args()

    range_ = [int(x) for x in args.f.split('-')]
    try:
        begin, end = range_
    except ValueError:
        begin = end = range_[0]
    
    if not args.file:
        read_from_stdin(begin, end, args.d)
    else:
        abspath = os.path.join(ROOT, args.file)
        read_from_file(begin, end, args.d, abspath)
        

    

    
    
    

    
    
