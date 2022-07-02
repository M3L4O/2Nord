#!/home/melao/Codes/2Nord/venv/bin/python3.10

from PIL import Image
from sys import argv


# Dionário que armazena os pixels já alterados.
dict_colors = {}


def get_palette(palette_name):
    global palette
    palette = []
    with open(palette_name, "r") as palette_file:
        lines = palette_file.readlines()
        for line in lines:
            color = tuple(map(int, line.split(" ")))
            palette.append(color)


def best_color(pixel):
    distances = []
    global dict_colors
    try:
        return dict_colors[str(pixel)]
    except:
        for color in palette:
            # Distancia D4 :: D4 = |x1-x2|+|y1-y2|+|z1-z2|
            sum = (
                abs(pixel[0] - color[0])
                + abs(pixel[1] - color[1])
                + abs(pixel[2] - color[2])
            )
            distances.append(sum)

        dict_colors[str(pixel)] = palette[distances.index(min(distances))]
        return dict_colors[str(pixel)]


def change_color(img, filename, palette_style, ext):
    new_pixels = list(map(best_color, img.getdata()))

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    new_img.save(f"{filename}-{palette_style}.{ext}")


def main():
    if len(argv) > 1:
        filename = argv[1]

        palette_style = argv[2].split(".")[0]
        get_palette(argv[2])

        img = Image.open(filename)
        filename, ext = filename.split(".")
        change_color(img, filename, palette_style, ext)
    else:
        print(
            "Escreva o caminho até a imagem juntamente com a paleta de cores.\nEx.:python main.py window.png catppuccin"
        )


if __name__ == "__main__":
    main()
