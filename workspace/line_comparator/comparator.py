import sys
import os



def compare_all(dir_name):
    print(compare_multiple(os.listdir(dir_name), dir_name))


def compare_multiple(line_files, dir_name):
    result = read_line_file(line_files[0], dir_name)
    for i in range(0, len(line_files) - 1):
        result = compare_two(result, read_line_file(line_files[i + 1], dir_name))
    return result


def compare_two(line1, line2):
    result = set()
    for line in line1:
        if line in line2:
            result.add(line)
    return result


def read_line_file(file_name, dir_name):
    with open("{}/{}".format(dir_name, file_name)) as f:
        lines = f.readlines()
    return set([line.rstrip() for line in lines])
            


if __name__ == "__main__":
    # compare_two("data/{}.txt".format(sys.argv[1]), "data/{}.txt".format(sys.argv[2]))
    compare_all("data")