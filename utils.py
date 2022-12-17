import os
import imageio
import numpy as np
from PIL import Image


def get_data(file: str) -> list:
    if not os.path.isfile(file):
        print(f"Input file '{file}' not found")
        return

    with open(file) as f:
        return f.read().splitlines()


def save_picture(pixels: list, pic_name: str) -> None:
    array = np.array(pixels, dtype=np.uint8)
    img = Image.fromarray(array)
    img.save(f'images/frames/{pic_name}.png')


def create_gif(image_path: str, fps: int = 50, images_path: str = 'images/frames') -> None:
    frames = []
    for i in os.listdir(images_path):
        img = imageio.v2.imread(f'{images_path}/{i}')
        frames.append(img)

    imageio.mimsave(image_path, frames, fps=fps, loop=1)
