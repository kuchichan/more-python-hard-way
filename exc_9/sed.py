import re
import argparse

DELETE_COMMAND = "d"
SUBSTITUTE_COMMAND = "s"

def get_input():
    while True:
        try:
            yield input()
        except EOFError:
            break

def parse_s_command(command):
    command_elements = command.split("/")
    return command_elements

def s_from_stdin(pattern, replace):
    input_ = get_input()
    for line in input_:
        yield re.sub(pattern, replace, line)

def parse_range(command):
    range_ = command[:-1]
    return [int(x) for x in range_.split(",")]

def delete_lines(begin, end):
    stream = get_input()
    counter = 1
    for line in stream:
        if counter < begin or counter > end:
            yield line
        counter += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser("find")
    parser.add_argument("-e" , type=str)
    args =  parser.parse_args()
    command = args.e
    if command[-1] == "d":
        begin, end = parse_range(command)
        stream = delete_lines(begin, end)
        for elem in stream:
            print(elem)
    else:
        command, string_1, string_2, *_ = parse_s_command(command)
    
        pattern = re.compile(string_1)
        changed_lines = s_from_stdin(pattern, string_2)
    
        for elem in changed_lines:
            print(elem)

    
    
    

    
    

