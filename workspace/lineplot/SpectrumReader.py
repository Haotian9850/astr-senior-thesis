
class SpectrumReader():
    def __init__(self, data_dir, package_name, spectrum_file_name):
        self.data_dir = data_dir
        self.package_name = package_name
        self.spectrum_file_name = spectrum_file_name

    def read_cube_spectrum_file(self):
        x = []
        y = []
        for pair in [line.rstrip() for line in open("{}/{}/{}".format(self.data_dir, self.package_name, self.spectrum_file_name),'r').read().split('\n')[1:-1]]:
            x.append(float(pair.split()[0].strip()))
            y.append(10 ** float(pair.split()[1].strip()))
        return x, y
