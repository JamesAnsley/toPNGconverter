# should work with the cmd line `python pokedex\ new\`
import sys
import os
from PIL import Image

# Grab the first and second argument
folder = sys.argv[1]
destination = sys.argv[2]

# check if destination exists, and if not create it
if os.path.isdir(destination):
    print(f"{destination} exists")
else:
    print(f'making {destination}')
    os.makedirs(destination)

# Loop through folder and convert any images into png
for filename in os.listdir(folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{folder}\\{filename}')
    print(img)
    img.save(f'{destination}\\{clean_name}.png', 'png')
    print('all done')
