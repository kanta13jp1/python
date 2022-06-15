from PIL import Image, ImageDraw 

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
