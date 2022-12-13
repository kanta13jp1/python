from PIL import Image, ImageDraw 
from moviepy.editor import *
import glob

files = glob.glob("./tamaki/*")
for file in files:
    print(file)

image = Image.new("RGB", (400, 400), "blue" ) 

draw = ImageDraw.Draw( image) 

draw.rectangle((200, 100, 300, 200), fill="red") 

draw.rectangle((50, 50, 150, 150), fill="green", outline="yellow", width=3) 

image.save("output.jpg")

my_list = list('abcc')

print(my_list)

my_list.append('d')

print(my_list)

class Engineer:
    def __init__(self, name):
        self.name = name
        self.__starting_salary = 62000

dain = Engineer('Dain')
print(dain.name)
print(dain._Engineer__starting_salary)

import imageio

# filenames = [
#     "tamaki/FY46egnUsAEu3YL.jpg"]

images = []

filenames = glob.glob("./tamaki/*")
filenames.sort()

clips = [] 
for m in filenames:
    clip = ImageClip(m).set_duration('00:00:00.50')
    clip = clip.resize(height=640)
    clips.append(clip)

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_gif("test.gif", fps=1)

for file in filenames:
    print(file)

# for filename in filenames:
#     images.append(imageio.imread(filename))
# imageio.mimsave('movie.gif', images, 'GIF', duration=2)

#clcoding.com

