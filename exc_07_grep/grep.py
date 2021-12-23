import argparse
import glob
import re

from pathlib import Path

ROOT = Path.absolute(Path(__file__).parent)

def search_for_text_in_file(regex, file_, c_arg):
    with open(file_, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if regex.match(lines[i]) is not None and lines[i]:
                # this is not perfect!
                for elem in lines[i - c_arg: i + c_arg + 1]:
                    print(elem, end="")

def search_recursively(regex, path, c_arg):
    for file_ in glob.glob(str(path / "**")):
        if Path(file_).is_file():
            search_for_text_in_file(regex, file_, c_arg)

if  __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", help="grep recursively", action="store_true")
    parser.add_argument("-C", help="prints the N previous and next  lines", type=int, default=0)
    parser.add_argument("pattern", type=str, nargs=1)
    parser.add_argument("startpath", type=str, nargs=1)
    
    arguments = parser.parse_args()
    
    path = ROOT / Path(arguments.startpath[0])
    regex = re.compile(arguments.pattern[0])
    if arguments.r:
        search_recursively(regex, path, arguments.C)
    else:
        search_for_text_in_file(regex, path, arguments.C)

    
    
    
    
    
