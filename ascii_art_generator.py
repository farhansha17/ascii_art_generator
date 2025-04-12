from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def convert_to_ascii(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"Unable to open image. Error: {e}"

    image = resize_image(image)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_img = "\n".join([ascii_str[i:(i+img_width)] for i in range(0, len(ascii_str), img_width)])
    return ascii_img

# GUI
class ASCIIArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ASCII Art Generator")
        self.root.geometry("800x600")

        self.btn = tk.Button(root, text="Choose Image", command=self.load_image)
        self.btn.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 6))
        self.text_area.pack(expand=True, fill=tk.BOTH)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            ascii_art = convert_to_ascii(file_path)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, ascii_art)

if __name__ == '__main__':
    root = tk.Tk()
    app = ASCIIArtApp(root)
    root.mainloop()