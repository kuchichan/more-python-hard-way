import glob
import argparse
import os

def get_file(args):
    path = '**' if args.path == "." else args.path
    for elem in glob.glob(os.path.join(path, args.name), recursive=True):
        yield elem
    
def parse():
    parser = argparse.ArgumentParser(description="Find file/dir of given name")
    parser.add_argument("path", type=str)
    parser.add_argument("--type", choices=["d", "f"])
    parser.add_argument("--name", default="**")
    parser.add_argument("--action", dest="action", default="print")

    return parser.parse_args()

def pprint(files):
    for file_ in files:
        print(file_)

commands = {"print" : pprint}
        
if __name__ == "__main__":
    args = parse()
    files =  get_file(args)
    
    if args.type == "d":
        files = (file_ for file_ in files if os.path.isdir(file_))
    if args.type == "f":
        files = (file_ for file_ in files if os.path.isfile(file_))

    action = commands.get(args.action)
    action(files)
    
    
    
        

        
    
    
    
