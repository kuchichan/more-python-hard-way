def get_input():
    while True:
        try:
            yield input()
        except EOFError:
            break


if __name__ == "__main__":
    stdin = get_input()
    visited = []
    for elem in stdin:
        if elem not in visited:
            print(elem)
            visited.append(elem)
    
