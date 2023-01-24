import sys
import os
from PIL import Image

# grab the firs and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exist and if not create it
path = f'{output_folder}'
if not os.path.exists(path):
    os.makedirs(f'{output_folder}')
for file in os.listdir(f'{image_folder}'):
    img = Image.open(
        f'{image_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(
        f'{output_folder}{clean_name}.png', 'png')
    print('all done')
