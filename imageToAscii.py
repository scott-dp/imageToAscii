import numpy as np
from PIL import Image
import os

class Photo:
    def __init__(self, filenamePicture, filenameASCIIart):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.image =  image = Image.open(os.path.join(current_directory, filenamePicture))
        self.width, self.height = image.size
        self.imageArray = self.createImageArray()
        self.filenameASCIIart = filenameASCIIart
    
    def createImageArray(self):
        imageArray=[]
        for i in range(self.height):
            row=[]
            for j in range(self.width):
                row.append(self.rgbToGrayscale(self.image.getpixel((j, i))))
            imageArray.append(row)
        
        return imageArray
    
    def rgbToGrayscale(self, rgb):
        return int(0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])
    
    def convert(self):
        asciiArt = ""
        for i in self.imageArray:
            for j in i:
                if (j<25):
                    asciiArt+="#"
                elif (j<50):
                    asciiArt+="X"
                elif (j<75):
                    asciiArt+="%"
                elif (j<100):
                    asciiArt+="&"
                elif (j<125):
                    asciiArt+="*"
                elif (j<150):
                    asciiArt+="+"
                elif (j<175):
                    asciiArt+="/"
                elif (j<200):
                    asciiArt+="("
                elif (j<225):
                    asciiArt+="'"
                else:
                    asciiArt+=" "
            asciiArt+="\n"
        return asciiArt
    

    def writeToFile(self):
        with open(self.filenameASCIIart, "w") as file:
            file.write(self.convert())

picture = Photo("linux.jpg", "ascii.txt")
picture.writeToFile()


