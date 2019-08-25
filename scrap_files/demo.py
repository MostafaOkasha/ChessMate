import board
import glob


def main(input_folder, output_folder):
    input_images = glob.glob(input_folder + "/*.jpg")
    output_folder = output_folder

    for img in input_images:



if __name__ == "__main__":
    input_folder = input("Enter the folder of original images: ")
    output_folder = input("Enter the folder to store the processed images: ")

    main(input_folder, output_folder)