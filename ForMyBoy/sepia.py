from images import Image

def grayscale(image):
    """Converts an image to grayscale using the
    psychologically accurate transformations."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
    return image

def sepia(image):
    greyImage = grayscale(image)  
    for y in range(greyImage.getHeight()):
        for x in range(greyImage.getWidth()):  
            (red, green, blue) = greyImage.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
            greyImage.setPixel(x, y, (red, green, blue))
    

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    sepia(image)
    image.draw()

# The entry point for program execution
if __name__ == "__main__":
    main()
