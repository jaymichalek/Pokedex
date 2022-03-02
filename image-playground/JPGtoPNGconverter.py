import sys
import os
from PIL import Image

# Python script: python3 JPGtoPNGconverter.py Pokedex/ new/
# Converts images from Pokedex folder which are .jpg to .png and saves converted images to new folder.

# grab the first & second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new exists, if not create folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex and convert images to png
# save to new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # Grab only filename without the file type identifier (.jpg):
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('Image converted from JPG to PNG!')
