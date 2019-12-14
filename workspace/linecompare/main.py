import sys
import os
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-6s %(levelname)-4s %(message)s',
    datefmt='%m-%d %H:%M'
)


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
    print("\n\n\n")
    tex_print(result)


def read_all_admit_package(dir_name):
    for package in os.listdir(dir_name):
        logging.info("reading line results from admit data package {}...".format(package))
        print("\n\n")
        read_admit_package(dir_name, package, "lltable.9.json")
        print("\n\n\n")



def read_admit_package(dir_name, package_name, line_file):
    with open("{}/{}/{}".format(dir_name, package_name, line_file), "r") as p:
        for line in json.load(p)["linetable"]["lines"]:
            if line["formula"][0] == "U":
                continue
            print(pretty_print_molecule(line["formula"]))




def pretty_print(result):
    for key, value in sorted(result.items(), key=lambda item: item[1][0], reverse=True):
        print("{}: {} occurence(s) in {}".format(key, value[0], ", ".join(value[1])))



def tex_print(result):
    for key, value in sorted(result.items(), key=lambda item: item[1][0], reverse=True):
        print("${}$ & {} \\\\".format(
            key,
            ", ".join(value[1])
        ))


def pretty_print_molecule(compound):
    compoundList = []
    splitIndice = []
    result = []
    for i in range(0, len(compound) - 1):
        if (compound[i].isdigit() and not compound[i + 1].isdigit()):
            splitIndice.append(i + 1)
        elif (not compound[i].isdigit() and compound[i + 1].isdigit()):
            splitIndice.append(i + 1)

    splitIndice.insert(0, 0)
    splitIndice.insert(len(splitIndice), len(compound))

    for i in range(0, len(splitIndice) - 1):
        compoundList.append(compound[splitIndice[i] : splitIndice[i + 1]])
    for element in compoundList:
        newElement = element
        if element.isdigit():
            newElement = "_{" + element + "}"
        result.append(newElement)
    return "".join(result).replace("g'", "").replace("g-", "").replace("Ga-", "").replace("c-", "").replace("t-", "").replace("v=_{0" + "}", "").replace("s-", "").replace("vt=_{0" + "}", "").replace("&", "/").replace(";", "")



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
    return set(["{}".format(line.rstrip()) for line in lines])
            


if __name__ == "__main__":
    list_all("data")
    
    #read_all_admit_package("/media/haotian/documents-local/ASTR4998/data/raw")