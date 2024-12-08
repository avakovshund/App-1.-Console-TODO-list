FILEPATH = "todos.txt"

def read_file(filepath=FILEPATH):
    """Read a text file and return a list of to-do items."""
    with open(filepath, 'r') as txt:
        todos = txt.readlines()
        return todos


def write_file(todos, filepath=FILEPATH):
    """Write the to-do items in the text file."""
    with open(filepath, 'w') as txt:
        txt.writelines(todos)


if __name__ == "__main__":
    """You can write here that you want to not run 
    while importing a module
    """
    pass