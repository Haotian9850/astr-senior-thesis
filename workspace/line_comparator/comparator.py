import sys


def compare(f1, f2):
    line1 = set()
    line2 = set()
    result = set()
    cnt = 0
    with open(f1) as f:
        line = f.readline()
        if cnt != 0:
            line1.add(line)
        cnt += 1
    cnt = 0
    with open(f2) as f:
        line = f.readline()
        if cnt != 0:
            line2.add(line)
        cnt += 1
    for molecule in line1:
        if molecule in line2:
            result.add(molecule)
    print(result)
            


if __name__ == "__main__":
    compare("data/{}".format(sys.argv[1]), "data/{}".format(sys.argv[2]))