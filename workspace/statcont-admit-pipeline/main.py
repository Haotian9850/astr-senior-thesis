from config import CENTER_PIXEL, CROP_SIZE, SOURCE_FITS_PARENT_DIR, SOURCE_FITS_NAME, STATCONT_DIR, ADMIT_NUM_SIGMA, ADMIT_MIN_CHAN, ADMIT_MAX_CHAN, ADMIT_VLSR, STATCONT_TASK_NAME, STATCONT_NOISE_LEVEL
from statcont_continuum_finder import determine_continuum

if __name__ == "main":

    

    determine_continuum(
        SOURCE_FITS_PARENT_DIR,
        SOURCE_FITS_NAME,
        CENTER_PIXEL,
        CROP_SIZE,
        STATCONT_NOISE_LEVEL,
        STATCONT_TASK_NAME
    )
