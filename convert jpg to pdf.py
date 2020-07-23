
__author__ : "@rockdevu"

from PIL import Image

imagelist = list()

# I'm running this upto 8 because i've only 8 jpg images to convert.

for i in range(1,9):
    imagelist.append( (Image.open(r'%s.jpg'%i).convert('RGB') ))

imagelist[0].save(r'Programming.pdf', save_all=True, append_images=imagelist)

# Save this file to the same folder where you are having the jpg files
# otherwise add path while openning and saving files.
