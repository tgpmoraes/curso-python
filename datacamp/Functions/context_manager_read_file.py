import contextlib
import pathlib


@contextlib.contextmanager
def open_read_only(filename):
    """Open a file in read-only mode.

    Args:
      filename (str): The location of the file to read

    Yields:
      file object
    """
    read_only_file = open(filename, mode='r')
    # Yield read_only_file so it can be assigned to my_file
    yield read_only_file
    # Close read_only_file
    read_only_file.close()


current_path = pathlib.Path(__file__).parent
with open_read_only(f'{current_path}/my_file.txt') as my_file:
    print(my_file.read())
