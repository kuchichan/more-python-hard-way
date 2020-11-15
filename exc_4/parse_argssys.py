import sys
import glob

parsed_arguments = [args for args in sys.argv[1:]]

def is_help_needed(args):
    return any(arg in ("-h", "-help") for arg in args)

def is_flag_or_unix_arg(arg):
    return arg.startswith("-")

def is_keyword(arg):
    return "=" in arg

def get_options(args):
    dict_ = {}
    for elem in args:
        temp_list = elem.split("=")
        dict_[temp_list[0]] = temp_list.pop()
    return dict_

def parse():
    parsed_arguments = [arg for arg in sys.argv[1:]]
    if is_help_needed(parsed_arguments):
        print("this is some funny help")
    else:
        flag_or_unix = [arg for arg in parsed_arguments if is_flag_or_unix_arg(arg)]
        positional_args = [arg for arg in parsed_arguments if not  is_flag_or_unix_arg(arg)]
        keyword_args = [arg for arg in flag_or_unix if is_keyword(arg)]
        flags = [arg for arg in flag_or_unix if not is_keyword(arg)]
        keyword_args = get_options(keyword_args)

        print(f"flags: {flags}\n\n")
        print(f"kword args: {keyword_args}\n\n")
        print(f"pos args: {positional_args}\n\n")
        
    
if "__main__" == __name__:
    parse()
    
