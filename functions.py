# Required imports
from tkinter import *
from PIL import Image
from tkinter import filedialog
from PIL import Image
import img2pdf

# Convertion options
menu_options = {
    1: 'From [JPG -> PNG]',
    2: 'From [PNG -> JPG]',
    3: 'From [PNG/JPG -> ICO]',
    4: 'From [PNG/JPG -> PDF]',
    5: 'From [PNG/JPG -> WEBP]',
    6: 'From [WEBP -> PNG]',
    7: 'From [WEBP -> JPG]',
    8: 'From [ICO -> JPG]',
    9: 'From [ICO -> PNG]',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

# Select file menu display
def converter_menu(answer):
    global root
    
    def on_enter(event):
        button.config(cursor="hand2")
    
    root = Tk()
    root.title("File converter")
    root.iconbitmap("images/logo.ico")
    root.geometry("300x150")
    
    Label(root, text= "Select your File", font=('Arial Rounded MT Bold',20)).pack(pady=20)
    
    button = Button(root, text="Open a file", borderwidth=0, command=lambda: open_dialog_convertion(answer))
    img = PhotoImage(file="images/buttonOF.png")
    button.config(image=img)
    button.pack()
    button.bind("<Enter>", on_enter)
    
    root.resizable(False,False)
    root.attributes('-topmost',True)
    root.mainloop()


# Main function
def open_dialog_convertion(answer):
    global im1
    global filename
    
    # Executing the user´s input
    # JPG TO PNG
    if answer == "1": 
        print("\n··· [JPG -> PNG] Selected ···")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("JPG files", "*.jpg"),("All files", "*.*")))
        if filename.endswith(".jpg"):
            im1 = Image.open(filename)
            export_filename = filedialog.asksaveasfilename(title="Save PNG As", defaultextension=".png", filetypes=(("PNG files", "*.png"),("All files", "*.*")))
            im1.save(export_filename)

            print("\n··· Your image has been converted! ··· ")
            root.destroy()
        else:
            print("Error - Something went wrong :(")
    
    # PNG to JPG        
    elif answer == "2":
        print("··· [PNG -> JPG] Selected ···")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("PNG files", "*.png"),("All files", "*.*")))
        if filename.endswith(".png"):
            im1 = Image.open(filename)
            export_filename = filedialog.asksaveasfilename(title="Save JPG As", defaultextension=".jpg", filetypes=(("JPG files", "*.jpg"),("All files", "*.*")))
            im1.save(export_filename)

            print("\n··· Your image has been converted! ··· ")
            root.destroy()
        else:
            print("Error - Something went wrong :(")
    
    # PNG/JPG to ICO  
    elif answer == "3":
        print("··· [PNG/JPG -> ICO] Selected ···")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("PNG files", "*.png"),("JPG files", "*.jpg")))
        if filename.endswith(".png") or filename.endswith(".jpg"):
            im1 = Image.open(filename)
            export_filename = filedialog.asksaveasfilename(title="Save ICO As", defaultextension=".ico", filetypes=(("ICO files", "*.ico"),("All files", "*.*")))
            im1.save(export_filename)

            print("\n··· Your image has been converted! ··· ")
            root.destroy()
        else:
            print("Error - Something went wrong :(")
    
    # PDF convertion using img2pdf
    elif answer == "4":
        print("··· [PNG/JPG -> PDF] Selected ···")
        print("\n - You can select multiple images -")
        filenames = filedialog.askopenfilenames(
        initialdir="/", 
        title="Select Files", 
        filetypes=(("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*"))
        )
    
        if filenames:
            export_filename = filedialog.asksaveasfilename(
                title="Save PDF As",
                defaultextension=".pdf",
                filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
            )
            
            if export_filename:
                pdf_bytes = img2pdf.convert(filenames)
                with open(export_filename, "wb") as f:
                    f.write(pdf_bytes)
                print("\n··· Your images have been converted to PDF! ··· ")
                root.destroy()
            else:
                print("Error - No file selected for saving.")
        else:
            print("Error - No files selected.")
    
    # PNG/JPG to WEBP
    elif answer == "5":
        print("··· [PNG/JPG -> WEBP] Selected ···")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("PNG files", "*.png"),("JPG files", "*.jpg")))
        if filename.endswith(".png") or filename.endswith(".jpg"):
            im1 = Image.open(filename)
            export_filename = filedialog.asksaveasfilename(title="Save WEBP As", defaultextension=".webp", filetypes=(("WEBP files", "*.webp"),("All files", "*.*")))
            im1.save(export_filename)

            print("\n··· Your image has been converted! ··· ")
            root.destroy()
        else:
            print("Error - Something went wrong :(")
            
    # WEBP to PNG
    elif answer == "6":
        print("··· [WEBP -> PNG] Selected ···")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("WEBP files", "*.webp"),("All files", "*.*")))
        if filename.endswith(".webp"):
            im1 = Image.open(filename)
            export_filename = filedialog.asksaveasfilename(title="Save PNG As", defaultextension=".png", filetypes=(("PNG files", "*.png"),("All files", "*.*")))
            im1.save(export_filename)

            print("\n··· Your image has been converted! ··· ")
            root.destroy()
        else:
            print("Error - Something went wrong :(")
    
    # WEBP to JPG
    elif answer == "7":
        print("··· [WEBP -> JPG] Selected ···")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("WEBP files", "*.webp"),("All files", "*.*")))
        if filename.endswith(".webp"):
            im1 = Image.open(filename)
            export_filename = filedialog.asksaveasfilename(title="Save JPG As", defaultextension=".jpg", filetypes=(("JPG files", "*.jpg"),("All files", "*.*")))
            im1.save(export_filename)

            print("\n··· Your image has been converted! ··· ")
            root.destroy()
        else:
            print("Error - Something went wrong :(")
    
    # ICO to JPG
    elif answer == "8":
        print("··· [ICO -> JPG] Selected ···")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("ICO files", "*.ico"),("All files", "*.*")))
        if filename.endswith(".ico"):
            im1 = Image.open(filename)
            export_filename = filedialog.asksaveasfilename(title="Save JPG As", defaultextension=".jpg", filetypes=(("JPG files", "*.jpg"),("All files", "*.*")))
            im1.save(export_filename)

            print("\n··· Your image has been converted! ··· ")
            root.destroy()
        else:
            print("Error - Something went wrong :(")
    
    # ICO to PNG
    elif answer == "9":
        print("··· [ICO -> PNG] Selected ···")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("ICO files", "*.ico"),("All files", "*.*")))
        if filename.endswith(".ico"):
            im1 = Image.open(filename)
            export_filename = filedialog.asksaveasfilename(title="Save PNG As", defaultextension=".png", filetypes=(("PNG files", "*.png"),("All files", "*.*")))
            im1.save(export_filename)

            print("\n··· Your image has been converted! ··· ")
            root.destroy()
        else:
            print("Error - Something went wrong :(")

