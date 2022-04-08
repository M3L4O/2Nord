from http.client import ImproperConnectionState
from PIL import Image
from sys import argv
nord = [(46, 52, 64), (59, 66, 82), (67, 76, 94), (76, 86, 106), (216, 222, 233), (229, 233, 240), (236, 239, 244), (143, 188, 187), (136, 192, 208), (129, 161, 193), (94, 129, 172), (191, 97, 106), (208, 135, 112), (235, 203, 139), (163, 190, 140), (180, 142, 173)]


def diff_in_color(pixel):
    diff = []
    for color in nord:
        sum = abs(pixel[0] - color[0]) + abs(pixel[1] - color[1]) + abs(pixel[2] - color[2])
        diff.append(sum)
     
    return nord[diff.index(min(diff))]


def change_color(img, filename, ext):
    new_pixels = list(map(diff_in_color, img.getdata()))
    
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    new_img.save(f'{filename}-nord.{ext}')


def main():
    if len(argv) > 1:
        filename = argv[1]
        img = Image.open(filename)
        filename, ext = filename.split('.')
        change_color(img, filename, ext)
    else:
        print("Escreva o caminho até a imagem.\nEx.:python twonord.py window.png")


if __name__ == "__main__":
    main()
