#!/home/melao/Codes/2Nord/venv/bin/python3.10

from PIL import Image
from sys import argv


#Paleta do tema NORD.
palette = [(46, 52, 64), (59, 66, 82), (67, 76, 94), (76, 86, 106), (216, 222, 233), (229, 233, 240), (236, 239, 244), (143, 188, 187), (136, 192, 208), (129, 161, 193), (94, 129, 172), (191, 97, 106), (208, 135, 112), (235, 203, 139), (163, 190, 140), (180, 142, 173), (59, 66, 82)]

#Dionário que armazena os pixels já alterados.
dict_colors = {}

def get_palette(palette_name):
    global palette
    palette = []
    with open(palette_name, 'r') as palette_file:
        lines = palette_file.readlines()
        for line in lines:
            color = tuple(map(int, line.split(' ')))
            palette.append(color)


def best_color(pixel):
    diff = []

    global dict_colors
    try:
        return dict_colors[str(pixel)]
    except:
        for color in palette:
            sum = abs(pixel[0] - color[0]) + abs(pixel[1] - color[1]) + abs(pixel[2] - color[2])
            diff.append(sum)

        dict_colors[str(pixel)] = palette[diff.index(min(diff))]
        return dict_colors[str(pixel)]



def change_color(img, filename, palette_style, ext):
    new_pixels = list(map(best_color, img.getdata()))
    
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    new_img.save(f'{filename}-{palette_style}.{ext}')



def main():
    if len(argv) > 1:
        filename = argv[1]
        palette_style = 'nord'

        if len(argv) > 2:
            palette_style = argv[2].split('.')[0]
            get_palette(argv[2])
        
        img = Image.open(filename)
        filename, ext = filename.split('.')
        change_color(img, filename, palette_style, ext)
    else:
        print("Escreva o caminho até a imagem.\nEx.:python twonord.py window.png")


if __name__ == "__main__":
    main()
