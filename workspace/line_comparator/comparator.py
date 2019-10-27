import sys


def compare(f1, f2):
    result = set()
    for line in read_line_file(f1):
        if line in read_line_file(f2):
            result.add(line)
    print(result)


def read_line_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return set([line.rstrip() for line in lines])
            


if __name__ == "__main__":
    compare("data/{}.txt".format(sys.argv[1]), "data/{}.txt".format(sys.argv[2]))