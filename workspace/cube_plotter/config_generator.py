import yaml
import json 

DATA_PATH = "/mnt/documents-local/ASTR4998/data/raw"


def write_to_config_file(data_path, package_name, file_name, extension_size, max_y, vlsr, config_name):
    config = {
        "promising_lines": generate_lines_config(data_path, package_name, file_name, extension_size)
    }
    config["max_y"] = max_y
    config["vlsr"] = vlsr
    print(config)
    with open("{}.yaml".format(config_name), "w") as config_file:
        yaml.dump(config, config_file, default_flow_style=False)




def generate_lines_config(data_path, package_name, file_name, extension_size):
    result = dict()
    with open("{}/{}/{}".format(data_path, package_name, file_name), "r") as line_file:
        for line in json.load(line_file)["linetable"]["lines"]:
            if line["formula"][0] != "U":
                result[line["name"]] = [int(line["startchan"]), int(line["endchan"]), extension_size, pretty_print_molecule(line["formula"])]
    return result

    



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



write_to_config_file(
    DATA_PATH,
    "SerpS_TC_spw1.pbcor_cutout_180_180_100_line.fits.admit",
    "lltable.4.json",
    0.2,
    0.2,
    8.0,
    "config_test"
)

            


