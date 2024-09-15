#!!!IMPORTANT!!! 
#Requires user to run 'pip install pillow' in terminal prior to running code

print("!!!IMPORTANT!!! This program requires user to run 'pip install pillow' in terminal and save image file to C:\VSPython\Assignment 2\Q2\chapter1.jpg prior to running code")

#Import Pillow package
from PIL import Image 

#Open the image
image = Image.open("C:\VSPython\Assignment 2\Q2\chapter1.jpg")

#Use given code to generate number 'n'
def get_n():
    import time
    current_time = int(time.time())
    generated_number = (current_time %100) + 50

    if generated_number %2 == 0:
        generated_number += 10
    return generated_number

#Function adds 'n' to r,g,b values of the image
def rgbn(image):
    """Adds the value 'n' to the r,g,b values of the image."""
    n = get_n()
    #Ensures image in rgb mode
    image = image.convert('RGB')
    #Loads pixel data
    pixels = image.load()
    #Image width and heighta
    width, height = image.size
    #Loop through every pixel
    for y in range(height):
        for x in range(width):
            #Get current pixels rgb values
            (r, g, b) = pixels[x, y]
            #Adds value 'n' to r g b
            r = (r + n)
            g = (g + n)
            b = (b + n)
            #Sets new rgb values to pixel
            pixels[x, y] = (r, g, b)
    #Save output
    image.save("C:\VSPython\Assignment 2\Q2\chapter1out.jpg")

image = Image.open("C:\VSPython\Assignment 2\Q2\chapter1out.jpg")

#Function adds values of red channel to sum
def redSum(image):
    """Adds the value 'n' to the r,g,b values of the image."""
    sumOut = 0
    #Ensures image in rgb mode
    image = image.convert('RGB')
    #Loads pixel data
    pixels = image.load()
    #Image width and heighta
    width, height = image.size
    #Loop through every pixel
    for y in range(height):
        for x in range(width):
            #Get current pixels rgb values
            (r, g, b) = pixels[x, y]
            #Add red values to sum
            sumOut += r
    #Return Output
    return sumOut

rgbn(image)
print("Image is saved to: 'C:\VSPython\Assignment 2\Q2\chapter1out.jpg'")

print(redSum(image))
