from PIL import Image
import os
import sys

def convert_images(webp_dir, png_dir):
    os.makedirs(png_dir, exist_ok=True)
    webpInDir = False

    for filename in os.listdir(webp_dir):
        file_path = os.path.join(webp_dir, filename)
        if os.path.isfile(file_path) and filename.endswith(".webp"):
            webp_image = Image.open(file_path)
            png_image = webp_image.convert("RGBA")
            png_image.save(os.path.join(png_dir, filename.replace(".webp", ".png")))
            webpInDir = True

    if not webpInDir:
        print("\033[91mERROR: No .webp files found in the directory\033[0m")

def display_help(index = 0):
    print("Usage: python main.py <command> [arguments]")
    print("")
    print("Global options:")
    print("")
    print("-h, --help       display this help message.")
    print("-o, --output     look for webp files in the current directory and output the converted png files.")
    
    print("\nUsage: python main.py <webp directory path> <output png path>")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        if len(sys.argv) == 1:
            display_help()
        else:
            if (sys.argv[1] == "-o" or sys.argv[1] == "--output"):
                convert_images("./", "./converted")
            else:
                display_help()
            
    else:
        webp_dir = sys.argv[1]
        png_dir = sys.argv[2]
        convert_images(webp_dir, png_dir)