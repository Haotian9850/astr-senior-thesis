class MoleculePrettyTexPrinter():
    def __init__(self):
        pass 

    def pretty_print_molecule(self, compound):
        if compound[0] == 'U':
            return
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
        return "".join(result)

    def pretty_print_transition(self, transition):
        return transition.replace("(", "_{").replace(")", "}")