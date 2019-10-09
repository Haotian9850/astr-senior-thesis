import os 

PARENT_DIRECTORY_FLAG = '-p'
IMAGE_NAME_FLAG = '-i'
NOISE_LEVEL_FLAG = '-n'
CROP_FLAG = '--cutout'


def assemble_bash_command(tokens):
    return ' '.join(tokens)

def determine_continuum(image_parent_directory, image_name, central_pixel, crop_size, noise_level, task_name):
    os.system(assemble_bash_command(
        [
            'statcont',
            PARENT_DIRECTORY_FLAG,
            image_parent_directory,
            IMAGE_NAME_FLAG,
            image_name,
            NOISE_LEVEL_FLAG,
            noise_level,
            task_name,
            CROP_FLAG,
            central_pixel,
            central_pixel,
            crop_size
        ]
    ))