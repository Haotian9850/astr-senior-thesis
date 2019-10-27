import sys
import os
import pprint 


def list_all(dir_name):
    result = {}
    for line_file in os.listdir(dir_name):
        lines = read_line_file(line_file, dir_name)
        for line in lines:
            if line not in result:
                result[line] = [1, [line_file.split(".")[0]]]
            else:
                result[line][0] += 1
                result[line][1].append(line_file.split(".")[0])
    pretty_print(result)


def pretty_print(result):
    for key, value in sorted(result.items(), key=lambda item: item[1][0], reverse=True):
        print("{}: {} occurence(s) in {}".format(key, value[0], str(value[1])))


def compare_all(dir_name):
    compare_multiple(os.listdir(dir_name), dir_name)


def compare_multiple(line_files, dir_name):
    result = read_line_file(line_files[0], dir_name)
    for i in range(0, len(line_files) - 1):
        result = compare_two(result, read_line_file(line_files[i + 1], dir_name))
    print(result)


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
    #compare_two("data/{}.txt".format(sys.argv[1]), "data/{}.txt".format(sys.argv[2]))
    #compare_all("data")
    #compare_multiple(["ser-emb1.txt", "svs13-a.txt"], "data")
    list_all("data")