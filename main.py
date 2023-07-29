# Imports
from pyfiglet import figlet_format
from functions import print_menu
from functions import converter_menu

# Variables
correct_answer = False

# Title
print(figlet_format("File Converter", font= "slant"))
print("Made by: [https://github.com/camilo-zuluaga]")

# Script
print("\nWelcome to File converter!, this is a simple script to convert your document´s extension.")
print("These are the supported extensions [JPG, PNG, PDF, ICO, WEBP].")

answer = input("\nDo you wanna convert any files? [Y/N]: ")

while answer == "Y" or answer == "y":
    print("\nThese are the options below!:")
    print_menu()
    answer_convertion = input("\n···> ")

    # Answer validation
    while correct_answer == False:
        if not ('1' <= answer_convertion <= '9'):
            print("Invalid answer. Must be between 1 and 9.")
            answer_convertion = input("--> ")
            correct_answer = False
        else:
            converter_menu(answer_convertion)
            correct_answer = True
    answer = input("\nDo you wanna convert another file? [Y/N]: ")
else:
    print("Finishing script...")
