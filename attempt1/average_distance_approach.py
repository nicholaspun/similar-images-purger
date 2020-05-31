#
# -- Average Angular Distance -- #
#

#  -- Setup -- # 
import numpy as np
from PIL import Image

NUM_IMAGES = 4
images = [ Image.open('images/image{}.jpg'.format(i)) for i in range(1, NUM_IMAGES + 1) ]

# Resize images for equal comparison
MIN_WIDTH = min(im.size[0] for im in images)
MIN_HEIGHT = min(im.size[1] for im in images)
images = [im.resize((MIN_WIDTH, MIN_HEIGHT), resample=Image.LANCZOS)
          for im in images]

image_datas = [ np.array(im.getdata()) for im in images ]
# ------------- #

# -- Main Content -- #
def distance(v1, v2):
    '''
    Returns the average angular distance (in radians) between every pixel in the two images

    v1      numpy.ndarray
    v2      numpy.ndarray     
    '''

    dot_prods = np.einsum('ij, ij -> i', v1, v2)
    v1_norms = np.linalg.norm(v1, axis = 1)
    v2_norms = np.linalg.norm(v2, axis = 1)

    normalized_dot_prods = dot_prods / (v1_norms * v2_norms)

    return np.arccos(np.clip(np.nanmean(normalized_dot_prods), -1, 1))

result = np.empty((NUM_IMAGES, NUM_IMAGES))
for i, image_1 in enumerate(image_datas):
    for j, image_2 in enumerate(image_datas):
        result[i][j] = distance(image_1, image_2)

print(result)
# ------------------ #