from ContourPlotter import ContourPlotter


if __name__ == "__main__":
    plotter = ContourPlotter(
        ".",
        "SerpS_TC_spw0.pbcor_cutout_180_180_100_line.fits",
        30,
        [200],
        90,
        10,
        "spw0",
        False
    )
    plotter.plot_slices()