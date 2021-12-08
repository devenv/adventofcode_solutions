import inspect
import os

def read_input(sample=False):
    abs_path = os.path.abspath((inspect.stack()[1])[1])
    directory_of_caller = os.path.dirname(abs_path)
    file_name = "input.txt" if not sample else "input_sample.txt"
    with open(os.path.join(directory_of_caller, file_name)) as fp:
        return [line.strip() for line in fp.readlines()]

