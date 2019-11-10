import sys

from latex_line_printer import latex_print_lines

ADMIT_PACKAGE_PATH = "/mnt/documents-local/ASTR4998/data/raw"
LINE_FILE = "lltable.4.json"
VLSR = 8.0

if __name__ == "__main__":
    latex_print_lines(ADMIT_PACKAGE_PATH, sys.argv[1], LINE_FILE, VLSR)

    