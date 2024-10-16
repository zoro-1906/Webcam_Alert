import os
import glob

def clean_folder():
    images = glob.glob("images/*.png")
    # Iterate over the list and remove each file
    for image in images:
        os.remove(image)  # Remove each file individually

# if __name__ == "__main__":
#     clean_folder()