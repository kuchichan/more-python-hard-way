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
        print(" ".join(line.split(delimiter)[begin:end]))

def read_from_file(begin, end, delimiter, file_):
    with open(file_, 'r') as f:
        for line in f:
            print(" ".join(line.split(delimiter)[begin:end]))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser("find")
    parser.add_argument("-d", type=str, default="\t")
    parser.add_argument("-f", type=str, default="")
    parser.add_argument("file", type=str)

    args = parser.parse_args()
    begin, end = [int(x) for x in args.f.split('-')]
    if args.file is None:
        read_from_stdin(begin, end, args.d)
    else:
        abspath = os.path.join(ROOT, args.file)
        read_from_file(begin, end, args.d, abspath)
        

    

    
    
    

    
    
