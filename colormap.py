'''
This script changes the color map of the image.
'''
from PIL import Image
import numpy as np
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('image_path', type=str, help='Path to the image')
argparser.add_argument('save_path', type=str, help='Path to save the output')
argparser.add_argument('colormap', type=str, help='rearrange RGB to any of the 6 colormaps')

args = argparser.parse_args()
reg_seq = {'R':0, 'G':1, 'B':2}

def colormap_image(image_path:str, save_path:str, colormap:str):
    '''
    image_path: str, path to the image
    save_path: str, path to save the encrypted image
    colormap: str, colormap to use. Use _ to inverse the color value.
    '''
    img = Image.open(image_path)
    img = np.asarray(img)
    print(img.shape)
    h, w, d = img.shape[0], img.shape[1], img.shape[2]
    if d == 4:
        transparency = img[:, :, 3]
        img = img[:, :, :3]
    else:
        transparency = None
    new_img = np.zeros_like(img)
    ptr = 0
    flag = 1
    for i in colormap:
        if i == '_':
            if flag == -1:
                print('Invalid colormap')
                return
            flag = -1
        else:
            if i not in reg_seq:
                print('Invalid colormap')
                return
            target = reg_seq[i]
            if flag == 1:
                new_img[:, :, ptr] = img[:, :, target]
            else:
                new_img[:, :, ptr] = 255 - img[:, :, target]
            ptr += 1
            flag = 1
    img = new_img
    if transparency is not None:
        img = np.concatenate((img, transparency[:, :, np.newaxis]), axis=2)
    img = np.uint8(np.round(img))
    ret = Image.fromarray(img)
    ret.save(save_path)

if __name__ == '__main__':
    image_path = args.image_path
    save_path = args.save_path
    colormap = args.colormap
    colormap_image(image_path, save_path, colormap)

    print('Done')