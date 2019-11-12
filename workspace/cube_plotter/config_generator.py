import yaml
import json 

DATA_PATH = "/mnt/documents-local/ASTR4998/data/raw"


def write_to_config_file(data_path, package_name, file_name, extension_size, max_y, vpos, vlsr, config_name):
    config = {
        "promising_lines": generate_lines_config(data_path, package_name, file_name, extension_size, vpos)
    }
    config["max_y"] = max_y
    config["vlsr"] = vlsr
    print(config)
    with open("{}.yaml".format(config_name), "w") as config_file:
        yaml.dump(config, config_file, default_flow_style=False)




def generate_lines_config(data_path, package_name, file_name, extension_size, vpos):
    result = dict()
    with open("{}/{}/{}".format(data_path, package_name, file_name), "r") as line_file:
        for line in json.load(line_file)["linetable"]["lines"]:
            if line["formula"][0] != "U":
                result[line["name"]] = [int(line["startchan"]), int(line["endchan"]), extension_size, vpos, line["formula"].replace("v=0", ""), float(line["frequency"])]
    return result




write_to_config_file(
    DATA_PATH,
    "SerpS_TC_spw1.pbcor_cutout_180_180_100_line.fits.admit",
    "lltable.4.json",
    0,
    50,
    0.6,
    8.0,
    "config_spw1"
)

            


