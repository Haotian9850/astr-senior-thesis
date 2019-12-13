from TexTableGenerator import TexTableGenerator

DATA_DIR = "/media/haotian/documents-local/ASTR4998/data/raw"
PACKAGE_NAME = "SerpS_TC_spw0.pbcor_cutout_180_180_100_line.fits.admit_BDP"
HEADER = ["Molecule", "Name", "Transition", "Frequency", "$E_{{u}}$", "Intensity", "Velocity", "$V_{{lsr}}$", "peak / rms"]
VLSR = 8.0

if __name__ == "__main__":
    generator = TexTableGenerator(
        DATA_DIR,
        PACKAGE_NAME,
        HEADER,
        VLSR
    )
    generator.make_table()

    