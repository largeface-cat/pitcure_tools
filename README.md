# pitcure_tools
### pitcure_encryption
A simple script to encode / decode pictures by shuffling pixels.

usage: pic_encrypt.py [-h] {D,E} image_path key save_path

positional arguments:
  {D,E}       Decrypt(D) or encrypt(E) the image
  image_path  Path to the image
  key         Seed of the shuffle
  save_path   Path to save the encrypted image

options:
  -h, --help  show this help message and exit
