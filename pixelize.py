'''
This script pixelize images by doing a mean pooling operation on the image.
'''
from PIL import Image
import numpy as np
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('image_path', type=str, help='Path to the image')
argparser.add_argument('save_path', type=str, help='Path to save the output')
argparser.add_argument('scale', type=int, help='n*n pixels to 1 pixel')
argparser.add_argument("-k", "--keep_size", help="Keep output size same as input", action="store_true")

args = argparser.parse_args()

mapping_method = np.mean

def pixelize_image(image_path:str, save_path:str, scale:int, keep_size=True):
    '''
    image_path: str, path to the image
    save_path: str, path to save the encrypted image
    '''
    img = Image.open(image_path)
    img = np.asarray(img)
    print(img.shape)
    h, w, d = img.shape[0], img.shape[1], img.shape[2]
    
    pad_h = (scale - (h % scale)) % scale
    pad_w = (scale - (w % scale)) % scale
    
    padded_img = np.pad(img, ((0, pad_h), (0, pad_w), (0, 0)), mode='edge')
    
    h_padded, w_padded = padded_img.shape[0], padded_img.shape[1]
    
    reshaped = padded_img.reshape(
        h_padded // scale, scale,
        w_padded // scale, scale,
        d
    )
    pixelated = mapping_method(reshaped, axis=(1, 3))
    pixelated = np.uint8(np.round(pixelated))
    print(pixelated.dtype, pixelated.shape)
    if keep_size:
        pixelated = np.repeat(np.repeat(pixelated, scale, axis=0), scale, axis=1)
        pixelated = pixelated[:h, :w, :]
    pixelated = Image.fromarray(pixelated)
    pixelated.save(save_path)

if __name__ == '__main__':
    image_path = args.image_path
    save_path = args.save_path
    scale = args.scale
    keep_size = args.keep_size
    pixelize_image(image_path, save_path, scale, keep_size)

    print('Done')