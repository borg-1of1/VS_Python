"""
File: posterize.py
Project 7.5

Defines and tests a function for posterizing images.
"""

from images import Image


""" Write your code here """
def posterize(imageFile,color = (0, 0,0)):    
    whitePixel = (255, 255, 255)
    for y in range(imageFile.getHeight()):
        for x in range(imageFile.getWidth()):
            (r, g, b) = imageFile.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                imageFile.setPixel(x, y, color)
            else:
                imageFile.setPixel(x, y, whitePixel)


def main():
    filename = input("Enter the image file name: ")
    red = int(input("Enter an integer [0..255] for red: "))
    green = int(input("Enter an integer [0..255] for green: "))
    blue = int(input("Enter an integer [0..255] for blue: "))                    
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()

if __name__ == "__main__":
   main()

