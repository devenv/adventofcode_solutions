import inspect
import os

def read_input(sample=False):
    abs_path = os.path.abspath((inspect.stack()[1])[1])
    directory_of_caller = os.path.dirname(abs_path)
    with open(os.path.join(directory_of_caller, "input.txt")) as fp:
        return [line.strip() for line in fp.readlines()]

