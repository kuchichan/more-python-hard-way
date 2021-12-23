import argparse
import sys

parse = argparse.ArgumentParser(description="prints arguments")
parse.add_argument("--files", nargs="+")
parse.add_argument("--log", default=sys.stdout, help="where_to_log")
parse.add_argument("--flag1", "-f1", default=False, help="turns something")
parse.add_argument("--flag2", "-f2", default=False, help="turns something")
parse.add_argument("--flag3", "-f3", default=False, help="turns something")
parse.add_argument("--dict1", "-d1", nargs=1, action="stores")
parse.add_argument("--dict2", "-d2", nargs=2)
parse.add_argument("--dict3", "-d3", nargs=3)

args = parse.parse_args()
print(args)
