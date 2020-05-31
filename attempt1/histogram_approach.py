#
# -- Angular Distance b/w Histograms -- #
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

histograms = [ np.array(im.histogram()) for im in images ]
# ------------- #

# -- Main Content -- #
def distance(v1, v2):
    '''
    Returns the angular distance (in radians) between two vectors

    v1      numpy.ndarray
    v2      numpy.ndarray     
    '''

    v1_normalized = v1 / np.linalg.norm(v1)
    v2_normalized = v2 / np.linalg.norm(v2)

    return np.arccos(np.clip(np.dot(v1_normalized, v2_normalized), -1, 1))

result = np.empty((NUM_IMAGES, NUM_IMAGES))
for i, image_1 in enumerate(histograms):
    for j, image_2 in enumerate(histograms):
        result[i][j] = distance(image_1, image_2)

print(result)
# ------------------ #

