import json

def print_lines(dir_name, package_name, line_file, vlsr):
    print("-------- Parsing lines for {}: --------".format(package_name))
    with open("{}/{}/{}".format(dir_name, package_name, line_file), "r") as p:
        for line in json.load(p)["linetable"]["lines"]:
            if line["formula"][0] == "U":
                continue    # ignore unknown lines
            print("${}$ & {} & ${}$ & ${}$ & ${}$ & ${}$ & ${}$ & ${}$ & ${}$").format(
                line["formula"],
                line["name"],
                line["transition"],
                line["frequency"],
                line["Eu"],
                line["peakintensity"],
                line["velocity"],
                str(vlsr),
                line["peakrms"]
            )
    print("-------- End of parsing --------")


def pretty_print_transition(transition):
    return transition.replace("(", "_{").replace(")", "}")


def pretty_print_molecule(molecule):
    moleculeList = []
    splitIndice = []
    result = []
    for i in range(0, len(molecule) - 1):
        if (molecule[i].isdigit() and not molecule[i + 1].isdigit()):
            splitIndice.append(i + 1)
        elif (not molecule[i].isdigit() and molecule[i + 1].isdigit()):
            splitIndice.append(i + 1)

    splitIndice.insert(0, 0)
    splitIndice.insert(len(splitIndice), len(molecule))

    for i in range(0, len(splitIndice) - 1):
        moleculeList.append(molecule[splitIndice[i] : splitIndice[i + 1]])
    for element in moleculeList:
        newElement = element
        if element.isdigit():
            newElement = "_{" + element + "}"
        result.append(newElement)
    return ""
