import numpy as np
from PIL import Image

###############################
##### Auxiliary Functions #####
###############################
def angular_distance_between_images(image_1, image_2):
    '''
    Returns the angular distance (in radians) between two images

    image_1      numpy.ndarray
    image_2      numpy.ndarray     
    '''

    image1_normalized = image_1 / np.linalg.norm(image_1)
    image2_normalized = image_2 / np.linalg.norm(image_2)

    return np.arccos(np.clip(np.inner(image1_normalized, image2_normalized), -1, 1))

def average_angular_distance_between_RGB_channels_of_images(image_1, image_2):
    '''
    Computes the dot product between the RGB channels of image_1 and image_2
    separately and returns the average angular distance (in radians).

    image_1      numpy.ndarray
    image_2      numpy.ndarray
    '''

    image_1_normalized = image_1 / np.linalg.norm(image_1, axis = 0)
    image_2_normalized = image_2 / np.linalg.norm(image_2, axis = 0)

    angular_distances = np.arccos(np.clip(np.sum(image_1_normalized * image_2_normalized, axis = 0), -1, 1))
    
    return np.average(angular_distances) 

#######################
######## SETUP ########
#######################

NUM_IMAGES = 4
images = [ Image.open('images/image{}.jpg'.format(i)) for i in range(1, NUM_IMAGES + 1) ]

# Resize images for equal comparison
MIN_WIDTH = min(im.size[0] for im in images)
MIN_HEIGHT = min(im.size[1] for im in images)
images = [im.resize((MIN_WIDTH, MIN_HEIGHT), resample=Image.LANCZOS)
          for im in images]

image_datas = [ np.array(im.getdata()) for im in images ]
histograms = [ np.array(im.histogram()) for im in images ]

#####################################
##### Average of Channel Angles #####
#####################################
result_1 = np.empty((NUM_IMAGES, NUM_IMAGES))
for i, image_1 in enumerate(image_datas):

    for j, image_2 in enumerate(image_datas):
        result_1[i][j] = average_angular_distance_between_RGB_channels_of_images(image_1, image_2)

###########################################
##### Angular Distance b/w Histograms #####
###########################################
result_2 = np.empty((NUM_IMAGES, NUM_IMAGES))
for i, image_1 in enumerate(histograms):
    for j, image_2 in enumerate(histograms):
        result_2[i][j] = angular_distance_between_images(image_1, image_2)

print(result_1)
print(result_2)


