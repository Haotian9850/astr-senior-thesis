import json 
import logging 

from MoleculePrettyTexPrinter import MoleculePrettyTexPrinter


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-6s %(levelname)-4s %(message)s',
    datefmt='%m-%d %H:%M'
)


class TexTableGenerator():
    def __init__(self, data_dir, package_name, line_file, header, vlsr=8.0):
        self.data_dir = data_dir
        self.package_name = package_name
        self.line_file = line_file
        self.header = header
        self.vlsr = vlsr
        self.moleculePrettyTexPrinter = MoleculePrettyTexPrinter()

    def make_table_head(self):
        print("\\hline")
        print("{} \\\\".format(
            " & ".join(self.header)
        ))
        print("\\hline")



    def make_table(self):
        logging.info("parsing lines for {}\n\n\n\n\n".format(self.package_name))
        self.make_table_head()
        with open("{}/{}/{}".format(self.data_dir, self.package_name, self.line_file), "r") as p:
            for line in json.load(p)["linetable"]["lines"]:
                if line["formula"][0] == "U" and self.moleculePrettyTexPrinter.pretty_print_molecule(line["formula"]) is None:
                    continue
                print("${}$ & {} & ${}$ & ${}$ & ${}$ & ${}$ & ${}$ & ${}$ & ${}$\\\\".format(
                    self.moleculePrettyTexPrinter.pretty_print_molecule(line["formula"]),
                    line["name"],
                    self.moleculePrettyTexPrinter.pretty_print_transition(line["transition"]),
                    line["frequency"],
                    round(float(line["Eu"]), 4),
                    round(float(line["peakintensity"]), 4),
                    round(float(line["velocity"]), 4),
                    str(self.vlsr),
                    round(float(line["peakrms"]), 4)
                ))
        print("\\hline\n\n\n\n\n")
        logging.info("end of parsing {}".format(self.package_name))
        
