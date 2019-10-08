import matplotlib.pyplot as plt
import csv

file_name = "/mnt/documents-local/ASTR4998/test_cases/products/SPEC_TESTS/my_absorption_continuum.line.dat"
# /mnt/documents-local/ASTR4998/test_cases/data/SPEC_TESTS/my_absorption.dat
# /mnt/documents-local/ASTR4998/test_cases/products/SPEC_TESTS/my_absorption_continuum.line.dat

delimiter = " "

def plot(file_name, delimiter):
    x = []
    y = []
    file = open(file_name)
    plots = csv.reader(file, delimiter = delimiter)
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    plot(file_name, delimiter)


