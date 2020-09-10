import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("open file")
    yield {}
    print("end")

with file_open("feta.txt") as file:
    print("file processing")