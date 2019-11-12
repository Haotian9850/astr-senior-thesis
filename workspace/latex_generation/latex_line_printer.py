import json

def latex_print_lines(dir_name, package_name, line_file, vlsr):
    print("-------- Parsing lines for {}: --------".format(package_name))
    with open("{}/{}/{}".format(dir_name, package_name, line_file), "r") as p:
        for line in json.load(p)["linetable"]["lines"]:
            if line["formula"][0] == "U" and pretty_print_molecule(line["formula"]) is None:
                continue
            print("${}$ & {} & ${}$ & ${}$ & ${}$ & ${}$ & ${}$ & ${}$ & ${}$\\\\".format(
                pretty_print_molecule(line["formula"]),
                line["name"],
                pretty_print_transition(line["transition"]),
                line["frequency"],
                round(float(line["Eu"]), 4),
                round(float(line["peakintensity"]), 4),
                line["velocity"],
                str(vlsr),
                round(float(line["peakrms"]), 4)
            ))
    print("-------- End of parsing --------")


def pretty_print_transition(transition):
    return transition.replace("(", "_{").replace(")", "}")


def pretty_print_molecule(molecule):
    if molecule[0] == 'U':
        return None
    moleculeList = []
    splitIndice = []
    result = []
    molecule_preprocessed = molecule.replace("v=0", "").replace("v=1", "")
    for i in range(0, len(molecule_preprocessed) - 1):
        if (molecule_preprocessed[i].isdigit() and not molecule_preprocessed[i + 1].isdigit()):
            splitIndice.append(i + 1)
        elif (not molecule_preprocessed[i].isdigit() and molecule_preprocessed[i + 1].isdigit()):
            splitIndice.append(i + 1)
    splitIndice.insert(0, 0)
    splitIndice.insert(len(splitIndice), len(molecule))
    for i in range(0, len(splitIndice) - 1):
        moleculeList.append(molecule_preprocessed[splitIndice[i] : splitIndice[i + 1]])
    for element in moleculeList:
        newElement = element
        if element.isdigit():
            newElement = "_{" + element + "}"
        result.append(newElement)
    return "".join(result)


if __name__ == "__main__":
    pass