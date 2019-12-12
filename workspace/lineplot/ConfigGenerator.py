import yaml
import json 


class ConfigGenerator():
    def __init__(self, data_dir, package_name, lines_file_name, max_y, vpos, vlsr, config_name):
        self.data_dir = data_dir
        self.package_name = package_name
        self.lines_file_name = lines_file_name
        self.max_y = max_y 
        self.vpos = vpos
        self.vlsr = vlsr 
        self.config_name = config_name

    def write_to_config_file(self):
        config = {
            "promising_lines": self.generate_lines_config()
        }
        config["max_y"] = self.max_y
        config["vlsr"] = self.vlsr
        print(config)
        with open("{}.yaml".format(self.config_name), "w") as config_file:
            yaml.dump(config, config_file, default_flow_style=False)


    def generate_lines_config(self):
        result = dict()
        with open("{}/{}/{}".format(self.data_dir, self.package_name, self.lines_file_name), "r") as line_file:
            for line in json.load(line_file)["linetable"]["lines"]:
                if line["formula"][0] != "U":
                    result[line["name"]] = [int(line["startchan"]), int(line["endchan"]), 0, self.vpos, line["formula"].replace("v=0", ""), float(line["frequency"])]
        return result



            


