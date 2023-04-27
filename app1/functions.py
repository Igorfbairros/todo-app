FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """Read a test file and return the list of to-do items."""

    with open(filepath, 'r') as file_local:
        """ READ A TEXT FILE AND RETURN THE LIST OF TO-DO ITEMS."""
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath = FILEPATH):
    """write to-do list items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_args)


print("Hello")