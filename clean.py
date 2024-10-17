import os
import glob

def clean_folder():
    print("clean_folder function started")
    images = glob.glob("images/*.png")
    # Iterate over the list and remove each file
    for image in images:
        os.remove(image)  # Remove each file individually
    print("clean_folder function ended")

# if __name__ == "__main__":
#     clean_folder()