import os 
import sys 

PARENT_DIRECTORY_FLAG = "-p"
IMAGE_NAME_FLAG = "-i"
NOISE_LEVEL_FLAG = "-n"
CROP_FLAG = "--cutout"
TASK_NAME = "--continuum"


def assemble_bash_command(tokens):
    return " ".join(tokens)

def determine_continuum(image_name, noise_level, central_pixel, crop_size):
    command = assemble_bash_command([
            "statcont",
            IMAGE_NAME_FLAG,
            image_name,
            NOISE_LEVEL_FLAG,
            noise_level,
            TASK_NAME,
            CROP_FLAG,
            central_pixel,
            central_pixel,
            crop_size
        ])
    print(command)
    os.system(command)



if __name__ == "__main__":
    determine_continuum(
        sys.argv[1],    # image name
        sys.argv[2],    # noise level 
        sys.argv[3],    # central pixel
        sys.argv[4]     # crop size
    )