from PIL import Image

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

print(redSum(image))
